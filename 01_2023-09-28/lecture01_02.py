def lecture01_02(t:tuple, a:list) -> None:
    # kを作成
    k = []
    for elem in t:
        k.append(elem)
    for elem in a:
        k.append(elem)
    
    # kの要素に１を加える
    for i in range(len(k)):
        k[i] += 1
    
    # kを出力
    print(k)
    
    
    # kの最大値を出力
    print(max(k))
    # kの最小値を出力
    print(min(k))
    # kの合計値を出力
    print(sum(k))
    # kの昇順ソート結果を出力
    print(sorted(k))
    

if __name__ == '__main__':
    i=(1,5,8,2)
    j=[10,3,7,4]
    lecture01_02(i, j)
    print(f"関数呼び出し後のに期待されるi=(1,5,8,2)")
    print(f"実際のi={i}")
    print(f"関数呼び出し後に期待されるj=[10,3,7,4]")
    print(f"実際のj={j}")