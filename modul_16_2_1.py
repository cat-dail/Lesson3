# Задача "Аннотация и валидация":
# Допишите валидацию для маршрутов из предыдущей задачи при помощи классов Path и Annotated:
# '/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id,
# для которого необходимо написать следующую валидацию:
# Должно быть целым числом
# Ограничено по значению: больше или равно 1 и меньше либо равно 100.
# Описание - 'Enter User ID'
# Пример - '1' (можете подставить свой пример не противоречащий валидации)
# '/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту,
# принимает аргументы username и age, для которых необходимо написать следующую валидацию:
# username - строка, age - целое число.
# username ограничение по длине: больше или равно 5 и меньше либо равно 20.
# age ограничение по значению: больше или равно 18 и меньше либо равно 120.
# Описания для username и age - 'Enter username' и 'Enter age' соответственно.
# Примеры для username и age - 'UrbanUser' и '24' соответственно. (можете подставить свои
# примеры не противоречащие валидации).

from fastapi import FastAPI
from typing import Annotated
from fastapi import Path

app = FastAPI()


@app.get("/")
async def read_root() -> str:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def read_admin() -> str:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user_id(
    user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]
) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def get_user_username(
    username: Annotated[str, Path(min_length=5,
                                  max_length=20, regexp="^[a-zA-Z0-9_-]+$",
                                  description="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
