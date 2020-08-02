
# "pip install watchdog" to install watchdog dependency
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
import threading


class Handler(FileSystemEventHandler):
    def __init__(self, tracked_dir, root_dest_dir):
        self.tracked_dir = tracked_dir
        self.root_dest_dir = root_dest_dir

    def on_modified(self, event):
        for file_name in os.listdir(self.tracked_dir):
            file_src = self.tracked_dir + "/" + file_name
            fname = os.path.splitext(file_name)
            dest_dir = self.root_dest_dir + "/" + get_dst_by_ext(fname[1])
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            new_file_name = fname[0] + "_" + \
                str(time.time()).replace(".", "") + fname[1]
            file_dst = dest_dir + "/" + new_file_name
            os.rename(file_src, file_dst)


def get_dst_by_ext(extension):
    if extension == "":
        return "folders"
    for key in extensions:
        for ext in extensions[key]:
            if ext == extension:
                return key
    return "other"


extensions = {
    "images": [".png", ".jpg", ".jpeg", ".gif", "tiff"],
    "videos": [".avi", ".wmv", ".mp4"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".jar"],
    "documents": [".pdf", ".docx", ".txt"],
    "executables": [".exe", ".msi"]
}


def start(tracked_dir, root_dest_dir):
    event_handler = Handler(tracked_dir, root_dest_dir)
    observer = Observer()
    observer.schedule(event_handler, tracked_dir, recursive=True)

    try:
        observer.start()
        while True:
            time.sleep(10)
    except Exception:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    folders = {
        "Downloads": ["C:/Users/Abdo/Downloads", "C:/Users/Abdo/Sorted_Downloads"]
    }

    for folder in folders:
        thread = threading.Thread(target=start, args=(
            folders[folder][0], folders[folder][1],))
        thread.daemon = True
        thread.start()
    try:
        isActive = True
        while isActive:
            time.sleep(10)
    except KeyboardInterrupt:
        isActive = False
        