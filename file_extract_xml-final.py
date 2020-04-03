import xmltodict
import pprint
import json

open1 = open('valid_permission_artifact.xml','r')
doc = xmltodict.parse(open1.read())#parse xml
#print(doc)

doc1 = 0
#pp = pprint.PrettyPrinter(indent=4)

dict2 = json.dumps(doc)#convert xml to json
#print(dict2)
#dict1 = pp.pprint(json.dumps(doc))
#pp.pprint((doc))
    
data = json.loads(dict2)#Json to dict
#print("\n",data)


def parameter():
#Parameters
    last_up = data["UAPermission"]['@lastUpdated']
    print("lastUpdated=",last_up)

    permissionArtifact_Id = data["UAPermission"]['@permissionArtifactId']
    print("permissionArtifactId=",permissionArtifact_Id)

    pilot_PinHash = data["UAPermission"]['@pilotPinHash']
    print("pilotPinHash=",pilot_PinHash)

    ttl = data["UAPermission"]['@ttl']
    print("ttl=",ttl)
    
    txn_Id = data["UAPermission"]['@txnId']
    print("txnId=",txn_Id)
    
    operator_id = data["UAPermission"]['Permission']['Owner']['@operatorId']
    print('operatorId=',operator_id)

    Pilot_Id = data["UAPermission"]['Permission']['Owner']['Pilot']['@PilotId']
    print('PilotId=',Pilot_Id)

    valid_UpTo = data["UAPermission"]['Permission']['Owner']['Pilot']['@validUpTo']
    print('validUpTo=',valid_UpTo)
    
    UU_ID = data["UAPermission"]['Permission']['FlightDetails']['UADetails']['@UUID']
    print("UUID=",UU_ID)
    
    frequency = data["UAPermission"]['Permission']['FlightDetails']['FlightPurpose']['@frequency']
    print("frequency=",frequency)
    
    short_desc = data["UAPermission"]['Permission']['FlightDetails']['FlightPurpose']['@shortDesc']
    print("shortDesc=",short_desc)

    payload_details = data["UAPermission"]['Permission']['FlightDetails']['PayloadDetails']['@payloadDetails']
    print("payloadDetails=",payload_details)

    payload_Weight = data["UAPermission"]['Permission']['FlightDetails']['PayloadDetails']['@payloadWeight']
    print("payloadWeight=",payload_Weight)

    end_time = data["UAPermission"]['Permission']['FlightDetails']['FlightParameters']['@flightEndTime']
    print("flightEndTime=",end_time)

    start_time = data["UAPermission"]['Permission']['FlightDetails']['FlightParameters']['@flightStartTime']
    print("flightStartTime=",start_time)
    
    max_Altitude = data["UAPermission"]['Permission']['FlightDetails']['FlightParameters']['@maxAltitude']
    print("maxAltitude=",max_Altitude)

    frequencies_Used = data["UAPermission"]['Permission']['FlightDetails']['FlightParameters']['@frequenciesUsed']
    print("frequenciesUsed=",frequencies_Used)

    lat =[]
    long =[]
    for data1 in data["UAPermission"]['Permission']['FlightDetails']['FlightParameters']['Coordinates']['Coordinate']:
        #print(data1)
        print()
        for key,value in data1.items():
            #print(key,value)
            if '@longitude' == key:
                print("longitude =",value)
                long.append(value)
            elif '@latitude' == key:
                print("latitude =",value)
                lat.append(value)
   
    #print("longitude list=",long)
   
    #print("latitude list=",lat)
parameter()

