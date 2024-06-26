from flask import Flask, render_template, jsonify
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


# http://127.0.0.1:5000/json_sample
@app.route('/json_sample')
def json_sample():

    # レスポンスデータをDictで構築
    ret = {
        "message": "こんにちは！WebAPI!!!",
    }

    # Flask.json.jsonifyを使ってJSONデータをレスポンスとする
    return jsonify(ret)
    # ↑ jsonifyを使うことで、HTTPのレスポンスヘッダもJSONデータ返信用に整えられます。


# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)