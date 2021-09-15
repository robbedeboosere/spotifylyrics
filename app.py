from flask import Flask
import lyric

app = Flask(__name__)

@app.route("/")
def hello_world():
    return lyric.get_current_lyrics()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)