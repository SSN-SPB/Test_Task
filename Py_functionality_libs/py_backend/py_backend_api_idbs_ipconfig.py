#!/usr/bin/env python3


# import pytest
import urllib.request
import json
import requests
import ipaddress
from ipaddress import IPv4Network
from ipaddress import ip_network
from ipaddress import ip_interface
# https://requests.readthedocs.io/en/master/
# https://requests.readthedocs.io/en/master/api/#main-interface
# https://www.w3schools.com/python/ref_requests_post.asp

USER_LOGIN = 'sn2_qatestenv@idbs.com'
USER_PASSWORD = 'supernova2_qa'
X_API = '7bRwIK19AALByHRv55g19lIJ7wwtNB'
SITE_URL = 'https://pas-test-client.supernova-qa.idbs-ecs-dev.eworkbookcloud.com/login/default-qatestenv'
#ENDPOINT = 'https://ipconfig-service.sn2-qa.supernova.eworkbookcloud.com/ipconfig/api/v1/default-qatestenv/ipranges'
ENDPOINT = 'https://idbs-admin-portal-qa.eu2.idbs-dev.com/audit/api/v1/default-qatestenv/ipranges'

def get_token(url, login, password, xAPI):

    response_text = requests.post(url,
                      headers={'Content-Type': 'application/json',
                               'X-API-KEY': xAPI},
                      json={"app": "ecs",
                            "username": login,
                            "password": password,
                            "scopes": "user-admin,eln,request",
                            "pas_type" : "ldap"})
    

    token = json.loads(response_text.text)["access_token"]
    return token

def post_iprange(get_endpoint,bear_token,iprange,
                 ip_descripton = 'Default description'):
    
    request_body = {"cidr": iprange,
             "description": ip_descripton}

    post_iprange = requests.post(get_endpoint,json = request_body,
                      headers={'Content-Type': 'application/json',
                               'Authorization': bear_token})
    print('Adding range return code is {} and description is \'{}\''
          .format(post_iprange, json.loads(post_iprange.text)))

def get_ipranges(endpoint,token):
    get_iprange_text = requests.get(endpoint,
                                    headers={'Content-Type': 'application/json',
                                             'Authorization': token})
    ipranges_list = json.loads(get_iprange_text.text)
    print(ipranges_list)
    return ipranges_list

def get_ipranges_cidrs(endpoint,token):
    get_ipranges(endpoint,token)
    cidr_list =[]
    ip_list = get_ipranges(endpoint,token)
    for exact_ip in ip_list:
        # print(exact_ip['cidr'])
        cidr_list.append(exact_ip['cidr'])
    return cidr_list

def add_new_range(get_endpoint,bear_token,iprange, ipdescription):
    list_of_cidrs = get_ipranges_cidrs(get_endpoint,bear_token)
    modified_ip = str(ip_interface(iprange).network)
    if (modified_ip != iprange):
        print('Ip you want to add {} is modified to {}.'
              .format(iprange, modified_ip))    
    if not (modified_ip in list_of_cidrs):
        post_iprange(get_endpoint,bear_token,modified_ip, ipdescription)
    else:
        print('Your {} is treated as {}, but it is in list already'
              .format(iprange, modified_ip))
        
def print_iprange_list(get_endpoint,bear_token):
    theJSONformat = get_ipranges(get_endpoint,bear_token)
    print(theJSONformat)
    total_records = 0
    print('------- List of ranges: ----------')
    for i in theJSONformat:
        total_records = total_records + 1
        print(total_records)
        print(i)
        print (type(i))
        for key in i.items():
            print('The key is: {}'.format(key))
        # ipranges_range_parameters = json.loads(i)            
        # for k in ipranges_range_parameters:
        #     print(k)
        #print('------------------------------')
        print(i['id'])
    print('Total number of records is: {}'.format(total_records))
    
def print_iprange_cidr_list(get_endpoint,bear_token):
    list_of_cidrs = get_ipranges_cidrs(get_endpoint,bear_token)
    print('----- All CIDRs --------')
    for i in list_of_cidrs:
        print(i)
    print('0.0.0.0/0 is in list: ')
    print('0.0.0.0/0' in list_of_cidrs)    
    

def main():
    # input data
    url = SITE_URL
    get_endpoint = ENDPOINT
    xAPI = X_API
    login = USER_LOGIN,
    password = USER_PASSWORD

    # Getting token
    token_current = get_token(url, login, password, xAPI)
    # print('Requested current token is: ' + token_current)

    # getting token
    bear_token = 'Bearer ' + token_current
    print(bear_token)
    
    get_ipranges(get_endpoint,bear_token)
    

    # print_iprange_list(get_endpoint,bear_token)
    
    #add_new_range(get_endpoint,bear_token
    #              ,'14.12.20.3/32', 'Demo SN2-83 Before backup 03')
    # add_new_range(get_endpoint,bear_token
    #              ,'0.0.0.0/32', 'Demo SN2-83 Before backup 04')
    # add_new_range(get_endpoint,bear_token
    #             ,'14.12.20.11/32', 'Autotests')
    # add_new_range(get_endpoint,bear_token
    #             ,'17.11.128.69/0', 'Autotest decription')
    # print_iprange_list(get_endpoint,bear_token)
    # print_iprange_cidr_list(get_endpoint,bear_token)
  
if __name__ == '__main__': main()


