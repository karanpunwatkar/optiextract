# 📄 DOCUMENTATION.md  
**OptiExtract Take-Home Assignment — File Uploader and Tracker**

---

## 🧠 1. Project Overview

This project is a small full-stack web app that lets users **upload any file** (like PDF, image, or text) and then **see all their uploaded files in a table**.  
It’s like a mini version of how a real platform (like Google Drive) handles the first steps of file storage — saving the file and remembering its details.

When a file is uploaded:
1. It’s saved on my computer inside a folder called `uploaded_files`.
2. Its information (like original name, size, and upload time) is saved in a small **SQLite database**.
3. Another page shows all the uploaded files in a nice table.

---

## 🏗️ 2. Folder Structure

Here’s how I organized the project:

optiextract/
│
├── backend/               # FastAPI backend code
│   ├── main.py            # API routes and logic
│   ├── models.py          # Database model (File table)
│   └── database.py        # Database connection setup
│
├── frontend/              # Frontend (HTML, CSS, JS)
│   ├── upload.html        # Page to upload a file
│   ├── files.html         # Page to show uploaded files
│   └── style.css          # Styling for both pages
│
├── uploaded_files/        # Where uploaded files are stored
│
├── requirements.txt       # All Python packages used
└── DOCUMENTATION.md       # This file


This structure keeps **backend** and **frontend** separate, so everything is organized and easy to maintain.

---

## ⚙️ 3. How It Works (Step-by-Step)

### 🧩 Backend (FastAPI + SQLAlchemy + SQLite)

1. **Database setup**  
   I used `SQLAlchemy` to create a database model called `File`.  
   Each record stores:
   - original filename  
   - system filename (a unique name with UUID)  
   - file size  
   - upload time  

2. **Upload API (POST /upload-document)**  
   When a file is uploaded, it’s saved inside the `uploaded_files` folder.  
   I used `uuid.uuid4()` to give every file a **unique system name**, so even if two users upload “resume.pdf”, both are saved safely.

3. **List API (GET /files)**  
   This endpoint sends all the stored file details (metadata) to the frontend.  
   It converts timestamps into human-readable dates before returning them.

---

### 💻 Frontend (HTML + CSS + JavaScript)

1. **Upload Page (`upload.html`)**  
   Has a simple file input and a button.  
   When you click “Upload File”, JavaScript sends the file to the backend using the **Fetch API**.

2. **History Page (`files.html`)**  
   When this page opens, JavaScript automatically calls the `/files` API to get all uploaded file details and shows them in a **nice-looking table**.

3. **CSS (`style.css`)**  
   I added a simple, clean, and professional design:
   - Centered content  
   - Rounded boxes  
   - Subtle colors  
   - Hover effects  
   - Consistent spacing

---

## 4. Why I Chose These Design Decisions

### 🧾 Unique Filenames with UUID
Using `uuid.uuid4()` ensures every uploaded file gets a **unique system name**.  
If two files have the same original name, they won’t overwrite each other.

### Safe File + Database Sync
First, I save the file physically on disk.  
Then I insert the metadata (name, size, timestamp) into the SQLite database.  
This order ensures the file and database record always match.

### Simplicity and Clarity
I didn’t use React or heavy frameworks since the assignment asked for basic HTML + JS.  
Everything is **lightweight and beginner-friendly** but still professional.

---

## 5. How to Run the Project (Local Setup)

Follow these steps to run the app locally on any Ubuntu or Linux system:

1. **Clone the repository**
   ```bash
   git clone <your-github-repo-url>
   cd optiextract
2. Create a virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install all dependencies

pip install -r requirements.txt

4. Run the FastAPI backend

uvicorn backend.main:app --reload
→ This starts your backend API at: http://127.0.0.1:8000

5. Run the frontend

cd frontend
python3 -m http.server 5500

→ Open:
Upload page: http://127.0.0.1:5500/upload.html

History page: http://127.0.0.1:5500/files.

| Problem              | What Happened                  | Solution                                   |
| -------------------- | ------------------------------ | ------------------------------------------ |
| CORS Error           | Frontend couldn’t call backend | Added `CORSMiddleware` in FastAPI          |
| File Overwriting     | Two files had same name        | Used `uuid.uuid4()` to create unique names |
| SQLite access issues | Multiple threads error         | Used `check_same_thread=False`             |
| Empty table display  | Needed readable timestamp      | Converted datetime using `.strftime()`     |

## 6. AI Tools Used (Not Evaluated)

I used ChatGPT only to help with:

Setting up the FastAPI boilerplate

CSS styling improvements

Debugging CORS and JS fetch issues

All logic, structure, and documentation writing were done by me.

## 7. Final Thoughts

This project taught me how a full-stack workflow works:
Frontend sends data → Backend processes → Database stores → Frontend displays results.
I also learned how to structure a project, handle CORS, and use UUIDs for file safety.
Overall, it’s a small but complete real-world example of file ingestion + tracking, built using FastAPI, SQLAlchemy, HTML, CSS, and JS.