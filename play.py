from orchestrator import api_client

client = api_client.APIClient()


async def main():
    data = await client.get("/")
    print(data)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
