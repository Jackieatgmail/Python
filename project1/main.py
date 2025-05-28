from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool, tool
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

@tool
def calcultor(input_string: str) -> str:
    """A simple calculator tool that adds two numbers. Provide the numbers separated by a comma."""
    try:
        nums = [float(x.strip()) for x in input_string.split(',')]
        if len(nums) != 2:
            return "Please provide exactly two numbers separated by a comma."
        a, b = nums
        return f"The sum of {a} and {b} is {str(a + b)}."
    except ValueError:
        return "Please provide valid numbers separated by a comma."
    
@tool
def say_hello(name: str) -> str:
    """A simple tool that greets the user by name."""
    print("Tool has been called with name:", name)
    return f"Hello, {name}!"

def main():
    model = ChatOpenAI(temperature=0)
    tools = [calcultor, say_hello]
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=model, tools=tools, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit. ")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        print("\nAssistant: ", end="")
        response = agent_executor.invoke({"input": user_input})
        print(response["output"])

if __name__ == "__main__":
    main()

