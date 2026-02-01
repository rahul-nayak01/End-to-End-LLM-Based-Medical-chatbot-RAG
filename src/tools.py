from langchain.tools import Tool

def get_retriever_tool(retriever):
    return Tool(
        name="Medical_Knowledge_Retriever",
        func=lambda q: "\n".join(
            [doc.page_content for doc in retriever.get_relevant_documents(q)]
        ),
        description=(
            "Use this tool to retrieve medical knowledge from documents. "
            "Input should be a medical question or keyword."
        )
    )
