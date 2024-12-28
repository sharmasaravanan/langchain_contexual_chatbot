""" This file contains the code to create a contextual chatbot using the langchain library. """
# to install the required packages, run the following command in the terminal
# !pip install langchain-community langchain-core -q

import sys
import os
import time

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferWindowMemory
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda

from typing import List, Tuple
from operator import itemgetter

import warnings

warnings.filterwarnings("ignore")
os.environ["OPENAI_API_KEY"] = "Your_key_here"


# function to format the message
def format_message(role: str, content: str) -> str:
    """Format the message to be printed in the console."""
    return f"{role.capitalize()}: {content}"


# function to get the chat memory
def get_chat_memory(memory) -> List[Tuple[str, str]]:
    """Get the chat memory from the memory object."""
    return [(msg.type, msg.content) for msg in memory.chat_memory.messages]


# function to print the typing effect
def print_typing_effect(text: str, delay: float = 0.05) -> None:
    """Print the text with a typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# function to run the chatbot
def run_chatgpt_chatbot(system_prompt="", history_window=30, temperature=0):
    """Run the chatbot with the specified parameters."""
    # Create the chatbot model
    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=temperature)

    if system_prompt:
        system_message = system_prompt
    else:
        system_message = "You are a helpful assistant."
    # Create the chat prompt template with the system message and history placeholder
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ]
    )

    # Create the memory object to store the chat history
    memory = ConversationBufferWindowMemory(
        memory_key="history",
        k=history_window,
        return_messages=True
    )

    # Create the conversation chain with the prompt and model as the steps
    conversation_chain = (
            RunnablePassthrough.assign(
                history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
            )
            | prompt
            | model
    )

    # Start the conversation
    print_typing_effect("Assistant: hello, i am your chatbot. Let's ask some questions!")
    # Print the instructions
    print("Type 'STOP' to end the conversation, 'HISTORY' to view chat history, 'CLEAR' to clear the history ")

    # Start the conversation loop with the user input and the conversation chain
    while True:
        user_input = input("\nUser: ")

        # Check if the user input is a special command to stop the conversation
        if user_input.upper() == "STOP":
            print_typing_effect("Assistant: Goodbye! :). It was nice talking to you.")
            break

        # Check if the user input is a special command to view the chat history
        elif user_input.strip().upper() == "HISTORY":
            chat_history = get_chat_memory(memory)
            print("-----Chat History----")
            for role, content in chat_history:
                print(format_message(role, content))
            print("-----End of Chat History----")
            continue

        # Check if the user input is a special command to clear the chat history
        elif user_input.strip().upper() == "CLEAR":
            memory.clear()
            print_typing_effect("Assistant: Chat history cleared.")
            continue

        # Invoke the conversation chain with the user input
        user_inp = {"input": user_input}
        response = conversation_chain.invoke(user_inp)
        print_typing_effect(format_message("assistant", response.content))
        # Save the context of the conversation
        memory.save_context(
            {"input": user_input},
            {"output": response.content}
        )


if __name__ == "__main__":
    # Run the chatbot
    run_chatgpt_chatbot()
