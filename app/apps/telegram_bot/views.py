"""Telegram bot with basic commands and notification functionality."""

import os
import logging
from telebot import TeleBot, types

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize bot with token and settings from environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
REVIEWS_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Parse thread IDs
try:
    FEEDBACK_THREAD_ID = int(os.getenv('TELEGRAM_FEEDBACK_THREAD_ID', '0')) or None
    BOOKING_THREAD_ID = int(os.getenv('BOOKING_THREAD_ID', '0')) or None
except (TypeError, ValueError) as e:
    logger.warning(f"Error parsing thread IDs: {e}. Will send to main chat")
    FEEDBACK_THREAD_ID = None
    BOOKING_THREAD_ID = None

if not TELEGRAM_TOKEN:
    logger.error("TELEGRAM_BOT_TOKEN environment variable is not set!")
    exit(1)

bot = TeleBot(TELEGRAM_TOKEN)

def _safe_send_message(chat_id: int, text: str, thread_id: int = None) -> None:
    """Safely send a message to a chat or a specific thread/topic.
    
    Args:
        chat_id: ID of the chat to send the message to
        text: Message text to send
        thread_id: Optional thread/topic ID within the chat
    """
    try:
        kwargs = {}
        if thread_id is not None:
            kwargs['message_thread_id'] = thread_id
        bot.send_message(chat_id, text, **kwargs)
    except Exception as e:
        logger.error(f"Failed to send message: {e}")

def send_contact_request_notification(name: str, contact: str) -> None:
    """Send notification about new contact request to the booking thread."""
    if not REVIEWS_CHAT_ID:
        logger.warning("REVIEWS_CHAT_ID is not set, skipping notification")
        return
        
    text = (
        "📩 Новая заявка на консультацию\n"
        f"Имя: {name}\n"
        f"Контакт: {contact}"
    )
    _safe_send_message(int(REVIEWS_CHAT_ID), text, thread_id=BOOKING_THREAD_ID)


def send_review_notification(name: str, review_text: str) -> None:
    """Send notification about new review to the feedback thread."""
    if not REVIEWS_CHAT_ID:
        logger.warning("REVIEWS_CHAT_ID is not set, skipping notification")
        return
        
    text = (
        "📝 Новый отзыв\n"
        f"Имя: {name}\n"
        f"Отзыв: {review_text}"
    )
    _safe_send_message(int(REVIEWS_CHAT_ID), text, thread_id=FEEDBACK_THREAD_ID)

@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message) -> None:
    """Send a welcome message when the command /start is issued."""
    welcome_text = (
        "👋 Привет! Добро пожаловать в бот!\n"
        "Я простой бот, который умеет отвечать на команду /start\n"
        "Попробуйте отправить мне /start"
    )
    bot.reply_to(message, welcome_text)

def run_bot() -> None:
    """Start the bot."""
    logger.info("Starting Telegram bot...")
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        logger.error(f"Error in bot: {e}")
        # Try to restart the bot after an error
        run_bot()

if __name__ == "__main__":
    run_bot()