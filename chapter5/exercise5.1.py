import time

timenow = time.time()

print (time.localtime(timenow))

seconds = int(timenow % 60)
timenow = timenow // 60

minutes = timenow % 60
timenow = timenow // 60

hours = timenow % 24
timenow = timenow // 24

days = int(timenow % 365.2425)


print ("day {0} - hours {1} - minutes {2} - seconds {3} ".format(days, hours, minutes, seconds))