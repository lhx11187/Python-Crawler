#  -*- coding:utf-8 -*-
import requests 
import re
import sys
import threading
import time
reload(sys)
sys.setdefaultencoding('utf-8')
class Archives(object):

    def save_links(self,url):
        try:
            data=requests.get(url,timeout=3)
            content=data.text
            #link_pat='"(ed2k://\|file\|[^"]+?\.(S\d+)(E\d+)[^"]+?1024X\d{3}[^"]+?)"'
            link_pat='ed2k:.*?\|\/|magnet:?[^\"]+|http://pan.baidu.com/?[^\"]+'
            name_pat=re.compile(r'<h2 class="entry_title">(.*?)</h2>',re.S)
            links = set(re.findall(link_pat,content))
            name=re.findall(name_pat,content)
            links_dict = {}
            count=len(links)
            print count
        except Exception,e:
            pass
        with open('D:\\天天美剧1\\'+name[0].replace('/',' ')+'.txt','w') as f:
            for i in links:
                try:
                    print i
                    f.write(i + '\n')
                except Exception,e:
                    print str(e)
                    pass
        print "Get links ... ", name[0], count

    def get_urls(self):
        try:
            for i in range(229,25000):
                base_url='http://cn163.net/archives/'
                #print str(i)
                url=base_url+str(i)+'/'
                print url
                if requests.get(url).status_code == 404:
                    print requests.get(url).status_code
                    continue
                else:
                    print requests.get(url).status_code
                    self.save_links(url)
        except Exception,e:
            pass
    def main(self):
        thread1=threading.Thread(target=self.get_urls())
        thread1.start()
        thread1.join()
if __name__ == '__main__':
        start=time.time()
        a=Archives()
        a.main()
        end=time.time()
        print end-start
