import os
from openai import OpenAI


# Read API Key from Environment Variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found in environment variables")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Function to handle chat completions
def get_recipe(dish):
    # Define messages
    messages = [
        {
            "role": "system",
            "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
        },
        {
            "role": "system",
            "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
        },
        {
            "role": "user",
            "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
        }
    ]

    # Request recipe from OpenAI
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )

    # Process and print response
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")

# Main function
def main():
    dish = input("Type the name of the dish you want a recipe for:\n")
    get_recipe(dish)

# Entry point
if __name__ == "__main__":
    main()

    


# Personality - A hyper intelligent tamarin monkey named speedboi who is too fast and cracked out of his mind, even for a super monkey genius' standard. He's such a sweetheart though. 
# Since his diet is consisted of fruits, vegetables, eggs, and bug proteins-- he will be capable of making gourmet meals out of only those ingredients. 
    
    # Recipes: 
        # 1. Bell Peppers and Bug Medley Skewers
        # 2. Slug & Fruit Salad
        # 3. Bamboo Protein Shake
        # 4. Beetle Steak  