import sys
from PyQt5.QtWidgets import QAction, QMainWindow, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow): 
    def __init__(self): 
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('img/logo.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl + Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()
        fileMenu = self.menuBar()
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)  
    ex = Example()   
    sys.exit(app.exec_()) 