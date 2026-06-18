# PyOllamaChat
Simple CLI chatbot in Python powered by locally hosted Ollama models.

This project allows users to interact with locally hosted Large Language Models (LLMs) such as Qwen, Llama, Gemma, and DeepSeek through a conversational terminal interface while maintaining chat history throughout the session.

## Features

* Interactive command-line chat interface
* Support for any Ollama model installed on the system
* Conversation memory within a session
* Lightweight and beginner-friendly implementation
* Runs completely locally using Ollama

## Requirements

* Python 3.10+
* Ollama installed and running
* At least one downloaded Ollama model

## Installation

1. Clone the repository

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Start the application:

```bash
python PyOllamaChat.py
```

Enter the name of an installed Ollama model:

```text
Enter model: qwen3:8b
```

Begin chatting:

```text
You: Explain linked lists

AI: A linked list is a linear data structure...
```

Exit the application at any time:

```text
You: exit
```

## Example Models

* qwen3:8b
* qwen3-coder
* llama3.2
* gemma3
* deepseek-r1

List installed models:

```bash
ollama list
```

## How It Works

1. The user selects an installed Ollama model.
2. Messages are stored in a conversation history list.
3. The entire conversation history is sent to Ollama with each request.
4. The model generates a context-aware response.
5. The response is appended to the conversation history.

## Technologies Used

* Python
* Ollama Python Library
* Local Large Language Models (LLMs)

## Future Improvements

* Save chat history to files
* Web interface using

## License

MIT License
