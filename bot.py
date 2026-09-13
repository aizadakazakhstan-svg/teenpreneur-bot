"""
TeenPreneur Navigator — Telegram-бот (единый файл).
Практическая часть проекта «Teen Preneurs: Monetizing Hobbies vs.
Consumer Trap in Social Networks».

Всё в одном файле специально для удобного деплоя (например, с телефона
через GitHub + Railway) — не нужно создавать отдельные файлы/папки.
"""

import logging
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
