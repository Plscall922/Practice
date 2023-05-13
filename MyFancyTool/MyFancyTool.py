from PyQt5 import QtCore, QtGui, QtWidgets
import threading

class MyWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Window')
        self.setWindowOpacity(0.7)

        self.progress_bar = QtWidgets.QProgressBar(self)

        layoutProgress = QtWidgets.QHBoxLayout()
        layoutProgress.addWidget(self.progress_bar)
        layoutProgress.addWidget(self.progress_bar)

        self.start_button = QtWidgets.QPushButton('Start', self)
        self.start_button.clicked.connect(self.someActions)
        self.start_button.clicked.connect(self.start_button)

        self.cancel_button = QtWidgets.QPushButton('Cancel', self)
        self.cancel_button.clicked.connect(QtCore.QCoreApplication.instance().quit)

        layoutButtons = QtWidgets.QVBoxLayout()
        layoutButtons.addWidget(self.start_button)
        layoutButtons.addWidget(self.cancel_button)

        self.setLayout(layoutButtons)

        self.resize(600, 300)

    def someActions(self):
        print('Start button clicked!')

        for i in 10:
            print(i)
            self.progress_bar += i
        return False


app = QtWidgets.QApplication([])

window = MyWindow()

window.show()

app.exec_()



