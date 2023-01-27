from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5476404763:AAFrzXKJESgBDzpO2BU5roOtauxZ0Y3EzpY")

API_ID = int(os.environ.get("API_ID", "17983098"))

API_HASH = os.environ.get("API_HASH", "ee28199396e0925f1f44d945ac174f64")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
