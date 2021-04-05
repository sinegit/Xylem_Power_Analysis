import numpy as np
import requests
import json
import pandas as pd
import time
from datetime import datetime
from pytz import timezone

Server_url = 'http://X.X.X.X:8080/' #Use an appropriate server address here
Client_id = 'Sinelab_ClientDTLS/'
Object_ID_Temp = '3303/'
Instance_ID_Temp = '0/'
Resource_ID_Temp = '5700'
Temperature_Value = Server_url + 'api/clients/' + Client_id + Object_ID_Temp + Instance_ID_Temp + Resource_ID_Temp
Object_ID_Reboot = '3/'
Instance_ID_Reboot = '0/'
Resource_ID_Reboot = '4'
Reboot_function = Server_url + 'api/clients/' + Client_id + Object_ID_Reboot + Instance_ID_Reboot + Resource_ID_Reboot

def getResourceValue(Temperature_Value):
    r = requests.get(Temperature_Value, timeout=30)
    r.raise_for_status
    data = json.loads(r.text)
    if data['status'] == 'CONTENT' and data['success']:
        return {r.headers._store['date'][1]: data['content']['value']}
    else:
        return None

def ClientLoop(Loops,Temp_Val_per_Loop):    
    data_to_append = {}
    current_temp = {}    
    for j in range(Loops):
        i=0
        while i < Temp_Val_per_Loop:     
            try:                
                current_temp = getResourceValue(Temperature_Value)  
                i+= 1  
                data_to_append.update(current_temp)        
                print(current_temp)            
            except:
                exception_data = {time.strftime("%a, %d %b %Y %I:%M:%S GMT", time.gmtime()): "Network error, wait for it to reconnect!!"}
                data_to_append.update(exception_data)
                print(exception_data) 
            time.sleep(5)   
        requests.post(Reboot_function, timeout=30)
        time.sleep(100)
    return data_to_append