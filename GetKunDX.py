import gkcommon

#gmail
gml = 'bpm.2110@gmail.com'

def sGendama():
    print('Start sGendama')
    print('End sGendama')

def sPointIncom():
    print('Start sPointIncom')
    print('End sPointIncom')

def mGendama():
    print('Start mGendama')
    print('End mGendama')

def mPointIncom():
    print('Start mPointIncom')
    print('End mPointIncom')

def PointTown():
    print('Start PointTown')
    
    searchopt1_1 = 'FROM pointmail@pointmail.com'
    searchopt1_2 = 'FROM info@point.gmo.jp'
    searchopt2 = 'UNSEEN'
    loginidname = 'uid'
    loginid = gml
    loginpassname = 'pass'
    loginpass = 'asdoij49a'
    loginurl = 'http://www.pointtown.com/ptu/logon.do'
    charset = 'euc-jp'
    name = 'PointTown'
    searchurl = 'http://www.pointtown.com/ptu/search.do?function=pointpark&type=pointpark_organic&user_gender=1&o=yst&large_img=on&q='

#    #########search
#    tlist = ['init']
#    tlist[0] = searchurl
#    gkcommon.accesser(loginidname, loginid, loginpassname, loginpass,loginurl, tlist)    

    #########mail1
    target = gkcommon.mailreader(name + '1_1', searchopt1_1, searchopt2, charset)
    tlist = gkcommon.listcutter(target, charset)
    gkcommon.accesser(loginidname, loginid, loginpassname, loginpass,loginurl, tlist)

#    #########mail2
#    target = gkcommon.mailreader(name + '1_2', searchopt1_2, searchopt2, charset)
#    tlist = gkcommon.listcutter(target, charset)
#    gkcommon.accesser(loginidname, loginid, loginpassname, loginpass,loginurl, tlist)

    print('End PointTown')

if(__name__ == '__main__'):
    PointTown()
