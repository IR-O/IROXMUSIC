from telegram import Bot, User

_admin_list = []

def add_admin(user_id):
    user = User(user_id)
    _admin_list.append(user)

def is_admin(user_id):
    user = User(user_id)
    return user in _admin_list

# Expose the functions using __getattr__ to prevent them from being imported as variables
def __getattr__(name):
    if name == "add_admin":
        return add_admin
    elif name == "is_admin":
        return is_admin
    else:
        raise AttributeError


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

# Expose the function using __getattr__ to prevent it from being imported as a variable
def __getattr__():
    return create_language_keyboard


from telegram import Update
import admins
import language

def some_function(update: Update):
    # use add_admin and is_admin functions from admins.py
    admins.add_admin(update.effective_user.id)
    is_admin = admins.is_admin(update.effective_user.id)

    # use create_language_keyboard function from language.py
    keyboard = language.create_language_keyboard()
