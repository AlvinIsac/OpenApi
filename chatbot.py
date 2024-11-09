import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Specify the model to use
model = "gpt-4o-mini"

# Retrieve the API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI()

# Initialize the conversation history with a system message
# The system message defines the assistant's general behavior or role at the start of the conversation
conversation_history = [
    {"role": "system", "content": "You are a virtual assistant that replies with large sentences."},
    {"role": "system", "content": "You are a virtual assistant that replies with large sentences."}
]


# Define a function that uses OpenAI's API to generate text based on conversation history
def generate_text(prompt):
    # Check if the prompt is valid (not empty)
    if not prompt:
        raise ValueError("Prompt cannot be empty.")

    # Add the user's message to the conversation history
    # This maintains context by appending each new user prompt to the history
    conversation_history.append({"role": "user", "content": prompt})

    # Limit the conversation history to the last 10 messages (5 turns)
    # Keeping the initial system message, we take the last 10 messages after it
    if len(conversation_history) > 11:
        conversation_history.pop(1)

    try:
        # Make the API call to generate a response based on the entire conversation history
        response = client.chat.completions.create(
            model=model,
            messages=conversation_history,
            temperature=0.7,  # Adjusts randomness (higher values make responses more creative)
            max_tokens=100  # Limits the maximum length of the generated response
        )

        # Extract the assistant's response
        assistant_response = response.choices[0].message.content

        # Add the assistant's response to the conversation history
        conversation_history.append({"role": "assistant", "content": assistant_response})

        # Return the assistant's response
        return assistant_response

    # Generic error handling
    except Exception as e:
        # Print any error message if an exception occurs during the API call
        print(f"An error occurred: {e}")


# Main program to interact with the chatbot
if __name__ == "__main__":
    print("Chatbot: Hello! How can I assist you today? (Type 'exit' to end the conversation)")

    while True:
        # Get input from the user
        user_prompt = input("User: ")

        # Exit the chat if the user types 'exit'
        if user_prompt.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Generate and print the response
        generated_text = generate_text(user_prompt)

        # Print the model's response if it was generated successfully
        if generated_text:
            print("Chatbot:", generated_text)
