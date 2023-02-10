import flask

app = flask.Flask(__name__)

@app.route('/')

def resume():
    return flask.send_file("Ella_Soccoli_Resume_Feb_2023.pdf")

app.run()