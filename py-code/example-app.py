from PyQt4.QtGui import *
import sys

class Dialog(QDialog):
    def __init__(self, parnet=None):
        QDialog.__init__(self)
        layout = QVBoxLayout()
        hello_label = QLabel("Hello PyMNtos!")
        hello_label.setStyleSheet("font-size: 24pt")        
        
        button = QPushButton("Click Me!")
        button.clicked.connect(self.showMsg)
        button.setStyleSheet("font-size: 18px; padding: 5px 0 5px 0")
        
        layout.addWidget(hello_label)
        layout.addWidget(button)
        self.setLayout(layout)

    def showMsg(self):
        QMessageBox.information(self, "PyMNtos", "Hello from Python!")


app = QApplication(sys.argv)
dialog = Dialog()
dialog.show()
app.exec_()