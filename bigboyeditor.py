from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QVBoxLayout,
    QMenu,
    QAction,
    QFileDialog,
    QWidget
)
from PyQt5.QtGui import QIcon  # Import QIcon for icons

import random #random

#random titles
titles = [
    "big boy editor",
    "big booty editor",
    "big boy editor | helo worlt",
    "big boy editor | save changes to untitled?",
    "big boy editor | welcome",
]

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.editor = QTextEdit()

        # Create a layout and add the text edit widget
        layout = QVBoxLayout()
        layout.addWidget(self.editor)

        # Create a menu bar
        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu("&File")

        # Create actions for saving and loading files
        self.saveAction = QAction(QIcon("save.png"), "&Save", self)  # Add icon (optional)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save_file)

        self.loadAction = QAction(QIcon("open.png"), "&Open", self)  # Add icon (optional)
        self.loadAction.setShortcut("Ctrl+O")
        self.loadAction.triggered.connect(self.load_file)

        # Add actions to the menu
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.loadAction)

        # Set central widget and window title (optional central widget)
        self.setCentralWidget(QWidget())  # Optional central widget
        self.centralWidget().setLayout(layout)
        self.setWindowTitle(random.choice(titles))

        self.filename = None  # Track the currently loaded file

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.editor.toPlainText())
        else:
            # Optionally prompt for a filename if none is set
            filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text files (*.txt)")
            if filename:
                self.filename = filename
                with open(filename, "w") as f:
                    f.write(self.editor.toPlainText())

    def load_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text files (*.txt)")
        if filename:
            with open(filename, "r") as f:
                text = f.read()
                self.editor.setPlainText(text)
                self.filename = filename

    def get_save_filename(self): 
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text files (*.txt)")
        return filename

if __name__ == "__main__":
    app = QApplication([])
    editor = TextEditor()
    editor.show()
    app.exec_()
