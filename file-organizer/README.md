# python-automation/file-organizer
A simple multithreaded script that automates the task of organizing single/multiple folders, the script watches target directories for change and once the event is triggered it collects all files/folders and sorts them based on the file type. currently, the script sorts files based on the extensions dictionary, any filetype that is not included in the extensions dictionary will be placed in the "Others" folder. the script can watch multiple folders, just add the new folder and destination path "where to put the organized files".  
## Changes and Running the script
### Dependencies
- <a href="https://pypi.org/project/watchdog/"> watchdog</a>
<pre>pip install watchdog</pre>
### Vars
- extensions: a dictionary that groups file types that should be sorted by the script, any type that is not included will be placed in the Others folder. The dictionary key is used to create the organized file structure
- folders: a dictionary of arrays, the key is just an identifier for each folder, index [0] is the folder to track and index [1] is where orgnized files will be stored
