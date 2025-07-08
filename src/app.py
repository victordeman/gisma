import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Streamlit page configuration
st.set_page_config(page_title="SQLValidator Demo", layout="wide")

# Database connection (update credentials as needed)
DATABASE_URL = "postgresql://user:password@localhost:5432/student_db"
engine = create_engine(DATABASE_URL)

# ETL Pipeline function
def run_etl_pipeline(course_id=101):
    try:
        query = f"""
        SELECT student_id, AVG(score) as avg_score
        FROM student_scores
        WHERE course_id = {course_id}
        GROUP BY student_id
        """
        df = pd.read_sql(query, engine)
        df['avg_score'] = df['avg_score'].round(2)
        df.to_sql('avg_scores', engine, if_exists='replace', index=False)
        return df
    except Exception as e:
        st.error(f"Error during ETL pipeline: {e}")
        return None

# Streamlit app
st.title("SQLValidator Demo: Scalable SQL Applications")
st.subheader("Visualizing Student Performance Data")

# Sidebar for user input
st.sidebar.header("Configuration")
course_id = st.sidebar.number_input("Select Course ID", min_value=101, max_value=102, value=101)
run_pipeline = st.sidebar.button("Run ETL Pipeline")

# Main content
if run_pipeline:
    with st.spinner("Running ETL pipeline..."):
        df = run_etl_pipeline(course_id)
        if df is not None:
            st.success("ETL Pipeline completed successfully!")
            st.write("### Average Scores per Student")
            st.dataframe(df, use_container_width=True)

            # Visualization
            fig = px.bar(df, x='student_id', y='avg_score', title=f"Average Scores for Course {course_id}",
                         labels={'student_id': 'Student ID', 'avg_score': 'Average Score'},
                         color='avg_score', color_continuous_scale='Blues')
            st.plotly_chart(fig, use_container_width=True)

            # Save output to CSV
            df.to_csv('../data/sample_output.csv', index=False)
            st.write("Output saved to `data/sample_output.csv`")
else:
    st.info("Select a Course ID and click 'Run ETL Pipeline' to view results.")

# Query optimization demo
st.header("Query Optimization Demo")
st.write("Run the following SQL queries to compare performance with/without indexing:")
st.code("""
-- Initial query
EXPLAIN ANALYZE
SELECT student_id, AVG(score) AS avg_score
FROM student_scores
WHERE course_id = 101
GROUP BY student_id;

-- Create index
CREATE INDEX idx_course_id ON student_scores(course_id);

-- Optimized query
EXPLAIN ANALYZE
SELECT student_id, AVG(score) AS avg_score
FROM student_scores
WHERE course_id = 101
GROUP BY student_id;
""", language="sql")

# Footer
st.markdown("""
---
**About**: Developed by Dr. Chukwuka Victor Obionwu for Gisma University of Applied Sciences.  
**GitHub**: [github.com/victordeman/sqlvalidator-demo](https://github.com/victordeman/sqlvalidator-demo)
""")
