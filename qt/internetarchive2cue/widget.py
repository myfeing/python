# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

from PySide6.QtCore import (QItemSelection, QLibraryInfo, QLocale, QTranslator)
import rc_internetarchive2cue

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    path = QLibraryInfo.path(QLibraryInfo.TranslationsPath)
    translator = QTranslator(app)
    if translator.load(QLocale.system(), 'qtbase', '_', path):
        print('loaded qtbase')
        app.installTranslator(translator)
    translator = QTranslator(app)
    path = ':/translations'
    if translator.load(QLocale.system(), 'translations\internetarchive2cue', '_', path):
        print('loaded internetarchive2cue')
        app.installTranslator(translator)

    widget = Widget()
    widget.show()
    sys.exit(app.exec())
