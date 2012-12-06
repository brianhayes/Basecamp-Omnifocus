#!/usr/bin/python 

from subprocess import Popen, PIPE
import elementtree.ElementTree as ET
from basecamp import Basecamp

# Prepare the interaction with Basecamp.
bc = Basecamp('URL BASECAMP URL', 'USERNAME', 'PASSWORD')

# Set project name for Omnifocus
theProject = 'PROJECT NAME'

# Get list of milestones
xml = bc.list_milestones(PROJECT ID)

# print milestones
items = ET.fromstring(xml).findall('milestone')

theTask = {}

# Let's use the ElementTree API to access data via path expressions:
for item in items:
	if item.find("completed").text == 'false':
		#convert date to applescript friendly format
		strDate = item.find("deadline").text
		listDate = strDate.split('-')
		asDate = listDate[1]+'/'+listDate[2]+'/'+listDate[0]+' 09:00:00 AM'

		# print item.find("title").text, item.find("deadline").text
		scpt = '''
			on run {x,y,z}
			set todoName to x 
			set projectName to z
		    
			    tell application "OmniFocus"
					tell default document
						if project projectName exists then
							set projectName to project projectName
						else
							set projectName to make new project with properties {name:projectName}
						end if
					end tell
				end tell
				
				set strDate to y
				set todoDate to date strDate
			    
			    tell application "OmniFocus"
					tell projectName
						set newTask to make new task with properties {name:todoName, containing project:projectName, due date:todoDate}
					end tell
				end tell
				
		    
			end run'''
		
		args = [item.find('title').text, asDate, theProject]
		
		p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		stdout, stderr = p.communicate(scpt)
		print (p.returncode, stdout, stderr)