# ![PandasAI](images/logo.png)


PandasAI is a Python library that makes it easy to ask questions to your data in natural language. It helps you to explore, clean, and analyze your data using generative AI.

# 🔧 Getting started

The documentation for PandasAI to use it with specific LLMs, vector stores and connectors, can be found [here](https://pandas-ai.readthedocs.io/en/latest/).

## 📦 Installation

With pip:

```bash
pip install pandasai
```

With poetry:

```bash
poetry add pandasai
```

## 🔍 Demo

Try out PandasAI yourself in your browser:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZnO-njhL7TBOYPZaqvMvGtsjckZKrv2E?usp=sharing)

# 🚀 Deploying PandasAI

PandasAI can be deployed in a variety of ways. You can easily use it in your Jupyter notebooks or streamlit apps, or you can deploy it as a REST API such as with FastAPI or Flask.

If you are interested in managed PandasAI Cloud or self-hosted Enterprise Offering, take a look at [our website](https://pandas-ai.com) or [book a meeting with us](https://zcal.co/gventuri/pandas-ai-demo).

## 💻 Usage

### Ask questions

```python
import os
import pandas as pd
from pandasai import Agent

# Sample DataFrame
sales_by_country = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "sales": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})

# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
os.environ["PANDASAI_API_KEY"] = "YOUR_API_KEY"

agent = Agent(sales_by_country)
agent.chat('Which are the top 5 countries by sales?')
```

```
China, United States, Japan, Germany, Australia
```

---

Or you can ask more complex questions:

```python
agent.chat(
    "What is the total sales for the top 3 countries by sales?"
)
```

```
The total sales for the top 3 countries by sales is 16500.
```

### Visualize charts

You can also ask PandasAI to generate charts for you:

```python
agent.chat(
    "Plot the histogram of countries showing for each the gdp, using different colors for each bar",
)
```

![Chart](images/histogram-chart.png?raw=true)

### Multiple DataFrames

You can also pass in multiple dataframes to PandasAI and ask questions relating them.

```python
import os
import pandas as pd
from pandasai import Agent

employees_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Emma', 'Liam', 'Olivia', 'William'],
    'Department': ['HR', 'Sales', 'IT', 'Marketing', 'Finance']
}

salaries_data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Salary': [5000, 6000, 4500, 7000, 5500]
}

employees_df = pd.DataFrame(employees_data)
salaries_df = pd.DataFrame(salaries_data)

# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
os.environ["PANDASAI_API_KEY"] = "YOUR_API_KEY"

agent = Agent([employees_df, salaries_df])
agent.chat("Who gets paid the most?")
```

```
Olivia gets paid the most.
```
