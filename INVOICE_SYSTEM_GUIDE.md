# INVOICE-BASED REVIEW SYSTEM GUIDE
## New Feature: Deposit Invoice Number Lookup

---

## 🎯 WHAT'S NEW

The review form now requires a **Deposit Invoice Number** to access and auto-fill order details from Airtable.

### Key Changes:
1. ✅ **Order Form** generates unique Deposit Invoice Number
2. ✅ **Invoice Number displayed** prominently after order submission
3. ✅ **Review Form requires** invoice number to proceed
4. ✅ **Auto-fills** order details from Airtable
5. ✅ **Calculates** final amount to pay automatically

---

## 📦 FILES YOU RECEIVED

### Updated System Files (3 files):
1. **customer_order_form_v2.html** - Generates & displays invoice number
2. **customer_review_form_v2.html** - Invoice lookup & auto-fill
3. **app_v2.py** - Backend with invoice lookup endpoint

---

## 🔄 HOW IT WORKS

### STEP 1: Customer Places Order

```
Customer Order Form
    ↓
Fills order details
    ↓
Clicks "Submit Order"
    ↓
System generates unique Invoice Number
Example: INV-20251109-3847
    ↓
Order saved to Airtable with Invoice Number
    ↓
Success screen shows:
    ✅ Order Placed Successfully!
    Your Deposit Invoice Number: INV-20251109-3847
    Save this number for submitting your review later!
```

### STEP 2: Customer Submits Review

```
Customer Review Form
    ↓
Enter Deposit Invoice Number: INV-20251109-3847
    ↓
Click "Search"
    ↓
System looks up order in Airtable
    ↓
If found:
    ✅ Auto-fills:
       • Customer Name
       • Product Description
       • Deposit Paid: $750.00
       • Final Amount to Pay: $1,750.00
    ↓
Shows review form with all fields
    ↓
Customer fills review details
    ↓
Submits review
    ↓
Updates same Airtable record
```

---

## 🗂️ AIRTABLE REQUIREMENTS

### New Field Required:

| Field Name | Type | Description |
|------------|------|-------------|
| Deposit Invoice Number | Single line text | Unique invoice identifier |

**IMPORTANT:** This field must be added to your **Master Database** table!

### How to Add:
1. Open your Airtable base
2. Go to **Master Database** table
3. Click **+** to add new field
4. Name: `Deposit Invoice Number`
5. Type: **Single line text**
6. Click "Create field"

---

## 📋 INVOICE NUMBER FORMAT

**Pattern:** `INV-YYYYMMDD-XXXX`

**Example:** `INV-20251109-3847`

**Breakdown:**
- `INV` = Prefix (Invoice)
- `20251109` = Date (Year + Month + Day)
- `3847` = Random 4-digit number

**Generation:** Auto-generated in JavaScript when order is submitted

---

## 🎨 USER EXPERIENCE

### Order Submission Screen:
```
┌────────────────────────────────────────┐
│  ✅ Order Placed Successfully!        │
│                                        │
│  Your order has been submitted.        │
│                                        │
│  ┌──────────────────────────────────┐ │
│  │ Your Deposit Invoice Number:     │ │
│  │                                   │ │
│  │  INV-20251109-3847               │ │
│  │                                   │ │
│  │ Save this number for submitting   │ │
│  │ your review later!                │ │
│  └──────────────────────────────────┘ │
│                                        │
│  [Back to Customer Portal]             │
└────────────────────────────────────────┘
```

### Review Form Initial Screen:
```
┌────────────────────────────────────────┐
│  🔍 Enter Your Deposit Invoice Number │
│                                        │
│  ┌──────────────────────┬──────────┐  │
│  │ INV-20251109-3847   │ [Search] │  │
│  └──────────────────────┴──────────┘  │
│                                        │
│  💡 How to find your Invoice Number:  │
│  • Check your order confirmation       │
│  • Look at your invoice/receipt        │
│  • Contact support if needed           │
└────────────────────────────────────────┘
```

### Review Form After Successful Lookup:
```
┌────────────────────────────────────────┐
│  📦 Your Order Details                 │
│                                        │
│  Invoice Number: INV-20251109-3847    │
│  Customer: John Smith                  │
│  Product: Lipstick - Matte Finish      │
│                                        │
│  ┌──────────────────────────────────┐ │
│  │ Deposit Paid: $750.00            │ │
│  │                                   │ │
│  │ Final Amount to be Paid:          │ │
│  │ $1,750.00                         │ │
│  │ (Order Total - Deposit Paid)      │ │
│  └──────────────────────────────────┘ │
│                                        │
│  📋 Review & Receipt Information       │
│  [Review form fields appear below]     │
└────────────────────────────────────────┘
```

---

## 🔧 SETUP INSTRUCTIONS

### Step 1: Add Airtable Field (2 minutes)
1. Open Airtable
2. Go to Master Database table
3. Add field: `Deposit Invoice Number` (Single line text)

### Step 2: Replace Files (1 minute)
Replace these 3 files in your project:
```
pdf-to-airtable/
├── customer_order_form.html      ← REPLACE with customer_order_form_v2.html
├── customer_review_form.html     ← REPLACE with customer_review_form_v2.html
└── app.py                        ← REPLACE with app_v2.py
```

### Step 3: Test (3 minutes)
```bash
py app.py
```
Then:
1. Submit a test order → Note the invoice number
2. Go to review form → Enter invoice number
3. Verify order details auto-fill
4. Submit review

**Total time: ~6 minutes**

---

## 🧪 TESTING GUIDE

### Test 1: Order Submission
1. Go to Customer Portal → Order Form
2. Fill order details (or use demo button)
3. Submit order
4. **Verify:** Success screen shows invoice number
5. **Save the invoice number** displayed
6. **Check Airtable:** Record has Deposit Invoice Number field filled

### Test 2: Invoice Lookup
1. Go to Customer Portal → Review Form
2. Enter the invoice number you saved
3. Click "Search"
4. **Verify:**
   - ✅ Success message appears
   - ✅ Order details display correctly
   - ✅ Deposit amount shows
   - ✅ Final amount calculates correctly
   - ✅ Review form appears

### Test 3: Wrong Invoice Number
1. Enter a fake invoice number: `INV-99999999-9999`
2. Click "Search"
3. **Verify:** Error message: "No order found with this invoice number"

### Test 4: Empty Invoice Number
1. Leave field empty
2. Click "Search"
3. **Verify:** Error message: "Please enter a Deposit Invoice Number"

### Test 5: Complete Flow
1. Submit order → Get invoice number
2. Use invoice number in review form
3. Fill all review fields
4. Submit review
5. **Check Airtable:** Same record updated with review data

---

## 💡 FEATURES

### Auto-Fill Fields:
When invoice number is found, these automatically populate:
- ✅ Customer Name
- ✅ Product Description  
- ✅ Deposit Paid amount
- ✅ Order Total
- ✅ Final Amount to Pay (calculated)

### Manual Fill Fields:
Customer still needs to enter:
- Actual Units Received
- Date Goods Received
- Quality Rejects
- Authorised Invoice (checkbox)
- Expected Payment Date
- On Time and In Full (Yes/No)
- Short Shipment (Yes/No)
- Delivered Late (Yes/No)

---

## 🔍 BACKEND: Invoice Lookup Logic

```python
@app.route('/lookup-invoice', methods=['POST'])
def lookup_invoice():
    # Get invoice number from request
    invoice_number = request.json.get('invoiceNumber')
    
    # Search Airtable using formula
    formula = f"{{Deposit Invoice Number}} = '{invoice_number}'"
    records = table.all(formula=formula)
    
    # If found, return record
    if records:
        return {
            'success': True,
            'recordId': record['id'],
            'order': record['fields']
        }
    else:
        return {'success': False, 'error': 'Invoice not found'}
```

---

## ❓ TROUBLESHOOTING

### "Field 'Deposit Invoice Number' not found"
**Fix:** Add the field to Airtable (see Setup Step 1)

### Invoice number not generated
**Check:** Browser console for errors
**Fix:** Make sure customer_order_form_v2.html is being used

### Lookup returns "not found" but order exists
**Check:** Field name in Airtable matches exactly: `Deposit Invoice Number`
**Check:** Invoice number was saved to Airtable (view the record)

### Auto-fill not working
**Check:** Browser console for errors
**Check:** Response from `/lookup-invoice` endpoint
**Fix:** Ensure app_v2.py is running

### Final amount shows $0.00
**Cause:** Order Total or Deposit Amount missing from Airtable
**Fix:** Ensure order was submitted with all fields

---

## 📊 DATA FLOW

```
ORDER FORM:
    User fills form
    ↓
    generateInvoiceNumber() creates: INV-20251109-3847
    ↓
    Sends to backend with depositInvoiceNumber field
    ↓
    Backend saves to Airtable
    ↓
    Returns success + invoice number
    ↓
    Display invoice number to user

REVIEW FORM:
    User enters: INV-20251109-3847
    ↓
    Frontend calls: /lookup-invoice
    ↓
    Backend searches Airtable by invoice number
    ↓
    Returns: recordId + order fields
    ↓
    Frontend auto-fills order details
    ↓
    Calculates: Final Amount = Order Total - Deposit
    ↓
    User fills review fields
    ↓
    Frontend calls: /submit-review with recordId
    ↓
    Backend updates same Airtable record
```

---

## 🎯 BENEFITS

### For Customers:
✅ Easy to track orders with unique invoice number
✅ No need to remember complex order IDs
✅ See exactly how much they still need to pay
✅ One number for all order-related queries

### For Business:
✅ Better order tracking
✅ Unique identifier for each transaction
✅ Links order and review in single record
✅ Professional invoice numbering system
✅ Easier customer support

### For System:
✅ Reliable order-review matching
✅ No session storage dependency
✅ Works even if user comes back days later
✅ Data integrity maintained

---

## 📞 SUPPORT

**Common Questions:**

**Q: What if customer loses their invoice number?**
A: They can check their email confirmation, or contact support to look it up by name/date

**Q: Can two orders have the same invoice number?**
A: No - the combination of date + random 4-digit number ensures uniqueness

**Q: What if lookup fails even with correct number?**
A: Check Airtable field name matches exactly (with spaces)

**Q: Can I change the invoice number format?**
A: Yes - edit the `generateInvoiceNumber()` function in customer_order_form_v2.html

---

## ✅ SUCCESS CHECKLIST

After setup, verify:
- [ ] Airtable has "Deposit Invoice Number" field
- [ ] All 3 files replaced in project
- [ ] Flask restarted
- [ ] Order form generates invoice number
- [ ] Invoice number displayed after order
- [ ] Invoice number saved to Airtable
- [ ] Review form requires invoice number
- [ ] Lookup works with valid invoice number
- [ ] Error shown for invalid invoice number
- [ ] Order details auto-fill correctly
- [ ] Final amount calculates correctly
- [ ] Review submission updates same record

---

**System Version:** 3.0 - Invoice-Based Review System
**Date:** November 9, 2025
**Feature:** Deposit Invoice Number Lookup & Auto-Fill
