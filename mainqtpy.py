import sys
from PyQt4 import QtGui, QtCore

button_size = 90
button_yoffset = 35
normal_font = QtGui.QFont("Arial", 14)
display_width = 1918
display_height = 1010

global sideInt

sideInt = 1

sideBar_width = int(display_width/5)

#colors
white = "background-color: #ffffff"
blue = "background-color: #0000ff"
lightblue = "background-color: #3399ff"
lighterblue = "background-color: #1a75ff"
red = "background-color: #ff0000"
green = "background-color: #00ff00"
grey_90 = "background-color: #909090"
black = "background-color: #000000"

border_style = "; border:1px solid rgb(0, 0, 0)"



class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1, 30, display_width, display_height)
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
        topBar = QtGui.QFrame(self)
        topBar.resize(display_width, button_yoffset)
        topBar.setStyleSheet(grey_90+border_style)

        sideBar = QtGui.QFrame(self)
        sideBar.resize(sideBar_width, display_height-button_yoffset)
        sideBar.move(button_size, button_yoffset)
        sideBar.setStyleSheet(lighterblue+border_style)

        topBar2 = QtGui.QFrame(self)
        topBar2.resize(display_width - sideBar_width - button_size, button_yoffset)
        topBar2.move(sideBar_width + button_size, button_yoffset)

        btn_frame = QtGui.QFrame(self)
        btn_frame.resize(button_size, display_height - button_yoffset)
        btn_frame.move(0, button_yoffset)

        btn_frame.setStyleSheet(lightblue)

        btn_inbox = QtGui.QPushButton("Inbox", self)
        btn_projects = QtGui.QPushButton("Projects", self)
        btn_tags = QtGui.QPushButton("Tags", self)
        btn_forecast = QtGui.QPushButton("Forecast", self)
        btn_flagged = QtGui.QPushButton("Flagged", self)
        btn_review = QtGui.QPushButton("Review", self)

        Buttons = [btn_inbox, btn_projects, btn_tags, btn_forecast, btn_flagged, btn_review]



        # Buttonplacement
        k = 0
        for i in Buttons:
            i.resize(button_size, button_size)
            i.move(0, button_yoffset + k * button_size)
            i.setFont(normal_font)
            if k == sideInt:
                i.setStyleSheet(lighterblue)
                i.resize(button_size + 20, button_size)
            else:
                i.setStyleSheet(lightblue)
            k += 1

        #Button events
        btn_inbox.clicked.connect(lambda: self.setPage(0, Buttons))
        btn_projects.clicked.connect(lambda: self.setPage(1, Buttons))
        btn_tags.clicked.connect(lambda: self.setPage(2, Buttons))
        btn_forecast.clicked.connect(lambda: self.setPage(3, Buttons))
        btn_flagged.clicked.connect(lambda: self.setPage(4, Buttons))
        btn_review.clicked.connect(lambda: self.setPage(5, Buttons))




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
        choice = QtGui.QMessageBox.question(self, "Quit", "Do you really want to Quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def closeEvent(self, event):
        event.ignore()
        self.close_application()


    def setPage(self, site, Buttons):
        k = 0
        for i in Buttons:
            if site == k:
                i.setStyleSheet(lighterblue)
                i.resize(button_size + 20, button_size)
            else:
                i.setStyleSheet(lightblue)
                i.resize(button_size, button_size)
            k += 1
def run():

    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()

