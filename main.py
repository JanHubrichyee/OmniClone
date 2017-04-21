import datetime, json, os

actions = []
inbox = []
projects = []
tags = []

def saveToFile(list, PATH):
	f = open(PATH, 'w')
	if PATH in ['actions.txt', 'inbox.txt', 'projects.txt']:
		for item in list:
			json_str = json.dumps(item.__dict__)		# convert data to encoded string
			f.write(json_str + '\n')			# write encoded string to .txt
	elif PATH in ['tags.txt']:
		for item in list:
			f.write(item + '\n')
	f.close()

def loadFromFile(PATH):
	list = []
	f = open(PATH, 'r')
	if PATH in ['actions.txt', 'inbox.txt', 'projects.txt']:
		for line in f.readlines():			
			list.append(json.loads(line[0:-1]))		# Load json from file into var
	elif PATH in ['tags.txt']:
		for line in f.readlines():
			list.append(line[0:-1])
	return list
	f.close()

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
		# What about actions without projects?
		self.project = project

def main():
	# load contents into variables
	actions = loadFromFile('actions.txt')
	inbox = loadFromFile('inbox.txt')
	projects = loadFromFile('projects.txt')
	tags = loadFromFile('tags.txt')


	













	# Write to files
	saveToFile(actions, 'actions.txt')
	saveToFile(inbox, 'inbox.txt')
	saveToFile(projects, 'projects.txt')
	saveToFile(tags, 'tags.txt')
	# Create backups periodically 
main()
