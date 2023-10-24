from datetime import datetime

date1 = datetime(2023, 10, 19, 17, 17, 30)
date2 = datetime(2023, 10, 19, 17, 17, 10)

time_difference = (date2 - date1).total_seconds()

print(abs(time_difference))
