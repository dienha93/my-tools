#!/usr/bin/python
import os
import json
import subprocess
import sys

user_name=sys.argv[1]
password=sys.argv[2]
bitbucket_server_url=sys.argv[3] # sample: code.sample.com
project_key=sys.argv[4]
def clone_project(user_name, password, bitbucket_server_url, project_key):
  stdout = subprocess.check_output(['curl', '-s', '--location', '--request', 'GET', 'https://%s/rest/api/1.0/projects/%s/repos?limit=1000' % (bitbucket_server_url, project_key), '-u', '%s:%s' % (user_name, password)])
  json_object = json.loads(stdout)
  for item in json_object["values"]:
    print("------------------------------------------------------------------------------------------")
    for clone in item["links"]["clone"]:
      if clone["name"] == "http":
        os.system('git clone ' + clone["href"])

  print("Finished!!!")

clone_project(user_name, password, bitbucket_server_url, project_key)


### HOW TO USE ###
# pip install requests
# python git-clone-bitbucket-server.py <username> <password> <your project key> <your work space>
### ---------- ###