from flask import Flask, request, jsonify
app = Flask(__name__)

# Как принимать данные из get-формы


@app.route('/form')
def page_get():
    phone = request.form.get("phone")
    return f"Получен телефон {phone}"

# Как принимать данные из post-формы

@app.route('/', methods=["GET", "POST"])
def page_form():

    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")

    return f"Получены данные  {name} {phone} {email}"

# Как получать и сохранять файлы


# Как паковать данные в JSON

@app.route('/api')
def get_json():

    items = ["admission", "occupy", "site", "poison", "physical", "horror", "crackpot", "restrict"]
    jsonify(items)


# Как тестировать json-запросы?

Используйте Postman

# Как получать данные из JSON

@app.route('/', methods=["POST"])
def save_data():
    json_data = request.get_json()
    print(json_data.get("name"))




