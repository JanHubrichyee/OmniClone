#!/usr/local/bin/python\ 3.6
import datetime, json, os, random, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Gui options
app = QApplication(sys.argv)

def save_to_file(list, PATH):
	f = open(PATH, 'w')
	if PATH in ['actions.txt', 'inbox.txt', 'projects.txt']:
		for item in list:
			json_str = json.dumps(item.__dict__)			# convert data to encoded string
			f.write(json_str + '\n')				# write encoded string to .txt
	elif PATH in ['tags.txt']:
		for item in list:
			f.write(item + '\n')
	f.close()

def load_from_file(PATH):
	list = []
	f = open(PATH, 'r')
	if PATH in ['actions.txt', 'inbox.txt', 'projects.txt']:
		for line in f.readlines():			
			list.append(json.loads(line[0:-1]))			# load json from file into var
	elif PATH in ['tags.txt']:
		for line in f.readlines():
			list.append(line[0:-1])
	f.close()
	return list

class Window(QMainWindow):
	def __init__(self, mode):
		super(Window, self).__init__()
		self.screen_size = QSize()
		self.screen_size.setWidth(3600)
		self.screen_size.setHeight(1800)
		#-self.setWindowIcon(GtGui.QIcon('pythonlogo.png'))
		self.win = QDialog()
		self.win.setGeometry(0, 0, self.screen_size.width(), self.screen_size.height())
		self.win.setWindowTitle('OmniClone')	
		#-make size constant throughout all display sizes/formats	
		self.display(mode)
		sys.exit(app.exec_())
	
	def bCalendarClicked(self):
		pass
	def bInboxClicked(self):
		print('click')
	def bFlaggedClicked(self):
		pass
	def bForecastClicked(self):
		pass
	def bProjectsClicked(self):
		pass
	def bReviewClicked(self):
		pass
	def bTagsClicked(self):
		pass

	def display(self, mode):
		# Widget Instantiation+Arrangement
		gwindow = QGridLayout()
		self.actionList = QFrame(self.win)
		self.calendar = QFrame(self.win)
		self.inspectorCal = QFrame(self.win)
		self.inspectorRem = QFrame(self.win)
		self.projectList = QFrame(self.win)
		self.selector = QFrame(self.win)	
		self.toolbar = QFrame(self.win)
		gwindow.addWidget(self.toolbar, 0, 0, 1, 34)
		gwindow.addWidget(self.selector, 2, 0, 18, 2)
		
		self.bCalendar = QPushButton(self.selector)
		self.bFlagged = QPushButton(self.selector)
		self.bInbox = QPushButton(self.selector)
		self.bProjects = QPushButton(self.selector)
		self.bReview = QPushButton(self.selector)
		self.bTags = QPushButton(self.selector)
		
		self.bCalendar.clicked.connect(self.bCalendarClicked)
		self.bInbox.clicked.connect(self.bInboxClicked)
		self.bProjects.clicked.connect(self.bProjectsClicked)
		self.bTags.clicked.connect(self.bTagsClicked)
		self.bFlagged.clicked.connect(self.bFlaggedClicked)
		self.bReview.clicked.connect(self.bReviewClicked)

		# Widget Stylesheets
		bc = '#c5c9c7'
		self.actionList.setStyleSheet('background-color : ' + bc)
		self.calendar.setStyleSheet('background-color : ' + bc)
		self.inspectorCal.setStyleSheet('background-color : ' + bc)
		self.inspectorRem.setStyleSheet('background-color : ' + bc)
		self.projectList.setStyleSheet('background-color : ' + bc)
		self.selector.setStyleSheet('background-color : ' + bc)
		self.toolbar.setStyleSheet('background-color : ' + bc)
		for w in [self.actionList, self.calendar, self.inspectorCal, self.inspectorRem, self.projectList, self.selector, self.toolbar]:
			w.setLineWidth(3)

		# Button Styles
		self.Buttons = [self.bCalendar, self.bFlagged, self.bInbox, self.bProjects, self.bReview, self.bTags]
		self.swidth = self.selector.frameGeometry().width()
		self.sheight = self.selector.frameGeometry().height()
		i = 0
		for b in self.Buttons:
			b.resize(self.swidth + self.sheight*2, self.swidth + self.sheight*2)
			b.move(0, (self.swidth + self.sheight*2)*i)
			i += 1
		
		# Displaying main section
		if mode == 'calendar':
			gwindow.addWidget(self.calendar, 2, 2, 18, 25)
			gwindow.addWidget(self.inspectorCal, 2, 27, 18, 7)

		elif mode in ['inbox', 'forecast', 'projects', 'review', 'tags']:
			gwindow.addWidget(self.projectList, 2, 2, 18, 8)
			gwindow.addWidget(self.actionList, 2, 10, 18, 17)
			gwindow.addWidget(self.inspectorRem, 2, 27, 18, 7)
			if mode == 'inbox':
				pass
			elif mode == 'forecast':
				pass
			elif mode == 'projects':
				pass
			elif mode == 'review':
				pass
			elif mode == 'tags':
				pass

		self.win.setLayout(gwindow)
		self.win.show()

	'''def createWidgets(self):
		self.BoxSelector = QVBoxLayout()
		self.BoxSelector.addWidget(self.bInbox)
		self.BoxSelector.addWidget(self.bProjects)
		self.BoxSelector.addWidget(self.bTags)
		self.BoxSelector.addWidget(self.bFlagged)
		self.BoxSelector.addWidget(self.bReview)
		self.selector.setLayout(self.BoxSelector)

		self.vbox = QVBoxLayout()
		self.hbox = QHBoxLayout()

		self.vbox.addWidget(self.toolbar)
		self.vbox.addWidget(self.main)
		self.hbox.addWidget(self.selector)
		self.hbox.addWidget(self.project_list)
		self.hbox.addWidget(self.action_list)
		self.hbox.addWidget(self.inspector)

		self.toolbar.resize(self.getSize(self.toolbar)[0], 20)
		self.main.resize(self.getSize(self.main)[0], self.window_height - self.getSize(self.toolbar)[1])

		self.win.setLayout(self.vbox)
		self.main.setLayout(self.hbox)
		
		self.b1 = QPushButton(self.inspector)
		self.b1.setText('Sooßen')
		self.b1.move(150, 150)

	def b1_clicked():
			r1 = random.randint(0, 100)
			r2 = random.randint(0, 100)
			self.b1.move(r1, r2)
	
		self.b1.clicked.connect(lambda: b1_clicked())
	'''

class Project():
	def __init__(self):
		self.completed = False
		self.title = ''
		self.tags = []
		self.deferUntil = ''
		self.due = ''
		self.estTime = ''
		self.comment = ''
		self.flagged = False
		self.dateAdded = ''
		self.dateChanged = ''
		# Repeat settings
		# Review settings
		# initialize displayNr (append as last item in displayed list)

class Action(Project):
	def __init__(self, project):
		super(Action, self).__init__()
		# actions without projects have inbox as their project
		self.project = project

actions = load_from_file('actions.txt')					# load contents into variables
inbox = load_from_file('inbox.txt')
projects = load_from_file('projects.txt')
tags = load_from_file('tags.txt')

GUI = Window('projects')

#-do stuff

save_to_file(actions, 'actions.txt')					# write to files
save_to_file(inbox, 'inbox.txt')
save_to_file(projects, 'projects.txt')
save_to_file(tags, 'tags.txt')

#-create backups periodically 
