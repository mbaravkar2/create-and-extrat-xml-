from tkinter import *
import tkinter.messagebox as MessageBox
import xml.etree.cElementTree as ET    

def submit1():
    
    last_u = lastUpdated_e.get()
    per_art = permissionArtifactid_e.get()
    pilot_ph = pilotPinHash_e.get()
    ttl1 = ttl_e.get()
    txn = txnId_e.get()
    ope_id = operatorId_e.get()
    pilot_id = PilotId_e.get()
    val_up = validUpTo_e.get()
    uuid = UUID_e.get()
    freq = frequency_e.get()
    short_de = shortDesc_e.get()
    pay_l = payloadDetails_e.get()
    pay_l_w = payloadWeight_e.get()
    end = flightEndTime_e.get()
    start = flightStartTime_e.get()
    max_al = maxAltitude_e.get()
    freq_u = frequenciesUsed_e.get()
  
    root = ET.Element('UAPermission',lastUpdated = last_u, permissionArtifactId= per_art,pilotPinHash=pilot_ph,ttl = ttl1,txnId = txn)#Tree
    root1 = ET.SubElement(root,'Permission')
    root2  = ET.SubElement(root1,"Owner",operatorId = ope_id)
    ET.SubElement(root2,"Pilot", PilotId = pilot_id  ,validUpTo = val_up)
    root3  = ET.SubElement(root1,"FlightDetails")
    ET.SubElement(root3,"UADetails",UUID = uuid)
    ET.SubElement(root3,"FlightPurpose",frequency = freq , shortDesc = short_de )
    ET.SubElement(root3,"PayloadDetails",payloadDetails = pay_l ,payloadWeight = pay_l_w  )
    root4 = ET.SubElement(root3,"FlightParameters",flightEndTime= end , flightStartTime = start ,maxAltitude = max_al,frequenciesUsed = freq_u)
    #XML Generation
    root5 = ET.SubElement(root4,"Coordinates")
    e = T.get("1.0",END)
    lat = []
    long = []
    m = e.split(",")
    print(m)
    ele =0
    while(ele<len(m)):
        if(ele==len(m)-2):
            m[ele+1]=m[ele+1][0:len(m[ele+1])-1]
        lat.append(m[ele])  
        long.append(m[ele+1])
        
        ele=ele+2
        
    print(long)
    print(lat)
    
    eter = 0
    while eter<(len(m)/2):
        lat1 = lat[eter]
        print(lat1)
        long1 = long[eter]
        print(long1)
        ET.SubElement(root5, "Coordinate", latitude = lat1 , longitude = long1)
        eter += 1
 
    
    #ET.SubElement(root , "field2", name="asdfasd")

    tree = ET.ElementTree(root)
    tree.write("valid_permission_artifact.xml")

    #Message box
    if (e or oper_id or id1 or  val_to or uin or short_d or pay_wtkg or paylo or adc or fic or end_t or start_t or max_a or recu_t or rec_t_t or rec_tdm) == '':
        MessageBox.showinfo("Insert Status","All fields are required")
    else:
        MessageBox.showinfo("Insert Status","Added successfully")
        
    widg.destroy()
    
  
widg = Tk()
widg.title("GBSoftronics")
widg.geometry('1366x738')
widg.config(bg='white')
widg.resizable(0,0)
#lastupdated
lastUpdated = Label(widg,text="lastUpdated")
lastUpdated.config(font=('Times new romen',12),bg='white')
lastUpdated.place(x = 10,y = 10)
lastUpdated_e = Entry(widg)
lastUpdated_e.place(x = 300,y = 10)
#permissionArtifactid
permissionArtifactid = Label(widg,text="permissionArtifactId")
permissionArtifactid.config(font=('Times new romen',12),bg='white')
permissionArtifactid.place(x = 10,y = 50)
permissionArtifactid_e = Entry(widg)
permissionArtifactid_e.place(x = 300,y = 50)
#validTo
pilotPinHash = Label(widg,text="pilotPinHash")
pilotPinHash.config(font=('Times new romen',12),bg='white')
pilotPinHash.place(x = 10,y = 90)
pilotPinHash_e = Entry(widg)
pilotPinHash_e.place(x = 300,y = 90)
#ttl
ttl = Label(widg,text="ttl")
ttl.config(font=('Times new romen',12),bg='white')
ttl.place(x = 10,y = 130)
ttl_e = Entry(widg)
ttl_e.place(x = 300,y = 130)
#txnId
txnId = Label(widg,text="txnId")
txnId.config(font=('Times new romen',12),bg='white')
txnId.place(x = 10,y = 170)
txnId_e = Entry(widg)
txnId_e.place(x = 300,y = 170)
#operatorId
operatorId = Label(widg,text="operatorId")
operatorId.config(font=('Times new romen',12),bg='white')
operatorId.place(x = 10,y = 210)
operatorId_e = Entry(widg)
operatorId_e.place(x = 300,y = 210)
#PilotId
PilotId = Label(widg,text="PilotId")
PilotId.config(font=('Times new romen',12),bg='white')
PilotId.place(x = 10,y = 250)
PilotId_e = Entry(widg)
PilotId_e.place(x = 300,y = 250)
#validUpTo
validUpTo = Label(widg,text="validUpTo")
validUpTo.config(font=('Times new romen',12),bg='white')
validUpTo.place(x = 10,y = 290)
validUpTo_e = Entry(widg)
validUpTo_e.place(x = 300,y = 290)
#UUID
UUID = Label(widg,text="UUID")
UUID.config(font=('Times new romen',12),bg='white')
UUID.place(x = 10,y = 330)
UUID_e = Entry(widg)
UUID_e.place(x = 300,y = 330)
#frequency
frequency = Label(widg,text="frequency")
frequency.config(font=('Times new romen',12),bg='white')
frequency.place(x = 10,y = 370)
frequency_e = Entry(widg)
frequency_e.place(x = 300,y = 370)
#shortDesc
shortDesc = Label(widg,text="shortDesc")
shortDesc.config(font=('Times new romen',12),bg='white')
shortDesc.place(x = 10,y = 410)
shortDesc_e = Entry(widg)
shortDesc_e.place(x = 300,y = 410)
#payloadDetails
payloadDetails = Label(widg,text="payloadDetails")
payloadDetails.config(font=('Times new romen',12),bg='white')
payloadDetails.place(x = 10,y = 450)
payloadDetails_e = Entry(widg)
payloadDetails_e.place(x = 300,y = 450)
#payloadWeight
payloadWeight = Label(widg,text="payloadWeight")
payloadWeight.config(font=('Times new romen',12),bg='white')
payloadWeight.place(x = 10,y = 490)
payloadWeight_e = Entry(widg)
payloadWeight_e.place(x = 300,y = 490)
#flightEndTime
flightEndTime = Label(widg,text="flightEndTime")
flightEndTime.config(font=('Times new romen',12),bg='white')
flightEndTime.place(x = 500,y = 10)
flightEndTime_e = Entry(widg)
flightEndTime_e.place(x = 800,y = 10)
#flightStartTime
flightStartTime = Label(widg,text="flightStartTime")
flightStartTime.config(font=('Times new romen',12),bg='white')
flightStartTime.place(x = 500,y = 50)
flightStartTime_e = Entry(widg)
flightStartTime_e.place(x = 800,y = 50)
#maxAltitude
maxAltitude = Label(widg,text="maxAltitude")
maxAltitude.config(font=('Times new romen',12),bg='white')
maxAltitude.place(x = 500,y = 90)
maxAltitude_e = Entry(widg)
maxAltitude_e.place(x = 800,y = 90)
#frequenciesUsed
frequenciesUsed = Label(widg,text="frequenciesUsed")
frequenciesUsed.config(font=('Times new romen',12),bg='white')
frequenciesUsed.place(x = 500,y = 130)
frequenciesUsed_e = Entry(widg)
frequenciesUsed_e.place(x = 800,y = 130)
#long&lat
text_a = Label(widg,text="Longitude-Latitude")
text_a.config(font=('Times new romen',12),bg='white')
text_a.place(x = 500,y = 170)
T = Text(widg, height=8, width=30)
T.place(x = 800,y = 170)

submit = Button(widg,text='Submit',bg='green',fg='black',width=15,height=2,command=submit1)
submit.place(x = 750,y = 400)
widg.mainloop()
