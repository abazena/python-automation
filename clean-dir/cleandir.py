import os
import time
from datetime import date

extensions = {
    "images": [".png", ".jpg", ".jpeg", ".gif", "tiff"],
    "videos": [".avi", ".wmv", ".mp4"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".jar"],
    "documents": [".pdf", ".docx", ".txt"],
    "executables": [".exe", ".msi"]
}


def get_dst_by_ext(extension):
    if extension == "":
        return "folders"
    for key in extensions:
        for ext in extensions[key]:
            if ext == extension:
                return key
    return "other"


if __name__ == "__main__":

    target_dir = "C:/Users/Abdo/Desktop/downloads"
    dir_name = target_dir.split("/")
    dir_name = dir_name[len(dir_name) - 1] + " " + str(date.today())
    try:
        target_dir_files = os.listdir(target_dir)
        root_dest_dir = target_dir + "/" + dir_name
        if not os.path.exists(root_dest_dir):
            os.makedirs(root_dest_dir)
        for file_name in target_dir_files:
            file_src = target_dir + "/" + file_name
            fname = os.path.splitext(file_name)
            dest_dir = root_dest_dir + "/" + get_dst_by_ext(fname[1])
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            file_dst = dest_dir + "/" + file_name
            os.rename(file_src, file_dst)
    except Exception:
        print("File Not Found")
