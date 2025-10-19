# E-commerce Product API

A Django REST Framework backend for managing products, categories, users and simple e-commerce features. This repository contains the code for the BE Capstone project and the API implemented so far: authentication (JWT), product CRUD, search and filtering, reviews, wishlist, and basic user management.

## Features (implemented)

- JWT Authentication (login, refresh, logout via token blacklist)
- User registration and profile endpoints
- Product CRUD with ownership checks and admin override
- Product search and filtering (including price range and stock availability)
- Category read endpoints
- Product reviews (create/list) and basic review model
- Wishlist: add/list/remove items for authenticated users
- Pagination on list endpoints

## Tech stack

- Python / Django
- Django REST Framework
- djangorestframework-simplejwt (JWT)
- django-filter
- SQLite (development)

## Installation

Clone the repo:

```bash
git clone https://github.com/zsegla/alx-project-ecommerce-platform.git
cd alx-project-ecommerce-platform
```

Create & activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

## API Endpoints

Base URL: http://127.0.0.1:8000/

Auth

- POST /api/auth/register/ — Register a new user
- POST /api/auth/login/ — Obtain JWT access + refresh tokens
- POST /api/auth/token/refresh/ — Refresh access token
- POST /api/auth/logout/ — Blacklist refresh token (body: {"refresh": "<token>"})

Users

- GET /api/users/ — List users (admin only)
- GET /api/users/{id}/ — Retrieve user profile (owner or staff)
- PATCH/PUT /api/users/{id}/ — Update user profile (owner or staff)

Products

- GET /api/products/ — List products (supports search, filters, ordering, pagination)
  - Query params: `search=`, `category__id=`, `min_price=`, `max_price=`, `in_stock=true|false`, `ordering=` (e.g. `ordering=-created_at`), `page=`
- POST /api/products/ — Create product (auth required)
- GET /api/products/{id}/ — Retrieve product details
- PUT /api/products/{id}/ — Update product (owner or staff)
- DELETE /api/products/{id}/ — Delete product (owner or staff)

Categories

- GET /api/categories/ — List categories
- GET /api/categories/{id}/ — Category details

Reviews

- GET /api/products/{product_pk}/reviews/ — List reviews for a product
- POST /api/products/{product_pk}/reviews/ — Create a review for a product (auth required)

Wishlist

- GET /api/wishlist/ — List current user's wishlist items
- POST /api/wishlist/ — Add a product to wishlist (body: {"product": <product_id>})
- GET /api/wishlist/{id}/ — Get wishlist item (owner or staff)
- DELETE /api/wishlist/{id}/ — Remove wishlist item (owner or staff)

## Example usage

1. Login to obtain tokens:

POST /api/auth/login/

```json
{ "username": "alice", "password": "pass1234" }
```

Response:

```json
{ "refresh": "<refresh>", "access": "<access>" }
```

Use the access token for authenticated requests:

Header: Authorization: Bearer <access>

2. Create a product (authenticated):

POST /api/products/

```json
{
  "name": "Sample",
  "description": "Example",
  "price": "10.00",
  "category_id": 1,
  "stock_quantity": 20,
  "image_url": "https://..."
}
```

3. Add to wishlist:

POST /api/wishlist/

```json
{ "product": 3 }
```

## Roadmap (remaining tasks)

- Orders & stock management (order model, transactional stock reduction, admin order update)
- Image upload & media settings (Pillow + MEDIA config)
- Tests & deployment prep (Procfile, gunicorn, automated tests)

## Notes

- The DRF browsable API is available in development when `DEBUG=True`.
- If you want me to implement the next roadmap item (orders, image uploads, tests/deploy), tell me which one to pick and I'll add it next.
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
- GET /api/products/low_stock/?threshold={n} → List products with stock_quantity less than or equal to `n` (default `5`). Supports pagination.
