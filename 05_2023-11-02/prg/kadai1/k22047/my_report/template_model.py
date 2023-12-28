import string
import json
import os

class report_model:
    """
    テキストデータの管理(get,set)および保管(save,load)を行うクラス
    """

    KEY_LIST = ["CLASS_NO","MY_INFO", "APP_SPEC_DESCRIBE","APP_IMAGE","WORK_FLOW","MY_WEEKLY_REPORT","THANKS2MEMBER","MY_THOUGHTS_AND_NEXT_WORKS"]

    def __init__(self):
        file_name = "status.json"
        if os.path.isfile(file_name):
            with open(file_name) as f:
                self.status = json.load(f)
        else:
            print("status.jsonファイルを準備してください")
            exit()
        if not hasattr(self, 'status'):
            self.status={}
        if "basic_info" not in self.status.keys():
            self.status["basic_info"]={}
            # 初期値入力ダイアログ呼び出し
        if "history" not in self.status.keys():
            self.status["history"]={}
            ## 作成者情報
            self.status["history"]["MY_INFO"] = self.get_template_my_info()
            ## 仕様
            self.status["history"]["APP_SPEC_DESCRIBE"] = report_model.get_template_app_spec_describe()
            ## アプリ完成イメージ
            self.status["history"]["APP_IMAGE"] = report_model.get_template_app_image()
            ## 作業分担
            self.status["history"]["WORK_FLOW"] = report_model.get_template_work_flow()
            ## 作業報告
            self.status["history"]["MY_WEEKLY_REPORT"] = report_model.get_template_my_weekly_report()
            ## グループ内でお世話になった人2〜3名を理由とともに挙げる
            self.status["history"]["THANKS2MEMBER"] = report_model.get_template_thanks2member()
            ## 振り返り（感想含む）と次回までの作業予定
            self.status["history"]["MY_THOUGHTS_AND_NEXT_WORKS"] = report_model.get_template_my_thoughts_and_next_works()

    def get_body(self) -> str:
        t = string.Template(self.__get_template_body())
        ret = t.safe_substitute(self.status["history"])
        t = string.Template(ret)
        ret = t.safe_substitute(self.status["basic_info"])
        return ret

    def __get_template_body(self) -> str:
        return """\
# オブジェクト指向プログラミングおよび演習 第$CLASS_NO回進捗レポート

## 作成者情報
$MY_INFO

## 仕様
$APP_SPEC_DESCRIBE

## アプリ完成イメージ
$APP_IMAGE

## 作業分担
$WORK_FLOW

## 作業報告
$MY_WEEKLY_REPORT

## グループ内でお世話になった人2〜3名を理由とともに挙げる
$THANKS2MEMBER

## 振り返り（感想含む）と次回までの作業予定
$MY_THOUGHTS_AND_NEXT_WORKS
"""

    def get_template_class_no(self) -> int:
        return self.status['basic_info']["CLASS_NO"]

    def get_template_my_info(self) -> str:
        ret = """\
- 学籍番号：$MY_ID
- 氏名：$MY_NAME
- グループ：$GROUP_ID
    - メンバー
        - $LEADER_ID $LEADER_NAME（チームリーダー）
"""
        if "MEMBER_ID_1" in self.status['basic_info'].keys():
            ret += """
        - $MEMBER_ID_1 $MEMBER_NAME_1
"""
        if "MEMBER_ID_2" in self.status['basic_info'].keys():
            ret += """
        - $MEMBER_ID_2 $MEMBER_NAME_2
"""
        if "MEMBER_ID_3" in self.status['basic_info'].keys():
            ret += """
        - $MEMBER_ID_3 $MEMBER_NAME_3
"""
        if "MEMBER_ID_4" in self.status['basic_info'].keys():
            ret += """
        - $MEMBER_ID_4 $MEMBER_NAME_4
"""
        if "MEMBER_ID_5" in self.status['basic_info'].keys():
            ret += """
        - $MEMBER_ID_5 $MEMBER_NAME_5
"""
        if "MEMBER_ID_6" in self.status['basic_info'].keys():
            ret += """
        - $MEMBER_ID_6 $MEMBER_NAME_6
"""
        # if 7th member exists then you add their lines
        return ret

    def get_template_app_spec_describe() -> str:
        return """\
- flaskを使ったフォトアルバム
- 画像をアップロードできる
- アップロードした画像にタグをつけられる
- アップロードした画像にコメントを書ける
- 画像検索ページでタグやコメントから画像を検索できる
- CSSで画面を見やすくする
"""

    def get_template_app_image() -> str:
        return """\
- ここにトップページの手書きいらすと（top_page.jpegもMoodleへアップロードした）
- ここに画像リストページの手書きイラスト(image_list_page.jpeg)
- ここに画像アップロードページの手書きいらすと(upload_page.jpeg)
- ここに画像検索ページの手書きイラスト(search_page.jpeg)
"""

    def get_template_work_flow() -> str:
        return """\
- 画像をアップロードできる（担当：$MEMBER_ID_3 $MEMBER_NAME_3）
- アップロードした画像にタグをつけられる（主担当：$MEMBER_ID_1 $MEMBER_NAME_1，副担当：$MEMBER_ID_2 $MEMBER_NAME_2）
- アップロードした画像にコメントを書ける（主担当：$MEMBER_ID_2 $MEMBER_NAME_2，副担当：$MEMBER_ID_1 $MEMBER_NAME_1）
- 画像検索ページでタグやコメントから画像を検索できる（担当：$MEMBER_ID_4 $MEMBER_NAME_4）
- CSSで画面を見やすくする（担当：$MEMBER_ID_5 $MEMBER_NAME_5）
"""

    def get_template_my_weekly_report() -> str():
        return """\
- (これはサンプルです)
- 画像を保管する仕様を愛知花子と話あって決めた
- 保管した画像がWebページに表示されるところまで愛知花子と共同作業して作った
    - プルリクエストへのリンク
    - 上のプルリクエストがマージされた
"""

    def get_template_thanks2member() -> str():
        return """\
- 画像処理のベースプログラム実装を一緒にした($MEMBER_ID_2 $MEMBER_NAME_2)
- プルリクエストを処理してくれた（$MEMBER_ID_1 $MEMBER_NAME_1）
- 調べ物を手伝ってくれた($MEMBER_ID_5 $MEMBER_NAME_5)
"""

    def get_template_my_thoughts_and_next_works() -> str:
        return """\
- 計画通りに作業は進んでいる
- 画像を取り扱う共通仕様は愛知花子と共同で作成したが，来週からは作業を分担してすすめる
"""

    def get_text_by_key(self, key_name : str) -> str:
        if self.KEY_LIST.index(key_name)==0:
            return str(self.status["basic_info"][self.KEY_LIST[0]])
        if self.KEY_LIST.index(key_name)==1:
            return self.status["history"][self.KEY_LIST[1]]
        if self.KEY_LIST.index(key_name)==2:
            return self.status["history"][self.KEY_LIST[2]]
        if self.KEY_LIST.index(key_name)==3:
            return self.status["history"][self.KEY_LIST[3]]
        if self.KEY_LIST.index(key_name)==4:
            return self.status["history"][self.KEY_LIST[4]]
        if self.KEY_LIST.index(key_name)==5:
            return self.status["history"][self.KEY_LIST[5]]
        if self.KEY_LIST.index(key_name)==6:
            return self.status["history"][self.KEY_LIST[6]]
        if self.KEY_LIST.index(key_name)==7:
            return self.status["history"][self.KEY_LIST[7]]

    def set_text_by_key(self, key_name : str, value : str):
        if self.KEY_LIST.index(key_name)==0:
            self.status['basic_info'][self.KEY_LIST[0]] = int(value)
        if self.KEY_LIST.index(key_name)==1:
            self.status['history'][self.KEY_LIST[1]] = value
        if self.KEY_LIST.index(key_name)==2:
            self.status['history'][self.KEY_LIST[2]] = value
        if self.KEY_LIST.index(key_name)==3:
            self.status['history'][self.KEY_LIST[3]] = value
        if self.KEY_LIST.index(key_name)==4:
            self.status['history'][self.KEY_LIST[4]] = value
        if self.KEY_LIST.index(key_name)==5:
            self.status['history'][self.KEY_LIST[5]] = value
        if self.KEY_LIST.index(key_name)==6:
            self.status['history'][self.KEY_LIST[6]] = value
        if self.KEY_LIST.index(key_name)==7:
            self.status['history'][self.KEY_LIST[7]] = value

    def save_file(self, file_name : str, file_text : str):
        """
        さきにマークダウンとして保存してからhistoryを保存するとよい
        """
        
        with open("status.json", "w") as f:
            f.write(json.dumps(self.status))
        
        self.save_file_without_history(file_name, file_text)
        # historyの保存
        # raise NotImplementedError

    def save_file_without_history(self, file_name : str, file_text : str):
        with open(file_name, "w") as f:
            f.write(file_text)
