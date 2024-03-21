from pyrogram.enums import ParseMode
from pyrogram.errors import ChatAdminRequired, UserIsBlocked

from IroXMusic import app, LOGGER_ID, USERNAME
from IroXMusic.utils.database import is_on_off
from IroXMusic.utils.decorators import errors


@errors
async def play\_logs(message, streamtype):
if not await is\_on\_off(2):
return

try:
logger\_text = f"""
<b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>

<b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>
<b>ᴄʜᴀᴛ ɴᴀᴍᴇ :</b> {message.chat.title}
<b>ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.chat.username}

<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from\_user.id}</code>
<b>ɴᴀᴍᴇ :</b> {message.from\_user.mention}
<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from\_user.username}

<b>ǫᴜᴇʀʏ :</b> {message.text.split(None, 1)[1]}
<b>sᴛʀᴇᴀᴍᴛʏᴘᴇ :</b> {streamtype}"""
if message.chat.id != LOGGER\_ID:
await app.send\_message(
chat\_id=LOGGER\_ID,
text=logger\_text,
parse\_mode=ParseMode.HTML,
disable\_web\_page\_preview=True,
)
except ChatAdminRequired:
await message.reply\_text(
"⚠️ **I'm not a admin in this chat, please add me as an admin to send logs.**",
parse\_mode=ParseMode.MARKDOWN
)
except UserIsBlocked:
await message.
