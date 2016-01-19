## Written by Sonia Hu
## Last modified: Jan 6, 2016
## NEXT STEPS: Add functionality for a list of courses
import json
import urllib2
import time
import ctypes

## Constants
url = 'https://api.uwaterloo.ca/v2/courses'
gTerm = 1159      #The number for the desired term
gKey = '063082f318c211babaf6c579c69c3323'  #the API key
minpertry = 20    #number of minutes between attempts;
                  #note that the API key has a use limit of 25000 per month
secs_per_min = 60;
tries = 0;  #number of attemps made so far
success = False;  #set to true when any course is open

# api search takes in sCourse, an integer,
# sTerm, a 4-digit integer, and sKey, an API key,
# and determines if the course is open.
def apiSearch(sCourse,sTerm,sKey):
    jsonLink = url + '/' + str(sCourse) + '/' + 'schedule.json'
    query = jsonLink + '?term=' + str(sTerm) + '&key=' + sKey
    data = json.load(urllib2.urlopen(query))
    
    # retrieved data
    title = data['data'][0]['title']
    coursetitle = data['data'][0]['subject'] + ' ' + data['data'][0]['catalog_number']
    enrolCap = data['data'][0]['enrollment_capacity']
    enrolTot = data['data'][0]['enrollment_total']
    lastUpdate = data['data'][0]['last_updated']
    instructor = data['data'][0]['classes'][0]['instructors'][0]
    
    print coursetitle + ' - ' + instructor + ' // last updated: ' + lastUpdate
    print "Currently at: " + str(enrolTot) + "/" + str(enrolCap)
    
    # success: course is open
    if enrolTot < enrolCap:
        text = ''
        text += 'Class : ' + course + '\n'
        text += 'Enrolment Cap : ' + str(enrolCap) + '\n'
        text += 'Enrolment Total : ' + str(enrolTot) + '\n'
        text += 'Instructor : ' + str(instructor)
        print text
        print '\7\7\7'
        successtext = data['data'][0]['subject'] + " " + data['data'][0]['catalog_number']
        ctypes.windll.user32.MessageBoxW(0, text, u'A COURSE IS AVAILABLE', 0)
        success = True;

# main loop
while True:
    tries += 1;
    print "Tries : " + str(tries)
    for i in range(0, len(courseList)):
        apiSearch(courselist[i],gTerm,gKey);
    if (success == True):
        break;
    else:
        print "\n>> Trying again in " + str(minpertry) + " minutes.\n"
        time.sleep(minpertry*secs_per_min);

    

