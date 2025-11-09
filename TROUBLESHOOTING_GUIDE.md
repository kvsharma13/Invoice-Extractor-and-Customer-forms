# REVIEW FORM TROUBLESHOOTING GUIDE

---

## 🔧 COMMON ERRORS & FIXES

### ❌ "Connection error. Please check your internet and try again."

This error appears when the frontend cannot connect to the backend.

**Possible Causes:**

1. **Flask is not running**
   - **Check:** Look at your terminal/command prompt
   - **Fix:** Run `py app.py` or `python app.py`
   - **Verify:** You should see "Running on http://127.0.0.1:5000"

2. **Wrong endpoint URL**
   - **Check:** Browser console (F12 → Console tab) for 404 errors
   - **Fix:** Ensure app_v2.py has `/submit-review` endpoint

3. **Port mismatch**
   - **Check:** Flask running on port 5000
   - **Fix:** Access via http://localhost:5000, not other ports

4. **CORS issues**
   - **Check:** Browser console for CORS errors
   - **Fix:** Ensure `CORS(app)` is in app_v2.py

**How to Debug:**

```bash
# Step 1: Check Flask is running
py app.py

# Step 2: You should see:
# * Running on http://127.0.0.1:5000

# Step 3: Open browser console (F12)
# Look for red error messages

# Step 4: Try the endpoint directly:
# Open: http://localhost:5000/customer-review
```

---

### ❌ "Invoice number not found"

**Possible Causes:**

1. **Invoice number doesn't exist in Airtable**
   - **Check:** Open Airtable → Master Database table
   - **Verify:** Search for the invoice number in "Deposit Invoice Number" column
   - **Fix:** Make sure you submitted an order first

2. **Field name mismatch**
   - **Check:** Airtable field name is exactly: `Deposit Invoice Number`
   - **Fix:** Rename field if it's different (include the space!)

3. **Wrong table name**
   - **Check:** `.env` file has correct table name
   - **Fix:** `AIRTABLE_ORDERS_TABLE=Master Database` (or your table name)

**How to Debug:**

```python
# Check Flask terminal output
# Should show: "Invoice lookup successful! Found record: recXXXX"
# If you see error, that's the issue
```

---

### ❌ "Field 'Deposit Invoice Number' not found"

**This is an Airtable field error.**

**Fix:**
1. Open Airtable base
2. Go to Master Database table
3. Add field: `Deposit Invoice Number`
4. Type: **Single line text**
5. Restart Flask

**Verify:**
- Field name has a **space**: `Deposit Invoice Number`
- NOT: `DepositInvoiceNumber` or `Deposit_Invoice_Number`

---

### ❌ "Record ID is required"

**Possible Causes:**

1. **Invoice lookup didn't complete**
   - **Fix:** Make sure you searched and found an order first
   - **Check:** Hidden field `<input id="recordId">` should have a value

2. **Form submitted before lookup finished**
   - **Fix:** Wait for "Order found!" message before filling form

**How to Debug:**

```javascript
// In browser console (F12), type:
document.getElementById('recordId').value

// Should return something like: "recXXXXXXXXX"
// If empty "", the lookup didn't work
```

---

### ❌ Form submits but nothing happens

**Possible Causes:**

1. **JavaScript error**
   - **Check:** Browser console (F12 → Console tab)
   - **Look for:** Red error messages

2. **Response not being handled**
   - **Check:** Network tab (F12 → Network)
   - **Look for:** `/submit-review` request
   - **Verify:** Response is 200 OK

**How to Debug:**

```javascript
// Check console logs:
// Should show:
// 📤 Submitting review: {...}
// 📥 Response: {success: true, ...}
```

---

### ❌ Success shows but Airtable not updated

**Possible Causes:**

1. **Wrong record ID**
   - **Check:** Flask terminal shows the record ID being updated
   - **Verify:** Record ID exists in Airtable

2. **Airtable API error**
   - **Check:** Flask terminal for error messages
   - **Verify:** API key is correct in `.env`

3. **Field name mismatch**
   - **Check:** All review field names match exactly in Airtable
   - **Fix:** See field list below

**Required Airtable Fields:**
```
✓ Actual Units Received (Number)
✓ Date Goods Received Warehouse (Date)
✓ Quality Rejects on Inspection (Number)
✓ Authorised Invoice (Checkbox)
✓ Expected Payment Date (Date)
✓ On Time and In Full (Single line text)
✓ Short Shipment (Single line text)
✓ Delivered Late (Single line text)
```

---

### ❌ "Server error: 500"

**This is a backend error.**

**How to Debug:**

1. **Check Flask terminal**
   - Look for red error traceback
   - Read the error message

2. **Common causes:**
   - Airtable API key expired
   - Field name mismatch
   - Data type mismatch

**Example Fix:**

```python
# If you see: "Unknown field name: 'On Time and In Full'"
# Fix: Add the field to Airtable
```

---

## 🔍 DEBUGGING CHECKLIST

When review form doesn't work, check in this order:

### 1. Flask Backend
- [ ] Flask is running (`py app.py`)
- [ ] No errors in Flask terminal
- [ ] Correct endpoints exist (`/lookup-invoice`, `/submit-review`)

### 2. Browser Console
- [ ] Open DevTools (F12)
- [ ] Check Console tab for JavaScript errors
- [ ] Check Network tab for failed requests

### 3. Airtable
- [ ] Field "Deposit Invoice Number" exists
- [ ] All review fields exist
- [ ] Field names match exactly (with spaces)
- [ ] Record with invoice number exists

### 4. .env File
- [ ] AIRTABLE_API_KEY is correct
- [ ] AIRTABLE_BASE_ID is correct
- [ ] AIRTABLE_ORDERS_TABLE matches your table name

---

## 🛠️ QUICK FIXES

### Fix 1: Restart Everything
```bash
# 1. Stop Flask (Ctrl+C)
# 2. Restart Flask
py app.py

# 3. Refresh browser (Ctrl+F5)
```

### Fix 2: Clear Browser Cache
```
# Chrome/Edge:
Ctrl+Shift+Delete → Clear cached images and files

# Firefox:
Ctrl+Shift+Delete → Cached Web Content
```

### Fix 3: Check File Versions
```bash
# Make sure you're using the updated files:
# - customer_review_form_v2.html (not v1)
# - app_v2.py (not app.py)
```

### Fix 4: Verify Endpoints
```bash
# Test lookup endpoint:
curl -X POST http://localhost:5000/lookup-invoice \
  -H "Content-Type: application/json" \
  -d '{"invoiceNumber":"INV-20251109-1234"}'

# Should return: {"success": true, "recordId": "...", ...}
# Or: {"success": false, "error": "..."}
```

---

## 📝 TESTING FLOW

**Complete test to verify everything works:**

```
1. Submit a test order
   ↓
2. Note the invoice number shown
   ↓
3. Go to Airtable
   ↓
4. Verify invoice number is in the record
   ↓
5. Go to review form
   ↓
6. Enter invoice number
   ↓
7. Click "Search"
   ↓
8. Check browser console for logs:
   - Should see: "Invoice lookup successful!"
   ↓
9. Verify order details auto-fill
   ↓
10. Fill review form
   ↓
11. Submit
   ↓
12. Check browser console for:
    - 📤 Submitting review: {...}
    - 📥 Response: {success: true}
   ↓
13. Check Flask terminal for:
    - "Review submitted! Updated record: recXXXX"
   ↓
14. Check Airtable
    - Same record should have review data
```

---

## 🆘 STILL NOT WORKING?

**Collect this information:**

1. **Error message** (exact text)
2. **Browser console** screenshot (F12 → Console)
3. **Flask terminal** output
4. **Airtable fields** screenshot
5. **Which step fails** (lookup or submit)

**Then check:**
- All field names in Airtable match exactly
- Flask is running without errors
- Correct files are being used (v2 versions)
- .env file has correct credentials

---

## ✅ SUCCESS INDICATORS

**You know it's working when:**

✅ Flask terminal shows: "Running on http://127.0.0.1:5000"
✅ Invoice lookup shows: "✅ Order found!"
✅ Order details auto-fill correctly
✅ Form submission shows: "✅ Review submitted successfully!"
✅ Flask terminal shows: "Review submitted! Updated record: recXXXX"
✅ Airtable record has all review data
✅ No errors in browser console
✅ No errors in Flask terminal

---

**Most common issue:** Field name mismatch in Airtable. Always check spelling and spaces!
