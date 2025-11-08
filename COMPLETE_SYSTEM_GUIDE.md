# COMPLETE SYSTEM SETUP GUIDE
## Portal Selection + Customer/Admin Logins + Dashboards

---

## WHAT YOU'RE GETTING

Complete multi-user portal system:

1. **Main Portal Selection** - Choose: Customer, Admin, or Supplier
2. **Customer Login** → Customer Order Form + Review Form  
3. **Admin Login** → Dashboard with Master Table + AI Chatbot
4. **Supplier Login** → Under Maintenance (coming soon)

---

## DOWNLOAD ALL FILES (9 files)

### Core Application:
1. `app_final.py` - Rename to `app.py`
2. `requirements_complete.txt` - Rename to `requirements.txt`

### HTML Pages:
3. `portal_selection.html` - Main landing page
4. `customer_login.html` - Customer login
5. `admin_login.html` - Admin login  
6. `customer_order_form.html` - Order form (existing, updated)
7. `customer_review_form.html` - Review form (existing)
8. `invoice_extractor.html` - Invoice uploader (existing)
9. `admin_dashboard.html` - Admin panel with table + AI chatbot

---

## STEP 1: FILE SETUP

Your folder structure should be:

```
pdf-to-airtable/
├── app.py (renamed from app_final.py)
├── requirements.txt (renamed from requirements_complete.txt)
├── portal_selection.html
├── customer_login.html
├── admin_login.html
├── admin_dashboard.html
├── customer_order_form.html
├── customer_review_form.html
├── invoice_extractor.html
├── .env
```

---

## STEP 2: UPDATE .env FILE

Add admin credentials to your `.env`:

```
# Existing keys
OPENAI_API_KEY=your_key
AIRTABLE_API_KEY=your_key
AIRTABLE_BASE_ID=appYbFbCKk2PsGezK
AIRTABLE_TABLE_NAME=Invoice
AIRTABLE_ORDERS_TABLE=Orders
SENDGRID_API_KEY=your_key
SENDER_EMAIL=kavindrash12@gmail.com
NOTIFICATION_EMAIL=kavindrash12@gmail.com

# NEW: Admin credentials
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
```

**IMPORTANT:** Change `admin123` to your secure password!

---

## STEP 3: VERIFY AIRTABLE TABLES

### Orders Table (18 fields total):

**Order Fields (13):**
- Created Date (Date)
- Customer Name (Single line text)
- Product Description (Single line text)
- Unit Price (Single line text)
- Stock SKU Number (Single line text)
- Deposit % (Single line text)
- New Product (Checkbox)
- Press Check (Checkbox)
- Update Artwork (Checkbox)
- 5% Tolerance Order (Checkbox)
- Units to Order (Number)
- Order Total (Single line text)
- Deposit Amount (Single line text)

**Review Fields (5):**
- Actual Units Received (Number)
- Date Goods Received Warehouse (Date) ← NO @ SYMBOL!
- Quality Rejects on Inspection (Number)
- Authorised Invoice (Checkbox) ← NO ? SYMBOL!
- Expected Payment Date (Date)

**CRITICAL:** Field names must match EXACTLY!

---

## STEP 4: INSTALL & RUN

```bash
pip install -r requirements.txt
py app.py
```

---

## STEP 5: ACCESS THE SYSTEM

### Main Portal:
http://localhost:5000

You'll see 3 options:
- 👤 Customer Portal
- ⚙️ Admin Portal
- 🏭 Supplier Portal (under maintenance)

---

## USER JOURNEYS

### CUSTOMER FLOW:

```
1. Click "Customer Portal"
   ↓
2. Customer Login Page
   - Enter email/password OR
   - Click "Continue as Guest"
   ↓
3. Customer Order Form
   - Fill order details
   - Submit order
   ↓
4. Auto-redirect (3 seconds)
   ↓
5. Customer Review Form
   - Fill review details
   - Submit review
   ↓
6. Success! Back to home
```

### ADMIN FLOW:

```
1. Click "Admin Portal"
   ↓
2. Admin Login Page
   - Username: admin
   - Password: admin123
   ↓
3. Admin Dashboard
   - Tab 1: Master Table (all orders)
   - Tab 2: AI Analytics Chatbot
```

---

## ADMIN DASHBOARD FEATURES

### Stats Cards:
- Total Orders
- Total Revenue
- Pending Reviews
- Quality Issues

### Master Table Tab:
- Shows ALL Airtable fields
- Same structure as your Airtable
- Sortable columns
- Search/filter
- Pagination
- Refresh button

### AI Analytics Tab:
- Chatbot powered by OpenAI
- Ask questions about your data
- Examples:
  - "What's the total revenue?"
  - "Show me orders with quality issues"
  - "Which products are most popular?"
  - "How many pending payments?"
- Natural language queries
- Instant insights

---

## TESTING CHECKLIST

### Test Portal Selection:
- [ ] Can access http://localhost:5000
- [ ] See 3 portal options
- [ ] Supplier shows "Under Maintenance" alert

### Test Customer Flow:
- [ ] Customer login page loads
- [ ] "Continue as Guest" works
- [ ] Order form works
- [ ] Auto-redirects to review form
- [ ] Review form updates same Airtable record

### Test Admin Flow:
- [ ] Admin login page loads
- [ ] Login with admin/admin123 works
- [ ] Dashboard shows stats
- [ ] Master table displays all fields
- [ ] Can search/filter table
- [ ] AI chatbot responds to questions

---

## ADMIN CREDENTIALS

**Default Login:**
- Username: `admin`
- Password: `admin123`

**To Change:**
1. Update in `.env` file:
   ```
   ADMIN_USERNAME=your_username
   ADMIN_PASSWORD=your_secure_password
   ```
2. Restart app

---

## AI CHATBOT USAGE

Example questions to ask:

**Financial:**
- "What is the total revenue?"
- "Show me orders above $1000"
- "Calculate average order value"

**Operations:**
- "How many orders need review?"
- "List orders with quality rejects"
- "Show me pending authorizations"

**Analytics:**
- "Which products sell the most?"
- "What's the average deposit percentage?"
- "Show me orders from last week"

**Trends:**
- "Are quality issues increasing?"
- "What's our fulfillment rate?"
- "Compare this month vs last month"

---

## TROUBLESHOOTING

### "portal_selection.html not found"
- Make sure all 9 HTML files are in the same folder as app.py

### Admin login fails
- Check ADMIN_USERNAME and ADMIN_PASSWORD in .env
- Make sure no quotes around values in .env
- Restart Flask app after changing .env

### Master table empty
- Check Orders table exists in Airtable
- Check AIRTABLE_ORDERS_TABLE=Orders in .env
- Submit a test order first

### AI chatbot not responding
- Check OPENAI_API_KEY in .env
- Check browser console for errors
- Make sure you have OpenAI credits

### Field name errors on review form
- Remove @ symbol: "Date Goods Received Warehouse" (not "@ Warehouse")
- Remove ? symbol: "Authorised Invoice" (not "Authorised Invoice?")
- Match field names EXACTLY in Airtable

---

## SECURITY NOTES

**Current Setup:**
- Customer login: Any email/password (no validation)
- Admin login: Protected with username/password
- Sessions stored in browser

**For Production:**
- Implement real user authentication
- Add database for user accounts
- Use secure session management
- Add HTTPS/SSL
- Rate limiting on API endpoints

---

## CUSTOMIZATION

### Change Portal Colors:
Edit each HTML file's `<style>` section

### Add More Admin Users:
Currently supports one admin. To add more:
- Create user database
- Update /admin-auth endpoint
- Add user management page

### Customize Stats:
Edit `populateStats()` function in admin_dashboard.html

### Add More Chatbot Features:
- Update `/api/ai-analytics` endpoint in app.py
- Add charts/visualizations
- Export chat history

---

## WHAT'S WORKING

✅ Portal selection page
✅ Customer login (any credentials + guest access)
✅ Admin login (password protected)
✅ Customer order form → Airtable
✅ Customer review form → Updates same record
✅ Invoice extractor → Airtable
✅ Admin master table → Shows all Airtable data
✅ AI chatbot → Analyzes your data
✅ Auto-redirect after order submission
✅ Supplier "Under Maintenance" message

---

## FOLDER ORGANIZATION

```
Main Portal (/)
├── Customer Portal
│   ├── Login (/customer-login)
│   ├── Order Form (/customer-order)
│   └── Review Form (/customer-review)
├── Admin Portal
│   ├── Login (/admin-login)
│   └── Dashboard (/admin-dashboard)
│       ├── Master Table Tab
│       └── AI Analytics Tab
└── Supplier Portal
    └── Under Maintenance
```

---

## NEXT STEPS

After everything is working:

1. ✅ Change admin password
2. ✅ Test all user flows
3. ✅ Add real customer authentication (optional)
4. ✅ Customize colors/branding
5. ✅ Add more chatbot prompts
6. ✅ Build supplier portal (future)
7. ✅ Deploy to production server

---

## SUCCESS INDICATORS

You know it's working when:

✅ Portal page shows all 3 options
✅ Can login as customer (any credentials)
✅ Can login as admin (correct password)
✅ Customer orders save to Airtable
✅ Reviews update same records
✅ Admin sees master table with all fields
✅ AI chatbot answers questions
✅ Stats show correct numbers

---

## SUPPORT

If stuck, check:
1. Browser console (F12)
2. Flask terminal output
3. Airtable field names
4. .env file values
5. All 9 files in same folder

Everything is ready! 🚀
