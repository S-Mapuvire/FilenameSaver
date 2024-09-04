# add a clear log button
# allow 'enter' to start the process

import os
import shutil
import sys
from pathlib import Path

from PyQt6.QtGui import QLinearGradient, QIntValidator
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QProgressBar, QScrollArea)

# https://forum.qt.io/topic/85491/changing-the-background-color-of-the-qmainwindow-at-runtime/8

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Backup Maker")
        self.setMinimumSize(600, 600)

        self.container = QWidget(self)
        self.setCentralWidget(self.container)

        self.setup()
        self.styling()

    def setup(self):
        self.Layout = QVBoxLayout(self.container)

        self.header = QLabel("FILENAME BACKUP MAKER")
        self.header.setObjectName('header')
        self.Layout.addWidget(self.header)

        self.path = QLineEdit()
        self.path.setPlaceholderText("Folder destination name?")
        self.Layout.addWidget(self.path)

        self.explainer = QLabel("Copy and paste the folder name from address bar.")
        self.explainer.setObjectName("explainer")
        self.explainer.setWordWrap(True)
        self.Layout.addWidget(self.explainer)

        self.logScroll = QScrollArea()
        self.logScroll.setWidgetResizable(True)
        self.logScroll.setObjectName('logScroll')
        self.Layout.addWidget(self.logScroll)

        self.logArea = QWidget()
        self.logArea.setObjectName('logArea')
        self.logAreaLayout = QVBoxLayout()
        self.logArea.setLayout(self.logAreaLayout)
        self.logScroll.setWidget(self.logArea)

        self.prog_bar = QProgressBar()
        self.prog_bar.setGeometry(50, 100, 50, 30)
        self.prog_bar.setValue(0)
        self.Layout.addWidget(self.prog_bar)

        self.confirm = QPushButton("Confirm")
        self.confirm.setObjectName('confirm2')
        self.confirm.clicked.connect(self._make_backups)
        self.Layout.addWidget(self.confirm)

        self.blankSet = QHBoxLayout()
        self.Layout.addLayout(self.blankSet)

        self.blank1 = QLabel('jf')
        self.blank1.setObjectName('blank1')
        self.blankSet.addWidget(self.blank1)
        
        self.blank2 = QLabel('PP')
        self.blank2.setObjectName('blank2')
        self.blankSet.addWidget(self.blank2)
        
        self.blank3 = QLabel('V5.6')
        self.blank3.setObjectName('blank3')
        self.blankSet.addWidget(self.blank3)
        
        self.blank4 = QLabel('SL')
        self.blank4.setObjectName('blank4')
        self.blankSet.addWidget(self.blank4)
        
        self.blank5 = QLabel('//2197')
        self.blank5.setObjectName('blank5')
        self.blankSet.addWidget(self.blank5)


        self.barCode = QLabel("Made in PyQt6")
        self.barCode.setObjectName('barCode')
        self.Layout.addWidget(self.barCode)
    
    def _runtime(self):
        if self.path.cursorPosition() >= 1:
            print("Cursor is moving!!")
            self.path.setObjectName("activeLineEdit")
            print(self.path.objectName())
        else:
            print("there's nothign here!!")
            

    def styling(self):
        style_sheet = r'C:\Users\Aqua\Mega\Code\==mass file and folder creation tool\style.css'
        with open(style_sheet, 'r') as sheet:
            self.setStyleSheet(sheet.read())

    def _make_backups(self):

        if self.path.cursorPosition() == 0:
            self.errorMessage = QLabel('Error: --No Path Typed In \n -------------------------------------------------------------')
            self.errorMessage.setObjectName('errorMessage')
            self.logAreaLayout.addWidget(self.errorMessage)

            self.prog_bar.setStyleSheet('background-color: red')

        else:
            targetFolder = Path(self.path.text())
            
            if os.path.exists(targetFolder):
                prog_bar_step = 100 // len(os.listdir(targetFolder))
                template = targetFolder / '-1'

                # open to make the file
                with open(template, 'w') as makingTheTemplate:
                    pass
            else:
                print('Targer folder cannot be found')

            self.logMessage = QLabel(f"\nGoing into folder '{targetFolder.name}/ \'...")
            self.logMessage.setObjectName("traversalMessage")
            self.logMessage.setWordWrap(True)
            self.logAreaLayout.addWidget(self.logMessage)

            for originalFilename in targetFolder.iterdir():
                if originalFilename.is_dir():
                    self.logMessage = QLabel(f"Found folder: '{originalFilename.name}/ \'")
                    self.logMessage.setObjectName("logMessage")
                    self.logMessage.setWordWrap(True)
                    self.logAreaLayout.addWidget(self.logMessage)
                    
                    self.path.setText(f"{originalFilename}")
                    self._make_backups()
                else:
                    self.logMessage = QLabel(f"Found file: \'{originalFilename.name}\'")
                    self.logMessage.setObjectName("logMessage")
                    self.logMessage.setWordWrap(True)
                    self.logAreaLayout.addWidget(self.logMessage)
                    if originalFilename.suffix:
                        nameForBackupFile = str.split(str(originalFilename), originalFilename.suffix)
                        backupFilename = Path(nameForBackupFile[0])
                        shutil.copy(template, backupFilename)
                        self._progress_update(prog_bar_step)

            self.logMessage = QLabel(f"Leaving folder '{targetFolder.name}/ \' ...\n -------------------------------------------------------------")
            self.logMessage.setObjectName("traversalMessage")
            self.logMessage.setWordWrap(True)
            self.logAreaLayout.addWidget(self.logMessage)

            os.remove(template)
            self.prog_bar.setValue(100) 
    
    def _progress_update(self, step):
        value = self.prog_bar.value()
        self.prog_bar.setValue(value + step)


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

