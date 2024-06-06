from os import getenv

from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("TOKEN", "6589147306:AAE9y8vL41hky8XqxQtiwQ4IGGiKUneFuDM")
"Telegram bot token obtained from botfather"
DB_URI = getenv("MONGO_URL", "mongodb+srv://haris12:haris12@cluster0.u8qzvr4.mongodb.net/?retryWrites=true&w=majority")
"database url (mongo)"
OWNER_ID = 614393705
"Telegram ID of the bot owner"
LOGGER_ID = int(getenv("LOGGER_ID", "-1001457998546"))
"channel/group ID with `-` for keeping track of new errors where the bot gets..."
SUDO_USER = list(map(int, getenv("SUDO_USER", "614393705").split()))
"set of user ID which can have elevated privileges"
LOGGER_LEVEL = getenv("LOGGER_LEVEL", 20)
"logger level, `debug(10)`, `info(20)`, `warn(30)` and `error(40)`. default is `info`"

TIME_ZONE = "Asia/Kolkata"
