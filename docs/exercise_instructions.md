# Hands-On Exercise: Optimizing a Query and Building an ETL Pipeline

## Objective
Optimize a PostgreSQL query for student performance data, build a Python-based ETL pipeline, and visualize results using a Streamlit app.

## Prerequisites
- PostgreSQL installed and running.
- Python 3.x with dependencies (`pandas`, `sqlalchemy`, `psycopg2-binary`, `streamlit`, `plotly`).
- Sample database (`data/student_db.sql`).

## Setup
1. **Create Database**:
   - Open PostgreSQL and run:
     ```bash
     createdb student_db
     psql -d student_db -f data/student_db.sql
     ```
2. **Install Python Dependencies**:
   ```bash
   pip install -r src/requirements.txt
