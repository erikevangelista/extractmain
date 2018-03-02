import extracteslcaller as service
import extractreadfromfile as fileReader
import datetime
import strjoin as strjoin
import csv

print('Starting Main... for ESL Checks...')

sdate = datetime.datetime.now().strftime("%Y%m%d_%H%M")
myFile = strjoin.str_join(sdate, '_eslrtpa.csv')

eslfile =open(myFile,'wb')
csvwriter=csv.writer(eslfile)

print "Start Writing to ", myFile

def printer(serverInfo):
    print ("")

    # 1.fqdn
    fqdn = (serverInfo['Attributes']['PrimaryName']) + ('.') + (serverInfo['Attributes']['ArpaDomain'] )
    print fqdn
    # 2.osversion
    osversion = (serverInfo['Attributes']['OSVersion'])
    print osversion
    # 3.mgmtregion
    mgmtregion = (serverInfo['Attributes']['ManagementRegion'])
    print mgmtregion
    #4.vrrole
    vrrole = (serverInfo['Attributes']['VirtualizationRole'])
    print vrrole
    #5.vrtech
    vrtech = (serverInfo['Attributes']['VirtualizationTechnology'])
    print vrtech
    #10.parentrel
    parentrel = (serverInfo['ParentSystems'][0]['RelationshipType'])
    print parentrel

    sval=[fqdn,osversion,mgmtregion,vrrole,vrtech,parentrel]
    csvwriter.writerow(sval)


serverNames = fileReader.readFromFile("server.txt")

for serverName in serverNames:
    serverInfo = service.retrieveServerInfo(serverName)
    printer(serverInfo)


print "End Writing to ", myFile

print('Ending Main...')
