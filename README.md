# Government Fund Management System

A desktop application built with Python and Tkinter that allows citizens to register their details and apply for government schemes — including loans, pensions, and scholarships. A separate admin panel lets administrators view and manage all citizen records and applications.

## Features

### Citizen Portal
- **Sign Up / Sign In** – Citizens can create an account and log in securely (credentials stored in MySQL).
- **Citizen Registration** – Enter personal details including name, date of birth, age, gender, phone number, email, Aadhar card, PAN card, occupation, disability status, city, and bank account information.
- **Scheme Selection** – After registration, citizens can choose from the following government schemes:
  - **Loan Waiver** – Apply for a loan waiver by providing loan amount, loan type, and occupation.
  - **Pension Distribution** – Apply for pension benefits by providing retirement year, salary, and age.
  - **Scholarship Distribution** – Apply for scholarships by providing marks obtained, caste category, and occupation.

### Admin Panel
- **Admin Sign In** – Separate login page for administrators using an `admin_users` table.
- **Manage Citizens** – View, search, update, and delete citizen records.
- **Manage Applications** – View all loan, pension, and scholarship applications submitted by citizens.

## Tech Stack

| Component | Technology |
|-----------|------------|
| GUI | Python `tkinter` / `ttk` |
| Database | MySQL |
| DB Connector | `mysql-connector-python` |
| Image Handling | `Pillow` (PIL) |

## Prerequisites

- Python 3.x
- MySQL Server
- Required Python packages:
  ```
  pip install mysql-connector-python Pillow
  ```

## Database Setup

1. Start your MySQL server and log in as `root`.
2. Create the database:
   ```sql
   CREATE DATABASE cp;
   USE cp;
   ```
3. Create the required tables:
   ```sql
   CREATE TABLE users (
       username VARCHAR(50) PRIMARY KEY,
       password VARCHAR(50)
   );

   CREATE TABLE admin_users (
       username VARCHAR(50) PRIMARY KEY,
       password VARCHAR(50)
   );

   CREATE TABLE citizen (
       name        VARCHAR(100),
       age         INT,
       dob         VARCHAR(20),
       gender      VARCHAR(10),
       phone       VARCHAR(15),
       email       VARCHAR(100),
       aadhar      VARCHAR(20),
       pan         VARCHAR(20),
       occupation  VARCHAR(50),
       disability  VARCHAR(5),
       city        VARCHAR(50),
       bank_acc    VARCHAR(30),
       bank_ifsc   VARCHAR(20)
   );

   CREATE TABLE loan (
       aadhar      VARCHAR(20),
       name        VARCHAR(100),
       loan_amount INT,
       loan_type   VARCHAR(50),
       occupation  VARCHAR(50)
   );

   CREATE TABLE pension (
       name         VARCHAR(100),
       aadhar       VARCHAR(20),
       age          INT,
       salary       INT,
       ret_year     VARCHAR(10)
   );

   CREATE TABLE scholarship (
       name        VARCHAR(100),
       aadhar      VARCHAR(20),
       marks       INT,
       occupation  VARCHAR(50),
       caste       VARCHAR(20)
   );
   ```
4. Insert an admin user:
   ```sql
   INSERT INTO admin_users (username, password) VALUES ('admin', 'admin123');
   ```

## Configuration

Database credentials are currently hard-coded in each module. Update the following variables in `govfund.py`, `loan.py`, `pension.py`, `scholarship.py`, and `adminPage.py` to match your MySQL setup:

```python
MySQLPassword = 'your_password'
DatabaseName  = 'cp'
Username      = 'root'
```

The same credentials are also used in `signin.py`, `signup.py`, and `adminSignIn.py` — update those files as well.

## Running the Application

Launch the citizen-facing sign-in page:

```bash
python signin.py
```

This opens the **Sign In** window. From here you can:
- Sign in with an existing account to access the citizen portal.
- Click **Sign up** to create a new account.
- Click **Are you an admin? Click Here** to open the Admin Sign In window.

## Project Structure

```
govfund-management-system/
├── signin.py           # Citizen sign-in page (entry point)
├── signup.py           # Citizen sign-up page
├── govfund.py          # Citizen registration form (Citizen class)
├── choosingScheme.py   # Scheme selection screen
├── loan.py             # Loan Waiver application form (Loan class)
├── pension.py          # Pension Distribution form (Pension class)
├── scholarship.py      # Scholarship Distribution form (Scholarship class)
├── adminSignIn.py      # Admin sign-in page
├── adminPage.py        # Admin dashboard (Admin class)
└── images/             # Image assets used by the UI
```

## Screenshots

> Add screenshots of the application windows here.

## License

This project is intended for educational purposes.
