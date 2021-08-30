import json
import base64
import requests
import subprocess
import sys

username=sys.argv[1]
app_passwd=sys.argv[2]
project_key=sys.argv[3]
work_space=sys.argv[4]
print("username: %s \napp_passwd: %s \nproject_key:%s" % (username,app_passwd,project_key))
url='https://bitbucket.org/api/2.0/repositories/%s?q=project.key="%s"&pagelen=20' % (work_space, project_key)
def clones(url):
    index=len('https://%s' % username)
    cred='{}:{}'.format(username, app_passwd)
    based64 = base64.b64encode(cred.encode('utf-8')).decode('utf-8')
    r = requests.get(url, headers={'Authorization': 'Basic {}'.format(based64)})
    rp = r.content
    rp_obj = json.loads(rp)
    clones = [ clone['href'][:index] + ':%s' %  app_passwd + clone['href'][index:] for repo in rp_obj['values'] for clone in repo['links']['clone'] if clone['name'] == 'https' ]
    for clone in clones:
        subprocess.run(['git', 'clone', clone])
    if 'next' in rp_obj and rp_obj['next']:
        print("<============ Next Page %s ============>" % rp_obj['next'])
        clones(rp_obj['next'])

clones(url)

### HOW TO USE ###
# pip install requests
# python git-clone-bitbucket.py <username> <password> <your project key> <your work space>
### ---------- ###