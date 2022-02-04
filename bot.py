import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

DarkLord=Client(
    "ApprovedV2 Bot",
    bot_token = os.environ["5229022310:AAFr6QttWUFaBiwXBlF9HC_ih0-Uyw4pAnE"],
    api_id = int(os.environ["10585308"]),
    api_hash = os.environ["c8e7cb62c10c52bfae94ed0e3223103d"],
)

CHAT_ID=int(os.environ.get("CHAT_ID",1725059127))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "👋Hello {mention}\nWelcome To {title}\n\nYour ApprovedV2")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@darklord.on_message(filters.private & filters.command(["start"]))
async def start(client: DarkLord, message: Message):
    approvedV2bot = await client.get_me() 
    button=[[
      InlineKeyboardButton("📦 Repo", url="https://github.com/Bikash-Darklord/ApprovedV2-Bot"),
      InlineKeyboardButton("Updates 📢", url="@hellodarklord")
      ],[
      InlineKeyboardButton("➕️ Add Me To Your Group ➕️", url=f"http://t.me/{approvedV2bot.username}?startgroup=botstart")
      ]]
    await message.reply_text(text="**__Hello Iam ApprovedV2 Join Request Bot Repo https://github.com/Bikash-Darklord/ApprovedV2-Bot**__", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@Darklord.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} Joined 🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))
        print("Welcome....")

print("ApprovedV2 Bot")
DarkLord.run()
