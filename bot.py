from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes
import os

BOT_TOKEN = "8631577677:AAG5-0w1UGGkE5HsscPc2PUHAc_gOFPE0lQ"

async def approve_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request
    if join_request is None:
        return

    await context.bot.approve_chat_join_request(
        chat_id=join_request.chat.id,
        user_id=join_request.from_user.id
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(approve_join_request))
    app.run_polling()

if __name__ == "__main__":
    main()
