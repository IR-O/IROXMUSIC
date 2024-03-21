import textwrap
from markdown import Markdown

HELP_TEXT = """
# Admin commands

Just add `c` in the start of the commands to use them for channel.

/pause : Pause the current playing stream.
/resume : Resume the paused stream.
/skip : Skip the current playing stream and start streaming the next track in queue.
/end or /stop : Clear the queue and end the current playing stream.
/player : Get an interactive player panel.
/queue : Show the queued tracks list.

# Auth users

Auth users can use admin rights in the bot without admin rights in the chat.

/auth [USERNAME/USER_ID] : Add a user to the auth list of the bot.
/unauth [USERNAME/USER_ID] : Remove an auth user from the auth users list.
/authusers : Show the list of auth users of the group.

# Broadcast feature [ONLY FOR SUDOERS]

/broadcast [MESSAGE OR REPLY TO A MESSAGE] : Broadcast a message to served chats of the bot.

Broadcasting modes:
-pin : Pins your broadcasted messages in served chats.
-pinloud : Pins your broadcasted message in served chats and sends notification to the members.
-user : Broadcasts the message to the users who have started your bot.
-assistant : Broadcasts your message from the assistant account of the bot.
-nobot : Forces the bot not to broadcast the message..

Example: `/broadcast -user -assistant -pin Testing broadcast`

# Chat blacklist feature [ONLY FOR SUDOERS]

Restrict chats to use our bot.

/blacklistchat [CHAT ID] : Blacklist a chat from using the bot.
/whitelistchat [CHAT ID] : Whitelist the blacklisted chat.
/blacklistedchat : Show the list of blacklisted chats.

# Block users:

Starts ignoring the blocked users, so that he can't use bot commands.

/block [USERNAME OR REPLY TO A USER] : Block the user from our bot.
/unblock [USERNAME OR REPLY TO A USER] : Unblocks the blocked user.
/blockedusers : Show the list of blocked users.

# Channel play commands

You can stream audio/video in channel.

/cplay : Starts streaming the requested audio track on channel's videochat.
/cvplay : Starts streaming the requested video track on channel's videochat.
/cplayforce or /cvplayforce : Stops the ongoing stream and starts streaming the requested track.

/channelplay [CHAT USERNAME OR ID] OR [DISABLE] : Connect channel to a group and starts streaming tracks by the help of commands sent in group.

# Global ban feature [ONLY FOR SUDOERS]

/gban [USERNAME OR REPLY TO A USER] : Globally bans the user from all the served chats and blacklists him from using the bot.
/ungban [USERNAME OR REPLY TO A USER] : Globally unbans the globally banned user.
/gbannedusers : Show the list of globally banned users.

# Loop stream :

Starts streaming the ongoing stream in loop

/loop [enable/disable] : Enables/disables loop for the ongoing stream
/loop [1, 2, 3, ...] : Enables the loop for the given value.

# Maintenance mode [ONLY FOR SUDOERS]

/logs : Get logs of the bot.

/logger [ENABLE/DISABLE] : Bot will start logging the activities happening on bot.

/maintenance [ENABLE/DISABLE] : Enable or disable the maintenance mode of your bot.

# Ping & stats :

/start : Starts the music bot.
/help : Get help menu with explanation of commands.

/ping : Shows the ping and system stats of the bot.

/stats : Shows the overall stats of the bot.

# Play commands :

v : stands for video play.
force : stands for force play.

/play or /vplay : Starts streaming the requested track on videochat.

/playforce or /vplayforce : Stops the ongoing stream and starts streaming the requested track.

# Shuffle queue :

/shuffle : Shuffles the queue.
/queue : Shows the shuffled queue.

# Seek stream :

/seek [DURATION IN SECONDS] : Seeks the stream to the given duration.
/seekback [DURATION IN SECONDS] : Backward seeks the stream to the given duration.

# Song download

/song [SONG NAME/YT URL] : Download any track from youtube in mp3 or mp4 formats.

# Speed commands [ADMINS ONLY]

You can control the playback speed of the ongoing stream.

/speed or /playback : For adjusting the audio playback speed in group.
/cspeed or /cplayback : For adjusting the audio playback speed in channel.
"""

md = Markdown()
help_message = md.convert(HELP_TEXT)
