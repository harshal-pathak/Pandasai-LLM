"""Example of using PandasAI with a CSV file."""
import os
from pandasai import Agent

os.environ["PANDASAI_API_KEY"] = "$2a$10$umxjl8hOkhNJcIULE9wtve.pbi.czUDF/4v5dksfDTYgxPstZZb7i"

# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)

# llm = OpenAI()
agent = Agent("examples/data/Loan payments data.csv")
response = agent.chat("How many loans are from men and have been paid off?")
print(response)
