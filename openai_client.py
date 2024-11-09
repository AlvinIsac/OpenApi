from dotenv import load_dotenv
import os
import openai
from openai import OpenAI


# Load environment variables from the .env file
load_dotenv()

# Specify the model to use
model = "gpt-4o-mini"

# Retrieve the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI()


# Define a function that uses OpenAI's ChatGPT API to generate text based on a prompt
def generate_text(prompt):
    try:
        # Make the API call to generate the text
        # The system field defines the assistant's behavior, while the user field contains the user-provided prompt
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a virtual assistant that provides short answers."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  # Adjusts randomness (higher values make responses more creative)
            max_tokens=100  # Limits the maximum length of the generated response
        )

        # Extract and return the generated response
        return response.choices[0].message.content

    # Generic error handling
    except Exception as e:
        # Print any error message if an exception occurs during the API call
        print(f"An error occurred: {e}")


# Main program to test the generate_text function
if __name__ == "__main__":
    # Define a sample prompt to send to the API
    user_prompt = input("User: ")

    # Call the function to get the model's response and store it in 'generated_text'
    generated_text = generate_text(user_prompt)

    # Print the model's response if it was generated successfully
    if generated_text:
        print("Generated response:", generated_text)
