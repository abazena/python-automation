import os
import sys
from github import Github


projects_dir = 'C:/Users/Abdo/Documents/Projects'
github_access_token = "access token here"


def create_local_repo(name):
    # change command to 'touch README.md' in linux
    os.system('echo # '+name+' > README.md')
    # change command to 'touch LICENSE.md' in linux
    os.system('echo # '+name+'> LICENSE.md')
    os.system('git init')
    os.system('git add --all')
    os.system('git commit -m "initial commit" ')


def create_origin_repo(name):

    # using username and password
    # g = Github("user", "password")
    # or using an access token
    g = Github(github_access_token)
    u = g.get_user()
    try:
        repo = u.create_repo(name)
        os.system('git remote add origin ' + repo.clone_url)
        os.system('git push -u origin master')
    except Exception:
        print("Repo with this name exists! Choose another name")
        os.chdir(projects_dir)
        os.system('rmdir /Q /S "./'+name+'"')  # change to linux command
        print("Local repo deleted")


def create(project_name):

    if not os.path.exists(project_name):
        os.makedirs(project_name)
        os.chdir('./'+project_name)
        create_local_repo(project_name)
        create_origin_repo(project_name)
    else:
        print('Project with the name', project_name,
              'exists! Choose another name')


if __name__ == '__main__':
    os.chdir(projects_dir)
    project_name = sys.argv[1]
    create(project_name)
