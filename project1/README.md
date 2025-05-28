# AI Assistant with Calculator

This is a simple AI assistant built using LangChain that can perform calculations and chat with users. The assistant uses OpenAI's ChatGPT model and includes a calculator tool for basic arithmetic operations.

## Features

- Interactive chat interface
- Calculator tool for adding numbers
- Easy to extend with additional tools
- Uses LangChain's agent system

## Requirements

- Python 3.13+
- OpenAI API key
- Required packages:
  - langchain
  - langchain-openai
  - python-dotenv

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the assistant: `python main.py`

## Usage

Start the assistant and type your questions. You can:
- Ask it to perform calculations (e.g., "add 7 and 9")
- Chat with it naturally
- Type 'quit' to exit

## License

MIT License
