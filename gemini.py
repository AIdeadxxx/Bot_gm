import google.generativeai as genai
import config
import logging

logger = logging.getLogger(__name__)

class GeminiAPI:
    """Класс для взаимодействия с Google Gemini API"""
    
    def __init__(self):
        self.api_key = config.GEMINI_API_KEY
        self.model = config.GEMINI_MODEL
        self.temperature = config.TEMPERATURE
        self.max_tokens = config.MAX_TOKENS
        self.system_prompt = config.SYSTEM_PROMPT
        
        # Инициализация Gemini API
        if self.api_key:
            genai.configure(api_key=self.api_key)
        
    def generate_response(self, prompt, chat_history=None):
        """Генерирует ответ от Gemini API на основе запроса
        
        Args:
            prompt (str): Текст запроса
            chat_history (list, optional): История сообщений
            
        Returns:
            str: Сгенерированный ответ или сообщение об ошибке
        """
        if not self.api_key:
            return "Ошибка: API ключ Gemini не настроен"
        
        try:
            # Конфигурация модели
            generation_config = {
                "temperature": self.temperature,
                "max_output_tokens": self.max_tokens,
            }
            
            # Создаем экземпляр модели
            model = genai.GenerativeModel(
                model_name=self.model,
                generation_config=generation_config
            )
            
            # Добавляем системный промпт к запросу пользователя
            full_prompt = f"{self.system_prompt}\n\nЗапрос пользователя: {prompt}"
            
            # Если есть история чата, используем ее
            if chat_history:
                chat = model.start_chat(history=chat_history)
                response = chat.send_message(full_prompt)
            else:
                # Простой запрос без истории
                response = model.generate_content(full_prompt)
            
            # Получаем текст ответа
            return response.text
                
        except Exception as e:
            logger.error(f"Ошибка Gemini API: {str(e)}")
            return f"Ошибка Gemini API: {str(e)}" 