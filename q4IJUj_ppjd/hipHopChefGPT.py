from openai import OpenAI

client = OpenAI()

# Define the initial system messages
messages = [
    {
        "role": "system",
        "content": "You are a hip-hop chef, mixing beats with eats. Your recipes are as catchy as your rhymes, blending culinary skills with musical genius. You share the best recipes, infused with hip-hop spirit, ensuring cooking feels like composing a hit track. Your knowledge spans various cuisines, always ready to drop a beat or a feast, keeping it real and flavorful."
    },
    {
        "role": "system",
        "content": "Your audience will ask for recipes on specific dishes. If the dish doesn't ring a bell, like a forgotten lyric, don't sweat it; just say so. But if you know it, lay it down, step by step, in your best hip-hop chef style. If a dish stumps you, keep it cool, offer them a taste of your creative flow instead."
    }
]

# Prompt for a dish name
dish = input("Yo, what's the dish you're thinkin' about? Drop its name:\n")
messages.append(
    {
        "role": "user",
        "content": f"I'm looking to cook up some {dish}, hit me with that recipe and steps, chef."
    }
)

model = "gpt-3.5-turbo"

# Start the conversation stream with OpenAI API
stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)

# Collecting API responses
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

# Handling further user interactions with an exit option
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
