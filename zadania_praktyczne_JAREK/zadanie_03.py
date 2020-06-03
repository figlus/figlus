from flask import Flask, render_template, request

import zadanie_02 as zd

app = Flask(__name__)

# korzystając z poniżej napisanej funkcji, która będzie uruchamiała się za każdym razem gdy wejdziemy na adres naszego
# lokalnego serwera, połącz kod z zadania pierwszego oraz 2 tak by przekazać do funkcji render_template a w rezultacie
# do main.html po czym za pomocą konstrukcji {{}} wyświetl te produkty
# plik main.html umieść w folderze templates

@app.route('/')
def homepage():
	
	oferty = zd.get_some_offers
    return render_template("main.html", data = data)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=5000, debug=True)