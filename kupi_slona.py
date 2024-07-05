import logging
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError

logging.basicConfig(level=logging.INFO)
# Вставьте свои данные
api_id = 'API_ID'
api_hash = 'API_HASH'
phone = 'PHONE'
user_id = 'USER_ID'  # ID пользователя, которому нужно отвечать

# Инициализация клиента с использованием файла сессии
client = TelegramClient('existing_session.session', api_id, api_hash)

async def main():
    try:
        # Попытка запустить клиент с файлом сессии
        if not await client.is_user_authorized():
            print("Авторизация пользователя")
            await client.start(phone)

        @client.on(events.NewMessage(from_users=user_id))
        async def handler(event):
            response = "все так говорят, а ты купи слона"
            await client.send_message(event.chat_id, response)

        print("Bot is running...")
        await client.run_until_disconnected()
    except SessionPasswordNeededError:
        print("Пожалуйста, введите пароль двухфакторной аутентификации")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

with client:
    client.loop.run_until_complete(main())
