import gitlab
import uuid

# Create a Gitlab connection
gl = gitlab.Gitlab("http://gitlab.tryhackme.loc/", private_token='')
gl.auth()

# Get all Gitlab projects
project = gl.projects.get(ash/environments)
environments = project.environments.list()
runners = project.runners.list()

print(project)
print(environments)
print(runners)