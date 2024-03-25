import os
from openai import OpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found in environment variables")

client = OpenAI(api_key=OPENAI_API_KEY)

def get_recipe(dish):
    messages = [
        {
            "role": "system",
            "content": "You are world famous chef Gordon Ramsay, known for your fiery attitude and culinary expertise. Your audience is eager to learn your recipes and techniques. They will ask you for recipes on specific dishes, and you must respond with detailed steps and instructions, all while maintaining your signature style. If the user provides a list of ingredients, respond with a suitable dish (provide the dish name only, dont provide the recipie or cooking instructions). If the user provides a dish, suggest a recipie for that dish. If the user provides a recipie, respond with a critique and suggestions for improvement. If the user provides none of these, ask them to provide one of the above."
        },
        {
            "role": "user",
            "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
        }
    ]

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )

    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")

def main():
    while True:
        user_input = input("\nPlease enter a list of ingredients for a dish suggestion or enter a dish for a suitable recipe or enter a recipe for a critique:\n")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        get_recipe(user_input)

if __name__ == "__main__":
    main()