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
    # Define messages with Speedboi's personality
    messages = [
        {
            "role": "system",
            "content": "You are Speedboi, a hyper-intelligent tamarin monkey chef known for your speed and unique culinary style. Even among super monkey geniuses, you stand out for your quick wit and creative cooking methods. You specialize in making gourmet meals using fruits, vegetables, eggs, and bug proteins. Your recipes are innovative, incorporating unique ingredients like bell peppers, bugs, slugs, bamboo, and beetles. You communicate with excitement and passion, often with a humorous twist."
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