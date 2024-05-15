import os
from pandasai import Agent
from pandasai.connectors import MySQLConnector

# With a MySQL database
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


# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
os.environ["PANDASAI_API_KEY"] = "$2a$10$umxjl8hOkhNJcIULE9wtve.pbi.czUDF/4v5dksfDTYgxPstZZb7i"

agent = Agent([loan_connector])
response = agent.chat("How many rows are there in table?")
print(response)
