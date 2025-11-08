from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import PyPDF2
from pyairtable import Api
import os
from dotenv import load_dotenv
import io
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import secrets

load_dotenv()

app = Flask(__name__)
CORS(app)

# Email Configuration
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
NOTIFICATION_EMAIL = os.getenv('NOTIFICATION_EMAIL')

# Initialize OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Initialize Airtable
airtable_api = Api(os.getenv('AIRTABLE_API_KEY'))
base_id = os.getenv('AIRTABLE_BASE_ID')
invoice_table_name = os.getenv('AIRTABLE_TABLE_NAME', 'Invoice')
orders_table_name = os.getenv('AIRTABLE_ORDERS_TABLE', 'Master Database')

# Admin Credentials (changeable via .env)
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file"""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_data_with_openai(text):
    """Use OpenAI to extract structured data from text"""
    prompt = f"""
    Extract the following information from this invoice document and return it as JSON with these EXACT field names:
    - "Deposit Invoice #" (invoice number as text)
    - "Deposit Invoice Date" (date in format YYYY-MM-DD)
    - "Customer Name" (customer or company name)
    - "Customer Email" (customer email address - look for email in the document)
    - "Customer Address" (full address)
    - "Deposit Invoice Value" (total amount as number)
    - "Payment Date" (payment date in format YYYY-MM-DD)
    - "Line Items" (all items/products as a SINGLE text string, separated by commas or newlines)
    
    Document text:
    {text}
    
    Return only valid JSON format with these EXACT field names in quotes. Make sure "Line Items" is a string, not an array.
    If you cannot find the customer email in the document, set "Customer Email" to null.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a data extraction assistant. Extract information and return only valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    
    return response.choices[0].message.content

def send_email(subject, body, to_email):
    """Send email using SendGrid API"""
    try:
        message = Mail(
            from_email=SENDER_EMAIL,
            to_emails=to_email,
            subject=subject,
            html_content=body
        )
        
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        
        print(f"Email sent successfully to {to_email} - Status Code: {response.status_code}")
        return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False

def send_invoice_confirmation(invoice_data):
    """Send immediate confirmation email when invoice is uploaded"""
    customer_email = invoice_data.get('Customer Email')
    if not customer_email or customer_email == 'null' or '@' not in str(customer_email):
        recipient_email = NOTIFICATION_EMAIL
    else:
        recipient_email = customer_email
    
    subject = f"Invoice Received: {invoice_data.get('Deposit Invoice #', 'N/A')}"
    body = f"<html><body><h2>Invoice Confirmation</h2><p>Invoice #{invoice_data.get('Deposit Invoice #')} received.</p></body></html>"
    send_email(subject, body, recipient_email)

def send_payment_reminder(invoice_data):
    """Send payment reminder email 1 day before due date"""
    customer_email = invoice_data.get('Customer Email')
    if not customer_email or customer_email == 'null' or '@' not in str(customer_email):
        recipient_email = NOTIFICATION_EMAIL
    else:
        recipient_email = customer_email
    
    subject = f"Payment Reminder: Invoice {invoice_data.get('Deposit Invoice #', 'N/A')} Due Tomorrow"
    body = f"<html><body><h2>Payment Reminder</h2><p>Payment is due tomorrow!</p></body></html>"
    send_email(subject, body, recipient_email)

def check_payment_reminders():
    """Check for invoices due tomorrow and send reminders"""
    try:
        tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        table = airtable_api.table(base_id, invoice_table_name)
        records = table.all()
        
        for record in records:
            fields = record['fields']
            payment_date = fields.get('Payment Date', '')
            if payment_date == tomorrow:
                send_payment_reminder(fields)
    except Exception as e:
        print(f"Error checking payment reminders: {str(e)}")

def save_to_airtable(data, table_name):
    """Save data to Airtable"""
    cleaned_data = {}
    for key, value in data.items():
        if isinstance(value, list):
            cleaned_data[key] = ", ".join(str(item) for item in value)
        else:
            cleaned_data[key] = value
    
    table = airtable_api.table(base_id, table_name)
    record = table.create(cleaned_data)
    return record

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=check_payment_reminders, trigger="interval", hours=24)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

# ============= ROUTES =============

@app.route('/')
def home():
    """Portal selection page"""
    try:
        with open('portal_selection.html', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "Error: portal_selection.html not found"

@app.route('/customer-login')
def customer_login():
    """Customer login page"""
    try:
        with open('customer_login.html', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "Error: customer_login.html not found"

@app.route('/admin-login')
def admin_login():
    """Admin login page"""
    try:
        with open('admin_login.html', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "Error: admin_login.html not found"

@app.route('/admin-auth', methods=['POST'])
def admin_auth():
    """Authenticate admin credentials"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        token = secrets.token_hex(32)
        return jsonify({'success': True, 'token': token})
    else:
        return jsonify({'success': False, 'error': 'Invalid credentials'})

@app.route('/admin-dashboard')
def admin_dashboard():
    """Admin dashboard with master table and AI chatbot"""
    try:
        with open('admin_dashboard.html', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "Error: admin_dashboard.html not found"

@app.route('/invoice-extractor')
def invoice_extractor():
    """Invoice extractor page"""
    try:
        with open('invoice_extractor.html', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "Error: invoice_extractor.html not found"

@app.route('/customer-order')
def customer_order():
    """Customer order form page"""
    try:
        with open('customer_order_form.html', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "Error: customer_order_form.html not found"

@app.route('/customer-review')
def customer_review():
    """Customer review form page"""
    try:
        with open('customer_review_form.html', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return "Error: customer_review_form.html not found"

@app.route('/upload', methods=['POST'])
def upload_pdf():
    """Handle PDF invoice upload"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        invoice_type = request.form.get('invoice_type', 'Customer Invoice')
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.pdf'):
            return jsonify({'error': 'File must be a PDF'}), 400
        
        pdf_text = extract_text_from_pdf(io.BytesIO(file.read()))
        extracted_data_json = extract_data_with_openai(pdf_text)
        extracted_data = json.loads(extracted_data_json.strip('```json').strip('```').strip())
        extracted_data['Invoice Type'] = invoice_type
        
        airtable_record = save_to_airtable(extracted_data, invoice_table_name)
        send_invoice_confirmation(extracted_data)
        
        return jsonify({
            'success': True,
            'extracted_data': extracted_data,
            'airtable_id': airtable_record['id']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/submit-order', methods=['POST'])
def submit_order():
    """Handle customer order form submission"""
    try:
        order_data = request.json
        
        airtable_data = {
            'Created Date': order_data['createdDate'],
            'Customer Name': order_data['customerName'],
            'Product Description': order_data['productDescription'],
            'Unit Price': order_data['unitPrice'],
            'Stock SKU Number': order_data['stockSKU'],
            'Deposit %': order_data['depositPercent'],
            'New Product': order_data['newProduct'],
            'Press Check': order_data['pressCheck'],
            'Update Artwork': order_data['updateArtwork'],
            '5% Tolerance Order': order_data['toleranceOrder'],
            'Units to Order': int(order_data['unitsToOrder']),
            'Order Total': order_data['orderTotal'],
            'Deposit Amount': order_data['depositAmount']
        }
        
        record = save_to_airtable(airtable_data, orders_table_name)
        
        print(f"Order saved to Airtable! Record ID: {record['id']}")
        
        return jsonify({
            'success': True,
            'record_id': record['id'],
            'message': 'Order submitted successfully'
        })
    except Exception as e:
        print(f"Error saving order: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/submit-review', methods=['POST'])
def submit_review():
    """Handle customer review form submission - UPDATE existing Airtable record"""
    try:
        review_data = request.json
        order_id = review_data['orderId']
        
        update_data = {
            'Actual Units Received': review_data['actualUnitsReceived'],
            'Date Goods Received Warehouse': review_data['dateGoodsReceived'],
            'Quality Rejects on Inspection': review_data['qualityRejects'],
            'Authorised Invoice': review_data['authorisedInvoice'],
            'Expected Payment Date': review_data['expectedPaymentDate']
        }
        
        table = airtable_api.table(base_id, orders_table_name)
        record = table.update(order_id, update_data)
        
        print(f"Review submitted! Updated Airtable record: {order_id}")
        
        return jsonify({
            'success': True,
            'record_id': record['id'],
            'message': 'Review submitted successfully'
        })
    except Exception as e:
        print(f"Error submitting review: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/orders')
def get_orders():
    """API endpoint to get all records from Master Database for admin panel"""
    try:
        # Fetch from Master Database table for admin viewing
        master_db_table = os.getenv('AIRTABLE_MASTER_TABLE', 'Master Database')
        table = airtable_api.table(base_id, master_db_table)
        records = table.all()
        return jsonify({'success': True, 'records': records})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/ai-analytics', methods=['POST'])
def ai_analytics():
    """AI chatbot analytics endpoint - reads real Airtable data"""
    try:
        data = request.json
        question = data.get('question')
        orders_data = data.get('data', [])
        
        # Build comprehensive data context for AI
        context = "You are an AI analytics assistant for Cosmetic Vision. Analyze this real-time data from the Master Database:\n\n"
        
        context += f"=== SUMMARY ===\n"
        context += f"Total Records: {len(orders_data)}\n\n"
        
        if len(orders_data) > 0:
            # Get all field names
            field_names = list(orders_data[0]['fields'].keys())
            context += f"Available Fields: {', '.join(field_names)}\n\n"
            
            # Add detailed data for AI to analyze
            context += f"=== SAMPLE RECORDS (First 5) ===\n"
            for i, record in enumerate(orders_data[:5]):
                context += f"\nRecord {i+1}:\n"
                for field, value in record['fields'].items():
                    context += f"  {field}: {value}\n"
            
            # Calculate key metrics for AI
            context += f"\n=== KEY METRICS ===\n"
            
            # Total revenue
            total_revenue = 0
            for record in orders_data:
                order_total = str(record['fields'].get('Order Total', ''))
                amount = float(order_total.replace('$', '').replace(',', '')) if order_total and '$' in order_total else 0
                total_revenue += amount
            context += f"Total Revenue: ${total_revenue:,.2f}\n"
            
            # Count products
            products = {}
            for record in orders_data:
                product = record['fields'].get('Product Description', 'Unknown')
                products[product] = products.get(product, 0) + 1
            context += f"Unique Products: {len(products)}\n"
            context += f"Most Popular Product: {max(products, key=products.get) if products else 'N/A'}\n"
            
            # Quality issues
            quality_issues = sum(1 for r in orders_data if r['fields'].get('Quality Rejects on Inspection', 0) > 0)
            context += f"Orders with Quality Issues: {quality_issues}\n"
            
            # Pending reviews
            pending_reviews = sum(1 for r in orders_data if not r['fields'].get('Actual Units Received'))
            context += f"Pending Reviews: {pending_reviews}\n"
        
        # Create AI prompt with full context
        prompt = f"{context}\n\n=== USER QUESTION ===\n{question}\n\nProvide a detailed, data-driven answer with specific numbers and insights."
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert data analyst. Provide clear, specific answers with actual numbers from the data. Format responses nicely with bullet points when appropriate."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        answer = response.choices[0].message.content
        
        return jsonify({'success': True, 'answer': answer})
    except Exception as e:
        print(f"AI Analytics error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
