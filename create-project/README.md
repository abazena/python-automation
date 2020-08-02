# python-automation/create-project
## Description
A simple script that automates the task of creating a project, initializing a local repo with README and License files then connects to GitHub using <a href="https://github.com/PyGithub/PyGithub"> PyGithub Lib </a> "which uses Github API" and creates the remote repo and eventually opens the new project in VS Code. Script was made to run on Windows but it can run on Linux after changing commands passed to <b>os.system("")</b>

## Changes and Running the script
### Running parameters 
- New project name 
### Dependencies 
- PyGithub 
<pre> $ pip install PyGithub </pre>
### Vars
Root directory of projects folder
<pre> projects_dir = ""   </pre>
Personal github access token
<pre> github_access_token = ""   </pre>
### Notes 
Github auth can be done using username and password instead of access_token, just uncomment line 23 (pass your username and password) and comment line 25
