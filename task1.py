import time
import uuid  
from queue import Queue

class Request:
  def __init__(self):
    self.req = uuid.uuid4().hex

  def __str__(self):
    return self.req
  

queue = Queue()

def generate_request():
  req = Request()
  queue.put(req)

def process_request():
    if not queue.empty():
        req = queue.get()
        print("Request is processed: ", req)
    else:
        print("Queue is empty.")

while True:
    time.sleep(1)
    generate_request()
    process_request()
