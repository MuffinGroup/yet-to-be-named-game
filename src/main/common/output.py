import time

def log(logMessage):
    now = time.gmtime()
    hour = now[3].__str__()
    minutes = now[4].__str__()
    seconds = now[5].__str__()
    #0 is the year
    #1 is the month
    #2 is the day
    #3 is the hour
    #4 is the minutes
    #5 is the seconds
    print("<" + hour + ":" + minutes + ":" + seconds + ">" + " " + logMessage)
    #Reminder: Make it output to the log
    open()