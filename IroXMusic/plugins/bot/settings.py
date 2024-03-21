# This function handles the /settings and /setting command in a group chat
# It shows the settings menu for the group chat
def handle_settings_command(update, context):
    chat_id = update.effective_chat.id
    settings_keyboard = [
        [
            InlineKeyboardButton("Setting 1", callback_data="setting_1"),
            InlineKeyboardButton("Setting 2", callback_data="setting_2"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="back"),
        ],
    ]
    update.effective_message.reply_text("Settings Menu:", reply_markup=InlineKeyboardMarkup(settings_keyboard))

