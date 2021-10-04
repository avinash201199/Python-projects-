#Execute - python downloads-watchdog.py "/your/downloads/folder"

import os
import time
import sysfrom watchdog.observers 
import Observer
from watchdog.events import FileSystemEventHandler
folder_to_monitor = sys.argv[1]
file_folder_mapping = {
    '.png':'images',
    '.jpg':'images',
    '.jpeg':'images',
    '.gif':'images',
    '.pdf':'pdfs',
    '.mp4':'videos',
    '.mp3':'audio',
    '.zip':'bundles'
}
class DownloadedFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if any(event.src_path.endswith(x) for x in file_folder_mapping):
            parent = os.path.join(os.path.dirname(os.path.abspath(event.src_path)), file_folder_mapping.get(f".{event.src_path.split('.')[-1]}"))
            if not os.path.exists(parent):
                os.makedirs(parent)
            os.rename(event.src_path, os.path.join(parent, os.path.basename(event.src_path)))event_handler = DownloadedFileHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_monitor, recursive=True)
print("Monitoring started")
observer.start()
try:
    while True:
        time.sleep(10)except KeyboardInterrupt:
    observer.stop()
    observer.join()
