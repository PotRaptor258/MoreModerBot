from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from tokens import TOKEN, ADMIN_ID, ID, HASH
from pyrogram import Client
import asyncio

"""Создание экземпляров бота и клиента"""
bot = Bot(token=TOKEN)
dp = Dispatcher()
app = Client("Tool", api_id=ID, api_hash=HASH, bot_token=TOKEN, in_memory=True)

"""Функция очистки чата от удалённых аккаунтов"""
@dp.message(Command(commands=['no_deleted']))
async def no_deleted(message: Message):
    count = 0
    """Проверка на группу или канал"""
    if message.chat.type in ['group', 'supergroup', 'channel']:
        try:
            """Проверка на администратора"""
            if message.from_user.id in [admin.user.id for admin in await bot.get_chat_administrators(message.chat.id)] and not message.from_user.is_bot:
                """Запуск клиента"""
                try:
                    await app.start()
                except:
                    pass
                """Перебор участников чата"""
                async for member in app.get_chat_members(chat_id=message.chat.id):
                    if member.user.is_deleted:
                        await bot.ban_chat_member(message.chat.id, member.user.id)
                        count += 1
                """Остановка клиента"""
                try:
                    await app.stop()
                except:
                    pass

            await message.reply(f"Убрано удалённых аккаунтов из чата: {count}")

        except Exception as e:
            await message.reply("Ошибка!")
            await bot.send_message(ADMIN_ID, str(e))
    else:
        await message.reply("Невозможно использовать команду здесь!")


"""Функция очистки истории чата от пользователя"""
@dp.message(Command(commands=['clear_messages']))
async def no_deleted(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    """Проверка на группу"""
    if message.chat.type in ['group', 'supergroup']:
        try:
            await bot.ban_chat_member(chat_id, user_id, revoke_messages=True)
            await bot.unban_chat_member(chat_id, user_id)
            await message.reply("Сообщения были удалены!")
        except Exception as e:
            await message.reply("Ошибка!")
            await bot.send_message(ADMIN_ID, str(e))
    else:
        await message.reply("Невозможно использовать команду здесь!")


@dp.message()
async def start(message: Message):
    if message.chat.id == message.from_user.id:
        await message.reply('👋')


async def on_startup():
    bot_info = await bot.get_me()
    await bot.send_message(ADMIN_ID, f'Бот @{bot_info.username} включён')


async def on_shutdown():
    bot_info = await bot.get_me()
    await bot.send_message(ADMIN_ID, f'Бот @{bot_info.username} выключен')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
