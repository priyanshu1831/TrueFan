FastAPI Product Inventory
This project is a FastAPI-based web application for managing a product inventory. It provides RESTful API endpoints for performing CRUD operations on products stored in a PostgreSQL database.

Features
FastAPI Framework: Utilizes FastAPI, a modern web framework for building APIs with Python.
PostgreSQL Database: Uses a PostgreSQL database to store product information.
Dockerized: Docker and Docker Compose are used to containerize the application and its dependencies, making it easy to deploy and run in any environment.
Async Database Operations: Utilizes async functionality provided by SQLAlchemy and databases library for efficient database operations.
API Documentation: Automatically generated API documentation provided by FastAPI's built-in Swagger UI.

Prerequisites
Before running the application, make sure you have the following installed on your system:

Docker
Docker Compose

Installation
Clone this repository to your local machine:
git clone https://github.com/your-username/fastapi-product-inventory.git

Navigate to the project directory:
    cd fastapi-product-inventory

Build the Docker containers:
docker-compose build

Usage

Start the Docker containers:
docker-compose up
Once the containers are running, you can access the API documentation at http://localhost:8000/docs in your web browser.

Use the provided API endpoints to manage the product inventory.

Configuration
The application's configuration can be modified via environment variables. The following environment variables are available:

DATABASE_URL: Connection URL for the PostgreSQL database. Default is postgresql://postgres:postgres@db:5433/postgres