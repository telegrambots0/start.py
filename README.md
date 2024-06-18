<h1 align="center">
  <b>Save restricted Content Bot By <a href="https://t.me/SmexyOP"> 𝙎𝙢𝙚𝙭𝙮 ᥫ᭡ </a>
</h1> 

<img src="https://graph.org/file/c9669066860d912fd5035.jpg" alt="StringGen">

Contact: [Telegram](https://t.me/SmexyOP)

## A stable telegram bot to get restricted messages with custom thumbnail support , made by [𝙎𝙈𝙀𝙓𝙔 𝙎𝙏𝙊𝙍𝙀 🇮🇳](https://t.me/SmexyStore) This bot can run in channels directly (in this case custom thumbnail not supported)

- works for both public and private chats
- Custom thumbnail support for Pvt medias
- supports text and webpage media messages
- Faster speed
- Force subscribe available
- To save from bots send link in this format : `t.me/b/bot_username/message_id` (use plus messenger for message_id)
- `/batch` - (For owner only) Use this command to save upto 10000 files from a pvt or public restricted channel at once.
- `/cancel` -  Use this to stop batch
- Time delay is added to avoid FloodWait and keep user account safe.
- `/setchat` directly upload in channel or group
  
## 🗒️ ɴᴇᴄᴇssᴀʀʏ ᴠᴀʀs

☞ `API_ID` - Get your API_ID from [my.telegram.org](https://my.telegram.org/apps)<br>
☞ `API_HASH` - Get your API_HASH from [my.telegram.org](https://my.telegram.org/apps)<br>
☞ `BOT_TOKEN` - Get your BOT_TOKEN from [@BotFather](https://t.me/BotFather)<br>
☞ `SESSION` - Get SESSION from [sᴛʀɪɴɢ ʙᴏᴛ 🍑](https://telegram.me/SmexyStringSessionBot)<br>
☞ `AUTH` - Owner user id
☞ `FORCESUB` - Public channel username without '@'. Don't forget to add bot in channel as administrator. 

# Get API & PYROGRAM:
 
API: [Telegram.org](https://my.telegram.org/auth)

PYROGRAM SESSION: Search for it ... Make sure the source be trusted otherwise it will lead to accound delete or ban

#How to get vars - [𝙎𝙈𝙀𝙓𝙔 𝙎𝙏𝙊𝙍𝙀 🇮🇳](https://t.me/SmexyStore)

BOT TOKEN: @Botfather on telegram

AUTH: Go to @missrose_bot, start and send /info to get your id

FORCESUB: Before starting building bots create a public channel and get the username withou '@'

# Deploying Guide - [𝙎𝙈𝙀𝙓𝙔 𝙎𝙏𝙊𝙍𝙀 🇮🇳](https://t.me/SmexyStore)

Deploy on `VPS`

Easy Method:

- Go to main then edit ```__init__.py``` as below
- Place '#' befpre every config and after '=' write your vars in single inverted comma. see example below

```
# variables
API_ID = "1234567" #config("API_ID", default=None, cast=int)
API_HASH = "1167433546577f90e4519b65634b7" #config("API_HASH", default=None)
BOT_TOKEN = "7173773796:AAEYdIdgUg1_SYR7wSaMpgY0" #config("BOT_TOKEN", default=None)
SESSION = "BQHDMOUAIOGZHesmwkhKztZ1bU7NokB1HVLtNKHAnr35ElBp-FQ7IPkvayF0s5JoOGLN44ksi4kqeUNxnG56Vd8Mh_2Lo3ICHSN2J2u0WyYIOj96FBxN2gq_iekABQkL-vdXTB1DrOswqzBJBG9RaGPFVoiEYDAd0iD2vqgT3x2wOz98gBZNKPCGpWQYbGR6GKe66W5SRZRlLWJaEDQcTEIxNF48nIEGW7cwK2AG3eR4-iyVg5Zxaje_ACeNuCN5kLtQsNkGEV23f7-EdLQTG1zKnZ57AjUvYQdJ7o1pdGhkKknUUmOcfG4xn42RbHUwccqD1CmsGLU5Zh-vTbgBGh9AiP79HAAAAAGlHSMFAA" #config("SESSION", default=None)
FORCESUB = "channel username without @" #config("FORCESUB", default=None)
AUTH = "1234567" #config("AUTH", default=None)

```
- Now run following commands one by one...

```
sudo apt update
sudo apt install ffmpeg git python3-pip
git clone your_repo_link
cd saverestrictedcontentbot 
pip3 install -r requirements.txt
python3 -m main
```

- if you want bot to be running in background then enter `screen -S gagan` before `python3 -m main` 
- after `python3 -m main`, click ctrl+A, ctrl+D
- if you want to stop bot, then enter `screen -r gagan` and to kill screen enter `screen -S gagan -X quit`.


Deploy your bot on `heroku`

» Method - 1:
- Star the repo, and fork it in desktop mode
- Go to settings of your forked repo
- Rename your repo by any other name
- Click on  [![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/telegrambots0/Save-Restricted-Content-Bot-Repo-)
 
» Method - 2:
- Star the repo, and fork it in desktop mode
- create app in heroku
- go to settings of ```app›› config vars››``` add all variables
- add buildpacks
- connect to github and deploy
- turn on dynos

# Editing Repo - [𝙎𝙈𝙀𝙓𝙔 𝙎𝙏𝙊𝙍𝙀 🇮🇳](https://t.me/SmexyStore)

You can freely edit repo the customisation you can do is -
- Change command pattern like /batch to other name (edit this in ```main/plugins/batch.py```)
- Adding Custom Text in caption (edit this in ```main/plugins/pyroplug.py```) search for 
```
caption = f"{msg.caption}\n\n__Unrestricted by **[𝙎𝙈𝙀𝙓𝙔 𝙎𝙏𝙊𝙍𝙀 🇮🇳](https://t.me/SmexyStore)**__" if msg.caption else "__Unrestricted by **[𝙎𝙈𝙀𝙓𝙔 𝙎𝙏𝙊𝙍𝙀 🇮🇳](https://t.me/SmexyStore)**__"
``` 
change accordingly within ```f""```

- Change Start pic and text (edit this in ```main/plugins/start.py```) search for ```TEXT=```, ```START_PIC=``` and then edit those after ```=```
- Change Default thumbnail in main directory there is file named ```thumb.jpg``` remove that and upload your custom ```thumb.jpg```
- Change cancel command (edit this also in ```batch.py```) search for ```/cancel``` and then change the command accordingly

# Commands Available in Bot - [𝙎𝙈𝙀𝙓𝙔 𝙎𝙏𝙊𝙍𝙀 🇮🇳](https://t.me/SmexyStore)

- ```/start``` - to start the bot
- ```/batch``` - to download the files in range/bulk by giving one post link and range value
- ```/cancel``` - to cancel the onging /batch task
- ```/stats``` - to viewing the statics of bot
- ```/speedtest``` - can be executed by owner only
- ```/setchat``` - Set forwarding to a channel/group via channel/group ID including -100
- ```/dl``` - to download videos from `youtube`, `pinterest`, `linkedin`, `internet archive`, `amazon mini tv`, `xvi..deos`, `xn..xx` sites.
- ```/Remthumb``` - to remove to thumbnail.
- ```/logs``` - to get the logs directly on telegram (now upto 2 min you can increase it accordingly)
- ```/help``` -to get help
### 🙄 ᴅᴇᴍᴏ/ᴛᴇsᴛ ʙᴏᴛ
  
  [sᴛʀɪɴɢ ʙᴏᴛ 🍑](https://telegram.me/Save-Restricted-Content-Bot-Repo-)

  # Updates

## Update: 6th June 2024
- Fixed Peer ID Invalid Error
- Removed `invalid` command handler as it is not needed anymore
- Added `speedboost.py` (dem)
## Update: 28th May 2024
- in `batch.py`, `.json` method implemented for saving batch details on `/batch` command. 
- `cancel` command fixed to clear the batch details and stop further processing.
- `/dl` command added to download videos from `youtube`, `pinterest`, `linkedin`, `internet archive`, `amazon mini tv`, `xvi..deos`, `xn..xx` sites.
- `set` and `remt` callback handlers removed now you have to send pic directly to set it as thumbnail and `/remthumb` to remove to thumbnail.
- `/logs` command added to get the logs directly on telegram (now upto 2 min you can increase it accordingly)
- `/help` command added
- Private topic groups are now supported, single link (for batch processing modify code by yourself)
- fixed peer id invalid error for some channel which do not support `-100` as prefix, use `/invalid` command to deal with this error (not fully resolved yet)
- Contact us on Telegram and request new changes and report bugs.


```
Atleast Give A Star and Fork The Repo 🖤
```


<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">












