import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget

def dialog_test():
    file,check = QtWidgets.QFileDialog.getOpenFileName(None,"ファイルを選択してください。","","All Files (*);;Python Files (*.py);;Text Files (*.txt)")

    if check:
        print(file)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_widget = QWidget()
    main_widget.resize(300,300)
    main_widget.setWindowTitle('ファイルダイアログ')

    button = QtWidgets.QPushButton(main_widget)
    button.setText("ファイルを選択する")
    button.clicked.connect(dialog_test)
    button.move(50,50)

    main_widget.show()
    sys.exit(app.exec())
