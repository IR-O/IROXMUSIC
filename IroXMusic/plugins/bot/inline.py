from pyrogram.types import (    # Importing necessary modules from pyrogram library
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from youtubesearchpython.__future__ import VideosSearch  # Importing VideosSearch from youtubesearchpython package

# Importing app instance from IroXMusic package
from IroXMusic import app

# Importing answer function from inlinequery.py
from IroXMusic.utils.inlinequery import answer

# Importing BANNED_USERS from config.py
from config import BANNED_USERS

# Decorator to handle inline queries from users not in BANNED_USERS list
@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):  # Defining the inline query handler function
    text = query.query.strip().lower()  # Stripping and converting query text to lowercase
    answers = []  # Initializing an empty list to store the answers

    # If the query is empty
    if text.strip() == "":
        try:
            # Answer the inline query with the cached answer
            await client.answer_inline_query(query.id, results=answer, cache_time=10)
        except:
            return  # If any exception occurs, return from the function
    else:
        # Search for videos using VideosSearch with the query text and limit of 20
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")  # Get the search result

        # Loop through the first 15 results
        for x in range(15):
            # Get the title of the video and convert it to title case
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]  # Get the duration of the video
            views = result[x]["viewCount"]["short"]  # Get the short view count of the video
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[0]  # Get the thumbnail URL of the video
            channellink = result[x]["channel"]["link"]  # Get the channel link of the video
            channel = result[x]["channel"]["name"]  # Get the channel name of the video
            link = result[x]["link"]  # Get the video link
            published = result[x]["publishedTime"]  # Get the published time of the video

            # Construct the description string
            description = f"{views} | {duration} ᴍɪɴᴜᴛᴇs | {channel}  | {published}"

            # Construct the InlineKeyboardMarkup for the InlineQueryResultPhoto
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʏᴏᴜᴛᴜʙᴇ 🎄",
                            url=link,
                        )
                    ],
                ]
            )

            # Construct the searched_text string
            searched_text = f"""
❄ <b>ᴛɪᴛʟᴇ :</b> <a href={link}>{title}</a>

⏳ <b>ᴅᴜʀᴀᴛɪᴏɴ :</b> {duration} ᴍɪɴᴜᴛᴇs
👀 <b>ᴠɪᴇᴡs :</b> <code>{views}</code>
🎥 <b>ᴄʜᴀɴɴᴇʟ :</b> <a href={channellink}>{channel}</a>
⏰ <b>ᴘᴜʙʟɪsʜᴇᴅ ᴏɴ :</b> {published}

<u>"""

            # Append the InlineQueryResultPhoto to the answers list
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    thumb_url=thumbnail,
                    title=title,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )

        # Answer the inline query with the answers list
        await client.answer_inline_query(query.id, results=answers, cache_time=10)
