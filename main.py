from PySide6 import QtWidgets

from translator.generator import PostfixGenerator
from PySide6.QtWidgets import QMainWindow, QApplication, QButtonGroup, QFileDialog, QMessageBox
import sys

from translator.recursive_descent import RecursiveDescent
from ui_main import Ui_MainWindow
from pathlib import Path

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

        self.original_file_path = ""
        self.ir_file_path = ""

    def init_ui(self):
        self.btnOpenOriginal.clicked.connect(self.select_original_file)
        self.btnSaveOriginal.clicked.connect(self.save_original_file)
        self.btnOpenIR.clicked.connect(self.select_ir_file)
        self.btnDisassemble.clicked.connect(self.disassemble)
        self.btnGenerate.clicked.connect(self.generate)
        self.btnSavePascal.clicked.connect(self.save_pascal_file)

    def select_original_file(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if dialog.exec():
            directory = dialog.selectedFiles()[0]
            self.original_file_path = Path(directory)
            self.labelSelectedOriginalFile.setText(f"Выбранный файл: {str(self.original_file_path.name)}")
            with open(self.original_file_path, "r") as f:
                self.plainTextOriginal.setPlainText(f.read())

    def save_original_file(self):
        with open(self.original_file_path, "w") as f:
            f.write(self.plainTextOriginal.toPlainText())

    def select_ir_file(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if dialog.exec():
            directory = dialog.selectedFiles()[0]
            self.ir_file_path = Path(directory)
            self.labelSelectedIRFile.setText(f"Выбранный файл: {str(self.ir_file_path.name)}")
            with open(self.ir_file_path, "r") as f:
                self.plainTextIR.setPlainText(f.read())

    def save_pascal_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                            "Save File", "", "All Files(*);;Text Files(*.txt)",
                                                            options=options)
        if fileName:
            with open(fileName, 'w') as f:
                f.write(self.plainTextEditPascal.toPlainText())

    def disassemble(self):
        recursive = RecursiveDescent(self.original_file_path)
        postfix_notation, ok = recursive.disassemble()
        postfix_notation = " ".join(postfix_notation)
        if ok:
            self.plainTextIR.setPlainText(postfix_notation)

            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                "Save File", "", "All Files(*);;Text Files(*.txt)",
                                                                options=options)
            if fileName:
                with open(fileName, 'w') as f:
                    f.write(postfix_notation)
                self.ir_file_path = Path(fileName)
                self.labelSelectedIRFile.setText(f"Выбранный файл: {self.ir_file_path.name}")
        else:
            button = QMessageBox.critical(
                self,
                "Ошибка!",
                "Файл семантически неверен",
                defaultButton=QMessageBox.Ok,
            )

    def generate(self):
        postfix_notation = self.plainTextIR.toPlainText()
        generator = PostfixGenerator(postfix_notation)
        pascal, _ = generator.generate(0)
        self.plainTextEditPascal.setPlainText(pascal)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()