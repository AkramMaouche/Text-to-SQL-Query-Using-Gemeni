from dotenv import load_dotenv
load_dotenv() 

import streamlit as st 
import os 
import sqlite3
import google.generativeai as genai 


#configuer Api key 
genai.configure(api_keys = os.getenv("GOOGLE_API_KEY"))

#Function to load gemini model and provide sql quory as response 

def get_response(question,prompt): 
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_contect([prompt,question])
    return response.text 


def read_sqlQuery(query,db): 
    connection = sqlite3.connect(db)
    curr = connection.cursor()
    curr.execute(query)
    rows = curr.fetchall 
    connection.commit()
    connection.close()
    for row in rows: 
        print(row)
    return rows 


# define the prompt 

prompt = """
You are an expert in converting English questions to SQL query. 
The SQL database has the following structure.

Create a SQL query that answers the question based on the database schema.
"""

st.title("App to retrieve SQL Data with GEMINI")


