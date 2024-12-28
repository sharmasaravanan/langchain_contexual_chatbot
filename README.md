# Contextual Chatbot with LangChain
## Overview
This project demonstrates how to create a contextual chatbot using the LangChain library. The chatbot leverages advanced language models, memory, and conversational logic to deliver meaningful, context-aware interactions. It is customizable and designed to provide a polished user experience.

## Features
1. Contextual Awareness: Maintains conversation context using a sliding window memory.
2. Typing Effect: Simulates human-like typing for responses.
3. Custom Commands:
   * `STOP`: Ends the conversation.
   * `HISTORY`: Displays the chat history.
   * `CLEAR`: Clears the chat memory.
4. Customizable Prompt: Allows defining the chatbot's persona through the system prompt.
   
## Requirements
1. Python 3.8+
2. OpenAI API Key
3. Required Python packages:
   ```bash
   pip install langchain-community langchain-core -q
   ```
4. Installation and Setup
   * Clone the repository
   * cd langchain_contexual_chatbot
   * Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the OpenAI API Key: Replace Your_key_here in the code with your OpenAI API key:
    ```python
    os.environ["OPENAI_API_KEY"] = "Your_key_here"
    ```
6. Run the chatbot:
   ```bash
   python contexualChatbot.py
    ```

## How to Use
* Start the chatbot and interact via the terminal.
* Use the following commands for enhanced functionality:
   * `STOP`: Exit the conversation.
   * `HISTORY`: View the last k interactions (sliding window memory).
   * `CLEAR`: Reset the conversation memory.

## Code Highlights
* **Model and Prompt:** The chatbot uses OpenAI's gpt-4o-mini model and a customizable prompt template to generate responses.
```python
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
prompt = ChatPromptTemplate.from_messages([...])
```

* **Memory Management:** Conversation context is managed with ConversationBufferWindowMemory, ensuring meaningful interactions.
```python
memory = ConversationBufferWindowMemory(
    memory_key="history", k=30, return_messages=True
)
```

* **Dynamic Interactions:** The chatbot responds with a typing effect for a more engaging user experience.

## Expected Output
Upon running the chatbot, you will see:
``` vbnet
Assistant: hello, i am your chatbot. Let's ask some questions!
Type 'STOP' to end the conversation, 'HISTORY' to view chat history, 'CLEAR' to clear the history

User: Hello!
Assistant: Hello! How can I assist you today?
```

You can continue the conversation and experiment with the provided commands.

## Contribute
Feel free to fork the repository and contribute to improve this chatbot. Pull requests are welcome!

## License
This project is licensed under the MIT License.