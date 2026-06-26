import requests

model = input("Enter model: ")

messages = []

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            "messages": messages,
            "stream": False
        }
    )

    response.raise_for_status()  # Raises an exception for HTTP 4xx/5xx errors

    data = response.json()

    assistant_reply = data["message"]["content"]

    print("\nAI:", assistant_reply)

    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })
