'''To indentify the geo'''
import requests
import urllib,urllib.error,urllib.request,urllib.parse
import os,time,sys
import json

base_url="https://freegeoip.app/json/"
def check_country():
    res=urllib.request.urlopen(base_url).read().decode()
    res=json.loads(res)
    country=(res["country_name"])

def raw_data():
    res_1=urllib.request.urlopen(base_url).read().decode()
    res_1=json.loads(res_1)
    #print(res_1)


