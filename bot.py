import telebot
from logic import calculate_score, get_insight, get_tips
from database import save_user
from scheduler import start_scheduler

TOKEN = "8621597556:AAFVUHz87CmKp91qgyxwCC1ufOCLlujE8es"
bot = telebot.TeleBot(TOKEN)

user_state = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "👋 Welcome to HealthTwin AI\n\nLet's check your health.\n\n🛌 Sleep hours?")
    user_state[message.chat.id] = {}

@bot.message_handler(func=lambda m: True)
def handle(message):
    chat_id = message.chat.id
    text = message.text

    data = user_state.get(chat_id, {})

    try:
        if "sleep" not in data:
            data["sleep"] = float(text)
            bot.send_message(chat_id, "💧 Water (liters)?")

        elif "water" not in data:
            data["water"] = float(text)
            bot.send_message(chat_id, "🚶 Steps?")

        elif "steps" not in data:
            data["steps"] = int(text)
            bot.send_message(chat_id, "🙂 Mood (1-5)?")

        elif "mood" not in data:
            data["mood"] = int(text)

            score = calculate_score(data)
            insight = get_insight(data)
            tips = get_tips(data)

            save_user(chat_id, data, score)

            bot.send_message(chat_id, f"""
📊 Health Score: {score}/100

💡 Insight:
{insight}

🎯 Actions:
{chr(10).join(tips)}
""")

            user_state[chat_id] = {}

        user_state[chat_id] = data

    except:
        bot.send_message(chat_id, "⚠️ Please enter valid number.")

start_scheduler(bot)

bot.polling()