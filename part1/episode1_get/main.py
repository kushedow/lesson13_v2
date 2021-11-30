from flask import Flask, request,render_template


app = Flask(__name__)


@app.route('/')
def page_form():
    pass

@app.route('/form')
def page_form():
    pass


app.run()


# Давайте посмотрим на очередное приложение - у нас есть форма и мы хотим обработать данные.
# Давайте посмотрим форму (открываем шаблон)
# Форма очень простая - называется перезвони мне и там только телефон.

# Давайте выведем эту форму при обращении на /

# @app.route('/')
# def page_form():
#     return render_template("index.html")

# Если мы отправим ее на http://httpbin.org/get то получим данные телефона
# Давайте примем ее с помощью фласка и тут нам пригодится объект реквест знакомый нам по работе с квери параметрами

# @app.route('/form')
# def page_get():
#     phone = request.args.get("phone")
#     return f"Получен телефон {phone}"

# Отправляем форму получаем данные. Окей, но можно лучше.

# # # # # # # # # # # # # #

# Мы можем объединить две вьюшки в одну, если будем проверять, были ли отправлены данные

# @app.route('/')
# def page_form():
#     request_data = request.args
#
#     if request_data:
#         phone = request_data.get("phone")
#         return f"Получен телефон {phone}"
#
#     return render_template("index.html")

# Вот и отлично - одна вьюшка и обрабатывает и показывает форму. Очень удобно!
