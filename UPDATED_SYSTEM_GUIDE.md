# UPDATED SYSTEM GUIDE - November 2025
## Changes: Separate Order/Review Forms + Shipping Type + Final Amount

---

## 🔄 WHAT'S CHANGED

### 1. **Customer Portal Redesigned**
   - Order Form and Review Form are now **separate options**
   - No automatic redirect between forms
   - Users can access either form independently
   - Both accessible from Customer Login page

### 2. **Shipping Type Field Added**
   - New dropdown in Order Form
   - 6 shipping options available
   - Required field

### 3. **Review Form Updates**
   - Shows **Final Amount to be Paid** (Order Total - Deposit)
   - Added 3 new Yes/No dropdowns
   - Can be filled independently (doesn't require order submission first)

### 4. **UI Text Changes**
   - Removed all mentions of "Airtable" from user-facing pages
   - Changed button text to be more user-friendly
   - Cleaner, more professional appearance

---

## 📁 FILES TO REPLACE

Replace these 4 files in your project:

1. **customer_login.html** - Updated with Order/Review options
2. **customer_order_form.html** - Added shipping type, removed auto-redirect
3. **customer_review_form.html** - Added final amount + 3 Yes/No fields
4. **app.py** - Updated backend to handle new fields

Keep all other files the same (no changes needed).

---

## 🗂️ NEW AIRTABLE FIELDS REQUIRED

Add these fields to your **Master Database** table in Airtable:

### New Order Field:
| Field Name | Field Type | Options |
|------------|------------|---------|
| Shipping Type | Single line text | - |

### New Review Fields:
| Field Name | Field Type | Options |
|------------|------------|---------|
| On Time and In Full | Single line text | - |
| Short Shipment | Single line text | - |
| Delivered Late | Single line text | - |

**Note:** These will store "Yes" or "No" as text values.

---

## 🎯 USER FLOW - BEFORE vs AFTER

### BEFORE (Old Flow):
```
Customer Login → Order Form → Auto-redirect → Review Form
```

### AFTER (New Flow):
```
Customer Login → Choose: [Order Form] OR [Review Form]
```

Users can now:
- Submit an order WITHOUT filling a review
- Submit a review WITHOUT having an order
- Fill review form independently any time

---

## 📋 SHIPPING TYPE OPTIONS

The dropdown includes 6 options:
1. **Sea LCL**
2. **Air-Direct**
3. **Small Parcel**
4. **Free of Charge**
5. **China Store**
6. **Exp Air**

This field is **required** in the order form.

---

## 💰 FINAL AMOUNT CALCULATION

**Review Form now displays:**
- Order Total (from previous order)
- Deposit Amount (already paid)
- **Final Amount to be Paid** = Total - Deposit

**Example:**
- Order Total: $2,500.00
- Deposit Paid: $750.00
- **Final Amount: $1,750.00** ← Shown prominently

**Note:** If no order data is available (standalone review), shows $0.00

---

## ✅ NEW YES/NO FIELDS IN REVIEW FORM

### 1. On Time and In Full
- **Question:** Was the delivery on time and complete?
- **Options:** Yes / No

### 2. Short Shipment
- **Question:** Was the shipment short (missing items)?
- **Options:** Yes / No

### 3. Delivered Late
- **Question:** Was the delivery late?
- **Options:** Yes / No

All three are **required** fields with dropdown selection.

---

## 🚀 SETUP INSTRUCTIONS

### Step 1: Update Airtable Fields
1. Go to your Airtable base
2. Open **Master Database** table
3. Add these 4 new fields:
   - Shipping Type (Single line text)
   - On Time and In Full (Single line text)
   - Short Shipment (Single line text)
   - Delivered Late (Single line text)

### Step 2: Replace Files
Replace these 4 files in your project folder:
```
pdf-to-airtable/
├── customer_login.html ✅ REPLACE
├── customer_order_form.html ✅ REPLACE
├── customer_review_form.html ✅ REPLACE
└── app.py ✅ REPLACE
```

### Step 3: Test
1. Restart Flask: `py app.py`
2. Go to: http://localhost:5000
3. Click "Customer Portal"
4. Test both Order Form and Review Form

---

## 🧪 TESTING CHECKLIST

### Order Form:
- [ ] Can select shipping type (6 options)
- [ ] All existing fields still work
- [ ] Demo button fills shipping type
- [ ] No auto-redirect after submission
- [ ] Shows success message
- [ ] Returns to Customer Portal

### Review Form:
- [ ] Can access directly from Customer Login
- [ ] Shows final amount calculation (if order exists)
- [ ] All 3 Yes/No dropdowns work
- [ ] Can submit without order data
- [ ] Shows success message
- [ ] Returns to Customer Portal

### Data Verification:
- [ ] Order saves to Airtable with shipping type
- [ ] Review saves with 3 new Yes/No fields
- [ ] No errors in browser console
- [ ] No errors in Flask terminal

---

## 📊 FIELD MAPPING REFERENCE

### Order Form → Airtable:
| Form Field | Airtable Field | Type |
|------------|----------------|------|
| customerName | Customer Name | Text |
| productDescription | Product Description | Text |
| **shippingType** | **Shipping Type** | **Text** ← NEW |
| unitPrice | Unit Price | Text |
| stockSKU | Stock SKU Number | Text |
| depositPercent | Deposit % | Text |
| unitsToOrder | Units to Order | Number |
| newProduct | New Product | Checkbox |
| pressCheck | Press Check | Checkbox |
| updateArtwork | Update Artwork | Checkbox |
| toleranceOrder | 5% Tolerance Order | Checkbox |
| orderTotal | Order Total | Text |
| depositAmount | Deposit Amount | Text |

### Review Form → Airtable:
| Form Field | Airtable Field | Type |
|------------|----------------|------|
| actualUnitsReceived | Actual Units Received | Number |
| dateGoodsReceived | Date Goods Received Warehouse | Date |
| qualityRejects | Quality Rejects on Inspection | Number |
| authorisedInvoice | Authorised Invoice | Checkbox |
| expectedPaymentDate | Expected Payment Date | Date |
| **onTimeInFull** | **On Time and In Full** | **Text** ← NEW |
| **shortShipment** | **Short Shipment** | **Text** ← NEW |
| **deliveredLate** | **Delivered Late** | **Text** ← NEW |

---

## 🎨 UI IMPROVEMENTS

### Text Changes:
| Old Text | New Text |
|----------|----------|
| "Saves to Airtable" | "Submit Order" |
| "Demo Submit (Test Airtable)" | "Demo Submit (Test)" |
| "Redirecting to Review Form..." | "Thank you for your order!" |
| Various Airtable mentions | Removed from UI |

### Navigation Changes:
- Success messages now link back to Customer Portal
- No automatic redirects between forms
- Clear separation between Order and Review processes

---

## 💡 USAGE SCENARIOS

### Scenario 1: Complete Order Flow
1. Customer logs in
2. Clicks "Order Form"
3. Fills order details + shipping type
4. Submits order
5. Returns to portal
6. (Later) Clicks "Review Form"
7. Fills review + Yes/No fields
8. Submits review

### Scenario 2: Review Only
1. Customer logs in
2. Clicks "Review Form" directly
3. Fills review manually
4. Selects Yes/No for delivery questions
5. Submits (creates new record or updates existing)

### Scenario 3: Order Only
1. Customer logs in
2. Clicks "Order Form"
3. Submits order
4. Done (no review required)

---

## 🔧 TROUBLESHOOTING

### "Shipping Type field not found in Airtable"
- **Fix:** Add "Shipping Type" field to Master Database table
- Must be "Single line text" type

### "On Time and In Full field not found"
- **Fix:** Add all 3 new fields to Airtable:
  - On Time and In Full
  - Short Shipment
  - Delivered Late

### Order submits but shipping type is empty
- **Check:** Field name in Airtable is exactly "Shipping Type" (with space)
- **Check:** Dropdown selection is required in form

### Final amount shows $0.00
- **Reason:** No order data in session storage
- **Expected:** Normal for standalone reviews
- **Fix:** Submit an order first to see calculation

### Review form can't update order
- **Check:** Order ID is stored in session
- **Workaround:** Review form now creates new record if no order ID

---

## 📝 DEMO DATA

Use the demo button in Order Form. It now fills:
- Customer Name: Demo Customer
- Product: Lipstick - Matte Finish
- **Shipping Type: Sea LCL** ← NEW
- Units: 100
- New Product: ✓
- Update Artwork: ✓

Total: $2,500.00
Deposit: $750.00
**Final Amount: $1,750.00**

---

## 🎉 WHAT'S BETTER NOW

✅ **Independent Forms** - Order and Review can be used separately
✅ **More Shipping Options** - 6 types to choose from
✅ **Clear Payment Info** - Final amount shown upfront
✅ **Better Delivery Tracking** - 3 Yes/No fields for assessment
✅ **Cleaner UI** - No technical jargon visible to users
✅ **Flexible Workflow** - Users choose their path

---

## 📞 SUPPORT

If you encounter issues:
1. Check browser console (F12)
2. Check Flask terminal output
3. Verify all 4 Airtable fields exist
4. Confirm field names match exactly (including spaces)
5. Restart Flask after any .env changes

---

**System Version:** 2.0 (November 2025)
**Last Updated:** User request - Separate forms + Shipping + Final amount + Yes/No fields
