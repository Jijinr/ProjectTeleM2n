import os

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = "47dadf1a-d598-4b2b-91fd-da255ff540ad"
    # get a token from @BotFather
    TG_BOT_TOKEN = "1160076176:AAEkIviWIdpqJMIhMTalNtVVDU58F5WYzXo"
    #TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # The Telegram API things
    #APP_ID = int(os.environ.get("APP_ID", 12345))
    APP_ID = 1716832
    #API_HASH = os.environ.get("API_HASH")
    API_HASH = "824debf2174102efdff18d7fc7312bcd"
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    #AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    AUTH_USERS = {7351948,466337795,1264945270,604378231}
    # reg: Procedures
    UTUBE_BOT_USERS = []
    SUPER_DLBOT_USERS = []
    SUPER3X_DLBOT_USERS = []
    SUPER7X_DLBOT_USERS = [1264945270,604378231]
    BANNED_USERS = []
    # Wat was I thinking? :\
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # for storing the user details
    DB_SQLALCHEMY = "USERS.session"
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # for Google Custom Search Engine
    GCS_API_KEY = os.environ.get("GCS_API_KEY", None)
    GCS_SE_ID = os.environ.get("GCS_SE_ID", None)
    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
