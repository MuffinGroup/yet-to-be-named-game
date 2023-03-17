import time

times = time.gmtime()
year = times[0].__str__()
month = times[1].__str__()
day = times[2].__str__()
hour = times[3].__str__()
minutes = times[4].__str__()
seconds = times[5].__str__()
fileName = "run.log"
timeInfo = "<" + hour + ":" + minutes + ":" + seconds + ">"
logContent = ["ee", "eee", "eeeeeeee"]

def log(logMessage, logFile):
    #0 is the year
    #1 is the month
    #2 is the day
    #3 is the hour
    #4 is the minutes
    #5 is the seconds
    pass