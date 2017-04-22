import datetime, json, os
from tkinter import *

root = Tk()								# GUI setup
root.wm_title('OmniClone')
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
			f.write(item + '\n')daaasddasda
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
	top_y = 70							# height of toolbar
	toolbar = Frame(		height = top_y,
					width = screen_width, bd = 0.5,
					relief = RAISED			)
	toolbar.configure(		background = '#e8e8e8'		)

	selector = Frame(		height = screen_height - top_y,
					width = screen_width*1.5/26,
					bd = 0.5,
					relief = RAISED			)
	selector.configure(		background = 'red'		)

	project_list = Frame(		height = screen_height - top_y, 
					width = screen_width*5.5/26,
					bd = 0.5,
					relief = RAISED			)
	project_list.configure(		background = 'orange'		)asdasda

	action_list = Frame(		height = screen_height - top_y,
					width = screen_width*12/26,
					bd = 0.5,
					relief = RAISED			)
	action_list.configure(		background = 'yellow'		)
	#action_list.columnconfigure(2, 	weight = 10			)

	inspector = Frame(		height = screen_height - top_y,
					width = screen_width*7/26,
		 = 0,
					columnspan = 3)
		self.selector.grid(	sticky = 'W')
		self.project_list.grid(	row = 1,
					column = 1)
		self.action_list.grid(	row = 1,
					column = 2)
		self.inspector.grid(	row = 1,
					column = 3)

class Project():
	def __init__(self):
		self.completed = False
		self.title = ''
		self.tags = []
		self.deferUntil = ''asdaskldjasdk
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
('inbox.txt')
	projects = load_from_file('projects.txt')
	tags = load_from_file('tags.txt')

	# Do stuff

	save_to_file(actions, 'actions.txt')				# write to files
	save_to_file(inbox, 'inbox.txt')
	save_to_file(projects, 'projects.txt')
	save_to_file(tags, 'tags.txt')

	# Create backups periodically 
asdaskjdasd
	Application(master = root).mainloop()
	
main()
