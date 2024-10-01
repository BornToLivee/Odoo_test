# Odoo test task


## Project Description

This project was created for a test task for the Odoo Fullstack Developer position. It includes the "Persons Management" module, which depends on the `website` module. The module has the following features:

- **Backend**: The `Persons` model stores information about first name, last name, age, gender, birthdate, and company. You can create and edit records using forms.
- **Frontend**: There is a controller that shows the 5 latest records from the `Persons` model on a webpage. The records are displayed as cards with full name, gender, age, and company.
- **Web Client**: A form is added to the website to create new records.

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/BornToLivee/Odoo_test
```

## 2. Install dependencies
Install virtual environment
```bash
python -m venv .venv
.venv\scripts\activate
```

## 3. Run
```bash
docker-compose up --build
```

## Additional Information
- Odoo Documentation: https://www.odoo.com/documentation/16.0/
- Odoo Official Repository: https://github.com/odoo/odoo
