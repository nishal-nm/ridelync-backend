# 🚗 RideLync — Backend

> Intelligent route-matching and ride-sharing platform backend built with Django REST Framework.

RideLync analyzes recurring vehicle movement patterns captured across camera checkpoints to intelligently match commuters traveling similar routes — making ride-sharing smarter and more data-driven.

---

## 🧠 What It Does

- Ingests vehicle movement data from multiple camera checkpoints
- Detects recurring travel patterns using route intelligence logic
- Matches riders traveling similar routes and notifies them via email
- Supports full ride lifecycle: offer, search, book, and review
- Real-time chat between users (1-on-1 and group)
- JWT-based authentication with OTP verification
- AI module powered by **YOLOv5** (vehicle detection) and **EasyOCR** (license plate recognition)

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 5.1, Django REST Framework |
| Auth | JWT (SimpleJWT) + Token Auth |
| Real-Time | Django Channels, WebSockets |
| Database | MySQL |
| Cache / Broker | Redis |
| Media Storage | Cloudinary |
| AI/ML | YOLOv5, EasyOCR |
| Deployment | Gunicorn, Render |

---

## 📁 Project Structure

```
ridelync-backend/
├── accounts/        # User auth, profiles, registration, OTP
├── rides/           # Ride offering, booking, ratings
├── ai/              # Route matching logic, ride-link email notifications
├── chat/            # Real-time 1-on-1 and group chat (WebSockets)
├── admin_panel/     # Owner/admin management, location mapping
└── backend/         # Django settings, ASGI/WSGI config, URL routing
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- MySQL
- Redis

### Installation

```bash
# Clone the repo
git clone https://github.com/nishal-nm/ridelync-backend.git
cd ridelync-backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True

DB_NAME=ridelync
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306

REDIS_URL=redis://localhost:6379

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

### Run the Server

```bash
# Apply migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

For WebSocket support in development, use:

```bash
daphne backend.asgi:application
```

---

## 🔗 Key API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/accounts/login/` | User login |
| POST | `/accounts/register/` | User registration |
| GET | `/rides/available/` | List available rides |
| POST | `/rides/offer/` | Offer a ride |
| POST | `/rides/book/<id>/` | Book a ride |
| GET | `/ai/all-rides/` | Fetch route-matched rides |
| POST | `/ai/request-mail/` | Send ride-link email to a matched user |

---

## 🌐 Live Backend

Deployed on Render: [https://ridelync-backend-t0y3.onrender.com](https://ridelync-backend-t0y3.onrender.com)

---

## 🔗 Related

- **Frontend Repo:** [ridelync-frontend](https://github.com/nishal-nm/ridelync-frontend)
