from flask import Flask, request,render_template

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def page_form():
    return render_template("index.html")


app.run()


# Не все данные текстовые, файлы приходится загружать файлы - картинки, видео, пдф и так далее.
# В объект реквест падают файлы, их можно переместить в папку вашего проекта, а в будущем
# можно отправить на отдельный сервер.

# Открываем форму, смотрим ее, готовим файл, говорим про files в request,

# Отлично, теперь осталось научиться файлы принимать

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == "POST":
        f = request.files['attachment']
        f.save(f.filename)
        return 'Файлы загружены'
    return render_template("index.html")


# Снова отправляем файл
# показываем что файл загрузился

