"""Модуль c роутингом"""


#### Category

# - POST `/api/category` - создание категории
# - GET `/api/category` - получение всех категории
# - GET `/api/category/<id:int>` - получение категории по идентификатору
# - PUT `/api/category/<id:int>` - изменение категории
# - DELETE `/api/category/<id:int>` - удаление категории


#### Question

# - POST `/api/question` - создание вопроса
# - GET `/api/question` - получение всех вопросов
# - GET `/api/question/<id:int>` - получение вопроса по идентификатору
# - GET `/api/question/by_text/<query: str>` - получение вопроса по тексту
# - POST `/api/question/<id:int>/check` - проверка ответа на вопрос
# - PUT `/api/question/<id:int>` - изменение вопроса
# - DELETE `/api/question/<id:int>` - удаление вопроса


#### Quiz

# - POST `/api/quiz` - создание квиза
# - GET `/api/quiz` - получение всех квизов
# - GET `/api/quiz/<id:int>` - получение квиза по идентификатору
# - GET `/api/quiz/<id:int>/random_question` - получение случайного вопроса по идентификатору квиза
# - GET `/api/quiz/by_title/<title: str>` - получение квиза по названию
# - PUT `/api/quiz/<id:int>` - изменение квиза
# - DELETE `/api/quiz/<id:int>` - удаление квиза


# Сюда добавляем все пути и их обработчики
urlpatterns = []
