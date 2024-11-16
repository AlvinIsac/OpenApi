# Customized Chatbot with OpenAI API

This project is a simple chatbot that leverages the OpenAI API to generate conversational responses based on user inputs and maintains conversation history for contextual relevance. 

## Features

- Uses OpenAI's API to generate responses with context retention.
- Configuration options for model selection, response creativity, and token length.
- Secure handling of API keys through environment variables.
- Terminal-based interface for user interaction.

## Prerequisites

Ensure you have the following installed:

- Python 3
- Virtual environment
- OpenAI API key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AlvinIsac/OpenApi.git
   ```

2. Navigate to the project directory:

   ```bash
   cd OpenApi
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY= <open_api_key>
   ```

   **Note**: You can purchase a new one from [OpenAI's Platform](https://platform.openai.com/docs/overview).

## Usage

1. Run the chatbot script:

   ```bash
   python chatbot.py
   ```

2. Interact with the chatbot by typing messages and you can also customise it for your needs. Type `exit` to end the conversation.

## Configuration

- `model`: Specifies the OpenAI model to use (default: `gpt-4o-mini`).
- `temperature`: Controls response creativity (default: 0.7).
- `max_tokens`: Sets the maximum length of responses (default: 100 tokens).


