# Create venv
python -m venv venv

# Activate venv
venv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Start FastAPI
uvicorn app.main:app --reload

# Create database tables
python -m app.db.init_db

# Check packages
pip list

# Check python version
python --version

# Save requirements
pip freeze > requirements.txt