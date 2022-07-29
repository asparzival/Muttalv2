## What's up Kangers

import os

from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):

    load_dotenv("local.env")

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQBWVcKH1F3JVfWXvYih_5I0EJ3n5zGwA7mlh6MF6UF-ITUiR4tokZl0dmzYIH286ypDvQqRmZdKQ4j3MxlNk7TdYLtf0UntFzv-Ybz-y6deM3yq7rlHFl1sKuXQXPGbg91ZZqgRK_PyQOPsl4TsUpSmpLxWvaK-5yzG2KpVgZNCFItU2UbSFUxUcXECEbfnk73bXk8mZavR1aYhXw_6YgZzuC3Sl-AxyRZLIPFW_IwjxVAN5zMbFyz6Mg4Biwn-gku7B3WWS6tnncza7FoqLdS1YZ40fmBfPssSG0nKIGCZdkf8ct7whX2HHXg1aYh3ySkCsarNhXXG7BJNr5exIMGBAAAAAT3DHw0A")

BOT_TOKEN = getenv("BOT_TOKEN", "2027168098:AAH5c_TldqNmdhwnQ21gjjJrnO0xmbOBXQ0")

BOT_NAME = getenv("BOT_NAME", "🔱🔥🔥𝙂𝙐𝘼𝙍𝘿𝙄𝘼𝙉🔥🔥🔱")

API_ID = int(getenv("API_ID", "16370815"))

API_HASH = getenv("API_HASH", "517001ea4680069862676319136179e6")

OWNER_NAME = getenv("OWNER_NAME", "GUARDIAN")

OWNER_USERNAME = getenv("OWNER_USERNAME", "parzival_as")

ALIVE_NAME = getenv("ALIVE_NAME", "🔱🔥🔥𝙂𝙐𝘼𝙍𝘿𝙄𝘼𝙉🔥🔥🔱")

BOT_USERNAME = getenv("BOT_USERNAME", "GUARDIAN_GOD_BOT")

ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GUARDIAN_ASSIT")

GROUP_SUPPORT = getenv("sandapodalama")

UPDATES_CHANNEL = getenv("guardians_1")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1730760573").split()))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! ,").split())

ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")

START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500"))

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")

IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")

IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")

IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")

IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")

IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
