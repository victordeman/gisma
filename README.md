# GISMA-Demo: Building Scalable SQL Applications with Python and PostgreSQL

This repository supports a course module for teaching scalable SQL applications, designed as a work sample for the Lecturer of Computer/Data Science position at Gisma University of Applied Sciences. It includes code, data, and a Streamlit app to demonstrate query optimization and ETL pipeline development using PostgreSQL and Python.  If you have trouble implementing of deploying the code, mail me. Afterwards, buy me a drink

## Repository Structure
- **data/**: Sample PostgreSQL database (`student_db.sql`) and ETL output (`sample_output.csv`).
- **src/**: Python script (`etl_pipeline.py`), SQL queries (`query_optimization.sql`), Streamlit app (`app.py`), and dependencies (`requirements.txt`).
- **docs/**: Exercise instructions (`exercise_instructions.md`) and optional slide deck (`slides.pdf`).
- **setup_dirs.sh**: Bash script to create the directory structure.
- **.gitignore**: Ignores common Python/PostgreSQL files.

## Prerequisites
- **PostgreSQL**: Version 15 or higher.
- **Python**: Version 3.8 or higher.
- **Streamlit**: For running the visualization app.
- **Git**: For cloning the repository.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/victordeman/gisma
   cd gisma
