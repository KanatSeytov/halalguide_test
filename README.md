
## Requirements
- python3.10

## Installation and Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd halalguide
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py migrate
```
### 5. Run the Development Server
```bash
python manage.py runserver
```
### 6. Access the Application
Visit the application at http://127.0.0.1:8000/