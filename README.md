# Contact Management System with Weather Integration

A Django-based contact management application which features full CRUD operations, live weather data for each contact's city via Open-Meteo API, bulk CSV import with upsert logic, and a REST API powered by Django REST Framework.

## Tech Stack

- **Backend:** Python 3.x, Django 5.x, Django REST Framework
- **Frontend:** Bootstrap 5, Vanilla JavaScript (Fetch API, localStorage)
- **External APIs:** Open-Meteo (weather), Nominatim (geocoding)
- **Containerization:** Docker

## Features

### Contact Management (CRUD)
- Full Create, Read, Update, Delete operations
- Search by first name, last name, or email
- Sorting by last name or creation date
- Bootstrap modals for deletion confirmation

### Weather Integration (AJAX + Caching)
- Live temperature, humidity, and wind speed for each contact's city
- Geocoding via Nominatim API (city name → coordinates)
- localStorage caching (15 min TTL) to minimize external API calls

### Bulk Data Import (CSV)
- Upload and process `.csv` files
- Upsert logic — updates existing records by email or creates new ones
- Automatic `ContactStatus` relationship handling

### REST API
- Endpoints at `/api/contacts/`
- Supports GET, POST, PUT, DELETE

## Getting Started

### Prerequisites

- Python 3.10+ **or** Docker

### Run with Docker

```bash
git clone https://github.com/onyevyerov/contact_app.git
cd contact_app
cp .env.sample .env   # edit with your SECRET_KEY
docker-compose up --build
```
The app will be available at `http://localhost:8000/`.

### Run locally

```bash
git clone https://github.com/onyevyerov/contact_app.git
cd contact_app
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
cp .env.sample .env             # edit with your SECRET_KEY

python manage.py migrate
python manage.py runserver
```

## Testing the CSV Import

A sample file `test_contacts.csv` is included in the root directory.

1. Open the application and navigate to **Import CSV**
2. Select `test_contacts.csv`
3. Submit — the system skips the header row and maps all fields automatically

## Edit .env.sample file

```
SECRET_KEY=<write_here_your_secret_key>
```
