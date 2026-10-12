import asyncio
import http.server
import os
import socketserver
import threading
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from telegram.request import HTTPXRequest

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = "852128844"  # Your personal Telegram User ID


# --- DUMMY HTTP SERVER FOR RENDER WEB SERVICE ---
def run_dummy_server():
  port = int(os.getenv("PORT", 8080))

  class SimpleHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
      self.send_response(200)
      self.end_headers()
      self.wfile.write(b"Habesha SMM Bot is live!")

  with socketserver.TCPServer(("", port), SimpleHandler) as httpd:
    httpd.serve_forever()


# --- BOT HANDLERS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  context.user_data.clear()

  keyboard = [
      [
          InlineKeyboardButton("📸 Instagram", callback_data="instagram"),
          InlineKeyboardButton("🎵 TikTok", callback_data="tiktok"),
      ],
      [
          InlineKeyboardButton("📘 Facebook", callback_data="facebook"),
          InlineKeyboardButton("✈️ Telegram", callback_data="telegram"),
      ],
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)

  await update.message.reply_text(
      "🤖 Welcome to Habesha SMM Shop!\n\nChoose a platform:",
      reply_markup=reply_markup,
  )


async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
  query = update.callback_query
  data = query.data
  await query.answer()

  if data == "instagram":
    keyboard = [
        [
            InlineKeyboardButton("👤 Followers", callback_data="ig_followers"),
            InlineKeyboardButton("❤️ Likes", callback_data="ig_likes"),
        ],
        [
            InlineKeyboardButton("👁️ Views", callback_data="ig_views"),
            InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back_home"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "📸 Instagram Services\n\nChoose a service:", reply_markup=reply_markup
    )

  elif data == "ig_followers":
    keyboard = [
        [InlineKeyboardButton("1K Followers — 500 ብር", callback_data="ig_f_1k")],
        [InlineKeyboardButton("5K Followers — 2,300 ብር", callback_data="ig_f_5k")],
        [
            InlineKeyboardButton(
                "10K Followers — 3,500 ብር", callback_data="ig_f_10k"
            )
        ],
        [
            InlineKeyboardButton(
                "50K Followers — 15,000 ብር", callback_data="ig_f_50k"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back to Instagram Menu", callback_data="instagram"
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "📈 Instagram Followers\n\nSelect a package:", reply_markup=reply_markup
    )

  elif data == "ig_likes":
    keyboard = [
        [InlineKeyboardButton("1K Likes — 300 ብር", callback_data="ig_l_1k")],
        [InlineKeyboardButton("5K Likes — 1,200 ብር", callback_data="ig_l_5k")],
        [
            InlineKeyboardButton(
                "10K Likes — 1,800 ብር", callback_data="ig_l_10k"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back to Instagram Menu", callback_data="instagram"
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "❤️ Instagram Likes\n\nSelect a package:", reply_markup=reply_markup
    )

  elif data == "ig_views":
    keyboard = [
        [InlineKeyboardButton("5K Views — 500 ብር", callback_data="ig_v_5k")],
        [InlineKeyboardButton("10K Views — 800 ብር", callback_data="ig_v_10k")],
        [
            InlineKeyboardButton(
                "⬅️ Back to Instagram Menu", callback_data="instagram"
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "👁️ Instagram Views\n\nSelect a package:", reply_markup=reply_markup
    )

  elif data == "tiktok":
    keyboard = [
        [
            InlineKeyboardButton("👤 Followers", callback_data="tt_followers"),
            InlineKeyboardButton("❤️ Likes", callback_data="tt_likes"),
        ],
        [
            InlineKeyboardButton("👁️ Views", callback_data="tt_views"),
            InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back_home"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🎵 TikTok Services\n\nChoose a service:", reply_markup=reply_markup
    )

  elif data == "tt_followers":
    keyboard = [
        [InlineKeyboardButton("1K Followers — 700 ብር", callback_data="tt_f_1k")],
        [InlineKeyboardButton("5K Followers — 2,700 ብር", callback_data="tt_f_5k")],
        [
            InlineKeyboardButton(
                "10K Followers — 5,000 ብር", callback_data="tt_f_10k"
            )
        ],
        [InlineKeyboardButton("⬅️ Back to TikTok Menu", callback_data="tiktok")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "📈 TikTok Followers\n\nSelect a package:", reply_markup=reply_markup
    )

  elif data == "tt_likes":
    keyboard = [
        [InlineKeyboardButton("1K Likes — 300 ብር", callback_data="tt_l_1k")],
        [InlineKeyboardButton("5K Likes — 1,200 ብር", callback_data="tt_l_5k")],
        [
            InlineKeyboardButton(
                "10K Likes — 1,800 ብር", callback_data="tt_l_10k"
            )
        ],
        [InlineKeyboardButton("⬅️ Back to TikTok Menu", callback_data="tiktok")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "❤️ TikTok Likes\n\nSelect a package:", reply_markup=reply_markup
    )

  elif data == "tt_views":
    keyboard = [
        [InlineKeyboardButton("5K Views — 500 ብር", callback_data="tt_v_5k")],
        [InlineKeyboardButton("10K Views — 800 ብር", callback_data="tt_v_10k")],
        [InlineKeyboardButton("⬅️ Back to TikTok Menu", callback_data="tiktok")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "👁️ TikTok Views\n\nSelect a package:", reply_markup=reply_markup
    )

  elif data == "facebook":
    keyboard = [
        [
            InlineKeyboardButton("👤 Followers", callback_data="fb_followers"),
            InlineKeyboardButton("❤️ Likes", callback_data="fb_likes"),
        ],
        [
            InlineKeyboardButton("👁️ Views", callback_data="fb_views"),
            InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back_home"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "📘 Facebook Services\n\nChoose a service:", reply_markup=reply_markup
    )

  elif data == "fb_followers":
    keyboard = [
        [InlineKeyboardButton("1K Followers — 400 ብር", callback_data="fb_f_1k")],
        [InlineKeyboardButton("5K Followers — 1,800 ብር", callback_data="fb_f_5k")],
        [
            InlineKeyboardButton(
                "10K Followers — 3,300 ብር", callback_data="fb_f_10k"
            )
        ],
        [InlineKeyboardButton("⬅️ Back to Facebook Menu", callback_data="facebook")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "📈 Facebook Followers\n\nSelect a package:", reply_markup=reply_markup
    )

  elif data == "fb_likes":
    keyboard = [
        [InlineKeyboardButton("1K Likes — 300 ብር", callback_data="fb_l_1k")],
        [InlineKeyboardButton("5K Likes — 1,200 ብር", callback_data="fb_l_5k")],
        [
            InlineKeyboardButton(
                "10K Likes — 1,800 ብር", callback_data="fb_l_10k"
            )
        ],
        [InlineKeyboardButton("⬅️ Back to Facebook Menu", callback_data="facebook")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "❤️ Facebook Likes\n\nSelect a package:", reply_markup=reply_markup
    )

  elif data == "fb_views":
    keyboard = [
        [InlineKeyboardButton("5K Views — 500 ብር", callback_data="fb_v_5k")],
        [InlineKeyboardButton("10K Views — 800 ብር", callback_data="fb_v_10k")],
        [InlineKeyboardButton("⬅️ Back to Facebook Menu", callback_data="facebook")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "👁️ Facebook Views\n\nSelect a package:", reply_markup=reply_markup
    )

  elif data == "telegram":
    keyboard = [
        [
            InlineKeyboardButton(
                "1K Subscriber — 500 ብር", callback_data="tg_1k"
            )
        ],
        [
            InlineKeyboardButton(
                "5K Subscriber — 2,300 ብር", callback_data="tg_5k"
            )
        ],
        [
            InlineKeyboardButton(
                "10K Subscriber — 3,500 ብር", callback_data="tg_10k"
            )
        ],
        [
            InlineKeyboardButton(
                "20K Subscriber — 6,500 ብር", callback_data="tg_20k"
            )
        ],
        [
            InlineKeyboardButton(
                "50K Subscriber — 15,000 ብር", callback_data="tg_50k"
            )
        ],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back_home")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "✈️ Telegram Services\n\nSelect a package:", reply_markup=reply_markup
    )

  elif (
      data.startswith("ig_")
      or data.startswith("tt_")
      or data.startswith("fb_")
      or data.startswith("tg_")
  ):
    context.user_data["selected_package"] = data
    context.user_data["step"] = "waiting_for_link"

    await query.edit_message_text(
        "📦 Package Selected!\n\n"
        "Please send your profile link, username, or post link in the chat now:"
    )

  elif data == "back_home":
    context.user_data.clear()
    keyboard = [
        [
            InlineKeyboardButton("📸 Instagram", callback_data="instagram"),
            InlineKeyboardButton("🎵 TikTok", callback_data="tiktok"),
        ],
        [
            InlineKeyboardButton("📘 Facebook", callback_data="facebook"),
            InlineKeyboardButton("✈️ Telegram", callback_data="telegram"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🤖 Welcome to Habesha SMM Shop!\n\nChoose a platform:",
        reply_markup=reply_markup,
    )


# --- FORWARD TEXT TRANSACTION TO ADMIN ---
async def handle_text_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
  current_step = context.user_data.get("step")

  if current_step == "waiting_for_link":
    user_link = update.message.text
    context.user_data["user_link"] = user_link
    context.user_data["step"] = "waiting_for_payment"
    selected_pkg = context.user_data.get("selected_package")

    await update.message.reply_text(
        f"🔗 Link Saved: {user_link}\n\n"
        "🏦💵 Payment Method 💵🏦\n"
        "▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️\n"
        "🟣 CBE: 1000452732298 (Emran)\n"
        "▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️\n"
        "🟢 TeleBirr: 0905145557 (Imran)\n"
        "▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️\n"
        "🟡 Abyssinia: 236272486 (Imran)\n"
        "▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️\n\n"
        f"Selected Package: {selected_pkg}\n\n"
        "📲 Please send your transaction reference number OR a screenshot photo of your receipt."
    )

  elif current_step == "waiting_for_payment":
    payment_info = update.message.text
    user = update.effective_user
    selected_pkg = context.user_data.get("selected_package")
    user_link = context.user_data.get("user_link")

    # Send Notification Direct to Your Personal Telegram
    if ADMIN_ID:
      try:
        admin_message = (
            "🚨 NEW ORDER FORWARDED 🚨\n\n"
            f"👤 Customer: {user.full_name} (@{user.username if user.username else 'None'})\n"
            f"🆔 User ID: {user.id}\n"
            f"📦 Package: {selected_pkg}\n"
            f"🔗 Link: {user_link}\n"
            f"🧾 Payment Ref: {payment_info}"
        )
        await context.bot.send_message(chat_id=int(ADMIN_ID), text=admin_message)
      except Exception as e:
        print(f"Failed to forward order to admin: {e}")

    await update.message.reply_text(
        "🎉 Order Submitted Successfully!\n\n"
        f"📦 Package: {selected_pkg}\n"
        f"🔗 Link: {user_link}\n"
        f"🧾 Payment Ref: {payment_info}\n\n"
        "⏳ Your order has been forwarded to support for verification!\n\n"
        "Type /start to make another order."
    )

    context.user_data.clear()

  else:
    await update.message.reply_text(
        "Please use /start to begin or click a package first!"
    )


# --- FORWARD SCREENSHOT TRANSACTION TO ADMIN ---
async def handle_photo_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
  current_step = context.user_data.get("step")

  if current_step == "waiting_for_payment":
    user = update.effective_user
    selected_pkg = context.user_data.get("selected_package")
    user_link = context.user_data.get("user_link")
    photo_file = update.message.photo[-1].file_id

    # Send Photo Direct to Your Personal Telegram
    if ADMIN_ID:
      try:
        admin_caption = (
            "🚨 NEW SCREENSHOT ORDER FORWARDED 🚨\n\n"
            f"👤 Customer: {user.full_name} (@{user.username if user.username else 'None'})\n"
            f"🆔 User ID: {user.id}\n"
            f"📦 Package: {selected_pkg}\n"
            f"🔗 Link: {user_link}"
        )
        await context.bot.send_photo(
            chat_id=int(ADMIN_ID), photo=photo_file, caption=admin_caption
        )
      except Exception as e:
        print(f"Failed to forward photo to admin: {e}")

    await update.message.reply_text(
        "🎉 Screenshot Order Submitted Successfully!\n\n"
        f"📦 Package: {selected_pkg}\n"
        f"🔗 Link: {user_link}\n\n"
        "⏳ Your receipt screenshot has been forwarded to support for verification!\n\n"
        "Type /start to make another order."
    )

    context.user_data.clear()
  else:
    await update.message.reply_text(
        "Please start an order first by pressing /start!"
    )


def main():
  threading.Thread(target=run_dummy_server, daemon=True).start()

  try:
    loop = asyncio.get_event_loop()
  except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

  custom_request = HTTPXRequest(read_timeout=30.0, connect_timeout=30.0)
  app = (
      Application.builder().token(TOKEN).request(custom_request).build()
  )

  app.add_handler(CommandHandler("start", start))
  app.add_handler(CallbackQueryHandler(button_click))
  app.add_handler(
      MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_input)
  )
  app.add_handler(MessageHandler(filters.PHOTO, handle_photo_input))

  print("Habesha SMM Shop bot is running...")
  app.run_polling()


if __name__ == "__main__":
  main()
