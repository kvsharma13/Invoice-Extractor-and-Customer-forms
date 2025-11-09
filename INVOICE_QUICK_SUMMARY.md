# QUICK SUMMARY - Invoice-Based Review System

---

## ✨ WHAT CHANGED

The Review Form now requires a **Deposit Invoice Number** for access. This number is auto-generated when orders are submitted and must be entered to view and fill the review form.

---

## 📦 3 NEW FILES

1. **customer_order_form_v2.html** - Generates & shows invoice number
2. **customer_review_form_v2.html** - Invoice lookup required
3. **app_v2.py** - Backend with lookup endpoint

---

## 🎯 HOW IT WORKS NOW

### Order Flow:
```
1. Customer fills order form
2. Submits order
3. System generates: INV-20251109-3847
4. Saves to Airtable
5. Shows invoice number on success screen
   "Save this number for your review!"
```

### Review Flow:
```
1. Customer opens review form
2. Enters Deposit Invoice Number
3. Clicks "Search"
4. System finds order in Airtable
5. Auto-fills:
   • Customer name
   • Product
   • Deposit paid
   • Final amount to pay
6. Customer fills review fields
7. Submits → updates same record
```

---

## ⚡ QUICK SETUP (3 STEPS)

### 1. Add Airtable Field
- Open Master Database table
- Add field: **Deposit Invoice Number**
- Type: Single line text

### 2. Replace Files
```
customer_order_form.html  → customer_order_form_v2.html
customer_review_form.html → customer_review_form_v2.html
app.py                    → app_v2.py
```

### 3. Test
```bash
py app.py
```
- Submit test order → Get invoice number
- Enter in review form → Verify auto-fill

**Done! 🎉**

---

## 🔑 KEY FEATURES

✅ **Unique Invoice Number** per order (e.g., INV-20251109-3847)
✅ **Auto-generated** when order submitted
✅ **Displayed prominently** after order submission
✅ **Required** to access review form
✅ **Auto-fills** order details from Airtable
✅ **Calculates** final amount to pay
✅ **Updates** same Airtable record

---

## 💡 BENEFITS

### Customer:
- Easy order tracking
- Know exact amount left to pay
- One number for everything

### Business:
- Professional invoice system
- Better order tracking
- Linked order & review data

---

## 🧪 QUICK TEST

1. Submit order → Note invoice number shown
2. Go to review form
3. Enter invoice number → Click Search
4. ✅ Check: Order details auto-fill
5. ✅ Check: Final amount shows correctly
6. Fill review → Submit
7. ✅ Check: Airtable record updated

---

## ⚠️ IMPORTANT

**Airtable Field Name Must Be Exact:**
- ✅ Correct: `Deposit Invoice Number`
- ❌ Wrong: `DepositInvoiceNumber`
- ❌ Wrong: `Deposit_Invoice_Number`

**Spacing matters!**

---

## 📄 FULL DOCUMENTATION

For complete details, read:
→ **INVOICE_SYSTEM_GUIDE.md**

---

That's it! Simple 3-step setup for a powerful invoice-based review system. 🚀
