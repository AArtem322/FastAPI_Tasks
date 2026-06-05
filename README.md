# FastAPI Task Project📋

Данная программа предназначена для формирования списка задач.

---
## Функционал проекта:

- Обновление, добавление и удаление списка задач
- Возможность получить полную информацию о списке задач
- Возможность отметить задачу как выполненную 

---
## Используемые библиотеки:
```commandline
python-dotenv
fastapi
sqlalchemy
pydantic
psycopg2-binary
jinja2
python-multipart
uvicorn
```

---
## Запуск проекта:
1. Создайте виртуальное окружение
```python
python -M venv .venv
Для Windows: .venv\Scripts\activate
```

2. Установить зависимости
```commandline
pip install -r requirements.txt
```
При необходимости установить дополнительные библиотеки, которые запрашивает программа.

3. Создайте файл `.env` и заполните его по примеру `.env.example`

4. Запустить программу через консоль с помощью команды:

```commandline
uvicorn main:app --reload
```
