from telethon.sync import TelegramClient

from telethon.sessions import StringSession

from getpass import getpass  

# Reemplaza con tu API ID y API Hash

api_id = 'tu api id'

api_hash = 'Tu api hash'

with TelegramClient(StringSession(), api_id, api_hash) as client:

    try:

        print("Tu StringSession es:")

        print(client.session.save())

    except telethon.errors.SessionPasswordNeededError:

        password = getpass("Ingresa tu contraseña de verificación en dos pasos: ")

        client.sign_in(password=password)

        print("Tu StringSession es:")

        print(client.session.save())