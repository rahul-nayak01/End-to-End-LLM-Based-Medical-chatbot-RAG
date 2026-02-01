from langchain.memory import ConversationBufferMemory

def get_conversation_memory():
    """
    Creates a conversation buffer memory to store full chat history.
    """
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    return memory
