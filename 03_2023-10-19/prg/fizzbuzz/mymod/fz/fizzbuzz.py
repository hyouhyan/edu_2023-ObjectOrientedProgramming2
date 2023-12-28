def _logic(num):
    """ fizzbuzzの内部処理をするメソッド
    アンダーバー1個は同じファイル内からのみ呼び出すという宣言
    """
    if num%15 == 0:
        return "FizzBuzz"
    elif num%3 == 0:
        return "Fizz"
    elif num%5 == 0:
        return "Buzz"
    else:
        return str(num)

def fizzbuzz(max_count: int) -> None:
    """ fizzbuzz関数はmax_count回結果を出力します

    parameters
    ----
    max_count: int
        出力回数を指定
    """

    for i in range(max_count):
        print(_logic(i+1))

if __name__ == '__main__':
    val=15
    expected = "FizzBuzz"
    if(_logic(val) == expected):
        print(f"_logic returns '{expected}'")
    else:
        print(f"_logic returns the invalid result({val})")
    val=5
    expected = "Buzz"
    if(_logic(val) == expected):
        print(f"_logic returns '{expected}'")
    else:
        print(f"_logic returns the invalid result({val})")
    val=3
    expected = "Fizz"
    if(_logic(val) == expected):
        print(f"_logic returns '{expected}'")
    else:
        print(f"_logic returns the invalid result({val})")
    val=2
    expected = "2"
    if(_logic(val) == expected):
        print(f"_logic returns '{expected}'")
    else:
        print(f"_logic returns the invalid result({val})")