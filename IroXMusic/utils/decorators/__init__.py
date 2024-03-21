# admins.py and language.py should be in the same directory as this file

# admins.py
from telegram import Bot, User

admin_list = []

def add_admin(user_id):
    user = User(user_id)
    admin_list.append(user)

def is_admin(user_id):
    user = User(user_id)
    return user in admin_list

__all__ = ['add_admin', 'is_admin']


# language.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def create_language_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("English", callback_data="en"),
            InlineKeyboardButton("Español", callback_data="es"),
        ],
        [
            InlineKeyboardButton("Français", callback_data="fr"),
            InlineKeyboardButton("Deutsch", callback_data="de"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

__all__ = ['create_language_keyboard']


# main.py
from telegram import Update
from .admins import *
from .language import *

def some_function(update: Update):
    # use add_admin and is_admin functions from admins.py
    # use create_language_keyboard function from language.py
