
from datetime import datetime

date_str1 = input("Enter the first date in YYYY-MM-DD HH:MM:SS format: ")
date_str2 = input("Enter the second date in YYYY-MM-DD HH:MM:SS format: ")

date1 = datetime.strptime(date_str1, '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(date_str2, '%Y-%m-%d %H:%M:%S')

diff_seconds = abs((date2 - date1).total_seconds())

print("The difference between the two dates is", diff_seconds, "seconds.")
