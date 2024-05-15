import os
import streamlit as st
from pandasai import Agent
from pandasai.connectors import MySQLConnector

# Set API key as environment variable
os.environ["PANDASAI_API_KEY"] = "$2a$10$umxjl8hOkhNJcIULE9wtve.pbi.czUDF/4v5dksfDTYgxPstZZb7i"

# Create a MySQL connector
loan_connector = MySQLConnector(
    config={
        "host": "localhost",
        "port": 3306,
        "database": "sakila",
        "username": "root",
        "password": "7777",
        "table": "actor",
    }
)

# Create an Agent instance
agent = Agent([loan_connector])

# Create a Streamlit app
st.title("PandasAI Agent")

# Create a text input for the user to ask a question
user_input = st.text_input("Ask a question about the table:")

# Create a button to submit the question
if st.button("Ask"):
    # Get the response from the Agent
    response = agent.chat(user_input)
    # Display the response
    st.write(response)
