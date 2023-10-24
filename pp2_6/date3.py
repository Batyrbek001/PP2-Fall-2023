from datetime import datetime

date_with_microseconds = datetime.now()

date_without_microseconds = date_with_microseconds.replace(microsecond=0)

print(date_with_microseconds)
print(date_without_microseconds)