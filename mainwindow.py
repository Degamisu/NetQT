import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow_ui import Ui_MainWindow  # Import the generated UI module

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        name = self.ui.lineEdit.text()
        self.ui.label.setText(f"Hello, {name}!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
