🏬 E-commerce Product API

A Django-based API for managing products, categories and users in an e-commerce platform. Built with Django REST Framework and JWT authentication. This repo is the BE Capstone implementation that focuses on product management, search, pagination and user-authenticated CRUD.

🚀 Features
This API is designed for product managers (admins) and customers (read-only consumers) and provides endpoints to manage products and categories.

✅ Current Features (Implemented)

- 🔐 JWT Authentication (login & token refresh)
- 🛍️ Product CRUD (create, read, update, delete) with ownership checks
- 🏷️ Category read endpoints and association to products
- 🔎 Search (by name, description, category) and filtering support
- 📄 Pagination for product listings
- ⚖️ Role-based access: only authenticated users can create/update/delete; owners or staff can modify a product
- ⚙️ Built with Django ORM and DRF (no raw SQL)

🧾 Functional Scope

1. Products — CRUD
   - Each product includes: name, description, price, category, stock_quantity, image_url, created_at, owner
   - Validation for required fields (name, price, stock_quantity)
2. Users — basic auth via Django + JWT
   - Login and token refresh implemented (registration endpoint can be added)
3. Product Search & Filters
   - Search by name/description/category (partial matches supported)
   - Filter by category id; ordering by price or created date
4. Pagination
   - Page-number pagination enabled with a default page size (configurable)

⚙️ Tech Stack

- Backend: Django, Django REST Framework
- Auth: djangorestframework-simplejwt (JWT)
- DB (dev): SQLite (easy local setup); swap to PostgreSQL for production
- Filtering: django-filter

🛠️ Installation
Clone the repo:

```bash
git clone https://github.com/zsegla/alx-project-ecommerce-platform.git
cd alx-project-ecommerce-platform
```

Create & activate virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS / Linux (zsh)
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Run the server:

```bash
python manage.py runserver
```

🔑 API Endpoints (implemented subset)
Base URL: http://127.0.0.1:8000/

Auth

- POST /api/auth/login/ → Obtain JWT (access + refresh)
- POST /api/auth/token/refresh/ → Refresh access token

Products

- GET /api/products/ → List products (supports search, filters, pagination)
- POST /api/products/ → Create product (auth required)
- GET /api/products/{id}/ → Retrieve product details
- PUT /api/products/{id}/ → Update product (owner or staff)
- DELETE /api/products/{id}/ → Delete product (owner or staff)

Categories

- GET /api/categories/ → List categories
- GET /api/categories/{id}/ → Category detail

Other

- The router also exposes the browsable DRF API when running the server in DEBUG mode.

🧪 Testing with Postman / curl

1. Login to get JWT tokens

Request (POST /api/auth/login/):

```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

Response:

```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

2. Use access token for authenticated requests (example header):

Authorization: Bearer <access_token>

3. Create a product (example POST /api/products/):

```json
{
  "name": "Sample Product",
  "description": "A short description",
  "price": "9.99",
  "category_id": 1,
  "stock_quantity": 100,
  "image_url": "https://example.com/image.jpg"
}
```

🛤️ Roadmap

- Add user registration, profile endpoints and logout (JWT blacklist)
- Reviews and ratings for products
- Wishlist and cart/order models + stock reduction on order
- Image upload (Pillow / media storage)
- Promotions & discounts
- Tests (unit + integration) and CI pipeline
- Production settings and deployment (Heroku / PythonAnywhere / Docker)

If you want the README adapted further (e.g., different wording, add registration endpoint docs, or include example curl commands), tell me what to change and I will update it.

# E-commerce Product API (Django + DRF)

This is a minimal backend for the BE Capstone E-commerce Product API project. It provides product and category management endpoints, JWT authentication, pagination and search.

Quick start

1. Create and activate a virtualenv:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Run migrations and create superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Run the server:

```bash
python manage.py runserver
```

API endpoints (partial)

- POST /api/auth/login/ (JWT obtain pair)
- POST /api/auth/token/refresh/
- GET /api/products/
- POST /api/products/ (auth required)
- GET /api/products/{id}/
- PUT /api/products/{id}/ (owner or staff)
- DELETE /api/products/{id}/ (owner or staff)
- GET /api/products/categories/ (list categories)
