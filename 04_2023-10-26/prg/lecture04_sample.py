#!/usr/bin/env python

import sys

class GameButton():
    def __init__(self, status):
        self.status = status
        self.text = ""

    def set_buttons(self, buttons):
        self.buttons = buttons

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def click(self):
        # import pdb; pdb.set_trace()
        if len(self.getText()) == 0:
            self.setText(self.status["text"])
            self.__check_win()
            if self.status["text"] == "○":
                self.status["text"] = "×"
            else:
                self.status["text"] = "○"

    def __check_win(self):
        my_index = self.buttons.index(self)
        print(my_index)

        patterns = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]

        btns : list[GameButton] = [self.buttons[i] for i in patterns[0]]
        result = [btn.getText() for btn in btns]
        if result[0] == result[1] == result[2] == "○":
            print("○の勝ち")
            #[btn.setStyleSheet("color : #ff0000;") for btn in btns]
            #色は変えられないので特別課題では不問(．．．の勝ちと出力されればOKとする)


class MainWidget():
    def __init__(self):
        self.game_status={}
        self.game_status["text"]="○"
        self.buttons = [GameButton(self.game_status) for _ in range(9)]
        [btn.set_buttons(self.buttons) for btn in self.buttons]

    def click(self, i, j):
        self.buttons[i*3+j].click()

    def __str__(self):
        texts = [btn.getText() for btn in self.buttons]
        texts = [t if len(t)>0 else "." for t in texts]
        return f"{texts[0]}{texts[1]}{texts[2]}\n{texts[3]}{texts[4]}{texts[5]}\n{texts[6]}{texts[7]}{texts[8]}"

if __name__ == "__main__":
    mw = MainWidget()
    print(mw)
    print("終了方法はCtrl+c")
    print("入力するマスの数字を入力(例: 0,0)")
    for line in sys.stdin:
        print("--> " + line)
        mw.click(*[int(x) for x in line.split(',')])
        print(mw)
        print("入力するマスの数字を入力(例: 0,0)")

# 以下出力例
"""
...
...
...
終了方法はCtrl+c
入力するマスの数字を入力(例: 0,0)
1,1
--> 1,1

4
...
.○.
...
入力するマスの数字を入力(例: 0,0)
1,0
--> 1,0

3
...
×○.
...
入力するマスの数字を入力(例: 0,0)
0,0
--> 0,0

0
○..
×○.
...
入力するマスの数字を入力(例: 0,0)
2,2
--> 2,2

8
○..
×○.
..×
入力するマスの数字を入力(例: 0,0)
0,1
--> 0,1

1
○○.
×○.
..×
入力するマスの数字を入力(例: 0,0)
2,0
--> 2,0

6
○○.
×○.
×.×
入力するマスの数字を入力(例: 0,0)
0,2
--> 0,2

2
○の勝ち
○○○
×○.
×.×
入力するマスの数字を入力(例: 0,0)
"""