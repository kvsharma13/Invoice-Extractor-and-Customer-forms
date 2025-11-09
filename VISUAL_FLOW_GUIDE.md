# VISUAL FLOW DIAGRAM - NEW CUSTOMER PORTAL

---

## 🎨 NEW USER FLOW

```
┌─────────────────────────────────────────────────────────┐
│                   PORTAL SELECTION                       │
│              http://localhost:5000/                      │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │   Customer   │  │    Admin     │  │   Supplier   │ │
│  │    Portal    │  │   Portal     │  │   Portal     │ │
│  │   (Active)   │  │   (Active)   │  │ (Maintenance)│ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────────┐
│                   CUSTOMER LOGIN                         │
│              /customer-login                             │
│                                                          │
│  Email: ________________                                 │
│  Password: _____________                                 │
│                                                          │
│  ┌──────────────────────────┐                          │
│  │      Sign In             │                          │
│  └──────────────────────────┘                          │
│                                                          │
│           OR                                             │
│                                                          │
│  Continue as Guest:                                      │
│  ┌──────────────┐  ┌──────────────┐                    │
│  │ 📝 Order     │  │ ⭐ Review    │                    │
│  │   Form       │  │    Form      │                    │
│  └──────────────┘  └──────────────┘                    │
└─────────────────────────────────────────────────────────┘
       │                    │
       │                    │
       ▼                    ▼
┌─────────────────┐  ┌─────────────────┐
│   ORDER FORM    │  │  REVIEW FORM    │
│  /customer-order│  │ /customer-review│
└─────────────────┘  └─────────────────┘
```

---

## 📝 ORDER FORM DETAILS

```
┌────────────────────────────────────────────────────────┐
│              CUSTOMER ORDER FORM                        │
│                                                         │
│  Step 1: Order Details                                 │
│  ─────────────────────────────────────                │
│                                                         │
│  Customer Name: ____________________                   │
│  Product: [Select Product ▼]                           │
│                                                         │
│  ⭐ NEW FIELD:                                         │
│  Shipping Type: [Select Type ▼]                        │
│    • Sea LCL                                           │
│    • Air-Direct                                        │
│    • Small Parcel                                      │
│    • Free of Charge                                    │
│    • China Store                                       │
│    • Exp Air                                           │
│                                                         │
│  Unit Price: $25.00 (auto-filled)                      │
│  SKU: SKU-LIP-001 (auto-filled)                        │
│  Deposit %: 30% (auto-filled)                          │
│  Units to Order: ___                                    │
│                                                         │
│  Order Options:                                         │
│  ☐ New Product    ☐ Press Check                       │
│  ☐ Update Artwork ☐ 5% Tolerance Order                │
│                                                         │
│  [Continue to Payment →]                               │
│                                                         │
├────────────────────────────────────────────────────────┤
│                                                         │
│  Step 2: Payment Summary                               │
│  ─────────────────────────────────────                │
│                                                         │
│  Product: Lipstick - Matte Finish                      │
│  Shipping Type: Sea LCL                                │
│  Units: 100                                            │
│  Unit Price: $25.00                                    │
│  Order Total: $2,500.00                                │
│  Deposit %: 30%                                        │
│  Deposit Amount: $750.00                               │
│                                                         │
│  [💳 Pay Deposit & Submit Order]                      │
│  [🎯 Demo Submit (Test)]                              │
│  [✕ Cancel Order]                                      │
│                                                         │
├────────────────────────────────────────────────────────┤
│                                                         │
│  Success Message:                                       │
│  ✅ Order Placed Successfully!                         │
│  Your order has been submitted successfully.            │
│                                                         │
│  ⭐ CHANGED: No auto-redirect                          │
│                                                         │
│  [Back to Customer Portal]                             │
│                                                         │
└────────────────────────────────────────────────────────┘
```

---

## ⭐ REVIEW FORM DETAILS

```
┌────────────────────────────────────────────────────────┐
│             CUSTOMER REVIEW FORM                        │
│                                                         │
│  ⭐ NEW: Final Amount Display                          │
│  ┌──────────────────────────────────────────────────┐ │
│  │ 📦 Your Order                                     │ │
│  │ Customer: Demo Customer                           │ │
│  │ Product: Lipstick - Matte Finish                  │ │
│  │ Order ID: recXXXX...                              │ │
│  │                                                    │ │
│  │ ┌────────────────────────────────────────────┐   │ │
│  │ │ Final Amount to be Paid:                    │   │ │
│  │ │ $1,750.00                                   │   │ │
│  │ │ (Order Total - Deposit Paid)                │   │ │
│  │ └────────────────────────────────────────────┘   │ │
│  └──────────────────────────────────────────────────┘ │
│                                                         │
│  Review & Receipt Information                           │
│  ─────────────────────────────────────                │
│                                                         │
│  Actual Units Received: ___                            │
│  Date Goods Received Warehouse: [Date ▼]              │
│  Quality Rejects on Inspection: ___                    │
│  ☐ Authorised Invoice                                 │
│  Expected Payment Date: [Date ▼]                       │
│                                                         │
│  ⭐ NEW: Delivery Assessment                           │
│  ─────────────────────────────────────                │
│                                                         │
│  On Time and In Full: [Select ▼]                       │
│    • Yes                                               │
│    • No                                                │
│                                                         │
│  Short Shipment: [Select ▼]                            │
│    • Yes                                               │
│    • No                                                │
│                                                         │
│  Delivered Late: [Select ▼]                            │
│    • Yes                                               │
│    • No                                                │
│                                                         │
│  [Submit Review →]                                     │
│                                                         │
├────────────────────────────────────────────────────────┤
│                                                         │
│  Success Message:                                       │
│  ✅ Review Submitted Successfully!                     │
│  Your review has been saved.                           │
│                                                         │
│  [Back to Customer Portal]                             │
│                                                         │
└────────────────────────────────────────────────────────┘
```

---

## 📊 DATA FLOW TO AIRTABLE

### ORDER SUBMISSION:
```
Order Form
    ↓
{
    customerName: "Demo Customer",
    productDescription: "Lipstick",
    shippingType: "Sea LCL",      ← NEW
    unitPrice: "$25.00",
    stockSKU: "SKU-LIP-001",
    depositPercent: "30%",
    unitsToOrder: 100,
    newProduct: true,
    pressCheck: false,
    updateArtwork: true,
    toleranceOrder: false,
    orderTotal: "$2,500.00",
    depositAmount: "$750.00"
}
    ↓
Master Database (Airtable)
    ↓
Returns: record_id = "recXXXXXXXXX"
    ↓
Stored in Session Storage
```

### REVIEW SUBMISSION:
```
Review Form
    ↓
{
    orderId: "recXXXXXXXXX",
    actualUnitsReceived: 100,
    dateGoodsReceived: "2025-11-10",
    qualityRejects: 2,
    authorisedInvoice: true,
    expectedPaymentDate: "2025-12-01",
    onTimeInFull: "Yes",          ← NEW
    shortShipment: "No",           ← NEW
    deliveredLate: "No"            ← NEW
}
    ↓
Updates existing record in Master Database
OR
Creates new record if no orderId
```

---

## 🎯 USE CASES

### Case 1: Complete Flow
```
User → Customer Login
     → Order Form
     → Submit Order
     → (Stores order_id in session)
     → Back to Portal
     → Review Form
     → (Uses stored order_id)
     → Submit Review
     → Updates same record
```

### Case 2: Review Only
```
User → Customer Login
     → Review Form (directly)
     → Fill manually
     → Submit
     → Creates new record
```

### Case 3: Order Only
```
User → Customer Login
     → Order Form (directly)
     → Submit Order
     → Done (no review needed)
```

---

## 💾 SESSION STORAGE DATA

**After Order Submission:**
```javascript
sessionStorage = {
    orderId: "recXXXXXXXXX",
    customerName: "Demo Customer",
    productDescription: "Lipstick - Matte Finish",
    orderTotal: "$2,500.00",       ← NEW
    depositAmount: "$750.00"        ← NEW
}
```

**Used in Review Form to:**
1. Display order information
2. Calculate final amount
3. Update the correct record

---

## 🔄 KEY DIFFERENCES FROM OLD SYSTEM

| Aspect | Old System | New System |
|--------|-----------|------------|
| **Navigation** | Linear (Order→Review) | Choice-based |
| **Auto-redirect** | Yes, after 3 seconds | No |
| **Forms** | Sequential | Independent |
| **Shipping** | Not tracked | 6 types |
| **Payment Info** | Deposit only | Shows final amount |
| **Delivery Info** | Basic fields | 3 Yes/No questions |
| **Flexibility** | Low | High |

---

This visual guide shows the complete new flow! 🎨
