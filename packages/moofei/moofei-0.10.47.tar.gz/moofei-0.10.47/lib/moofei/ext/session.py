#!/usr/bin/python
# coding: utf-8
# editor: mufei(ypdh@qq.com tel:15712150708)
'''
牧飞 _ __ ___   ___   ___  / _| ___(_)
| '_ ` _ \ / _ \ / _ \| |_ / _ \ |
| | | | | | (_) | (_) |  _|  __/ |
|_| |_| |_|\___/ \___/|_|  \___|_|
'''
import time,copy

__all__ = ['Session', 'Redis']


class Session(object):
    timeout = 60 * 15 #十五分钟
    cleanTime = time.time()
    is_attach = True
    _d = None
    
    def __init__(self, timeout=None, is_attach=None):
        if timeout is not None: self.timeout=timeout
        if self._d is None: self._d = {}
        if is_attach is not None: self.is_attach=is_attach
    def __len__(self):return len(self.clean())
    def __iter__(self): return iter(self._d)
    def keys(self): return self._d.keys()
    def values(self): return [v['data'] for v in self._d.values()]
    def items(self): return [(k, v['data']) for k, v in self._d.items()]
    def iterkeys(self): return self._d.iterkeys()
    def itervalues(self): return (v['data'] for v in self._d.itervalues())
    def iteritems(self):
        return ((k, v['data']) for k, v in self._d.iteritems())
    def has_key(self, key, ex=None, *value):
        """
            *: key,[ex, [value, ]]
            True: <ex; False: >ex
        """
        t = time.time()
        d = self.clean(t)
        v = key in d
        if v and ex:
            v = d[key]['et'] - d[key]['ex'] + ex > t 
        if v and value:
            v = d[key]["data"] in value       
        return v     
    def __contains__(self, key):
        return key in self.clean()
    def __delitem__(self, key): del self._d[key]
    def __getitem__(self, key): return self.get(key)
    def __setitem__(self, key, value): self.set(key, value)
    def set(self, key,  data, ex=None, nx=False, is_update=False, is_attach=True): #ex=7200, nx=True
        d = self._d 
        if ex is None: ex = self.timeout
        et = time.time()+ex if ex > 0 else -1
        if key not in d: 
            d[key] = {'data':data, 'ex':ex, 'et':et}
            if nx: return True
        else:
            if is_attach: 
                d[key]["ex"] = ex
                d[key]["et"] = et
            if is_update:
                d[key]["data"].update(data)
            else:
                d[key]["data"] = data
         
    def get(self, key, default=None, autoclean=True, is_del=False):
        t = time.time()
        timeout = self.timeout
        if autoclean and t-self.cleanTime > self.timeout: self.clean(t)
        d = self._d.get(key)
        if d :
            if t > d["et"] > 0:
                del self._d[key]
            elif is_del:
                del self._d[key]
                return d["data"]
            else:
                if self.is_attach and d["et"] > 0:
                    d["et"] = t + d['ex']
                return d["data"]
        return default
        
    def pop(self, key, default=None):
        return self.get(key, default, is_del=True) 
    delete = pop 
    
    def incr(self, key, step=1, ex=None, nx=True): #nx:max(data)
        d = self._d
        if ex is None: ex = self.timeout
        et = time.time()+ex if ex > 0 else -1
        if key not in d: 
            d[key] = {'data':1, 'ex':ex, 'et':et}
        else:
            if isinstance(nx, int):
                is_attach = nx > d[key]["data"]
            else:
                is_attach = bool(nx)   
            if is_attach: 
                d[key]["ex"] = ex
                d[key]["et"] = et
            d[key]["data"] += step
        return d[key]["data"]
        
    def expire(self, key, ex=0, nx=None):
        if key in self._d:
            if ex > 0:
                self._d[key]["ex"] = ex
                self._d[key]["et"] = time.time()+ex
            else:
                del self._d[key]
        
    def clean(self, t=None):
        t = t or time.time()
        self.cleanTime = t
        d = self._d
        for k in list(d.keys()):
            if  0<d[k]['et'] < t: del d[k]
        return d

class Redis(Session):        
    def ping(self):pass
    def hmset(self, key, value, expire=None): self.set(key,  value, ex=expire)
    def hmget(self, key): return copy.deepcopy(self.get(key, is_del=True))
    hgetall = hmget
    