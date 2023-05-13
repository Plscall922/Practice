from PyQt5 import QtCore, QtWidgets


class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.progress = 0

    @QtCore.pyqtSlot()
    def do_work(self):
        while self.progress < 100:
            self.progress += 1
            print(self.progress)
            QtCore.QThread.msleep(100)
        self.finished.emit()


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Window')
        self.setWindowOpacity(0.7)

        # start button
        self.start_button = QtWidgets.QPushButton('Start Boop', self)
        self.start_button.clicked.connect(self.start_action)

        # cancel button
        self.cancel_button = QtWidgets.QPushButton('Cancel Boop', self)
        self.cancel_button.clicked.connect(self.cancel_action)

        # create a progress bar
        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setFormat('Progress: %p%')

        self.progress_bar.setStyleSheet("""
            QProgressBar {
                text-align: center;
                border: 1px solid black;
                border-radius: 5px;
            }
            QProgressBar::chunk {
                background-color: #37c5ff;
                width: 10px;
                margin: 0.5px;
            }
        """)

        layout_buttons = QtWidgets.QVBoxLayout()
        layout_buttons.addWidget(self.start_button)
        layout_buttons.addWidget(self.cancel_button)
        layout_buttons.addWidget(self.progress_bar)

        self.setLayout(layout_buttons)
        self.resize(600, 200)

        self.worker = None

    def start_action(self):
        if not self.worker:
            self.worker = Worker()
            self.worker.finished.connect(self.action_finished)

            thread = QtCore.QThread(self)
            self.worker.moveToThread(thread)

            thread.started.connect(self.worker.do_work)
            thread.finished.connect(thread.deleteLater)

            self.start_button.setEnabled(False)
            thread.start()

    def cancel_action(self):

        if self.worker:
            self.worker.finished.disconnect(self.action_finished)
            self.worker.finished.emit()
            self.worker = None
            self.start_button.setEnabled(True)

    def action_finished(self):
        print("You are Booped")
        self.cancel_action()


app = QtWidgets.QApplication([])

window = MyWindow()
window.show()

app.exec_()