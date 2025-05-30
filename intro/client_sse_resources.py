from fastmcp  import Client

async def main():
    try:
        async with Client("http://localhost:8000/sse") as client:
            print("Client connected to server.")

            resources = await client.list_resources()
            print(f"Available resources: {resources}")

            if resources:
                resource = resources[0]
                print(f"Reading resource: {resource.name}")
                result = await client.read_resource(resource.uri)
                print(f"Resource '{resource}' content: {result}")
            else:
                print("No resources found on the server.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())