// データの初期表示
fetch("/address").then(response => {
    console.log(response);
    response.json().then((data) => {
        show_data(data);
    });
});

// データを表示させる関数
const show_data = (data) => {
    console.log(data);  // 取得されたレスポンスデータをデバッグ表示
    // データを表示させる
    const tableBody = document.querySelector("#address-list > tbody");

    // 表示された内容を一旦全消し
    tableBody.innerHTML = "";

    data.forEach(elm => {
        // 1行づつ処理を行う
        let tr = document.createElement('tr');
        // first name
        let td = document.createElement('td');
        td.innerText = elm.first_name;
        tr.appendChild(td);
        // last name
        td = document.createElement('td');
        td.innerText = elm.last_name;
        tr.appendChild(td);
        // email
        td = document.createElement('td');
        td.innerText = elm.email;
        tr.appendChild(td);

        // 1行分をtableタグ内のtbodyへ追加する
        tableBody.appendChild(tr);
    });
}

// メッセージ領域を初期化する関数
const clear_message = () => {
    document.getElementById('message-container').innerHTML = "";
    document.getElementById('message-container').style.display = "none";

    document.getElementById('error-container').innerHTML = "";
    document.getElementById('error-container').style.display = "none";
}

// search-submitが押された際のイベント
document.querySelector("#search-submit").addEventListener("click", (event) => {
    // デフォルトのイベントをキャンセル
    event.preventDefault();
    
    let serachFirstName = document.querySelector("#search-firstname").value;
    let serachLastName = document.querySelector("#search-lastname").value;
    let serachEmail = document.querySelector("#search-email").value;

    let params = new URLSearchParams();
    if (serachFirstName !== "") params.set("fn", serachFirstName);
    if (serachLastName !== "") params.set("ln", serachLastName);
    if (serachEmail !== "") params.set("em", serachEmail);

    fetch("/address?" + params.toString()).then(response => {
        console.log(response)
        response.json().then((data) => {
            console.log(data)
            show_data(data)
        })
    })
});

// add-submitが押された際のイベント
document.querySelector("#add-submit").addEventListener("click", (event) => {
    // デフォルトのイベントをキャンセル
    event.preventDefault();

    // メッセージ領域の初期化
    clear_message();

    let addFirstName = document.querySelector("#add-firstname").value;
    let addLastName = document.querySelector("#add-lastname").value;
    let addEmail = document.querySelector("#add-email").value;

    // 複数エラーがあったときのために、エラーメッセージを格納する変数を用意
    let error_message = ""

    if (addFirstName === "") error_message += "first nameが未入力です。<br>";
    if (addLastName === "") error_message += "last nameが未入力です。<br>";
    if (addEmail === "") error_message += "emailが未入力です。<br>";

    // エラーがあった場合は、エラーメッセージを表示して処理を終了する
    if (error_message !== "") {
        document.querySelector("#error-container").innerHTML = error_message;
        document.querySelector("#error-container").style.display = "block";
        return;
    }

    fetch('/address', {
        method: 'POST',
        body: new FormData(document.getElementById('add')),
    }).then((response) => {
        // 入力内容のリセット
        document.getElementById("add").reset();

        // レスポンスからjsonを取得
        response.json().then((data) => {
            if(data.status === "error") {
                // エラーがあった場合は、エラーメッセージを表示して処理を終了する
                document.querySelector("#error-container").innerHTML = data.content;
                document.querySelector("#error-container").style.display = "block";
                return;
            }else if(data.status === "success") {
                document.getElementById('message-container').innerHTML = "データの登録に成功しました";
                document.getElementById('message-container').style.display = "block";

                show_data(data.content);
            }
        });
    })
});