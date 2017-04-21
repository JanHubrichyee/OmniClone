import datetime, json, os
from tkinter import *

root = Tk()								# GUI setup
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (screen_width, screen_height))		# go fullscreen

def save_to_file(list, PATH):
	f = open(PATH, 'w')
	if PATH in ['actions.txt', 'inbox.txt', 'projects.txt']:
		for item in list:
			json_str = json.dumps(item.__dict__)		# convert data to encoded string
			f.write(json_str + '\n')			# write encoded string to .txt
	elif PATH in ['tags.txt']:
		for item in list:
			f.write(item + '\n')
	f.close()

def load_from_file(PATH):
	list = []
	f = open(PATH, 'r')
	if PATH in ['actions.txt', 'inbox.txt', 'projects.txt']:
		for line in f.readlines():			
			list.append(json.loads(line[0:-1]))		# load json from file into var
	elif PATH in ['tags.txt']:
		for line in f.readlines():
			list.append(line[0:-1])
	return list
	f.close()

class Application(Frame):

	def __init__(self, master = None):
		super().__init__(master)
		self.create_widgets()
	def create_widgets(self):
		self.inbox_button = Button(self, text = 'Inbox')
		self.inbox_button.grid(row = 5, column = 5)
		self.l1 = Label(root, text = 'name')
		self.l2 = Label(root, text = 'password')
		self.e1 = Entry(root)
		self.e2 = Entry(root)
		self.l1.grid(row = 0, column = 0)
		self.l2.grid(row = 1, column = 0)
		self.e1.grid(row = 0, column = 1)
		self.e2.grid(row = 1, column = 1)



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
		# Initialize displayNr (append as last item in displayed list)

class Action(Project):
	def __init__(self, project):
		super(Action, self).__init__()
		# What about actions without projects?
		self.project = project

def main():
	actions = load_from_file('actions.txt')				# load contents into variables
	inbox = load_from_file('inbox.txt')
	projects = load_from_file('projects.txt')
	tags = load_from_file('tags.txt')

	# Do stuff

	save_to_file(actions, 'actions.txt')				# write to files
	save_to_file(inbox, 'inbox.txt')
	save_to_file(projects, 'projects.txt')
	save_to_file(tags, 'tags.txt')

	# Create backups periodically 

	Application(master = root).mainloop()
main()
