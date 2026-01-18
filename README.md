# Contact Management System with Weather Integration

A professional recruitment task built with **Django**, featuring a robust contact database, dynamic weather updates, and bulk data processing.

## 🚀 Key Features

### 1. Contact Management (CRUD)
* **Full CRUD Operations**: Efficiently Create, Read, Update, and Delete contacts.
* **Search & Filter**: Real-time searching by first name, last name, or email.
* **Smart Sorting**: Toggle views between alphabetical order (last name) or latest additions.
* **User Experience**: Integrated Bootstrap modals for deletion confirmation to prevent accidental data loss.

### 2. Weather Integration (AJAX + Caching)
* **Live Weather Data**: Fetches current temperature, humidity, and wind speed for each contact's city using the **Open-Meteo API**.
* **Performance Optimization**: Implements `localStorage` caching. Weather data is stored for 15 minutes to minimize external API calls and ensure lightning-fast page reloads.

### 3. Bulk Data Import (CSV)
* **Automated Importer**: A dedicated tool to upload and process `.csv` files.
* **Data Integrity**: Features "upsert" logic—it automatically updates existing records based on email or creates new ones, ensuring no duplicate entries.
* **Smart Relations**: Automatically handles and creates `ContactStatus` relationships during the import process.

### 4. REST API
* **Django REST Framework**: Fully documented API endpoints available at `/api/contacts/`.
* **Standard Methods**: Supports GET, POST, PUT, and DELETE for seamless third-party integration.

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd supra_project
   
2. **Install dependencies:**:
   ```bash
   pip install -r requirements.txt
   
3. **Run the application**:
   ```bash
   python manage.py runserver
   
## 📥 Testing the Import Feature

A sample file named `test_contacts.csv` is included in the root directory for immediate testing.

**How to test:**

1.  **Navigate** to the **Import CSV** page in the application.
2.  **Select** the `test_contacts.csv` file from your project folder.
3.  **Submit** the form. The system is programmed to skip the header row and correctly map all contact fields.

---

## 🛠️ Tech Stack

* **Backend**: Python 3.x, Django 5.x, Django REST Framework.
* **Frontend**: Bootstrap 5, Vanilla JavaScript (Fetch API, LocalStorage).
* **External APIs**: Open-Meteo (Weather), Nominatim (Geocoding).