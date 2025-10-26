# 📝 OptiExtract — File Upload & Tracker

**OptiExtract** is a full-stack web application that allows users to:

- Upload any file (PDF, image, text, etc.)
- Store file metadata in a database
- View uploaded files in a neat, interactive table

It’s a mini version of file management systems like Google Drive, built using **FastAPI**, **SQLite**, and plain **HTML/CSS/JS**.

---

## 🚀 Features

- **File Upload:** Upload files safely with unique names.
- **Upload History:** View all uploaded files with original filename, size, and timestamp.
- **Lightweight Frontend:** Clean UI with HTML, CSS, and JS.
- **Safe Backend:** FastAPI handles uploads and stores metadata in SQLite.
- **Cloud Deployment:** Backend on Render, frontend on Vercel.

---

## 🗂️ Project Structure
```bash
optiextract/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│
├── frontend/
│   ├── upload.html
│   ├── files.html
│   └── style.css
│
├── uploaded_files/
│
├── requirements.txt
├── DOCUMENTATION.md
└── files.db  (auto-created when running)

```
---

## ⚙️ Installation & Setup (Local Development)

### 1. Clone the repository
```bash
git clone https://github.com/karanpunwatkar/optiextract.git
cd optiextract
```

## 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the backend (FastAPI)
```bash
uvicorn backend.main:app --reload
```

## Backend runs at:
```bash
https://optiextract.onrender.com
```
🌐 Deployment

Backend: Render → https://optiextract.onrender.com
Frontend: Vercel → https://optiextract-frontend.vercel.app

Make sure frontend fetch URLs point to the live backend.

### Usage
``` bash
1. Go to frontend URL (Vercel)
2. Upload any file → Click Upload
3. Click View Upload History → Table displays:
- Original Filename
- Size (bytes)
- Uploaded At (timestamp)
```

### Technical Details

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Frontend  | HTML + CSS + JavaScript (Fetch API) |
| Backend   | FastAPI + SQLAlchemy + SQLite       |
| Unique filenames  | uuid4 ensures no overwrites            |
| CORS Enabled:    | Allows frontend to communicate with backend            |

## 📂 Dependencies

Listed in requirements.txt:
```bash 
fastapi
uvicorn
sqlalchemy
python-multipart
```

## 🧾 Author
Karan Punwatkar
GitHub: karanpunwatkar

## ✅ License
This project is open for educational purposes.

