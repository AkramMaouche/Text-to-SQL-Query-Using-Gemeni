from dotenv import load_dotenv
load_dotenv() 

import streamlit as st 
import os 
import sqlite3
import google.generativeai as genai 


#configuer Api key 
genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

#Function to load gemini model and provide sql quory as response 

def get_response(question,prompt): 
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt,question])
    return response.text 


def read_sqlQuery(query,db): 
    connection = sqlite3.connect(db)
    curr = connection.cursor()
    curr.execute(query)
    rows = curr.fetchall()
    for row in rows: 
        print(row)
    connection.commit()
    connection.close()
    
    return rows 


# define the prompt 

prompt = """
You are an expert in converting English questions to SQL query. 
The SQL database has the following structure.

Create a SQL query that answers the question based on the database schema.\nExmeple1 -How many entries of records are present 
the sql command will be somthing like this SELECT COUNT(*) FROM STUDENT ; 
\nExmple 2 - tell me the student studying in the Chemistry class ?
the sql command will be somthing like this SELECT NAME FROM STUDENT WHERE Class = 'Chemistry' ;
\n also the sql syntax  should not have   " ```sql
```" in the beginning or in the end of the word in output 
"""

st.title("App to retrieve SQL Data with GEMINI")
st.subheader("Ask Me About the Database")
question = st.text_input("Enter your question",key = "input")

submit =  st.button("Get Response")

if submit : 

    response  =  get_response(question,prompt)
    print(response)
    data = read_sqlQuery(response, "Student.db")
    st.subheader("The Response is")
    print(data)
    st.header(data)


