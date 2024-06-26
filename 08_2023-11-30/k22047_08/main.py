from flask import Flask, request, render_template
import random # ランダムデータ作成のためのライブラリ
import datetime

app = Flask(__name__)

# 1. プロジェクトのトップ（じゃんけんアプリや、課題のアプリへのリンクを配置するだけ）
@app.route('/')
def index():
    return render_template('index.html')


# 2. じゃんけんアプリの入力フォーム
@app.route('/janken')
def janken():
    # じゃんけんの入力画面のテンプレートを呼び出し
    return render_template('janken_form.html')


# 3. じゃんけんデータ送信先とじゃんけん結果表示画面
@app.route('/janken/play', methods=["POST"])
def janken_play():

    # <input type="text" id="your_name" name="name">
    name = request.form.get("name")
    if not name:
        name = "名無しさん"
    
    # <input type="radio" id="hand_rock" value="rock" name="hand">
    # <input type="radio" id="hand_scissor" value="scissor" name="hand">
    # <input type="radio" id="hand_paper" value="paper" name="hand">
    hand = request.form.get("hand", None)
    
    settai = request.form.get("is_settai", None)

    # リストの中からランダムに選ぶ
    cpu = random.choice(["rock", "scissor", "paper"])
    
    if settai:
        if hand == "rock":
            cpu = "scissor"
        elif hand == "scissor":
            cpu = "paper"
        elif hand == "paper":
            cpu = "rock"
        else:
            if cpu == "rock":
                hand = "paper"
            elif cpu == "paper":
                hand = "scissor"
            elif cpu == "scissor":
                hand = "rock"

    # じゃんけん処理
    if hand == cpu:
        result_message = "あいこ"
        result = "draw"
    else:
        if hand == "rock":
            if cpu == "scissor":
                result_message = "{}の勝ち".format(name)
                result = "win"
            else:
                result_message = "{}の負け".format(name)
                result = "lose"
        elif hand == "scissor":
            if cpu == "paper":
                result_message = "{}の勝ち".format(name)
                result = "win"
            else:
                result_message = "{}の負け".format(name)
                result = "lose"
        elif hand == "paper":
            if cpu == "rock":
                result_message = "{}の勝ち".format(name)
                result = "win"
            else:
                result_message = "{}の負け".format(name)
                result = "lose"
        else:
            result_message = "後出しはダメです。"
            result = "late"
    
    # if settai:
    #     result_message += "(接待)"

    # 渡したいデータを先に定義しておいてもいいし、テンプレートを先に作っておいても良い
    return render_template('janken_play.html',
                            result_message=result_message,
                            name=name,
                            hand=hand,
                            cpu=cpu,
                            result = result)

@app.route('/uranai')
def uranai():
    return render_template('uranai_form.html')

@app.route('/uranai/play', methods=["POST"])
def uranai_play():
    birthday = request.form.get("birthday")
    name = request.form.get("name")
    
    # 入力された内容が正しいかチェック
    try:
        birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
    except ValueError:
        # ダメならNoneってことにする
        birthday = None
    
    if birthday is None or name is None:
        return render_template('uranai_play.html',
                                fortune = 1,
                                message = "入力不備で占えませんでした")

    # 今日の日付を取得
    today = datetime.date.today()
    
    # yyyyMMdd形式で数値化する
    birthday = int(birthday.strftime('%Y%m%d'))
    today = int(today.strftime('%Y%m%d'))
    
    # 数値化した現在日付から生年月日を減算し、結果の絶対値を算出する
    diff = abs(today - birthday)
    
    # 「減算結果の絶対値」と「名前の文字数」を掛け算にて算出する
    fortune = diff * len(name)
    
    # 掛け算結果を5で割った余り
    fortune %= 5
    
    # 運勢ポイントを出す
    fortuneTuple = (5, 1, 3, 2, 4)
    fortune = fortuneTuple[fortune]
    
    message = ""
    
    if fortune == 5:
        message = "最高の一日"
    elif fortune == 4:
        message = "楽しい一日"
    elif fortune == 3:
        message = "普通の一日"
    elif fortune == 2:
        message = "ちょっと良く無い一日"
    elif fortune == 1:
        message = "良く無い一日"
        
    return render_template('uranai_play.html',
                            fortune = fortune,
                            message = message)

if __name__ == '__main__':
    app.run(port = 8080)