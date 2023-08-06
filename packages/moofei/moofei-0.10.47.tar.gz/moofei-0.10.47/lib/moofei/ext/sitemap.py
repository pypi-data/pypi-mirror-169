#!/usr/bin/python
# coding: utf-8
# editor: mufei(ypdh@qq.com tel:15712150708)
'''
牧飞 _ __ ___   ___   ___  / _| ___(_)
| '_ ` _ \ / _ \ / _ \| |_ / _ \ |
| | | | | | (_) | (_) |  _|  __/ |
|_| |_| |_|\___/ \___/|_|  \___|_|
'''
import sys,os,json
import re
import requests
import time

time.sleep(3)

#设置运行目录
basedir = os.path.abspath(os.path.dirname(__file__))
exitfile = os.path.join(basedir, 'exit')

from functools import reduce

try:
    from urlparse import urlparse
except:
    from urllib.parse import urlparse

IMG_TYPE_ARR = ['jpg', 'png', 'ico', 'gif', 'jpeg', 'svg']
REG_URL = r'^(https?://|//)?((?:[a-zA-Z0-9-_]+\.)+(?:[a-zA-Z0-9-_:]+))((?:/[-_.a-zA-Z0-9]*?)*)((?<=/)[-a-zA-Z0-9]+(?:\.([a-zA-Z0-9]+))+)?((?:\?[a-zA-Z0-9%&=]*)*)$'
REG_RESOURCE_TYPE = r'(?:href|src|data\-original|data\-src)=["\'](.+?\.(?:js|css|png|jpg|jpeg|png|gif|svg|ico|ttf|woff2))[a-zA-Z0-9\?\=\.]*["\']'


IMG_TYPE_ARR = ('.jpg', '.png', '.ico', '.gif', '.jpeg', '.svg')

regUrl = re.compile(REG_URL)
regResouce = re.compile(REG_RESOURCE_TYPE, re.S)


REG_RESOURCE_TYPE1 = r'(?:href)=["\'](.+?)["\']'
regResouce1 = re.compile(REG_RESOURCE_TYPE1, re.I)


REG_RESOURCE_TYPE2 = r'(?:href|src|data\-original|data\-src)=["\'](.+?)["\']'
regResouce2 = re.compile(REG_RESOURCE_TYPE2, re.I)




def parseUrl(url):
    '''
    解析URL地址
    '''
    if not url:
        return
    res = regUrl.search(url)
    # 在这里，我们把192.168.1.109:8080的形式也解析成域名domain，实际过程中www.baidu.com等才是域名，192.168.1.109只是IP地址
    # ('http://', '192.168.1.109:8080', '/abc/images/111/', 'index.html', 'html', '?a=1&b=2')
    if res is not None:
        path = res.group(3)
        fullPath = res.group(1) + res.group(2) + res.group(3)
        if not path.endswith('/'):
            path = path + '/'
            fullPath = fullPath + '/'
        return dict(
            baseUrl=res.group(1) + res.group(2),
            fullPath=fullPath,
            protocol=res.group(1),
            domain=res.group(2),
            path=path,
            fileName=res.group(4),
            ext=res.group(5),
            params=res.group(6)
        )
        


class cSiteMap:
    host = None #下载站点 
    dst = None #下载目录
    is_face = None #是否转换为相对网址
    is_down = None #是否下载
    is_args = None #不分析get参数
    _default_page = 'index.php' #默认/页面
    sleep = 0.1
    _deep = -1
    type_arr = ('/', '', '.html', '.php', '.')
    conf = None
    _req = None
    _response = None
    
    
    def __init__(self, host='', dst='', is_face=1, deep=None, conf=None):
        self.conf = conf  if conf else {}
        if 'sleep' in self.conf:
            self.sleep = self.conf.get('sleep')
            
        if host:
            self.host =  conf['host'] = host
        else:
            self.host =  conf['host']
            
        if deep:
            self._deep =  conf['deep'] = deep
        else:
            self._deep =  conf.get('deep',-1)

        if dst:
            self.dst =  conf['dst'] = dst
        else:
            self.dst =  conf['dst']

        if is_face is not None:
            self.is_face =  conf['is_face'] = is_face
        else:
            self.is_face =  conf.get('is_face')

        self.is_down = self.conf.get('is_down')
        self._default_page = self.conf.get('_default_page') or self._default_page
            

        self.downloadedList = [] #已经下载路径
        self.downSrcUrlList = {} #已经下载网址
        
    
        


    

    


    
    def cookies(self):
        return self.conf.get('cookies') or {}
        
    def headers(self):
        return self.conf.get('headers') or {}
        
        
        
    def get_html2url(self, html, resourceUrl=None): #获取urls
        resList = []
        if html:
            resList = regResouce2.findall(html) or []
            _resList = []
            if resList:
                o = urlparse(resourceUrl)
            for url in resList:
                if url.startswith(('/', 'http://', 'https://')):
                    pass #_resList.append(url)
                elif url.startswith(('#',)): continue
                elif resourceUrl: #../ 或者其他相对路径
                    if url.lower().startswith(('javascript','data:','/data:')): continue
                    
                    #print ('vvvv', url, resourceUrl)
                    url = o.path.rsplit('/', 1)[0].rstrip('/')+'/'+url
                if url in self.downSrcUrlList: continue
                #if urlDict['path']=='/' and 'data:' in resourceUrl: continue
                #self.downSrcUrlList[url] = 0 
                _resList.append(url)    
            resList = _resList
        return resList
        
    def get_src2dist(self, srcPath, distPath=None, curPath=None): #对url路径进行绝对补全, 下载路径
        err = None, None
        if not distPath:
            if srcPath.lower().startswith('javascript'):
                print(srcPath, '-', self.domain);
                return err
            o = urlparse(srcPath)
            if o.netloc :
                if o.netloc!=self.domain:
                    print(srcPath, '-', self.domain)
                    return err
            else:
                srcPath = "http://"+self.domain+srcPath

            if self.is_down:
                path = o.path.replace('//','/').replace('\\','/').lstrip('/')
                if not path: path=self._default_page
                elif path.endswith(('/', '\\')): path = path+self._default_page
                distPath = os.path.join(self.dst, path)
            else:
                distPath = srcPath
                
        if distPath in self.downloadedList:
            print(srcPath, '-');
            return err
        
        if self.is_down:
            dirpath = (os.path.dirname(os.path.abspath(distPath)))
            
            if os.path.isfile(dirpath):
                dirpath = dirpath+'@'
                distPath = os.path.join(dirpath, os.path.basename(distPath))
            if not os.path.isdir(dirpath):
                try:
                    os.makedirs(dirpath)
                except:
                    return err
        return srcPath, distPath
            
   
    def downloadFile(self, srcPath, distPath=None, req=None, dstUrl=None): #下载文件
        '''
        下载文件
        '''
        srcPath, distPath = self.get_src2dist(srcPath, distPath)
        _srcPath = srcPath
        
        if distPath is None :
            return None, None
        #??????????????????//加入类型为*， 判断后缀文件， 防止过量下载

        rs = None
        try:
            if req:
                response = req.get(srcPath, verify=False)  #urllib.request.urlopen(srcPath)
            else:
                response = requests.get(srcPath, headers=self.headers(),
                                             cookies=self.cookies(),
                                    verify=False)  #urllib.request.urlopen(srcPath)
            self._response = response
            if response and response.status_code == 404:
                self.downSrcUrlList[srcPath] = 1
                return None, None 
            if response is None or response.status_code != 200:
                #print(response.headers.get('Content-Type'))
                if '404 Not Found' in response.reason: self.downSrcUrlList[srcPath] = 1    
                print ("> download", srcPath, response.status_code, response.reason)
                return None, None
            if response and response.status_code in (301,302):
                self.downSrcUrlList[srcPath] = 1
            
            _srcPath = response.url
            
            if srcPath!=_srcPath :
                
                srcPath,distPath = self.get_src2dist(_srcPath)
                
            if distPath is None:
                return None,None
            data = response.content
            if self.is_down:
                try:
                    f = open(distPath, 'wb')
                except PermissionError:
                    #文件已成目录
                    self.downSrcUrlList[_srcPath] = 1  
                    return None,None
                f.write(data)
                f.close()
            
            
            ContentType=response.headers.get('Content-Type','')
            if '/html' in ContentType or b'<html>' in data:
                if urlparse(_srcPath).netloc == self.domain:
                    rs = response.text
            self.downloadedList.append(distPath)
        except Exception as e:
            self._response = None
            print ('报错了：', srcPath, '~~~~~',e)
            raise
            
        self.downSrcUrlList[_srcPath] = 1
        return rs,_srcPath
        
    
    def is_filter_rules(self, url):
        rules = self.conf.get('filter_rules') or []
        if not rules:
            return
        for rule in rules:
            if re.search(rule,url):
                return True
        

    
    def main(self, url=None, is_continue=0):
        if not url:
            if ':' in self.host:
                url = self.host
            else:
                url = 'http://'+self.host
        
        # 首先创建这个站点的文件夹
        
        if os.path.isfile(exitfile):
            os.remove(exitfile)
        urlDict = parseUrl(url)
        domain = self.domain = urlDict['domain']
        datafile = os.path.join(basedir, domain+'.data')
        is_sess = self.conf.get('is_session')
        if is_sess:
            self._req = requests.session()
            self._req.get(url, headers=self.headers(), cookies=self.cookies(), verify=False)  
        if is_continue and os.path.isfile(datafile):
            print('...continue >>>> %s'%domain)
            resourceDict = self.conf.get('resourceDict') or json.load(open(datafile,'rb'))['resourceDict']
        else:
            data,_url = self.downloadFile(url, req=self._req)
            try:
                content = data.decode('UTF-8')
            except (UnicodeEncodeError,AttributeError): # 'str' object has no attribute 'decode'
                content = data
            if content:
                print ('> 网站内容抓取完毕，内容长度：', len(content))

            resourceList = self.get_html2url(content, _url) #regResouce2.findall(content) if content else []
            resourceDict = dict([(k, 0) for k in resourceList])

        while resourceDict:
            resourceUrl,deep = resourceDict.popitem() #pop()
            if deep > self._deep > 0 : continue 
            if not self.is_args and '?' in resourceUrl:
                resourceUrl = resourceUrl.split('?')[0]
            if resourceUrl in self.downSrcUrlList: continue
            if self.is_filter_rules(resourceUrl): continue
            urlDict = parseUrl(url)
            fileName  = urlDict['fileName'] or '/'
            
            if urlDict['path']=='/' and 'data:' in resourceUrl:
                continue

            if '*' in self.type_arr:
                if fileName and fileName.lower().endswith(self.type_arr):
                    pass
                elif 1:
                    pass #需要判断文件后缀，是否需要下载图片或压缩
            elif '.' in self.type_arr:
                pass
            elif fileName and not fileName.lower().endswith(self.type_arr): continue
 
            if self.sleep: time.sleep(self.sleep)
            
            data, _url = self.downloadFile(resourceUrl, req=self._req)
            self.downSrcUrlList[resourceUrl] = 1
            if '*' in self.type_arr and self._response:
                if 'html' not in self._response.headers.get('Content-Type', ''): continue
            
            if data:
                print(resourceUrl, '+')
                resList = self.get_html2url(data, _url) #regResouce2.findall(data)
                if resList:
                    resDict = [(k,deep+1) for k in resList]
                    #resourceList = resourceList + resList
                    resourceDict.update(resDict)
                    
            #open(exitfile, 'w').close()
            if os.path.isfile(exitfile) or self.conf.get('exit'):
                #self.conf.pop('exit', None)
                #self.conf['downloadedList'] = self.downloadedList
                #self.conf['resourceList'] = resourceList
                #json.dump(self.conf,open(datafile,'wb'))
                break

        
        open(exitfile, 'w').close()
        print(u'-----------------下载完成------------------')
        print(u'总共下载了%d个资源' % len(self.downloadedList))
        
        self.conf.pop('exit', None)
        self.conf['downloadedList'] = self.downloadedList
        self.conf['resourceDict'] = resourceDict
        json.dump(self.conf,open(datafile,'w'))
        print(self.conf)


    
        
        
if __name__ == "__main__":
    import warnings
    warnings.filterwarnings('ignore')
    cSiteMap(dst='/wwwroot/www.layui.com',
             host = 'https://www.layui.com/doc/index.html',
             
             conf = {'filter_rules':['/(?!abc)/.*'],
                     'is_down': 1,
                     'is_session':0,
                     'type_arr':None,
                       }
               ).main(is_continue=1)
    
        
        
        
        








