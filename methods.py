from .models import Users, Messages

# Получаем все сообщения
Messages.objects.all()
# Создаём пееменную с новым сообщением
new_message= Messages(user_id='', text='')
new_message.save() # Кидаем новое сообщение в БД

# Фильтр по полю "message_id"
Messages.objects.filter(id=1)

# Поиск по значениям полей
Messages.objects.filter(text__startswith= 'All')

# Получение ОДНОЙ записи по полю
Messages.objects.get(message_id=1)

# Наглое добавление записи в таблицу БД ()
Messages.objects.create(user_id='1', text='text')