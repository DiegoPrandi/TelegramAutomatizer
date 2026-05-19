from app.telegram.client import client

async def main():

    await client.start()

    me = await client.get_me()

    print(f"Logado como: {me.first_name}")

with client:
    client.loop.run_until_complete(main())