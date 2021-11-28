from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def save_data():
    pass


app.run()


# Открываем постман
# Переходим в режим жсон
# Пишем запрос типа POST / ["admission", "occupy", "site", "poison"]
# Переходим в редактор
# Пишем

@app.route('/', methods=["POST"])
def save_data():
    json_data = request.get_json()
    print(json_data)

# Открываем постман
# Переходим в режим жсон
# Пишем запрос типа POST / {"name":"Alex", "phone": "+12345678", "email":"alex@sky.pro"}
# Переходим в редактор
# Пишем


@app.route('/', methods=["POST"])
def save_data():
    json_data = request.get_json()
    print(json_data.get("name"))
    print(json_data.get("phone"))
    print(json_data.get("email"))

# Вот и отлично, мы получили наши данные.
# Как мы видим, работа с json даже немного более простая чем работа с шаблонами.
# Хотя результат не такой симпатичный
