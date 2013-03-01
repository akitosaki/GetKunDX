import imaplib
import re
import urllib
import urllib.request
import urllib.parse
import http
import http.cookiejar
from urllib.error import HTTPError

mcharset = 'ISO-2022-JP'

def mailreader(name, searchopt1, searchopt2, charset):
    target = 'tmp/' + name + '.txt'
    print('imaplibをインポート')
    imap=imaplib.IMAP4_SSL('imap.gmail.com', 993)
    print('gmail.comのオブジェクトを作成')

    #imap.login('bpm.2110@gmail.com', getpass.getpass())
    imap.login('bpm.2110@gmail.com', 'mori0061')
    print('gmailにログイン')

    imap.select()

    typ, data = imap.search(None, searchopt1, searchopt2)


    with open(target, 'w', encoding = charset) as afile:
        for i in range(100):
            try:
                num = data[0].split()[-1]
                typ, bodydata = imap.fetch(num, '(RFC822)')
                afile.write(bodydata[i][1].decode())

            except IndexError:
                pass

    imap.close()
    imap.logout()
    return target

def listcutter(target, charset):
    with open(target, 'r', encoding = charset) as afile:
        tlist = re.findall('http://.+', afile.read())
    try:
        j = 0
        for i in range(200):
            if('.jpg' in tlist[j]):
                tlist.pop(j)
            elif('.gif' in tlist[j]):
                tlist.pop(j)
            else:
                j = j + 1
    except IndexError:
        pass

    try:
        for i in range(200):
            if('"' in repr(tlist[i])):
                tlist[i] = tlist[i][0:repr(tlist[i]).index('"') - 1]
            else:
                pass
    except IndexError:
        pass

    return tlist


def pagegetter(loginidname, loginid, loginpassname, loginpass, loginurl, charset, name):
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/536.26.17 (KHTML, like Gecko) Version/6.0.2 Safari/536.26.17')]
    accessdict = {loginidname:loginid,loginpassname:loginpass}
    data = urllib.parse.urlencode(accessdict).encode()
    ##login
    opener.open(loginurl, data)
    ##write temporary file
    response = opener.open(url)
    with open('tmp/' + name + '.txt', 'w', encoding = charset) as afile:
        afile.write(response.read().decode(charset))
    

def accesser(loginidname, loginid, loginpassname, loginpass, loginurl, tlist):
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/536.26.17 (KHTML, like Gecko) Version/6.0.2 Safari/536.26.17')]
    accessdict = {loginidname:loginid,loginpassname:loginpass}
    data = urllib.parse.urlencode(accessdict).encode()
    ##login
    print('login:' + loginurl)
    response = opener.open(loginurl, data)

    name = 'tmp/login.txt'

    try:
        with open(name, 'w', encoding = 'euc-jp') as afile:
            afile.write(response.read().decode('euc-jp'))

    except UnicodeDecodeError:
        
        try:
            with open(name, 'w', encoding = 'shift-jis') as afile:
                afile.write(response.read().decode('shift-jis'))

        except UnicodeDecodeError:
            with open(name, 'w', encoding = 'utf-8') as afile:
                afile.write(response.read().decode('utf-8'))

    for i in range(200):
        try:
            print(tlist[i])
            response = opener.open(tlist[i])
            try:
                with open('tmp/' + str(i) + 'tmp_html.txt', 'w', encoding = 'euc-jp') as afile:
                    afile.write(response.read().decode('euc-jp'))
            except UnicodeDecodeError:

                try:
                    with open('tmp/' + str(i) + 'tmp_html.txt', 'w', encoding = 'shift-jis') as afile:
                        afile.write(response.read().decode('shift-jis'))
                except UnicodeDecodeError:
                    with open('tmp/' + str(i) + 'tmp_html.txt', 'w', encoding = 'utf-8') as afile:
                        afile.write(response.read().decode('utf-8'))
                    
        except IndexError:
            pass
        
        except HTTPError:
            print('')
            print('HTTPERROR!!!!')
            print('')

if(__name__ == '__main__'):
    pass
