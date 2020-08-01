
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
import json


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for file_name in os.listdir(tracked_dir):
            file_src = tracked_dir + "/" + file_name
            file_dst = dest_dir + "/"+ str(time.time()) + "_" + file_name
            os.rename(file_src, file_dst)

tracked_dir = "C:/Users/Abdo/Downloads"
dest_dir = "C:/Users/Abdo/Sorted_Downloads"

event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, tracked_dir, recursive=True)

try:
    observer.start()
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()