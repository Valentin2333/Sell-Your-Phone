# 📱 Sell Your Phone

A Django web application where users can register, list phones for sale, browse listings, like and comment on phones, and manage their own profile.

---

## Features

- **Authentication** — Register and log in with email; custom user model; profile auto-created via signals
- **List a Phone** — Post a phone for sale with brand, model, year, storage, price, contact number, and photo
- **Browse Listings** — Public phone listing page visible to all visitors
- **Search** — Search phones by brand or model name
- **Phone Details** — Full listing with like count, comments, and edit/delete controls for the owner
- **Like / Unlike** — Toggle likes on any phone listing (login required)
- **Comments** — Leave short comments on any listing (login required)
- **Edit & Delete** — Owners can edit or remove their own listings
- **User Profile** — Upload a profile photo and view all your own listings
- **Admin Panel** — Full Django admin at `/admin/`

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Runtime |
| Django 4.2+ | Web framework |
| PostgreSQL | Database |
| psycopg2-binary | PostgreSQL adapter |
| Pillow | Image upload handling |
| django-phonenumber-field | Phone number validation |
| phonenumbers | Phone number parsing |

---

## Project Structure

```
Sell-Your-Phone-Python-Web/
├── manage.py
├── requirements.txt
├── media_files/                    # Uploaded images (phones & profiles)
├── static/images/
├── templates/
│   ├── shared/base.html
│   ├── index.html
│   ├── accounts/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── user_profile.html
│   └── phones/
│       ├── phone_list.html
│       ├── phone_details.html
│       ├── phone_sell.html
│       ├── phone_edit.html
│       ├── phone_delete.html
│       └── search_results.html
└── sell_your_phone/
    ├── settings.py
    ├── urls.py
    ├── accounts/                   # Custom user + profile app
    ├── phones/                     # Phone listings app
    └── common/                     # Index view
```

---

## Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/Valentin2333/Sell-Your-Phone-Python-Web.git
cd Sell-Your-Phone-Python-Web
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Open `sell_your_phone/settings.py` and update the `DATABASES` section to match your local PostgreSQL setup:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

The app uses email-based login, so it will ask for an email and password.

### 7. Run the development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000** in your browser.
Admin panel: **http://127.0.0.1:8000/admin/**

---

## URL Routes

| URL | Description |
|---|---|
| `/` | Landing page |
| `/phones/` | Browse all listings |
| `/phones/sell/` | Post a phone (login required) |
| `/phones/<id>/` | Phone detail page |
| `/phones/<id>/edit/` | Edit listing (owner only) |
| `/phones/<id>/delete/` | Remove listing (owner only) |
| `/phones/<id>/like/` | Like / unlike (login required) |
| `/phones/<id>/comment/` | Post a comment (login required) |
| `/phones/search/` | Search results |
| `/accounts/register/` | Register |
| `/accounts/login/` | Log in |
| `/accounts/logout/` | Log out |
| `/accounts/profile/` | View & edit profile (login required) |
| `/admin/` | Django admin |

---

## Running Tests

```bash
python manage.py test tests
```

---

## Bug Fixes Applied

These bugs were found and fixed during development:

- **`core/forms.py`** — Missing space in `BootstrapFormMixin` caused CSS classes to concatenate incorrectly (e.g. `form-controlform-control`), breaking all form styling.
- **`accounts/views.py`** — `LoginView` was using `success_url` which it ignores; changed to `next_page` so login redirect works correctly.
- **`accounts/views.py`** — Profile form on GET requests did not pass `instance=profile`, so the form always appeared blank instead of pre-populated.
- **`accounts/managers.py`** — Stray unused `UserManager` import left dangling at module level; removed.
- **`phones/views.py`** — `ListPhonesView` and `SearchResultsView` used `ListView + FormView` multiple inheritance which causes `get()` method conflicts; refactored to single `ListView` with `get_context_data()`.
- **`phones/views.py`** — Brand field on `EditPhoneView` was only `readonly` client-side via HTML attribute, meaning anyone could tamper with it via a crafted POST request; fixed server-side using `field.disabled = True` in `get_form()`.
- **`common/views.py`** — Same `TemplateView + FormView` multiple inheritance issue; refactored.
- **`settings.py`** — Hardcoded secret key and database credentials; wrapped in `os.environ.get()` with local fallbacks. Added `LOGIN_URL` so `@login_required` redirects to the correct login page.
- **`index.html` + `phone_list.html`** — `{% csrf_token %}` was present inside GET forms (the search bar), which is incorrect; removed.

---

## License

This project is open source and available under the [MIT License](LICENSE).
