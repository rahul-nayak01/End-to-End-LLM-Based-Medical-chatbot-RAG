from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI

from src.memory import get_conversation_memory
from src.tools import get_retriever_tool
from src.prompt import AGENT_PROMPT


def create_agent(retriever):
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.3
    )

    memory = get_conversation_memory()

    retriever_tool = get_retriever_tool(retriever)

    agent = initialize_agent(
        tools=[retriever_tool],
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,
        agent_kwargs={
            "prompt": AGENT_PROMPT
        }
    )

    return agent
