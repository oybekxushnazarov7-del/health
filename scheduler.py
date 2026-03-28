import schedule
import time
from database import get_all_users

def job(bot):
    users = get_all_users()
    for user in users:
        chat_id = user[0]
        try:
            bot.send_message(chat_id, "⏰ Don't forget to log your health today! Type /start")
        except:
            pass


def start_scheduler(bot):
    schedule.every().day.at("09:00").do(job, bot)

    def run():
        while True:
            schedule.run_pending()
            time.sleep(1)

    import threading
    threading.Thread(target=run).start()