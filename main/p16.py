import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        lb11 = QLabel('Zetcode', self)
        lb11.move(15, 10)
        lb12 = QLabel('tutorials', self)
        lb12.move(15, 40)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  
    ex = Example()   
    sys.exit(app.exec_()) 
        