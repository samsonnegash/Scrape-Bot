import asyncio
from pyrogram import Client

api_id = 6714914
api_hash = "085be5963f38db1cb5dac0b01acdce55"


async def main():
    async with Client("my_account", api_id, api_hash) as app:


# Get members
async for member in app.get_chat_members(chat_id):
    print(member)

# Get administrators
administrators = []
async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
    administrators.append(m)

# Get bots
bots = []
async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
    bots.append(m)

asyncio.run(main())
