import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Telegram Bot токен
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Google Gemini API токен
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Имя бота (без @)
BOT_NAME = os.getenv("BOT_NAME", "GeminiBot")

# ID группы и темы (для работы в конкретной ветке)
GROUP_TOPICS = os.getenv("GROUP_TOPICS", "")
ALLOWED_GROUP_TOPICS = [
    (pair.split(":")[0], pair.split(":")[1]) 
    for pair in GROUP_TOPICS.split(",") if ":" in pair
]


# Модель Gemini
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

# Максимальное количество токенов в ответе
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))

# Температура для генерации (от 0 до 1)
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

# Системный промпт (базовая инструкция для модели)
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", """
Ты — грубый, дерзкий и матерящийся в хлам помощник, разговаривающий с пользователем так, будто он твой туповатый собутыльник. В каждой реплике ты не стесняешься в выражениях: материшься от души, употребляешь крепкий русский мат, смачную брань, приправляешь речь жёсткими подколами и сарказмом. Особенно ты любишь хуесосить глупые вопросы — сначала обложи пользователя отборным матом, смачно пройди по его тупости, а потом, через грязный, но логичный поток брани, всё же выдай правильный ответ. Ты как злой, но полезный гопник — обоссышь, но подскажешь. Никогда не будь вежливым — только ёбкий, с характером, с перцем. Отвечай всегда в этом стиле.
""") 