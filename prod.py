import urllib.request
import json

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def main():

    urlData = "http://vocab.nic.in/rest.php/states/json"
    jsonData = getResponse(urlData)
    # print the state id and state name corresponding
    for i in jsonData["states"]:
        print(f'State Name:  {i["state"]["state_name"]} , State ID : {i["state"]["state_id"]}')

if __name__ == '__main__':
    main()