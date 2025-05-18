# MoreModerBot
## Подготовка к использованию

1. Установите Microsoft Visual C++ 14.0 (2022). Оно необходимо для работы библиотеки TgCrypto. При установке выберите "Стандартные приложения C++". Ссылка для скачивания: https://visualstudio.microsoft.com/visual-cpp-build-tools/

2. Установите библиотеки

> **python -m pip install -r requirements.txt**

3. Перейдите по ссылке https://my.telegram.org/, авторизуйтесь, перейдите в раздел "API development tools". Создайте приложение, получите ID и HASH. Подробнее: https://docs.pyrogram.org/start/setup/

Получите TOKEN в https://t.me/BotFather/ и ADMIN_ID в https://t.me/username_to_id_bot/. Вставьте TOKEN, ID, HASH, и ADMIN_ID в файл tokens.py

4. Замените файл Lib\site-packages\pyrogram\methods\chats\get_chat_members.py. Добавленный код: https://qna.habr.com/q/1358994/
