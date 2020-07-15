# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:23:22 2019

@author: KRDOKIM13
"""

import sys, requests
from requests.auth import HTTPDigestAuth
#import parse

class methods:
    def __init__(self,host,username,password,payload,dataType):
        self.host=host
        self.username=username
        self.password=password
        self.payload=payload
        self.dataType=dataType
        self.digest_auth=HTTPDigestAuth(self.username,self.password)
        self.session=requests.Session()
        self.post_headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
                
    def post(self):
        #POST Method to update data 
        self.session.post(self.host,auth=self.digest_auth,headers=self.post_headers,data=self.payload)
        #self.cookies='-http-session-={0}; ABBCX={1}'.format(temp.cookies['-http-session-'], resp.cookies['ABBCX']
 
     
    def close(self):
        self.close()


        
def main(argv):
    try:
      #host = 'http://192.168.125.1/rw/rapid/execution'
      host = 'http://127.0.0.1/rw/rapid/execution'
      tempHost = host + '?action=request'
      dataType='mastershiprequest'
      payload={}
      ROB = methods(tempHost, 'Default User', 'robotics',payload,dataType)
      ROB.post()        
        
      #host = 'http://192.168.125.1/rw/rapid/execution'
      host = 'http://127.0.0.1/rw/rapid/execution'
      #'http://192.168.125.1:80/rw/rapid/execution'
      tempHost = host + '?action=resetpp' #reset pp to main
      dataType='resetpp'
      payload={}
      ROB = methods(tempHost, 'Default User', 'robotics',payload,dataType)
      ROB.post()          
              
      queryParameter = '?action=start' #execution start
      host = host + queryParameter
      dataType='exec'
      runmode = 'forever'
      payload = {'regain':'continue',
                 'execmode':'continue',
                 'cycle':runmode,
                 'condition':'none',
                 'stopatbp':'enabled',
                 'alltaskbytsp':'true'}
      ROB = methods(host, 'Default User', 'robotics',payload,dataType)
      ROB.post()

    except KeyboardInterrupt:
      ROB.close()
   
   
if __name__ == "__main__":
    main(sys.argv[1:])
   