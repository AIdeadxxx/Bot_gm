# Фиктивный модуль imghdr для обхода проблемы совместимости Python 3.13 и python-telegram-bot
# В Python 3.13 модуль imghdr был удален

def what(file, h=None):
    """Временная замена для imghdr.what() - определяет тип изображения
    
    Args:
        file: Путь к файлу или файлоподобный объект
        h: Заголовок файла (опционально)
        
    Returns:
        str: Предполагаемый тип изображения или None
    """
    # Простая реализация определения типа изображения по сигнатурам
    if h is None:
        if isinstance(file, str):
            with open(file, 'rb') as f:
                h = f.read(32)
        else:
            location = file.tell()
            h = file.read(32)
            file.seek(location)
            
    # Проверка сигнатур популярных форматов
    if h.startswith(b'\xff\xd8'):
        return 'jpeg'
    elif h.startswith(b'\x89PNG\r\n\x1a\n'):
        return 'png'
    elif h.startswith(b'GIF87a') or h.startswith(b'GIF89a'):
        return 'gif'
    elif h.startswith(b'BM'):
        return 'bmp'
    elif h.startswith(b'WEBP'):
        return 'webp'
    
    return None
    
# Другие необходимые функции из оригинального модуля
tests = [] 