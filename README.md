# Resume_AI
A Django-based AI tool that extracts and structures information from resumes for smarter analysis.

---

## ⚙️ Tech Stack
- **Backend:** Django (Python)
- **Libraries:** PyMuPDF (`fitz`), `nltk`, `spacy`, `re`
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default)

---

## 🛠️ Current Progress (as of Oct 15, 2025)
✅ Setup virtual environment  
✅ Installed all dependencies  
✅ Configured Django project and app structure  
✅ Fixed template rendering and import issues  
✅ Verified working of file upload page (upload.html)  
✅ Installed and verified `PyMuPDF` (fitz) for PDF parsing  

---

## 🚧 Next Tasks
- Implement file parsing logic in `utils/parse_resume.py`
- Extract key details (Name, Email, Skills, Experience)
- Display parsed output on the web interface
- Add error handling and invalid file detection


## 💡 Notes / Learnings
- Fixed “`No module named 'fitz'`” by installing **PyMuPDF**
- Confirmed proper use of Django’s `render()` with correct template path
- Used `venv` for clean dependency management

---

## 🗓️ Daily Log
**Oct 15:** Completed setup, fixed imports, tested initial page render.
