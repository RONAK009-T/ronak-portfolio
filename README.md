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

## 🖥️ Local Project Subprocess Runner Dashboard

When visiting your portfolio, you can scroll down to **Selected Projects** and click **Launch Server** on a project (e.g. *AI Interview Assistant* or *AI Code Reviewer*).
* The backend will spin up the local server inside your python environment on a dedicated port (e.g. `8001`).
* The browser will automatically open a new tab loading the project site (e.g. `http://127.0.0.1:8001`).
* You can click **Stop Server** on the portfolio dashboard to close the background process whenever you want.

---

## 📊 B.Com Microsoft Excel & PowerPoint Integration

You can click **Download Excel Analysis** or **Download PPT Report** inside the **Skills Matrix**:
* **Excel sheet**: Generates a custom stylized neon financial ledger calculating gross margins and tax profit forecasts utilizing `openpyxl`.
* **PowerPoint presentation**: Constructs a multislide summary of your developer profile using `python-pptx`.
