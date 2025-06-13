from datetime import datetime

# Example datetime object
dt = datetime.()

# Lambda to extract date, time, and month name
extract_DTM = lambda d: (d.date(), d.time(), d.strftime("%B"))

# Usage
print(extract_DTM(dt))

