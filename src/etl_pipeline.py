import pandas as pd
from sqlalchemy import create_engine

# Database connection (update credentials as needed)
DATABASE_URL = "postgresql://user:password@localhost:5432/student_db"
engine = create_engine(DATABASE_URL)

def run_etl_pipeline():
    """
    Extract: Query student scores from PostgreSQL.
    Transform: Calculate average scores per student for course_id = 101.
    Load: Save results to a new table 'avg_scores'.
    """
    try:
        # Extract
        query = """
        SELECT student_id, AVG(score) as avg_score
        FROM student_scores
        WHERE course_id = 101
        GROUP BY student_id
        """
        df = pd.read_sql(query, engine)

        # Transform (optional: additional processing can be added here)
        df['avg_score'] = df['avg_score'].round(2)

        # Load
        df.to_sql('avg_scores', engine, if_exists='replace', index=False)
        print("ETL Pipeline completed successfully!")
        print(df)

        # Save to CSV for reference
        df.to_csv('../data/sample_output.csv', index=False)

    except Exception as e:
        print(f"Error during ETL pipeline: {e}")

if __name__ == "__main__":
    run_etl_pipeline()
