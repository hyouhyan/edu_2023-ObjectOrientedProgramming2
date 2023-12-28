def lecture01_01() -> None:
    h={}
    h["ID"] = "k22047"
    h["attributes"] = ("横永 一斗", 22, "男")
    
    # hをprint関数で出力せよ．
    print(h)
    
    # hのキー一覧をprint関数で出力せよ．
    print(h.keys())
    
    # h.keys()で取得したオブジェクトの型をprint関数で出力せよ
    print(type(h.keys()))
    
    # h[“attributes”]の型をprint関数で出力せよ．
    print(type(h["attributes"]))
    
    # h[“attributes”]の各要素を１行づつprint関数で出力せよ．
    for elem in h["attributes"]:
        print(elem)
    
    # h[“attributes”]の各要素の型を１行づつprint関数で出力せよ．
    for elem in h["attributes"]:
        print(type(elem))


if __name__ == '__main__':
    lecture01_01()