"""Telegram bot views – minimal version with only /start command."""

from __future__ import annotations

import logging
import re
import time
import os
from telebot import TeleBot, types
from django.conf import settings as django_settings
from apps.contacts import models as contacts_models
from apps.contacts.models import Testimonial

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