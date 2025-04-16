# HELLO PROFESSOR!! THIS IS MY ASSIGNMENT 10!!

# Event Manager Company: User Management REST API

#### Welcome to the Event Manager Company! My work as a Software QA Analyst/Developer intern is displayed in this repository, where I worked to create and improve a safe REST API that supports OAuth2 authentication based on JWT. Future event administration and registration modules will be built on top of this API, which is intended to handle user-related tasks.

#### Project Overview:
[1. SETUP INSTRUCTIONS](#1-setup-instructions) <br>
[2. DATABASE MIGRATION](#2-database-migration) <br>
[3. RESOLVED ISSUES](#3-resolved-issues) <br>
[- CURL COMMAND AND EXAMPLE VALUE NICKNAME](#1-curl-command-and-example-value-nickname) <br>
[- VALIDATING URL](#2-validating-url) <br>
[- PASSWORD VALIDATION](#3-password-validation) <br>
[- EMAIL VERIFICATION](#4-email-verification) <br>
[- LOGIN VALIDATION](#5-login-validation) <br>
4. DOCKER HUB DEPLOYMENT <br>
5. TESTING <br>
6. COVERAGE <br>

## 1. SETUP INSTRUCTIONS :

- **STEP 1:** Fork the Professor's Repository to our own github account.

- **STEP 2:** To access the Forked Repository locally, clone the Forked Repository.

``` git clone git@github.com:Krishna-Sathvika-Ganni/event_manager.git```

- **STEP 3:** Start the application using Docker

``` docker compose up --build```

- **STEP 4:** Access Swagger UI at : localhost/docs

![Screenshot 2025-04-14 at 7 16 35 PM](https://github.com/user-attachments/assets/4a478103-c5bf-45a2-b909-90c68186f7b2)


- **STEP 5:** Access PGAdmin at : localhost:5050

![Screenshot 2025-04-14 at 7 16 55 PM](https://github.com/user-attachments/assets/9dcf1ff2-c024-45d1-8834-2149e371a10d)



## 2. DATABASE MIGRATION:

- **STEP 1:** Go to localhost:5050

- **STEP 2:** Add New Server with Configurations
General
  - server name : myserver
Connection
  - host name: postgres
  - port: 5432
  - database: myappdb
  - Username: give username
  - Password: give password

- **STEP 3:** Save the Configurations.

- **STEP 4:** Go to the VS Code terminal, where the Repository is cloned and give the code given below to create tables.

``` docker compose exec fastapi alembic upgrade head```


## 3. RESOLVED ISSUES:

### 1. CURL COMMAND AND EXAMPLE VALUE NICKNAME: 

Addressed a confusing inconsistency in the Swagger documentation where the nickname field in the cURL request and example response did not match.

- The nickname provided in the cURL request and the example response did not match the API description. 

- This discrepancy was fixed to increase the clarity of the documentation and avoid user confusion.

LINK TO CODE: [RESOLVED CURL COMMAND AND EXAMPLE VALUE NICKNAME](https://github.com/Krishna-Sathvika-Ganni/event_manager/commit/d6eba5b9cb62dcdd39cc8af018e00801e11388e5)

### 2. VALIDATING URL:

To check for both legitimate and invalid URL submissions, corresponding unit tests were included.

- Implemented strict URL validation for user profile fields such as profile_picture_url.

- Invalid URLs now return clear error messages.

- Now, when the system detects invalid URLs, it returns unambiguous error messages and compares them to standard validation rules. 

LINK TO CODE: [RESOLVED VALIDATING URL](https://github.com/Krishna-Sathvika-Ganni/event_manager/commit/1051253e6a0ef0431f9726024855f8c4553d8a2e) 

### 3. PASSWORD VALIDATION: 

Added robust password validation to detect incorrect passwords during user login attempts. 

- By guaranteeing that only users with legitimate credentials can access the system, this enhancement improves authentication security.

- The validation provides suitable error responses to assist users in resolving login problems.

LINK TO CODE: [RESOLVED PASSWORD VALIDATION](https://github.com/Krishna-Sathvika-Ganni/event_manager/commit/3595075a883c2cd1cc9a941302022a365da085a5)

### 4. EMAIL VERIFICATION:

Replaced username-based login with email-based verification to improve usability and identification. 

- Email addresses are now easier to use and more unique, which speeds up the user verification procedure. 

- The new system improves overall usability and offers a more straightforward user experience.

LINK TO CODE: [RESOLVED EMAIL VERIFICATION](https://github.com/Krishna-Sathvika-Ganni/event_manager/commit/b6495e32545a5adfc0664765ef1a61586d679f6f)

### 5. LOGIN VALIDATION:

Fixed issues with authorization when accessing protected endpoints via the Swagger UI. 

- Resolved an issue where the Swagger UI returned "Internal Server Error" due to missing/invalid access tokens. 

-  Improved error handling and added proper authorization feedback during login and authenticated operations.

LINK TO CODE: [RESOLVED LOGIN VALIDATION](https://github.com/Krishna-Sathvika-Ganni/event_manager/commit/4a3968a14b266920d63b6db7359cc20b36b671cd)


## 4. DOCKER HUB DEPLOYMENT:

![Screenshot 2025-04-15 at 9 15 09 PM](https://github.com/user-attachments/assets/6b769cb1-89af-4df9-9e46-969bffd2ff73)






