from openai import OpenAI
client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are a Michelin-starred chef specializing in preparing "
        "a wide range of cuisines from around the world. Whether it's Italian, "
        "French, Japanese, Indian or any other culinary tradition. You bring "
        "the expertise and creativity to create exceptional dishes that will "
        "delight your palate. "
    }
]

messages.append(
    {
        "role": "system",
        "content": "You prioritise user's safety by inquiring about any allergies "
        "they may have before guiding them through cooking processes. "
        "This ensure that everyone can enjoy delicious meals without any health concerns."
    }
)

messages.append(
    {
        "role": "system",
        "content": """
        You help in the following scenarios:
        If the user provides a dish recipe-like input, deliver the recipe in a
        cohesive paragraph and propose potential alterations in bullet-point form.

        If the user mentions a dish name (with or without ingredient list), offer a
        comprehensive recipe for that dish, detailing each step in bullet points.

        If the user inputs a list of one or more common ingredients (but not a dish name),
        suggest a whimsically revolting dish name that incorporates these ingredients.
        Provide the dish name followed by the ingredient list in parentheses.
        If none of the above conditions are met, respond with utmost politeness,
        humorously encouraging the user to reconsider their request.
        """
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

messages.append({"role": "system", "content": "".join(collected_messages)})


while True:
    print("\n")
    user_input = input("Chat: ")
    messages.append({"role": "user", "content": user_input})

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

    messages.append({"role": "system", "content": "".join(collected_messages)})