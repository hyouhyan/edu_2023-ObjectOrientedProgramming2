from http.server import BaseHTTPRequestHandler, HTTPServer  # モジュールのインポート


# BaseHTTPRequestHandlerを継承した自作クラスの定義
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self): # 親クラスの機能をオーバーライド

        # Responseのステータスコード設定（正常にレスポンスを返すので200 OKとする）
        self.send_response(200)
        # ResponseHeaderのContent-type設定
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        # ResponseHeader終端処理
        self.end_headers()

        # Responseコンテンツの構築
        self.wfile.write('<html>Hello, World!! (from GET)</html>'.encode())

    def do_POST(self): # 親クラスの機能をオーバーライド
        return self.do_GET() # GETと同じ処理を通過させる


if __name__ == '__main__':
    # サーバーアドレスの定義
    address = ('localhost', 8888)

    # 自作クラスの呼び出し
    with HTTPServer(address, MyHTTPRequestHandler) as server:
        server.serve_forever()