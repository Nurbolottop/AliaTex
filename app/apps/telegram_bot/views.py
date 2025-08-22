"""Telegram bot views – minimal version with only /start command."""

from __future__ import annotations

import logging
import re
import time
import os
from telebot import TeleBot, types
from django.conf import settings as django_settings

logger = logging.getLogger(__name__)

# Telegram bot initialisation
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = TeleBot(TELEGRAM_TOKEN)

# Chat/thread identifiers for testimonial moderation
REVIEWS_CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID", "0"))  # Group or channel where reviews are moderated
REVIEWS_THREAD_ID = os.getenv("TELEGRAM_REVIEWS_THREAD_ID")
REVIEWS_THREAD_ID = int(REVIEWS_THREAD_ID) if REVIEWS_THREAD_ID else None


@bot.message_handler(commands=["start"])
def start(message: types.Message) -> None:
    """Handle the /start command – send greeting."""
    bot.send_message(
        message.chat.id,
        "👋 Привет! Это официальный бот проекта. Пишите /start, чтобы начать!",
    )


def _safe_send_message(text: str) -> None:
    """Send a message to configured chat/thread, safely logging errors.

    Requires env vars: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID (and optional TELEGRAM_REVIEWS_THREAD_ID).
    If not configured, the function will log a warning and return silently.
    """
    if not TELEGRAM_TOKEN or not REVIEWS_CHAT_ID:
        logger.warning("Telegram is not configured (missing token or chat id). Message not sent.")
        return
    try:
        kwargs = {}
        if REVIEWS_THREAD_ID:
            kwargs["message_thread_id"] = REVIEWS_THREAD_ID
        bot.send_message(REVIEWS_CHAT_ID, text, **kwargs)
    except Exception as exc:  # pylint: disable=broad-except
        logger.error("Failed to send Telegram message: %s", exc)


def send_contact_request_notification(name: str, contact: str) -> None:
    """Notify about a new contact request from the site."""
    text = (
        "📩 Новая заявка на консультацию\n"
        f"Имя: {name}\n"
        f"Контакт: {contact}"
    )
    _safe_send_message(text)


def send_review_notification(name: str, review_text: str) -> None:
    """Notify about a new review submitted on the site."""
    text = (
        "📝 Новый отзыв\n"
        f"Имя: {name}\n"
        f"Отзыв: {review_text}"
    )
    _safe_send_message(text)


def run_polling() -> None:
    """Run the bot with basic restart logic."""
    while True:
        try:
            logger.info("Telegram bot polling started …")
            bot.polling(none_stop=True, interval=3)
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Bot crashed with error: %s", exc)
            time.sleep(15)
            try:
                bot.stop_polling()
            except Exception as stop_exc:  # pylint: disable=broad-except
                logger.error("Error while stopping bot: %s", stop_exc)


if __name__ == "__main__":
    run_polling()