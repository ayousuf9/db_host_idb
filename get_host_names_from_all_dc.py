#!/usr/bin/env python

import json
import requests
import getpass
import os
import re
import get_data_centers
from argparse import ArgumentParser
import pdb

def process_arguments():
    parser = ArgumentParser('Get host list from all Data Centers from iDB')
    parser.add_argument('-p', '--pattern', required=False,
         help='Provide pattern or string to search for in the hostname.\
               If not provided then all hosts will be returned.')
    args = parser.parse_args()
    return args

def get_hosts_from_all_dc(args):
    dc_list, total_dc = get_data_centers.get_data_centers()
    #print('dc_list: {}:'.format(dc_list))
    #print('total_dc: {}'.format(total_dc))
    #quit(3)
    for d in dc_list:
        url = 'https://cfg0-cidbapik1-0-prd.data.sfdc.net/cidb-api/' + d + '/1.04/allhosts?fields=name'
        # TODO: Get username automatically.
        r = requests.get(url, timeout=10, auth=requests.auth.HTTPBasicAuth('ayousuf', get_data_centers.get_user_password()))
        if r.ok:
            json_data = r.text
            dic_data = json.loads(json_data)
            #print(dic_data); quit(3)
            host_name_list = [ d['name'] for d in dic_data['data'] ]
            host_name_list.sort()
            #print(host_name_list); quit(3)
            if args.pattern == None:
                #print('No pattern to search')
                #quit(3)
                for h in host_name_list:
                    print(h)
            else:
                #print(type(host_name_list))
                # print(len(host_name_list))
                # print(host_name_list)
                host_name_list_filtered = [ h for h in host_name_list if h if args.pattern in h ]
                #[ h for h in l if 'Am' in h ]
                # print(type(host_name_list_filtered))
                # print(len(host_name_list_filtered))
                # print(host_name_list_filtered)
                # quit(3)
                if len(host_name_list_filtered) > 0:
                    for h in host_name_list_filtered:
                        print(h)
        else:
            print('Problem getting data from url: {}'.format(url))

if __name__ == '__main__':
    args = process_arguments()
    get_hosts_from_all_dc(args)
