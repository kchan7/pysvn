import os,sys
import csv
import pandas as pd
from collections import defaultdict
from datetime import datetime
import pysvn


###env
RESULT_FILE='file_list.csv'


class SvnClient:
    def __init__(self,url_or_path,user,passwd):
        self.client = pysvn.Client()
        self.url_or_path = url_or_path
        self.user = user
        self.passwd = passwd
        self.client.callback_get_login = self.get_login

    def get_login(self, realm, username, may_save):
        return True, self.user,self.passwd, False

    def ls(self):
        return self.client.ls(self.url_or_path, recurse=True)

if __name__ == '__main__':
    ## command sample
    ## python3 svnlog.py http://svn.sourceforge.jp/svnroot/simyukkuri/ "admin" "admin"
    argvs = sys.argv
    argc = len(argvs)
    if(argc != 4):
        sys.stderr.write( 'Usage:\n python %s url_or_path user pass' % argvs[0] )
        quit()
    url_or_path = argvs[1]
    user = argvs[2]
    passwd = argvs[3]

    client = SvnClient(url_or_path,user,passwd)
    ## pysvn.Client.ls
    ## https://pysvn.sourceforge.io/Docs/pysvn_prog_ref.html#pysvn_client_ls
    ## created_rev - pysvn.Revision - the revision of the last change
    ## has_props - bool - True if the node has properties
    ## kind - node_kind - one of the pysvn.node_kind values
    ## last_author - the author of the last change
    ## name - string - name of the file
    ## size - long - size of file
    ## time - float - the time of the last change

    df = pd.DataFrame(columns = ['dir_path','file_name','file_ext','size','created_rev','has_props','kind','last_author','time'])

    repo_infos = client.ls()
    for info in repo_infos:
        if str(info.kind) == "file":
            time = datetime.fromtimestamp(info.time).strftime('%Y-%m-%d %H:%M:%S')
            info_array = info.name.split('/')
            file_name = info_array[-1]
            path, file_ext = os.path.splitext(file_name)
            row = pd.DataFrame([[info.name, file_name, file_ext, info.size, info.created_rev, info.has_props, info.kind, info.last_author, time]], columns=df.columns)
            df = pd.concat([df,row],ignore_index=True)

    df.to_csv(RESULT_FILE, encoding='utf-8', index=True)
