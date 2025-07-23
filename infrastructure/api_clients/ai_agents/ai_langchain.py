





from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool

def search_orders(query):
    # логика поиска заказа
    return f"Результаты по '{query}'"

def send_prompt():
    tools = [
        Tool(name="Поиск заказов", func=search_orders, description="Ищет заказы по запросу")
    ]

    llm = ChatOpenAI(temperature=0.3)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

    result = agent.run("Найди заказы клиента Иванов")
    print(result)
    return True
