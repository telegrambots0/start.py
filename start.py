import pymongo
from .. import bot as gagan
from telethon import events, Button
from pyrogram import Client, filters
import re
import pymongo
import sys
import math
import os
import time
from datetime import datetime as dt, timedelta
import json
import asyncio
import cv2
from yt_dlp import YoutubeDL
from telethon.sync import TelegramClient
from .. import Bot as app
from telethon.tl.types import InputMediaPhoto

S = "/start"
START_PIC = "https://graph.org/file/c9669066860d912fd5035.jpg"
TEXT = "Send me the Link of any message of Restricted Channels to Clone it here.\nFor private channel's messages, send the Invite Link first.\n\n👉🏻Execute /batch for bulk process upto 10K files range.\n 👉🏻To Get Available Commands In The Bot Press /help."

def is_set_button(data):
    return data == "set"

def is_rem_button(data):
    return data == "rem"

@gagan.on(events.CallbackQuery(pattern=b"set"))
async def sett(event):    
    gagan = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with gagan.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
            return
        mime = x.file.mime_type
        if 'png' not in mime and 'jpg' not in mime and 'jpeg' not in mime:
            return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")

@gagan.on(events.CallbackQuery(pattern=b"rem"))
async def remt(event):  
    gagan = event.client            
    await event.edit('Trying... to save Bamby ... Wait')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        

@gagan.on(events.NewMessage(pattern=f"^{S}"))
async def start_command(event):
    # Creating inline keyboard with buttons
    buttons = [
        [Button.url("Join Channel", url="https://t.me/SmexyStore")],
        [Button.url("Contact Me", url="https://t.me/SmexyOP")],
        [Button.inline("SET THUMB", data="set"),
         Button.inline("REM THUMB", data="rem")]
    ]

    # Sending photo with caption and buttons
    await gagan.send_file(
        event.chat_id,
        file=START_PIC,
        caption=TEXT,
        buttons=buttons
    )

@gagan.on(events.NewMessage(pattern='/remthumb'))
async def remove_thumbnail(event):
    user_id = event.sender_id
    gagan_client = event.client
    try:
        os.remove(f'{user_id}.jpg')
        await event.respond('Thumbnail removed successfully!')
    except FileNotFoundError:
        await event.respond("No thumbnail found to remove.")


# Function to get video info including duration
def get_youtube_video_info(url):
    ydl_opts = {'quiet': True, 'skip_download': True}
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        if not info_dict:
            return None
        return {
            'title': info_dict.get('title', 'Unknown Title'),
            'duration': info_dict.get('duration', 0),  # Duration in seconds
        }

@app.on_message(filters.command("dl", prefixes="/"))
async def youtube_dl_command(_, message):
    # Check if the command has an argument (YouTube URL)
    if len(message.command) > 1:
        youtube_url = message.command[1]
        
        # Send initial message indicating downloading
        progress_message = await message.reply("Fetching video info...")

        try:
            # Fetch video info using yt-dlp
            video_info = get_youtube_video_info(youtube_url)
            if not video_info:
                await progress_message.edit_text("Failed to fetch video info.")
                return

            # Check if video duration is greater than 3 hours (10800 seconds)
            if video_info['duration'] > 10800:
                await progress_message.edit_text("Video duration exceeds 3 hours. Not allowed.")
                return
            
            await progress_message.edit_text("Downloading video...")

            # Safe file naming
            original_file = f"{video_info['title'].replace('/', '_').replace(':', '_')}.mp4"
            thumbnail_path = f"{video_info['title'].replace('/', '_').replace(':', '_')}.jpg"

            # Download video
            ydl_opts = {
                'format': 'best',
                'outtmpl': original_file,  # Output file template
                'noplaylist': True,  # Disable downloading playlists
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([youtube_url])  # Start downloading the video

            # Check if the original file exists before renaming
            if not os.path.exists(original_file):
                await progress_message.edit_text("Failed to download video.")
                return

            # Edit the progress message to indicate uploading
            await progress_message.edit_text("Uploading video...")

            # Get video metadata
            metadata = video_metadata(original_file)
            caption = f"{video_info['title']}\n\n__**Powered By [𝙎𝙢𝙚𝙭𝙮 ᥫ᭡](https://t.me/SmexyOP)**__"  # Set caption to the title of the video
            
            # Send the video file and thumbnail
            ggn = message.chat.id
            k = thumbnail(ggn)
            await app.send_video(
                chat_id=message.chat.id,
                video=original_file,
                caption=caption,
                thumb=k,
                width=metadata['width'],
                height=metadata['height'],
                duration=metadata['duration'],
            )

            # Clean up downloaded files
            os.remove(original_file)
            # os.remove(thumbnail_path)

            # Delete the progress message after sending video
            await progress_message.delete()

        except Exception as e:
            await progress_message.edit_text(f"An error occurred: {str(e)}")

    else:
        await message.reply("Please provide a YouTube URL after /dl.")


def video_metadata(file):
    vcap = cv2.VideoCapture(f'{file}')
    width = round(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = round(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = vcap.get(cv2.CAP_PROP_FPS)
    frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = round(frame_count / fps)
    return {'width': width, 'height': height, 'duration': duration}

REPO_URL = "https://t.me/SmexyOP"

HELP_TEXT = """Here are the available commands:

➡️ /batch - To process multiple links at once by taking start link, iterating though multple message ids.

➡️ /setchat - Forward messages directly to a groupID, channelID (with -100), or user (they must have started the bot) bot must be admin in channel or group. 

```Use: /setchat channelD```

No need to add -100 in the userid.

➡️ /remthumb - Delete your thumbnail.

Note: To set your custom thumbnail just sent without anycommand or else.

➡️ /cancel - Cancel ongoing batch process.

➡️ /dl - Download videos directly from Youtube, Linkedin, Xvideos, Xnxx, Pinterest, Internet Archive, Amazon Mini Tv.

➡️ /ivalid - try this command if you get peer id invalid error...

➡️ /Speedtest - To Check Speedtest Status (can be executed by owner only).

➡️ /stats - To Viewing The Statics Of The Bot

➡️ /logs - To get the logs directly on telegram (now upto 2 min you can increase it accordingly)

[DM TO Buy Repository](%s)
""" % REPO_URL


@gagan.on(events.NewMessage(pattern='/help'))
async def help_command(event):
    """
    Command to display help message
    """
    # Creating inline keyboard with a button linking to the GitHub repository
    buttons = [[Button.url("DM To Buy REPO", url=REPO_URL)]]

    # Sending the help message with the GitHub repository button
    await event.respond(HELP_TEXT, buttons=buttons, link_preview=False)
