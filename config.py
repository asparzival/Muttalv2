## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "BQBWVcKH1F3JVfWXvYih_5I0EJ3n5zGwA7mlh6MF6UF-ITUiR4tokZl0dmzYIH286ypDvQqRmZdKQ4j3MxlNk7TdYLtf0UntFzv-Ybz-y6deM3yq7rlHFl1sKuXQXPGbg91ZZqgRK_PyQOPsl4TsUpSmpLxWvaK-5yzG2KpVgZNCFItU2UbSFUxUcXECEbfnk73bXk8mZavR1aYhXw_6YgZzuC3Sl-AxyRZLIPFW_IwjxVAN5zMbFyz6Mg4Biwn-gku7B3WWS6tnncza7FoqLdS1YZ40fmBfPssSG0nKIGCZdkf8ct7whX2HHXg1aYh3ySkCsarNhXXG7BJNr5exIMGBAAAAAT3DHw0A":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "2027168098:AAH5c_TldqNmdhwnQ21gjjJrnO0xmbOBXQ0")
BOT_NAME = getenv("BOT_NAME", "GUARDIAN")

API_ID = int(getenv("API_ID", "16370815"))
API_HASH = getenv("API_HASH", "517001ea4680069862676319136179e6")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://mr:white@cluster0.n3huo.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "GUARDIAN")
OWNER_USERNAME = getenv("OWNER_USERNAME", "parzival_as")
ALIVE_NAME = getenv("ALIVE_NAME", "GUARDIAN")
BOT_USERNAME = getenv("BOT_USERNAME", "GUARDIAN_GOD_BOT")
OWNER_ID = getenv("OWNER_ID", "1828057558")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GUARDIAN_ASSIT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "sandapodalama")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "guardians_1")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1730760573").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/feb320da568222907cd32.jpg")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/20143a2f52fa22a6af3d9.jpg")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/ace3471aeaac81650931e.jpg")
HEROKU_MODE = getenv("HEROKU_MODE", None)
