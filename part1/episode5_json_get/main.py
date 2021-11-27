from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/', methods=["GET"])
def json_get():
    pass


app.run()

# Окей, давайте примем запрос и вернем что-нибудь

from flask import Flask, request, render_template, jsonify

@app.route('/', methods=["GET"])
def json_get():
    data = {"format": "json"}
    jsonify(data)

# Открываем постман и отправляем запрос

# GET /

# # # # # # # # # # # # # # # # # # # # # # # #

# Давайте примем запрос посложнее например поиск

from flask import Flask, request, jsonify

items = ["admission", "occupy", "site", "poison", "physical", "horror", "crackpot", "restrict"]


@app.route('/', methods=["GET"])
def json_get():

    items_match = []
    s = request.form.get("s")

    for item in items:
        if s in item:
            items_match.append(item)

    jsonify(items_match)

# Отлично, кажется все работает!
