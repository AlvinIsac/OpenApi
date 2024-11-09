from dotenv import load_dotenv
import os
import requests


# Load environment variables from the .env file
load_dotenv()

model = "gpt-4o-mini"

# Set the API endpoint and headers for the OpenAI request
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
    "Content-Type": "application/json"
}


# Define a function that uses OpenAI's REST API to generate text based on a prompt
def generate_text(prompt):
    # Define the request data, including the model, role messages, and other parameters
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a virtual assistant that provides short and very very happy answers."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7  # Adjusts randomness (higher values make responses more creative)
    }

    try:
        # Make the POST request to OpenAI's API
        response = requests.post(url, headers=headers, json=data)
        print(response)

        # Check for a successful response
        if response.status_code == 200:
            # Extract and return the assistant's response
            return response.json()['choices'][0]['message']['content']
        else:
            # Print an error message if the request was unsuccessful
            print(f"Request failed: {response.status_code} - {response.text}")

    # Generic error handling
    except Exception as e:
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
