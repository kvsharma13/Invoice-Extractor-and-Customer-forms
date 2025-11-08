# AIRTABLE MAPPING DOCUMENTATION
## End-to-End Data Flow: Customer Form → Airtable

---

## CRITICAL: Airtable Field Names (MUST MATCH EXACTLY)

Your Airtable "Orders" table MUST have these field names EXACTLY as shown:
(Spaces, capitals, and special characters matter!)

```
✓ Created Date          (not "CreatedDate" or "created date")
✓ Customer Name         (not "CustomerName" or "customer name")
✓ Product Description   (not "ProductDescription" or "product description")
✓ Unit Price            (not "UnitPrice" or "unit price")
✓ Stock SKU Number      (not "StockSKUNumber" or "SKU Number")
✓ Deposit %             (not "Deposit%" or "Deposit Percent" - NOTE THE SPACE!)
✓ New Product           (not "NewProduct" or "new product")
✓ Press Check           (not "PressCheck" or "press check")
✓ Update Artwork        (not "UpdateArtwork" or "update artwork")
✓ 5% Tolerance Order    (not "5%ToleranceOrder" or "tolerance order")
✓ Units to Order        (not "UnitsToOrder" or "units to order")
✓ Order Total           (not "OrderTotal" or "order total")
✓ Deposit Amount        (not "DepositAmount" or "deposit amount")
```

---

## DATA FLOW MAP

### Step 1: Customer Form Input

| Form Field ID | User Action | Example Value |
|---------------|-------------|---------------|
| `customerName` | Manual entry | "John Smith" |
| `productDescription` | Dropdown selection | "Lipstick - Matte Finish" |
| `unitsToOrder` | Manual entry | 100 |
| `newProduct` | Checkbox | ✓ (true) |
| `pressCheck` | Checkbox | ☐ (false) |
| `updateArtwork` | Checkbox | ✓ (true) |
| `toleranceOrder` | Checkbox | ☐ (false) |

### Step 2: Auto-Population (Happens Instantly)

| Form Field ID | Auto-Populated From | Example Value |
|---------------|---------------------|---------------|
| `unitPrice` | Product database | "$25.00" |
| `stockSKU` | Product database | "SKU-LIP-001" |
| `depositPercent` | Product database | "30%" |

### Step 3: Auto-Calculation (On Submit)

| Variable | Formula | Example Calculation |
|----------|---------|---------------------|
| `orderTotal` | unitPrice × unitsToOrder | $25.00 × 100 = $2,500.00 |
| `depositAmount` | orderTotal × (depositPercent / 100) | $2,500.00 × 30% = $750.00 |
| `createdDate` | Today's date | "2024-11-07" |

### Step 4: Data Sent to Backend (JSON)

```javascript
{
  "createdDate": "2024-11-07",
  "customerName": "John Smith",
  "productDescription": "Lipstick - Matte Finish",
  "unitPrice": "$25.00",
  "stockSKU": "SKU-LIP-001",
  "depositPercent": "30%",
  "unitsToOrder": 100,
  "newProduct": true,
  "pressCheck": false,
  "updateArtwork": true,
  "toleranceOrder": false,
  "orderTotal": "$2,500.00",
  "depositAmount": "$750.00"
}
```

### Step 5: Backend Processing (Flask)

```python
# app.py receives the data and maps it:

airtable_data = {
    'Created Date': order_data['createdDate'],           # → "2024-11-07"
    'Customer Name': order_data['customerName'],         # → "John Smith"
    'Product Description': order_data['productDescription'], # → "Lipstick - Matte Finish"
    'Unit Price': order_data['unitPrice'],               # → "$25.00"
    'Stock SKU Number': order_data['stockSKU'],          # → "SKU-LIP-001"
    'Deposit %': order_data['depositPercent'],           # → "30%"
    'New Product': order_data['newProduct'],             # → true
    'Press Check': order_data['pressCheck'],             # → false
    'Update Artwork': order_data['updateArtwork'],       # → true
    '5% Tolerance Order': order_data['toleranceOrder'],  # → false
    'Units to Order': int(order_data['unitsToOrder']),   # → 100
    'Order Total': order_data['orderTotal'],             # → "$2,500.00"
    'Deposit Amount': order_data['depositAmount']        # → "$750.00"
}
```

### Step 6: Airtable Record Created

| Airtable Field | Value Stored | Field Type |
|----------------|--------------|------------|
| Created Date | 2024-11-07 | Date |
| Customer Name | John Smith | Single line text |
| Product Description | Lipstick - Matte Finish | Single line text |
| Unit Price | $25.00 | Single line text |
| Stock SKU Number | SKU-LIP-001 | Single line text |
| Deposit % | 30% | Single line text |
| New Product | ✓ | Checkbox |
| Press Check | ☐ | Checkbox |
| Update Artwork | ✓ | Checkbox |
| 5% Tolerance Order | ☐ | Checkbox |
| Units to Order | 100 | Number |
| Order Total | $2,500.00 | Single line text |
| Deposit Amount | $750.00 | Single line text |

---

## ENVIRONMENT VARIABLES (.env file)

```bash
# Airtable Configuration
AIRTABLE_API_KEY=patXXXXXXXXXXXXXXXXXX        # Your Airtable API key
AIRTABLE_BASE_ID=appYbFbCKk2PsGezK             # Your base ID
AIRTABLE_TABLE_NAME=Invoice                     # For invoice extractor
AIRTABLE_ORDERS_TABLE=Orders                    # For customer orders ← IMPORTANT!

# Email Configuration
SENDGRID_API_KEY=SG.XXXXXXXXXXXXXXXXXXXXXXXX   # Your SendGrid key
SENDER_EMAIL=kavindrash12@gmail.com             # Sender email
NOTIFICATION_EMAIL=kavindrash12@gmail.com       # Where notifications go

# OpenAI Configuration (for invoice extractor only)
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX     # Your OpenAI key
```

---

## PRODUCT DATABASE (customer_order_form.html)

This JavaScript object defines your products:

```javascript
const products = {
    "Product Name Exactly As In Dropdown": {
        price: 25.00,        // Number (no $)
        sku: "SKU-XXX-001",  // String
        deposit: 30          // Number (percentage, no %)
    }
};
```

### Example with Real Products:

```javascript
const products = {
    "Lipstick - Matte Finish": {
        price: 25.00,
        sku: "SKU-LIP-001",
        deposit: 30
    },
    "Face Cream - Anti-Aging": {
        price: 45.00,
        sku: "SKU-CRM-002",
        deposit: 50
    },
    "Eye Shadow Palette": {
        price: 35.00,
        sku: "SKU-EYE-003",
        deposit: 40
    }
};
```

**CRITICAL:** Product names in dropdown MUST match the keys in this object EXACTLY!

---

## TESTING WITH DEMO BUTTON

### How to Test:

1. Open: http://localhost:5000/customer-order
2. Click **"Fill Demo Data"** button
3. Form fills automatically with test data
4. Click **"Continue to Payment"**
5. Review the summary
6. Click **"Demo Submit (Test Airtable)"** - GREEN BUTTON
7. Open browser console (F12) to see logs
8. Check your Airtable "Orders" table
9. You should see a new record!

### What the Demo Button Does:

```javascript
customerName: "Demo Customer"
productDescription: "Lipstick - Matte Finish"
unitsToOrder: 100
newProduct: ✓
updateArtwork: ✓
// Auto-calculates: $2,500 total, $750 deposit
```

### Console Logs to Watch:

```
📤 Sending to Airtable: {data object}
📥 Response from server: {success: true, record_id: "recXXXX"}
✅ SUCCESS! Check Airtable Orders table - Record ID: recXXXXXXXX
```

---

## TROUBLESHOOTING CHECKLIST

### If data not appearing in Airtable:

1. ☐ Check Orders table exists in Airtable
2. ☐ Check all 13 field names match EXACTLY (see top of document)
3. ☐ Check AIRTABLE_ORDERS_TABLE=Orders in .env
4. ☐ Check AIRTABLE_API_KEY is correct
5. ☐ Check AIRTABLE_BASE_ID is correct
6. ☐ Restart Flask app after changing .env
7. ☐ Check browser console for errors (F12)
8. ☐ Check Flask terminal for error messages

### Common Errors:

**"Unknown field name: 'Deposit%'"**
- Fix: Field must be "Deposit %" with a space before %

**"Table 'Orders' not found"**
- Fix: Create Orders table or check spelling in .env

**"Invalid value for column"**
- Fix: Check field types in Airtable match what's being sent

---

## FIELD TYPE REQUIREMENTS

| Field Name | Required Type | What Gets Saved |
|------------|---------------|-----------------|
| Created Date | Date | 2024-11-07 |
| Customer Name | Single line text | John Smith |
| Product Description | Single line text | Lipstick - Matte Finish |
| Unit Price | Single line text | $25.00 |
| Stock SKU Number | Single line text | SKU-LIP-001 |
| Deposit % | Single line text | 30% |
| New Product | Checkbox | true/false |
| Press Check | Checkbox | true/false |
| Update Artwork | Checkbox | true/false |
| 5% Tolerance Order | Checkbox | true/false |
| Units to Order | Number | 100 |
| Order Total | Single line text | $2,500.00 |
| Deposit Amount | Single line text | $750.00 |

---

## SUCCESS INDICATORS

### In Browser:
✅ Form fills correctly
✅ Prices auto-populate
✅ Calculations show correctly
✅ Success message appears
✅ Console shows "SUCCESS!"

### In Airtable:
✅ New record appears in Orders table
✅ All 13 fields are populated
✅ Data matches what was entered
✅ Calculated fields are correct

### In Flask Terminal:
✅ "Order saved to Airtable! Record ID: recXXXX"
✅ No error messages

---

## SUPPORT

If stuck, check:
1. Browser console (F12 → Console tab)
2. Flask terminal output
3. Airtable field names
4. .env file values

Provide these details for help:
- Error message (exact text)
- Screenshot of Airtable fields
- Browser console log
- Flask terminal output
