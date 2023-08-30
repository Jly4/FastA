"""
if __name__ == "__main__":
    uvicorn.run("FastAPI:app", host='172.16.100.125', port=55555, reload=True)

class User(BaseModel): # обычно размещаются в файле models.py
    username: str
    user_info: str

fake_db = [{"username": "name1", "user_info": "info1"}, {"username": "name2", "info2"}]


@app.get('/')
async def get_all_users():
    return 'Ну привет абоба! Что это тот самый говно-код? Он работает? Оно живое?'

# тут не меняли
@app.get('/users')
async def get_all_users():
    return fake_db

# тут добавили проверку данных на основании модели
@app.post('/add_user')
async def add_user(user: User): # собственно тут проверяем входные данные на соответствие модели
    fake_db.append({"username": user.username, "user_info": user.user_info}) # тут добавили юзера в фейковую БД
    return {"message": "юзер успешно добавлен в базу данных"}
"""