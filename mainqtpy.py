import sys
from PyQt4 import QtGui, QtCore

button_size = 90
button_yoffset = 0
normal_font = QtGui.QFont("Arial", 14)

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1, 30, 1918, 1010)
        self.setWindowTitle("OmniClone")
        self.setWindowIcon(QtGui.QIcon("Icon.ico"))

        ##MenuBar
        '''
        extractAction = QtGui.QAction("&Quit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave The App")
        extractAction.triggered.connect(lambda: self.close_application())

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)
        '''
        ##MenuBar

        self.home()

    def home(self):
        btn_inbox = QtGui.QPushButton("Inbox", self)
        btn_projects = QtGui.QPushButton("Projects", self)
        btn_tags = QtGui.QPushButton("Tags", self)
        btn_forecast = QtGui.QPushButton("Forecast", self)
        btn_flagged = QtGui.QPushButton("Flagged", self)
        btn_review = QtGui.QPushButton("Review", self)

        Buttons = [btn_inbox, btn_projects, btn_tags, btn_forecast, btn_flagged, btn_review]

        #Button events
        btn_inbox.clicked.connect(lambda: self.close_application())
        btn_projects.clicked.connect(lambda: self.close_application())
        btn_tags.clicked.connect(lambda: self.close_application())
        btn_forecast.clicked.connect(lambda: self.close_application())
        btn_flagged.clicked.connect(lambda: self.close_application())
        btn_review.clicked.connect(lambda: self.close_application())

        #Buttonplacement
        k = 0
        for i in Buttons:
            i.resize(button_size,button_size)
            i.move(0,button_yoffset+k*button_size)
            i.setFont(normal_font)
            k+=1


        ##ToolBar
        '''
        extractAction = QtGui.QAction(QtGui.QIcon("Icon.ico"), "Quit", self)
        extractAction.triggered.connect(lambda: self.close_application())

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)
        '''
        ##ToolBar

        self.show()

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Quit", "Do you really want two penises?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def closeEvent(self, event):
        event.ignore()
        self.close_application()


def run():

    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()