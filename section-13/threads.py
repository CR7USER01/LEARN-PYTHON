"""🧵 What is a Thread in Python?
A thread is a small unit of execution inside a program.
It allows your program to do multiple tasks at the same time (kind of)."""
#-----------------------------------------------


"""Does "creating a thread" mean creating memory?

👉 No. Not separate memory.
When we create a thread:

It does NOT create new memory like a process.
It shares the same memory of the program.
It only creates a new execution path (a new worker).
    
"""
#--------------------------------------------------
"""🚀 What is ThreadPoolExecutor in Python?

It is a tool from:
from concurrent.futures import ThreadPoolExecutor

It helps you:
Run multiple tasks using threads easily (without managing threads manually).
"""


#--------------------------------------------

#  Thread pool

"""_summary_You have 3 workers (threads).

Tasks arrive:

Download file 1

Download file 2

Download file 3

Download file 4

Workers take tasks one by one from the queue.
You don’t manually assign.
That is Thread Pool.
 """

