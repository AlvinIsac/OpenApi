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
   OPENAI_API_KEY=sk-proj-DYqEnmc8k0RVHIC6xe8ZqvJzKHaNArMGy0cidt9LtDOav7mQ7ZxTprwpvzk1y369PtPssIf-IO T3BlbkFJQYetvcgrpzQXHUoceHoYTxa_dNo9qenFQ90ILzBWwdluEaPCHncw0L-y7e4NDQiWK1Oj3De6cA
   ```

   **Note**: If the provided key is not working, you can purchase a new one from [OpenAI's Platform](https://platform.openai.com/docs/overview).

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

---

This `README.md` includes all relevant details for users to set up and interact with your project effectively. Let me know if there's anything more you'd like to add!
