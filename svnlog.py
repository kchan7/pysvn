import pysvn
import time
import sys
from collections import defaultdict


class SvnRepController:
  def __init__(self,url_or_path,user,passwd):
    self.client = pysvn.Client()
    self.url_or_path = url_or_path
    self.user = user
    self.passwd = passwd
    self.client.callback_get_login = self.get_login

  def get_login(self, realm, username, may_save):
    return True, self.user,self.passwd, False

  def log(self):
    return self.client.log(self.url_or_path, discover_changed_paths=True)

if __name__ == '__main__':
  argvs = sys.argv
  argc = len(argvs)
  if(argc != 4):
    sys.stderr.write( 'Usage:\n python %s url_or_path user pass' % argvs[0] )
    quit()
  url_or_path = argvs[1]
  user = argvs[2]
  passwd = argvs[3]
  client = SvnRepController(url_or_path,user,passwd)

  logs = client.log()
  for log in logs:
    print ("RevNo:%d" % (log.revision.number))
    print ("Author:%s date:%s" % (log.author, time.ctime(log.date)))
    print (log.message)
    for p in log.changed_paths:
      print ("  %s" % dict(p))
