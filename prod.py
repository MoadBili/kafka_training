import urllib.request
import json
from kafka import KafkaProducer                                                                                         
from time import sleep                                                                                                  

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def main():
    BROKER = 'localhost:9092'                                                                                               
    TOPIC = 'tweets' 
    try:                                                                                                                    
        p = KafkaProducer(bootstrap_servers=BROKER)                                                                         
    except Exception as e:                                                                                                  
        print(f"ERROR --> {e}")                                                                                             
    sys.exit(1)       
    urlData = "http://vocab.nic.in/rest.php/states/json"
    jsonData = getResponse(urlData)
    # print the state id and state name corresponding
    for i in jsonData["states"]:
        message=f'State Name:  {i["state"]["state_name"]} , State ID : {i["state"]["state_id"]}'
        p.send(TOPIC, bytes(message, encoding="utf8"))                                                                      
        sleep(randint(1,4))
if __name__ == '__main__':
    main()