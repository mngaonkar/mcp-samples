from fastmcp  import Client

async def main():
    try:
        async with Client("http://localhost:8000/sse") as client:
            print("Client connected to server.")
            prompts = await client.list_prompts()
            print(prompts)
            
            for prompt in prompts:
                print(f"Prompt: {prompt.name}")
                result = await client.get_prompt(prompt.name)
                print(f"result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())