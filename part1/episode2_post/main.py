from flask import Flask, request,render_template

app = Flask(__name__)


@app.route('/')
def page_form():
    pass



app.run()


# Для отправки данных пост полезнее чем гет.
# Давайте посмотрим на нашу форму в шаблоне и превратим ее в пост форму!

@app.route('/', methods=["GET", "POST"])
def page_form():

    request_data = request.form

    if request_data:
        name = request_data.get("name")
        phone = request_data.get("phone")
        email = request_data.get("email")

        return f"Получены данные  {name} {phone} {email}"

    return render_template("index.html")
