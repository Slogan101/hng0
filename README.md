# hng0
# Description

This project is a simple FastAPI-based API that returns a JSON response containing my email address,  current UTC datetime in ISO 8601 format. It also includes proper CORS handling to allow cross-origin requests.

## Setup Instructions

Prerequisites

Python 3.8+

pip 

Installation & Running Locally

1. Clone the repository:
git clone https://github.com/Slogan101/hng0.git
cd hng0

2. Install dependencies:
pip install -r requirements.txt

3. Run the application:
uvicorn app.main:app --reload

The API will be available at: http://127.0.0.1:8000

## API Documentation

Endpoint

URL: /home

Method: GET

Description: Returns the current datetime in ISO 8601 format (UTC).

Request Example
GET /home HTTP/1.1
Host: 127.0.0.1:8000

Response Example
{
  "email": "newson190@gmail.com",
  "current_datetime": "2025-01-28T23:48:20.770009+00:00",
  "github_url": "https://github.com/Slogan101/hng0.git"
}

Example Usage

Using curl
curl -X GET http://127.0.0.1:8000/home

Using Python requests
import requests

response = requests.get("http://127.0.0.1:8000/home")
print(response.json())

## Hire Developers
- [Hire Python Developers](https://hng.tech/hire/python-developers)
- [Hire C# Developers](https://hng.tech/hire/csharp-developers)
- [Hire Golang Developers](https://hng.tech/hire/golang-developers)
- [Hire PHP Developers](https://hng.tech/hire/php-developers)
- [Hire Java Developers](https://hng.tech/hire/java-developers)
- [Hire Node.js Developers](https://hng.tech/hire/nodejs-developers)
