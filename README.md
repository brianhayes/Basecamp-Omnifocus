Basecamp Importer: A simple import action for Omnifocus and Basecampe
============

This is a super simple script that grabs open milestones for a given project and imports them to Omnifocus. It doesn't even attempt to sync.

Installation
----------------

To install run from command line. You may need to use Python's easy_install for some packages.

How to use
----------------

The following need to be set for this script to work. 
Line 8: bc = Basecamp('URL BASECAMP URL', 'USERNAME', 'PASSWORD')
Line 11: theProject = 'PROJECT NAME'
Line 14: xml = bc.list_milestones(PROJECT ID)

You can then run from the command line or my personal favorite set a rule in Alfred App to run on an action. 
 

Notes
----------------

## Version History ##

### 1.0.0 - 2012-04-30 ###
- Initial Release
