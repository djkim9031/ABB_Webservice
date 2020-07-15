# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:48:11 2019

@author: KRDOKIM13
"""
import sys, requests, json
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
        
        
    def get(self):
        #GET Method to fetch data
        resp=self.session.get(self.host,auth=self.digest_auth)
        json_data=json.loads(resp.content)
        json_value=self.parser(json_data,self.dataType)
        #print('Status Code: ', resp.status_code)
        #print('################################')
        #print('Request Headers: ', resp.headers)
        #print('################################')
        #print('Request Content: ', json.dumps(json_data,indent=2,sort_keys=True))
        #print('################################')
        #print('Value: ', json_value)
        return json_value
      
        
    def post(self):
        #POST Method to update data 
        resp=self.session.post(self.host,auth=self.digest_auth,headers=self.post_headers,data=self.payload)
        #self.cookies='-http-session-={0}; ABBCX={1}'.format(temp.cookies['-http-session-'], resp.cookies['ABBCX']
        print('Status Code: ', resp.status_code)
        print('################################')
        print('Request Headers: ', resp.headers)
        print('################################')
        print('Request Content: ', resp.content)

    @staticmethod        
    def parser(json_data,dataType):   
        if(dataType=='signals'):
            json_value=json_data["_embedded"]
            json_value=json_value['_state']
            #print(len(json_value))
            #for i in range(len(json_value)):
            #    if(json_value[i]['category']==""):
            #        print(json_value[i]['name']+"'s value: ",json_value[i]['lvalue'])
            #json_value=json_value[94]
            #json_value=json_value['name']
            #json_value=json_value.split(',')
            #temp=json_value
            #temp[0]=json_value[0].replace("[[","")
            #temp[2]=json_value[2].replace("]","")
            #temp[3]=json_value[3].replace("[","")
            #temp[6]=json_value[6].replace("]","")
            #temp[7]=json_value[7].replace("[","")
            #temp[10]=json_value[10].replace("]","")
            #temp[11]=json_value[11].replace("[","")
            #temp[16]=json_value[16].replace("]]","")
            #for i in range(len(temp)):
            #    temp[i]=float(temp[i])
            #json_value=temp
            return json_value        
     
    def close(self):
        self.close()

def main(argv):
    try:
      temp=[]
      payload = {}
      dataType = "signals"
      
      for x in range(7):
          #host = "http://192.168.125.1:80/rw/iosystem/signals?start="+str(x)+"00&amp;limit=100&json=1"
          host = "http://127.0.0.1:80/rw/iosystem/signals?start="+str(x)+"00&amp;limit=100&json=1"
          ROB = methods(host, 'Default User', 'robotics',payload,dataType)
          tempOut = ROB.get()
          for y in range(len(tempOut)):
              temp.append(tempOut[y])
      output=temp
        
      return output
    
    except KeyboardInterrupt:
      ROB.close()
   
   
if __name__ == "__main__":
    main(sys.argv[1:])
        