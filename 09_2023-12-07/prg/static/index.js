console.log('JavaScript index.js fire!')  // JavaScriptが読み込まれて実行されたことをこれで確認できます。


// JSONデータ取得のWeb APIにJavaScriptからリクエストを投げ、レスポンスに応じてHTML要素を操作するサンプル
fetch(`/json_sample`)
    .then(response => {
        console.log(response.status)  // => 200
        return response.json().then(data => {
            // JSONをJSオブジェクトにパースされたオブジェクトがdataに格納される
            console.log(data);  // => {...}

            // HTMLの要素を取得
            const hedding1 = document.querySelector('h1#message')
            // 要素の文字部分にWeb APIから取得されたデータを設定する
            hedding1.textContent = data.message
        });
    });