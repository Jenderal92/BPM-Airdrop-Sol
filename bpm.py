# -*- coding: utf-8 -*-
#Bpm Missions auto Complete Task
#Shin_Code
#I Have Made A Simple Code But I Am Handsome 😎
import requests
import json

PASTE_BEARER = "eyJhbGci......"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
    "Authorization": "Bearer "+PASTE_BEARER,
    "Origin": "https://lfg.missionbpm.com",
    "Referer": "https://lfg.missionbpm.com/",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Linux\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

sex = requests.Session()

# Get user details
response = sex.get("https://api.bpmrewards.io:90/api/User/get-user-details", headers=headers)
user_data = response.json()
if 'result' in user_data:
    result = user_data['result']
    print("Success Log In  =>> " + result['referralCode'])
    print("Process Bypass Follow .....")

# Get user's missions
response2 = sex.get("https://api.bpmrewards.io:90/api/User/get-users-missions", headers=headers)
missions_data = response2.json()
if 'result' in missions_data:
    result2 = missions_data['result']
    for mission in result2:
        print("Try Bypass  =>> " + mission['title'])
        mission_id = mission['id']
        complete_url = "https://api.bpmrewards.io:90/api/User/complete-mission?MissionId=" + str(mission_id)
        response3 = sex.post(complete_url, headers=headers)
        print(response3.content)
        
