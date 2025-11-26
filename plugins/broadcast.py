from pyrogram import Client, filters
from pyrogram.types import Message

# Only allow owner (you)
OWNER_ID = 7845335174   # change to your ID

# Broadcast command
@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_func(client: Client, message: Message):
    reply = message.reply_to_message

    if not reply:
        return await message.reply("Reply to a message you want to broadcast.")

    sent = 0
    failed = 0

    async for dialog in client.get_dialogs():
        try:
            await reply.copy(dialog.chat.id)
            sent += 1
        except:
            failed += 1

    await message.reply(f"**Broadcast completed!**\n\n✅ Sent: {sent}\n❌ Failed: {failed}")
