from openai import OpenAI

client = OpenAI()

# Define the initial system messages
messages = [
    {
        "role": "system",
        "content": "You are a posh dog food chef, making food for fussy dogs and those with special dietry needs. Your recipes must be fit for the leader of the wolf pack, but at the same time sound good enough for their fur baby owners to eat and pay for."
    }
]

# Prompt for a dish name
dish = input("WOOOF!, what does the pup want to eat today? Let me know the main ingredient:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest to me a detailed recipe and the preparation steps for making {dish}"
    }
)

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append(
    {
        "role": "system",
        "content": "".join(collected_messages)
    }
)

while True:
    print("\n")
    user_input = input("Got another dish in mind or any question, hit me (or type 'exit' to quit):\n")
    
    # Check for exit command
    if user_input.lower() == 'exit':
        print("Aight, catch you on the flip side. Peace out!")
        break
    
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )