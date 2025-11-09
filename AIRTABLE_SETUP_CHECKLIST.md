# AIRTABLE SETUP CHECKLIST
## Add These 4 Fields to Your Master Database Table

---

## 📋 STEP-BY-STEP INSTRUCTIONS

### 1. Open Your Airtable Base
- Go to Airtable.com
- Open your base (the one with Base ID in your .env file)
- Open the **Master Database** table

---

## ✅ FIELD 1: Shipping Type

**Field Name:** `Shipping Type`
**Field Type:** Single line text

**Steps:**
1. Click the **+** button at the top right of your table
2. Name the field: `Shipping Type` (exactly as shown, with space)
3. Select field type: **Single line text**
4. Click "Create field"

**What It Stores:** 
- Sea LCL
- Air-Direct
- Small Parcel
- Free of Charge
- China Store
- Exp Air

---

## ✅ FIELD 2: On Time and In Full

**Field Name:** `On Time and In Full`
**Field Type:** Single line text

**Steps:**
1. Click the **+** button
2. Name the field: `On Time and In Full` (exactly as shown, with spaces)
3. Select field type: **Single line text**
4. Click "Create field"

**What It Stores:** 
- Yes
- No

---

## ✅ FIELD 3: Short Shipment

**Field Name:** `Short Shipment`
**Field Type:** Single line text

**Steps:**
1. Click the **+** button
2. Name the field: `Short Shipment` (exactly as shown, with space)
3. Select field type: **Single line text**
4. Click "Create field"

**What It Stores:** 
- Yes
- No

---

## ✅ FIELD 4: Delivered Late

**Field Name:** `Delivered Late`
**Field Type:** Single line text

**Steps:**
1. Click the **+** button
2. Name the field: `Delivered Late` (exactly as shown, with space)
3. Select field type: **Single line text**
4. Click "Create field"

**What It Stores:** 
- Yes
- No

---

## 🎯 QUICK VERIFICATION

After adding all 4 fields, your **Master Database** table should have these columns:

### Existing Order Fields (13):
- ✓ Created Date
- ✓ Customer Name
- ✓ Product Description
- ✓ Unit Price
- ✓ Stock SKU Number
- ✓ Deposit %
- ✓ New Product
- ✓ Press Check
- ✓ Update Artwork
- ✓ 5% Tolerance Order
- ✓ Units to Order
- ✓ Order Total
- ✓ Deposit Amount

### Existing Review Fields (5):
- ✓ Actual Units Received
- ✓ Date Goods Received Warehouse
- ✓ Quality Rejects on Inspection
- ✓ Authorised Invoice
- ✓ Expected Payment Date

### NEW Fields (4):
- ⭐ **Shipping Type** ← ORDER FIELD
- ⭐ **On Time and In Full** ← REVIEW FIELD
- ⭐ **Short Shipment** ← REVIEW FIELD
- ⭐ **Delivered Late** ← REVIEW FIELD

**Total Fields:** 22 fields

---

## ⚠️ IMPORTANT NOTES

### Field Names MUST Match Exactly:
- ❌ Wrong: `ShippingType` (no space)
- ✅ Correct: `Shipping Type` (with space)

- ❌ Wrong: `OnTimeAndInFull` (no spaces)
- ✅ Correct: `On Time and In Full` (with spaces)

- ❌ Wrong: `Short-Shipment` (hyphen)
- ✅ Correct: `Short Shipment` (space)

- ❌ Wrong: `DeliveredLate` (no space)
- ✅ Correct: `Delivered Late` (with space)

### Field Types:
- All 4 new fields should be **Single line text**
- Do NOT use "Single select" or "Multiple select"
- The form will send "Yes" or "No" as text

---

## 🧪 TEST YOUR SETUP

### Test 1: Submit an Order
1. Go to http://localhost:5000
2. Customer Portal → Order Form
3. Fill the form and select a shipping type
4. Submit
5. **Check Airtable:** The "Shipping Type" column should have a value

### Test 2: Submit a Review
1. Customer Portal → Review Form
2. Fill all fields including the 3 Yes/No dropdowns
3. Submit
4. **Check Airtable:** The 3 new columns should have "Yes" or "No"

---

## 📸 VISUAL REFERENCE

Your Airtable table structure should look like this:

```
┌──────────────┬──────────────┬─────────────┬──────────────┬─────────┐
│ Customer Name│  Product     │ Shipping    │ Units to     │ Order   │
│              │ Description  │ Type        │ Order        │ Total   │
├──────────────┼──────────────┼─────────────┼──────────────┼─────────┤
│ Demo Customer│ Lipstick     │ Sea LCL     │ 100          │ $2,500  │
│ John Smith   │ Face Cream   │ Air-Direct  │ 50           │ $2,250  │
└──────────────┴──────────────┴─────────────┴──────────────┴─────────┘

... (more columns) ...

┌──────────────┬──────────────┬──────────────┐
│ On Time and  │ Short        │ Delivered    │
│ In Full      │ Shipment     │ Late         │
├──────────────┼──────────────┼──────────────┤
│ Yes          │ No           │ No           │
│ No           │ Yes          │ Yes          │
└──────────────┴──────────────┴──────────────┘
```

---

## 🚨 COMMON ERRORS

### Error: "Unknown field name: 'Shipping Type'"
**Cause:** Field doesn't exist in Airtable
**Fix:** Add the field as shown above

### Error: "Unknown field name: 'ShippingType'"
**Cause:** Field name doesn't match (missing space)
**Fix:** Rename to `Shipping Type` with space

### Error: "Invalid value for column"
**Cause:** Field type is wrong (e.g., number instead of text)
**Fix:** Change field type to "Single line text"

---

## ✅ FINAL CHECKLIST

Before testing your updated system:

- [ ] Opened correct Airtable base
- [ ] Opened "Master Database" table
- [ ] Added "Shipping Type" field (Single line text)
- [ ] Added "On Time and In Full" field (Single line text)
- [ ] Added "Short Shipment" field (Single line text)
- [ ] Added "Delivered Late" field (Single line text)
- [ ] Verified all field names have correct spacing
- [ ] Verified all fields are "Single line text" type
- [ ] Replaced 4 files in project folder
- [ ] Restarted Flask application

---

**You're all set!** Your Airtable is ready for the updated forms. 🎉
