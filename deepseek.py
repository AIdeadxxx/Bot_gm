import requests
import json
import config

class DeepSeekAPI:
    """Класс для взаимодействия с API DeepSeek"""
    
    def __init__(self):
        self.api_key = config.DEEPSEEK_API_KEY
        self.api_url = config.DEEPSEEK_API_URL
        self.model = config.DEEPSEEK_MODEL
        self.max_tokens = config.MAX_TOKENS
        self.temperature = config.TEMPERATURE
        
    def generate_response(self, prompt, chat_history=None):
        """Генерирует ответ от DeepSeek API на основе запроса
        
        Args:
            prompt (str): Текст запроса
            chat_history (list, optional): История сообщений
            
        Returns:
            str: Сгенерированный ответ или сообщение об ошибке
        """
        if not self.api_key:
            return "Ошибка: API ключ DeepSeek не настроен"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        messages = []
        
        # Добавляем историю сообщений, если она есть
        if chat_history:
            messages.extend(chat_history)
        
        # Добавляем текущий запрос пользователя
        messages.append({"role": "user", "content": prompt})
        
        data = {
            "model": self.model,
            "messages": messages,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                data=json.dumps(data),
                timeout=30
            )
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data["choices"][0]["message"]["content"]
            else:
                return f"Ошибка API ({response.status_code}): {response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"Ошибка запроса: {str(e)}"
        except (KeyError, json.JSONDecodeError) as e:
            return f"Ошибка обработки ответа: {str(e)}" 