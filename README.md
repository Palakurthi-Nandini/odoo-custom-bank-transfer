# odoo-custom-bank-transfer
# Bank Transfer Payment Option for Odoo 17

This module adds a custom payment option to your Odoo 17 e-commerce website, allowing customers to pay via **Bank Transfer (NEFT/IMPS)**. It includes a user-friendly popup modal to display vendor bank details and allows the customer to upload payment proof.

---

## 🚀 Features

- Adds a new **"Transfer to Bank via NEFT/IMPS"** payment option at checkout
- Displays vendor bank information:
  - Bank Name
  - Account Number
  - IFSC Code
  - Branch
  - QR Code (optional image)
- Shows total order amount (including and excluding tax)
- Allows customer to:
  - Upload a screenshot of the transaction
  - Enter a transfer reference number
  - Add additional comments

---

## 🏗️ Module Structure

payment_bank_transfer_custom/ 
├── controllers/ # HTTP route for handling payment submission 
├── models/ # Custom model to store bank transfer info 
├── static/src/js/ # Frontend popup logic (JavaScript) 
├── views/ # Form view and template popup
├── security/ # Access control 
├── init.py 
├── manifest.py
