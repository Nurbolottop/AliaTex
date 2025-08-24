from django.core.management.base import BaseCommand
from apps.telegram_bot.views import run_bot
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **options):
        logger.info("Starting Telegram bot...")
        try:
            run_bot()
        except KeyboardInterrupt:
            logger.info("Bot stopped by user")
        except Exception as e:
            logger.error(f"Error in bot: {e}")
            raise
