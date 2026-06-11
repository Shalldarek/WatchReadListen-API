# Watch Read Listen API 🎬📚🎵

![FastAPI](https://img.shields.io/badge/FastAPI-0.136.3-009688?style=flat-square\&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square\&logo=python)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.50-red?style=flat-square)

A modern RESTful API for managing your personal entertainment backlog. Track movies, books, and albums, organize them by priority and mood, and get personalized recommendations when you're unsure what to watch, read, or listen to next.

---

## ✨ Overview

Choosing your next movie, book, or album can sometimes take longer than consuming it. **Watch Read Listen API** helps eliminate decision fatigue by maintaining a prioritized backlog and intelligently recommending items based on your preferences.

Built with **FastAPI**, **SQLAlchemy**, and **JWT authentication**, the project demonstrates clean backend architecture, secure authentication practices, and business-logic-driven recommendation features.

---

## 🚀 Features

### 🔐 Authentication & Security

* User registration and login
* JWT-based authentication
* Secure password hashing with Argon2
* Protected endpoints with authenticated access

### 🎬📚🎵 Media Backlog Management

* Create, read, update, and delete backlog items
* Support for:

  * Movies
  * Books
  * Albums
* Assign custom tags
* Add personal notes
* Mark items as completed
* Rate completed media

### 🎲 Smart Recommendation Engine

The `/pick` endpoint helps you decide what to consume next by selecting from your unfinished backlog using weighted randomness.

Priority weights:

| Priority | Weight |
| -------- | ------ |
| High     | 5×     |
| Medium   | 3×     |
| Low      | 1×     |

Recommendations can be filtered by:

* Media type (`MOVIE`, `BOOK`, `ALBUM`)
* Mood tags
* Completion status

This ensures high-priority items are more likely to be selected while still allowing variety.

### 📊 Statistics & Insights

Track your consumption habits with aggregated statistics:

* Total backlog size
* Completed item count
* Average ratings
* Media type distribution
* Progress overview

### 📖 Interactive Documentation

FastAPI automatically generates API documentation:

* Swagger UI → `/docs`
* ReDoc → `/redoc`

Explore and test endpoints directly from your browser.

---

## 🛠️ Tech Stack

| Category         | Technology        |
| ---------------- | ----------------- |
| Language         | Python 3.12       |
| Framework        | FastAPI           |
| ORM              | SQLAlchemy 2.0    |
| Database Driver  | PyMySQL           |
| Validation       | Pydantic          |
| Authentication   | JWT (python-jose) |
| Password Hashing | Argon2 (Passlib)  |

---

## 📂 Project Structure

```text
app/
├── api/
│   └── endpoints/       # API route handlers
├── core/                # Configuration and database setup
├── crud/                # Database operations
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas
├── services/            # Business logic and recommendation engine
└── main.py              # FastAPI application entry point
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/watchreadlisten-api.git
cd watchreadlisten-api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```powershell
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Environment Configuration

Create a `.env` file in the project root:

```env
DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
SECRET_KEY=your_super_secret_jwt_key
```

### Example

```env
DATABASE_URL=mysql+pymysql://admin:password123@localhost/watchreadlisten
SECRET_KEY=change_this_in_production
```

---

## ▶️ Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Documentation:

```text
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

---

## 📌 Example Workflow

1. Register a new user account
2. Authenticate and obtain a JWT token
3. Add movies, books, and albums to your backlog
4. Assign priorities and mood tags
5. Mark items as completed and rate them
6. Use `/pick` whenever you can't decide what to consume next
7. Monitor progress through the statistics endpoints

---

## 🔮 Future Improvements

* Recommendation history
* Favorite items and collections
* Social sharing features
* External metadata integrations (TMDb, Open Library, Spotify)
* Advanced recommendation algorithms
* Docker support and CI/CD pipelines

---

## 📄 License

This project is open-source and available under the MIT License.
