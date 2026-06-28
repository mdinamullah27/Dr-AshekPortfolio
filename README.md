# DrPortfolio - Backend API

A production-ready Django backend for a Doctor Professional Portfolio platform.

## Features

- **Custom User Model** with UUID primary key and email authentication
- **JWT Authentication** with access/refresh tokens
- **RESTful API** with Django REST Framework
- **PostgreSQL** database support
- **Doctor Profile** with SEO fields for Next.js SSR
- **CORS Support** for Next.js frontend
- **Production-ready** security settings
- **Global Exception Handling** with consistent error responses
- **Custom Pagination** and filtering

## Tech Stack

- Python 3.12+
- Django 5.x
- Django REST Framework
- PostgreSQL
- JWT (djangorestframework-simplejwt)
- python-decouple
- dj-database-url
- django-cors-headers

## Project Structure

```
drportfolio/
├── apps/
│   ├── accounts/          # Authentication & users
│   ├── profiles/          # Doctor profile with SEO
│   └── common/            # Shared utilities
├── api/
│   └── v1/
│       └── urls.py
├── config/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── scripts/
├── logs/
├── media/
├── static/
├── .env.example
├── .gitignore
├── manage.py
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd drportfolio
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements/development.txt
```

### 4. Environment setup

```bash
cp .env.example .env
```

Edit `.env` file with your configuration:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/drportfolio
```

### 5. Database setup

Create PostgreSQL database:

```sql
CREATE DATABASE drportfolio;
```

### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create superuser

```bash
python manage.py createsuperuser
```

### 8. Run development server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/v1/`

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register/` | Register new user |
| POST | `/api/v1/auth/login/` | Get JWT tokens |
| POST | `/api/v1/auth/refresh/` | Refresh access token |
| GET | `/api/v1/auth/me/` | Get current user profile |
| PUT | `/api/v1/auth/me/` | Update profile |

### Doctor Profiles (Public)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/profiles/` | List all active profiles |
| GET | `/api/v1/profiles/{slug}/` | Get profile by slug |

### Doctor Profiles (Admin)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/profiles/` | Create new profile |
| PUT | `/api/v1/profiles/{id}/` | Update profile |
| PATCH | `/api/v1/profiles/{id}/` | Partial update profile |
| DELETE | `/api/v1/profiles/{id}/` | Delete profile |

## JWT Usage

### Get Access Token

```bash
curl -X POST http://localhost:8000/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword"}'
```

### Use Access Token

```bash
curl http://localhost:8000/api/v1/auth/me/ \
  -H "Authorization: Bearer <your-access-token>"
```

### Refresh Token

```bash
curl -X POST http://localhost:8000/api/v1/auth/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "<your-refresh-token>"}'
```

## Migration Workflow

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations

# View SQL for specific migration
python manage.py sqlmigrate app_name migration_number
```

## Development Scripts

```bash
# Make scripts executable
chmod +x scripts/*.sh

# Run migrations
./scripts/migrate.sh

# Make migrations
./scripts/makemigrations.sh

# Run server
./scripts/runserver.sh
```

## SEO Optimization

The DoctorProfile model includes SEO fields optimized for Next.js SSR:

- `meta_title` - SEO meta title
- `meta_description` - SEO meta description
- `meta_keywords` - Comma-separated keywords
- `canonical_url` - Canonical URL
- `og_title` - Open Graph title
- `og_description` - Open Graph description
- `og_image` - Open Graph image

These fields are exposed through the API for dynamic metadata generation in Next.js.

## Production Deployment

### 1. Set environment variables

```env
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=postgresql://user:password@host:5432/drportfolio
ALLOWED_HOSTS=yourdomain.com
```

### 2. Install production dependencies

```bash
pip install -r requirements/production.txt
```

### 3. Collect static files

```bash
python manage.py collectstatic
```

### 4. Run with Gunicorn

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

## Security Features

- HTTPS enforcement (production)
- HSTS headers
- CSRF protection
- XSS protection
- Content type nosniff
- Secure cookies
- Rate limiting
- JWT token blacklisting

## Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.accounts
python manage.py test apps.profiles

# Run with coverage
coverage run manage.py test
coverage report
```

## Code Quality

```bash
# Run linter
ruff check .

# Run formatter
ruff format .

# Run type checker
mypy .
```

## License

MIT License
