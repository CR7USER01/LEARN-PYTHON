#normal time
from datetime import datetime

now = datetime.now()
print(now)

#🧠 Where UTC is used

"""Servers
Databases
Logs
APIs
Backend systems

Simple meaning
UTC is the reference clock for the whole world.
All countries compare their time with UTC
UTC never changes with country or season"""

#Final memory sentence
"""
Local time is for humans
UTC is for computers"""


from datetime import datetime, timezone, timedelta
today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)
print(today)
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M:%S'))




