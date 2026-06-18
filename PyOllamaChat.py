from ollama import chat

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

    response = chat(
        model=model,
        messages=messages
    )

    assistant_reply = response["message"]["content"]

    print("\nAI:", assistant_reply)

    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })
