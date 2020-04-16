#!/usr/bin/env python

import json
import requests
import getpass
import os
import re

'''
This is what you get:
{u'total': 28, u'data': [{u'@dataCenterJacksonId': u'90acf436-98bd-4c34-af5e-ae6c46350c57', u'name': u'PHX'}, {u'@dataCenterJacksonId': u'07d2233b-3c4b-4011-8d52-e3dcb9c0033f', u'name': u'YHU'}, {u'@dataCenterJacksonId': u'4c6fbef5-9e2d-4be5-a97d-7eae1ffa4cc1', u'name': u'IAD'}, {u'@dataCenterJacksonId': u'15f0e1ad-9cd7-4f52-9f66-ba1c93a02081', u'name': u'UKB'}, {u'@dataCenterJacksonId': u'35d211ce-bc30-40db-a169-27fa5502f41f', u'name': u'LO2'}, {u'@dataCenterJacksonId': u'5e311f29-1bb8-4f6d-add0-4a12a168e7aa', u'name': u'LO3'}, {u'@dataCenterJacksonId': u'a7f7ea21-99c2-47fb-9aa8-04404b4de729', u'name': u'YUL'}, {u'@dataCenterJacksonId': u'1bb27afb-64d5-42d9-83cb-4bb803d78f3d', u'name': u'FRA'}, {u'@dataCenterJacksonId': u'10110436-5ee1-48f1-a3e6-fb665b84d6f4', u'name': u'CRD'}, {u'@dataCenterJacksonId': u'aecd71db-c237-4b0d-bc54-c841d1883c01', u'name': u'FRF'}, {u'@dataCenterJacksonId': u'ee93e119-8108-4547-993d-692e1da28c05', u'name': u'IA2'}, {u'@dataCenterJacksonId': u'36b7b791-44cb-4e50-9460-80f8f46bd9d5', u'name': u'IA5'}, {u'@dataCenterJacksonId': u'f313c5be-adc8-4602-b4be-0f6021c88ebe', u'name': u'IA4'}, {u'@dataCenterJacksonId': u'1faad3ab-c3a5-4411-8e11-a78f6050dd36', u'name': u'HND'}, {u'@dataCenterJacksonId': u'c217c9cd-7a3c-4fa8-b741-c4077e50537e', u'name': u'ORD'}, {u'@dataCenterJacksonId': u'95f43497-f37c-46e1-a5b9-2eaa406f6faa', u'name': u'PAR'}, {u'@dataCenterJacksonId': u'2dbdd1e8-ff43-4c11-ab84-1001e9ffd99e', u'name': u'PRD'}, {u'@dataCenterJacksonId': u'25d8681d-fceb-4d50-80d6-502a4512cba2', u'name': u'CHI'}, {u'@dataCenterJacksonId': u'f4c62a99-5a32-491a-972e-b478127d95b7', u'name': u'CDG'}, {u'@dataCenterJacksonId': u'0aac5cfc-ae10-4547-83b5-6cd07a3e4a42', u'name': u'WAS'}, {u'@dataCenterJacksonId': u'63c362b6-f6b7-4f7f-bf98-13ea57a31ce0', u'name': u'CRZ'}, {u'@dataCenterJacksonId': u'82048ae2-1d7a-4914-b192-f32005b392bc', u'name': u'XRD'}, {u'@dataCenterJacksonId': u'2c0b9d19-6dab-4325-9300-5d0c8e895c58', u'name': u'WAX'}, {u'@dataCenterJacksonId': u'4680c550-0805-4ef2-a748-0f4ce4b1eeee', u'name': u'CHX'}, {u'@dataCenterJacksonId': u'aad7c0a1-d328-481e-ba7c-b29c88a622e8', u'name': u'DFW'}, {u'@dataCenterJacksonId': u'3b611f1e-dc73-4701-9de7-d7320cc95170', u'name': u'CDU'}, {u'@dataCenterJacksonId': u'1de618c0-5c7a-40bf-9372-141cfa80ab6f', u'name': u'PH2'}, {u'@dataCenterJacksonId': u'89b41c5f-ec24-4175-824b-694df7639b58', u'name': u'SYD'}], u'success': True}
'''

def get_user_password():
    """ This function will get the password from environment variable mypwd1.
        If environment variable is not set then, it will prompt the user for
        password.
        Return: It will return password
    """
    try:
        mypwd1 = os.environ['mypwd1']
        if re.search('"',mypwd1):
            raise KeyError()
        if re.search('\\"',mypwd1):
            raise KeyError()
    except KeyError:
        mypwd1 = getpass.getpass('Enter your password -> ')
    return mypwd1

def get_data_centers():
    #url = 'https://cfg0-cidbapik1-0-prd.data.sfdc.net/cidb-api/1.04/datacenters?fields=name'
    url = 'https://cfg0-cidbapik1-0-prd.data.sfdc.net/cidb-api/1.04/alldatacenters?fields=name'
    r = requests.get(url, timeout=10, auth=requests.auth.HTTPBasicAuth('ayousuf', get_user_password()))
    if r.ok:
        json_data = r.text
        dic_data = json.loads(json_data)
        #print(dic_data); quit(3)
        dc_names_list = [ d['name'] for d in dic_data['data'] ] 
        dc_names_list.sort()
        #print(dc_names_list); quit(3)
        total_dc = len(dc_names_list)
        for dc in dc_names_list:
            print(dc)
        print('Total Number of Data Centers: {}'.format(total_dc))
        return dc_names_list, total_dc
    else:
        print('Problem getting data from url: {}'.format(url))

if __name__ == '__main__':
    get_data_centers()

