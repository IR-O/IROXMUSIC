from typing import List, Union  # Importing List and Union from typing module
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  # Importing InlineKeyboardButton and InlineKeyboardMarkup from pyrogram.types module


def button(text: str, callback_data: str) -> InlineKeyboardButton:
    # This function creates an InlineKeyboardButton object with the given text and callback_data
    # Parameters:
    #   text (str): The text to be displayed on the button
    #   callback_data (str): The data to be sent back to the bot when the button is pressed
    # Returns:
    #   InlineKeyboardButton: A button object with the given text and callback_data


def keyboard_markup(buttons: List[List[Union[InlineKeyboardButton, str]]]) -> InlineKeyboardMarkup:
    # This function creates an InlineKeyboardMarkup object with the given list of buttons
    # Parameters:
    #   buttons (List[List[Union[InlineKeyboardButton, str]]]): A list of lists containing InlineKeyboardButton objects or strings (representing text for rows)
    # Returns:
    #   InlineKeyboardMarkup: A markup object with the given buttons


def stats_buttons(_, status):
    # This function creates a list of buttons for the stats command
    # Parameters:
    #   _ (dict): A dictionary containing bot settings
    #   status (bool): A boolean indicating whether the user is a sudo user or not
    # Returns:
    #   InlineKeyboardMarkup: A markup object containing the buttons

    not_sudo = [button(_["SA_B_1"], "TopOverall")] if _["SA_B_1"] else []  # If SA_B_1 is present in the dictionary, create a button with its value and "TopOverall" as callback_data
    sudo = [button(_["SA_B_2"], "bot_stats_sudo"), button(_["SA_B_3"], "TopOverall")] if _["SA_B_2"] and _["SA_B_3"] else []  # If both
