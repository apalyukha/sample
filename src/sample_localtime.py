import time

# Read current time in seconds
curTime = time.time()

# Read data and time values using localtime()
localTime = time.localtime(curTime)

# Print the output of the localtime()
print("The output of localtime() is :\n", localTime)

# Define the list of months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

# Define the list of week days
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print("\nThe formatted outputs are given below:")

# Print the current date
print("\nDate :", localTime.tm_mday, months[localTime.tm_mon - 1], localTime.tm_year)

# Print the current time
print("\nTime : %dh:%dm:%ds" % (localTime.tm_hour, localTime.tm_min, localTime.tm_sec))

# Print the current weekday name
print("\nToday is ", weekdays[localTime.tm_wday])

# Print the day of the year
print("\nToday is %d days of the year" % localTime.tm_yday)
