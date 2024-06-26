from FizzBuzzBase import FizzBuzzBase

# FizzBuzzクラスのコンストラクタからsuperを使ってFizzBuzzBaseクラスのコンストラクタを呼び出す
class FizzBuzz(FizzBuzzBase):
    def __init__(self, max_count=...):
        super().__init__(max_count)
        # ここ何も書かんくていいんかな？
        # とりあえず、何も書かずにやってみる
    
    def __convert(self, input: int) -> str:
        if(input % 3 == 0 and input % 5 == 0):
            rtn = "FizzBuzz"
        elif(input % 3 == 0):
            rtn = "Fizz"
        elif(input % 5 == 0):
            rtn = "Buzz"
        else:
            rtn = str(input)
        
        return rtn

    def print_fizzbuzz(self, max_count: int) -> None:
        number_list = list(range(1, max_count + 1))
        for i in number_list:
            print(self.__convert(i))

if __name__ == '__main__':
    FizzBuzz(20)