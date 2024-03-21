from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def speed_markup(chat_id, _):
    """
    Generates an InlineKeyboardMarkup object for speed controls.

    :param chat_id: The ID of the chat.
    :param _: The translation dictionary.
    :return: An InlineKeyboardMarkup object.
    """
    button_data_template = "SpeedUP {}"
    buttons = [
        [
            InlineKeyboardButton(
                text="🕒 0.5x",
                callback_data=button_data_template.format(button_data_template.format(chat_id, "0.5")),
            ),
            InlineKeyboardButton(
                text="🕓 0.75x",
                callback_data=button_data_template.format(button_data_template.format(chat_id, "0.75")),
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_4"],
                callback_data=button_data_template.format(button_data_template.format(chat_id, "1.0")),
            ),
        ],
        [
            InlineKeyboardButton(
                text="🕤 1.5x",
                callback_data=button_data_template.format(button_data_template.format(chat_id, "1.5")),
            ),
            InlineKeyboardButton(
                text="🕛 2.0x",
                callback_data=button_data_template.format(button_data_template.format(chat_id, "2.0")),
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
    ]
    return InlineKeyboardMarkup(buttons)
