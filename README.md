# PyOllamaChat

A simple command-line chatbot built in Python that interacts with locally hosted Large Language Models (LLMs) through Ollama's REST API.

Instead of using the Ollama Python package, this project communicates directly with the local Ollama server using the `requests` library, providing a hands-on example of REST API integration in Python.

---

## Features

* Interactive command-line chat interface
* Support for any Ollama model installed on the system
* Session-based conversation memory
* Direct communication with Ollama via its REST API
* Lightweight and beginner-friendly implementation
* Runs completely locally without external APIs

---

## Requirements

* Python 3.10+
* Ollama installed and running
* At least one downloaded Ollama model

---

## Installation

1. Clone the repository

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Ollama

Before starting the chatbot, ensure that the Ollama server is running and that you have downloaded at least one model.

For example:

```bash
ollama run qwen3:8b
```

You can view installed models with:

```bash
ollama list
```

---

## Usage

Run the chatbot:

```bash
python PyOllamaChat.py
```

Enter the name of an installed model:

```text
Enter model: qwen3:8b
```

Example conversation:

```text
You: Explain linked lists

AI: A linked list is a linear data structure...
```

Exit the application at any time:

```text
You: exit
```

---

## Supported Models

Any model installed through Ollama can be used, including:

* qwen3:8b
* qwen3-coder
* llama3.2
* gemma3
* deepseek-r1

---

## How It Works

1. The user selects an installed Ollama model.
2. Messages are stored in a conversation history list.
3. The application sends a POST request to Ollama's local REST API (`http://localhost:11434/api/chat`).
4. Ollama generates a context-aware response using the selected model.
5. The assistant's reply is displayed and added to the conversation history.

---

## Technologies Used

* Python
* Requests
* REST APIs
* Ollama
* Local Large Language Models (LLMs)

---

## Learning Outcomes

This project demonstrates:

* Consuming REST APIs using Python
* Sending HTTP POST requests with JSON payloads
* Parsing JSON responses
* Managing conversation history for LLM interactions
* Building a simple command-line chatbot
* Working with locally hosted AI models

---

## Future Improvements

* Streaming responses as they are generated
* Save chat history to files

---

## License

This project is licensed under the MIT License.
