# Futuristic 3D Developer Portfolio — Ronak (Pure Django Edition)

This is a premium, interactive developer portfolio for **Ronak** featuring a **Black + Neon Green + 3D Technology aesthetic**. 
The entire website is built as a **pure Django application** using HTML5 canvas projected 3D spheres/constellations, MS Excel/PowerPoint report builders, and a custom Local Subprocess Server Panel that lets you launch other local Django projects instantly.

---

## 📁 Project Structure

```text
ronak-portfolio/
│
└── backend/
    ├── manage.py
    ├── requirements.txt
    ├── config/             # Settings & main routing configurations
    │
    └── portfolio/          # Core portfolio models, seed commands, admin panel
        ├── models.py
        ├── views.py        # Index render, Excel/PPT builders, Subprocess runners
        ├── urls.py         
        │
        ├── templates/      # Glassmorphism HTML templates
        │   └── portfolio/
        │       ├── base.html           # Common CSS, particles, and cursor ring
        │       ├── index.html          # Subprocess triggers, 3D Canvas matrix, forms
        │       └── project_detail.html # Features lists and overview
        │
        └── management/     
            └── commands/   
                └── seed_portfolio.py   # Seeding script for projects, B.Com details
```

---

## 🛠️ Step-by-Step Installation & Run Instructions

### ⚙️ Prerequisite: Reuse the Workspace Virtual Environment
This project is configured to run using the virtual environment already set up at `C:\Users\RONAK\OneDrive\Desktop\django\venv`.

---

### 🚀 Running the Portfolio Server

1. **Open PowerShell and navigate to the backend directory**:
   ```powershell
   cd C:\Users\RONAK\OneDrive\Desktop\django\ronak-portfolio\backend
   ```

2. **Apply Database Migrations**:
   Django will initialize a local `db.sqlite3` database file in the backend directory.
   ```powershell
   ..\..\venv\Scripts\python.exe manage.py migrate
   ```

3. **Seed Database with Ronak's Profile Details**:
   Sets your education to **B.Com final year**, adds **MS Excel, PowerPoint, PPT and Financial Analysis** to your skills matrix, and registers the **9 projects**:
   ```powershell
   ..\..\venv\Scripts\python.exe manage.py seed_portfolio
   ```

4. **Start the Portfolio server on port 8090**:
   We bind it to port `8090` so it doesn't conflict with any of the projects you run:
   ```powershell
   ..\..\venv\Scripts\python.exe manage.py runserver 8090
   ```

5. Open **`http://127.0.0.1:8090`** in your browser.

---

## 🌐 Deploying to Render with MongoDB / Cloud Database

This project includes built-in configurations (`render.yaml`, `build.sh`, `Procfile`, `WhiteNoise`, and MongoDB connection support) for one-click or automated deployment to [Render](https://render.com).

### 🚀 Quick Render Deployment Steps

1. **Push your code to GitHub**:
   Ensure your repository is pushed to your GitHub account: `https://github.com/RONAK009-T/ronak-portfolio`.

2. **Create a Free MongoDB Cluster on MongoDB Atlas**:
   - Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and create a free tier cluster (M0).
   - Create a database user (e.g. `ronak` and secure password).
   - Under **Network Access**, allow access from anywhere (`0.0.0.0/0`).
   - Copy your connection string (`mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/ronak_portfolio?retryWrites=true&w=majority`).

3. **Deploy on Render**:
   - Log in to [Render Dashboard](https://dashboard.render.com).
   - Click **New +** &rarr; **Web Service**.
   - Connect your GitHub repository `RONAK009-T/ronak-portfolio`.
   - Configure the following settings:
     - **Name**: `ronak-portfolio`
     - **Runtime**: `Python 3`
     - **Build Command**: `./build.sh`
     - **Start Command**: `gunicorn --chdir backend config.wsgi:application`
   - In **Environment Variables**, add:
     - `DJANGO_SECRET_KEY`: *(Generate a secure random string)*
     - `DEBUG`: `False`
     - `ALLOWED_HOSTS`: `.onrender.com,localhost,127.0.0.1`
     - `MONGODB_URI`: `mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/ronak_portfolio?retryWrites=true&w=majority`
     - `MONGO_DB_NAME`: `ronak_portfolio`
     - `PYTHON_VERSION`: `3.11.9`
   - Click **Create Web Service**.

4. **Automatic Build & Seed**:
   Render will run `build.sh`, install all requirements from `backend/requirements.txt`, collect static files with WhiteNoise, run migrations, and automatically seed all your portfolio projects and profile information.

---

## 🔗 Official Links
- **GitHub Profile**: [https://github.com/RONAK009-T/](https://github.com/RONAK009-T/)
- **Live Portfolio**: Hosted on Render

