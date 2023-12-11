
# Django AWS S3 File Uploader

This project is a Django-based API for uploading files to an AWS S3 bucket, save it's information on MySQl database, read a JSON sensor data file and return responses of both to the frontend in JSON format.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)

## Overview

The project provides an API to upload files to an AWS S3 bucket securely. It also includes endpoints to retrieve file information.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/stormshadow47/BackendHackathon.git

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Setup environment variables:
   
   Create a .env file in the project root and add necessary configurations(credentials).

5. Virtual environment inside the project:
   
   Open command prompt/powershell inside the project folder to initiate a virtual environment and enter the project root directory:
    ```bash
    .\hack_project\Scripts\activate
    cd hack_project

6. Run migrations:
    ```bash
    python manage.py migrate

# Usage:

1. To start the development server:
   ```bash
   python manage.py runserver

2. Install [Postman API platform](https://www.postman.com/downloads/) to test the API's

3. Install [MySQL workbench](https://dev.mysql.com/downloads/workbench/) to view information from the database.

# API endpoints:

- GET /api/get-csrf-token/: Fetch the CSRF token (Place it in the header section of Postman with key X-CSRF token)
- POST /api/upload/: Upload a file to AWS S3 bucket. (Upload the credntialsfile through post request in Postman)
- GET /api/file/file_id/: Get file information.
- GET /api/get-sensor-data/: Fetch the sensor data from the JSON file and return it in JSON format to frontend.

# Technologies Used:

- Python 3
- Django
- Django REST Framework
- AWS SDK (Boto3)
- MySQL
  


    
 





   
   


