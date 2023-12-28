from flask import Flask, request, render_template, jsonify
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


# http://127.0.0.1:5000/address
@app.route('/address', methods=["GET"])
def address_get():

    # 検索パラメータの取得
    p_first_name = request.args.get('fn', None)
    p_last_name = request.args.get('ln', None)
    p_email = request.args.get('em', None)

    with open('address.json') as f:
        json_data = json.load(f)

    # パラメータにより返すデータをフィルタリングする
    if p_first_name is not None:
        # ラムダにより匿名関数化しているため、分かりづらく見えますが、filter関数には関数を渡す必要があるため、
        # json_dataの中からfirst_name内にパラメータの値が含まれているかどうかを判定する関数を匿名で作成し、
        # それによって得た結果のデータを基にlist生成しています。
        json_data = list(filter(lambda item: p_first_name.lower() in item["first_name"].lower(), json_data))
    if p_last_name is not None:
        json_data = list(filter(lambda item: p_last_name.lower() in item["last_name"].lower(), json_data))
    if p_email is not None:
        json_data = list(filter(lambda item: p_email.lower() in item["email"].lower(), json_data))

    
    return jsonify(json_data)

@app.route('/address', methods=["POST"])
def address_post():
    p_first_name = request.form.get("fn", None)
    p_last_name = request.form.get("ln", None)
    p_email = request.form.get("em", None)
    
    # 複数エラーあったときのために、+=で対応
    error_message = ""

    if p_first_name is None:
        error_message += "first nameが未入力です。<br>"
    if p_last_name is None:
        error_message += "last nameが未入力です。<br>"
    if p_email is None:
        error_message += "emailが未入力です。<br>"

    # エラーメッセージがあればerror_messageとして返す
    if error_message != "":
        return jsonify({
            "status": "error",
            "content": error_message
        })
    
    # json開く
    with open('address.json') as f:
        json_data = json.load(f)
    
    # jsonに追加
    json_data.append({
        'email': p_email,
        'first_name': p_first_name,
        'last_name': p_last_name
    })
    
    # ファイルに保存
    with open('address.json', 'w') as f:
        json.dump(json_data, f, indent=4)
    
    # 更新されたjson_dataを返す
    return jsonify({
        "status": "success",
        "content": json_data
    })

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("addressbook.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True, port=8080)