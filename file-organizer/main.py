
# "pip install watchdog" to install watchdog dependency
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
import json

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for file_name in os.listdir(tracked_dir):
            file_src = tracked_dir + "/" + file_name
            extension = os.path.splitext(file_src)[1]
            dest_dir = get_dst_by_ext(extension)
            if not os.path.exists(root_dest_dir +"/" + dest_dir):
                os.makedirs(root_dest_dir +"/" + dest_dir)
            file_dst = root_dest_dir +"/" + dest_dir + "/"+ str(time.time()) + "_" + file_name
            os.rename(file_src, file_dst)

def get_dst_by_ext(extension):
    if extension == "":
        return "folders"
    for key in extensions:
        for ext in extensions[key]:
            if ext == extension:
               return key
    return "other"

tracked_dir = "C:/Users/Abdo/Downloads"
root_dest_dir = "C:/Users/Abdo/Sorted_Downloads"

extensions = {
  "images": [".png", ".jpg", ".jpeg", ".gif", "tiff"],
  "videos": [".avi", ".wmv", ".mp4"],
  "archives": [".zip", ".rar", ".7z", ".tar", ".jar"],
  "documents": [".pdf", ".docx", ".txt"],
  "executables": [".exe", ".msi"]
}

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