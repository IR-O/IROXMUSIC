# Import necessary modules
# pyrogram: A Python library for the Telegram API
# filters, Message, InlineKeyboardMarkup: Classes from pyrogram for handling messages and inline keyboards
# BANNED_USERS: A list of banned users from the config file
# IroXMusic.core.call: A module for handling calls
# db: A database object
# AdminRightsCheck: A decorator for checking if the user is an admin
# close_markup: A function for creating a close button for inline keyboards
# auto_clean: A function for automatically cleaning up files
# get_thumb: A function for getting thumbnails

# Define the skip function
@app.on_message(filters.command(["skip", "cskip", "next", "cnext"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def skip(cli, message: Message, _, chat_id):
    # Check if the user provided an argument with the command
    if len(message.command) < 2:
        # Get the current queue for the chat from the database
        check = db.get(chat_id)
        # If the queue is empty, return an error message
        if not check:
            return await message.reply_text(_["queue_2"])
        # Skip the next song in the queue
        popped = check.pop(0)
        # Delete the song from the database
        if popped:
            await auto_clean(popped)
        # If the queue is empty after skipping the song, stop the stream and delete the corresponding stream data from the database
        if not check:
            try:
                await message.reply_text(
                    text=_["admin_6"].format(
                        message.from_user.mention, message.chat.title,
                    ),
                    reply_markup=close_markup(_),
                )
                await Irop.stop_stream(chat_id)
            except:
                return
    else:
        # Get the user-provided argument
        state = message.text.split(None, 1)[1].strip()
        # Check if the argument is a valid number
        if state.isnumeric():
            state = int(state)
            # Check if the loop status for the chat is not 0
            loop = await get_loop(chat_id)
            if loop != 0:
                return await message.reply_text(_["admin_8"])
            # Check if the number of songs to skip is within the range of the queue length
            count = len(check)
            if count > 2:
                count = int(count - 1)
                if 1 <= state <= count:
                    # Remove that many number of songs from the queue and delete them from the database
                    for x in range(state):
                        try:
                            popped = check.pop(0)
                        except:
                            return await message.reply_text(_["admin_12"])
                        if popped:
                            await auto_clean(popped)
                        if not check:
                            try:
                                await message.reply_text(
                                    text=_["admin_6"].format(
                                        message.from_user.mention,
                                        message.chat.title,
                                    ),
                                    reply_markup=close_markup(_),
                                )
                                await Irop.stop_stream(chat_id)
                            except:
                                return
                            break
                else:
                    return await message.reply_text(_["admin_11"].format(count))
            else:
                return await message.reply_text(_["admin_10"])
        else:
            return await message.reply_text(_["admin_9"])

    # Get the details of the next song in the queue
    queued = check[0]["file"]
    title = (check[0]["title"]).title()
    user = check[0]["by"]
    streamtype = check[0]["streamtype"]
    videoid = check[0]["vidid"]
    status = True if str(streamtype) == "video" else None

    # Update the played count for the current song in the queue
    db[chat_id][0]["played"] = 0

    # If the song has a previously recorded duration, update the duration and seconds values in the database
    exis = (check[0]).get("old_dur")
    if exis:
        db[chat_id][0]["dur"] = exis
        db[chat_id][0]["seconds"] =
