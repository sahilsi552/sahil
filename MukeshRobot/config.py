class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details
given by it
    API_ID = "20892750" # integer value, dont use ""
    API_HASH = "b0241677a3a2958667e93fa9a632c350"
    TOKEN = "7694231563:AAEEu-m6eC1vtwTLOAXE6C_qMAs1o2cXZUE"  # This var used to
 be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "7785947978" # If you dont know, run the bot and do /id in your p
rivate chat with it, also an integer
    SUPPORT_CHAT = "tyrosupport"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph/file/000625ad0b270aaea4ec6.jpg"
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled
disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://SATYAM847108:BIHARDARBHANGAA@cluster0.cfrj9.mon
godb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # RECOMMENDED
    DATABASE_URL = "postgres://kykrjayd:s_zaM4ZfJFVIBZzsQxoHi1JKbV5edFgJ@kandula
.db.elephantsql.com/kykrjayd"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = ""
    # Get your API key from https://timezonedb.com/api
    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
class Production(Config):
    LOGGER = True
class Development(Config):
    LOGGER = True
