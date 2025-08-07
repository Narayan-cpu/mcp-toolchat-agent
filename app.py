import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def run_memory_chat():
    # Load .env
    load_dotenv()

    groq_key = os.getenv("GROQ_API_KEY")
    if not groq_key:
        raise EnvironmentError("GROQ_API_KEY is missing. Please add it to your .env file.")

    # (Optional) Only if a library requires os.environ directly
    os.environ["GROQ_API_KEY"] = groq_key

    config_file = "browser_mcp.json"

    print("Initializing MCP Agent...")
    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="llama3-70b-8192")
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,
    )

    print("\n=== Interactive MCP Chat ===")
    print("Enter 'exit' to end the chat.")
    print("Enter 'clear' to clear the memory.")
    print("====================================")

    try:
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Memory cleared.")
                continue

            print("\nAssistant: ", end="", flush=True)
            try:
                response = await agent.run(user_input)
                print(response)
            except Exception as e:
                print(f"\nError: {e}")

    except KeyboardInterrupt:
        print("\nInterrupted by user.")

    finally:
        if client and client.sessions:
            await client.close_all_sessions()
            print("Closed all sessions.")

if __name__ == "__main__":
    asyncio.run(run_memory_chat())
