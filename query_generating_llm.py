# -*- coding: utf-8 -*-
import os
import json
from sqlalchemy import create_engine, inspect, text
import streamlit as st
from groq import Groq

client = Groq(api_key="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")  # Replace with your valid API key


def get_schema(engine):
    """
    Extract the schema of the SQLite database.

    Args:
        engine: SQLAlchemy database engine object.

    Returns:
        dict: A dictionary containing the database schema.
    """
    inspector = inspect(engine)
    schema = {}
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        foreign_keys = inspector.get_foreign_keys(table_name)
        schema[table_name] = {
            "columns": {col["name"]: str(col["type"]) for col in columns},
            "primary_keys": inspector.get_pk_constraint(table_name),
            "foreign_keys": {fk["constrained_columns"][0]: fk["referred_table"] for fk in foreign_keys},
        }
    return schema


def generate_query_with_groq(context, user_input):
    prompt = f"""
    The database schema is as follows:
    {json.dumps(context, indent=2)}

    Write only the SQL query for the following request:
    "{user_input}"
    Ensure the query is compatible with SQLite and uses SQLite syntax, such as strftime for date handling. Do not include explanations, assumptions, or comments. Only return the SQL query.
    """
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content.strip()

def execute_query(engine, query):
    """
    Execute the generated SQL query against the SQLite database.

    Args:
        engine: SQLAlchemy database engine object.
        query: str, The SQL query to execute.

    Returns:
        list or str: The result of the query or an error message.
    """
    try:
        if not query.strip().lower().startswith(("select", "insert", "update", "delete", "create", "drop")):
            return f"Invalid SQL query returned: {query}"
        with engine.connect() as conn:
            result = conn.execute(text(query)).fetchall()
        return result
    except Exception as e:
        return f"Error executing query: {str(e)}"


def main():
    """
    Main function to run the Streamlit app.
    """
    st.set_page_config(page_title="SQL Query Generator", layout="centered")

    # App Header
    st.title("Query Generating LLM Model")
    st.markdown("""
        Welcome to the SQL Query Generator.
        Upload your SQLite database file (`.db`) and generate SQL queries based on natural language input.
        Begin by uploading your database below.
    """)

    uploaded_file = st.file_uploader("Upload your SQLite database file (.db)", type="db")

    if uploaded_file is not None:
        db_path = os.path.join("temp_uploaded_db.db")
        with open(db_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Database file '{uploaded_file.name}' uploaded successfully.")

        engine = create_engine(f"sqlite:///{db_path}")

        schema = get_schema(engine)
        if not schema:
            st.error("The uploaded database contains no tables. Please upload a valid SQLite database.")
            return
        st.subheader("Database Schema")
        st.json(schema)

        user_input = st.text_input("Enter your query in plain English:")
        if st.button("Generate SQL Query"):
            if user_input.strip() == "":
                st.warning("Please enter a query.")
            else:
                sql_query = generate_query_with_groq(schema, user_input)
                st.subheader("Generated SQL Query")
                st.code(sql_query, language="sql")

                st.subheader("Query Results")
                results = execute_query(engine, sql_query)
                if isinstance(results, list):
                    st.write(results)
                else:
                    st.error(results)
    else:
        st.info("Upload your SQLite database file to get started.")

    st.markdown("""
    ---
    Created by Ankan.
    """)


if __name__ == "__main__":
    main()
