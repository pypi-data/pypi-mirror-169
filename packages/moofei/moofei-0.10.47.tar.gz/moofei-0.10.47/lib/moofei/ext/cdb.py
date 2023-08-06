#!/usr/bin/python
# coding: utf-8
# editor: mufei(ypdh@qq.com tel:15712150708)
'''
牧飞 _ __ ___   ___   ___  / _| ___(_)
| '_ ` _ \ / _ \ / _ \| |_ / _ \ |
| | | | | | (_) | (_) |  _|  __/ |
|_| |_| |_|\___/ \___/|_|  \___|_|
'''

__all__ = ['DB']

import os,sys,json
import re,time
import datetime
from decimal import Decimal
from moofei._find import bcolors, _get_chardet_detect as detect
from moofei._valid import VALID,ValidMethod
from moofei._db import _db, f_str, DBError, F, Q
_py = list(sys.version_info)
try:
    from pymysql import escape_string
except:
    from pymysql.converters import escape_string
            
try:
    unicode
except:
    unicode = str

def DBdefault(obj):  
    '''
    if isinstance(obj, MyClass):  
        return {'a':obj.a,'b':obj.b}  
    '''
    if isinstance(obj,  datetime.datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, datetime.date):
        return obj.strftime('%Y-%m-%d')
    elif isinstance(obj, datetime.time):
        return str(obj)
    elif isinstance(obj, datetime.timedelta):
        return str(obj)
    elif isinstance(obj, Decimal):
        return float(obj)    
    elif isinstance(obj, bytes):
        #print(obj)
        encoding = detect(obj)[0]
        return obj.decode(encoding, 'ignore')  
    else:
        print(type(obj))
        obj = str(obj)
        raise TypeError('%r is not JSON serializable' % obj)
DBdefault.enableTypes = ['datetime.datetime','datetime.date','datetime.time','decimal.Decimal','datetime.timedelta']


class DB(_db):
    @classmethod
    def dumps(cls, obj, *args, **awgs):
        " Serialize ``obj`` to a JSON formatted ``str``."
        awgs.setdefault('default', DBdefault)
        return json.dumps(obj, *args,**awgs)
        
    def sqlitedump(self, out_path, ext='', tables="", host='', cfg=None, debug=0):
        '''
        http://www.ibiblio.org/elemental/howto/sqlite-backup.html
        cd /home/sqlite
        sqlite3 sample.db .dump > sample.bak
        '''
        
    def sqliteload(self, in_path, ext='', is_repair=0, debug=0):
        '''
        cd /home/sqlite
        mv sample.db sample.db.old
        sqlite3 sample.db < sample.bak
        '''
        
    @classmethod
    def _check_field(cls, value, attrs):
        """
        attrs: 0-default, 1-is_nullable, 2-field_type, 3-key, 4-comment, 5-length, 6-scale, 7-data_type
        """
        data_type = attrs[7]
        prec = attrs[5]
        if value is None and attrs[1]=='NO': #is_nullable
            return "'%s' must be not null "%value    
        if data_type in ('tinyint','smallint','mediumint','int', 'integer', 'bigint', 'timestamp',) or \
            data_type in ('double','float','decimal','numeric'):
            if VALID.isFloat(value, prec=prec)[0]<1:
                return "'%s' must be %s "%(value,attrs[2])    
        elif data_type in ('char','varchar', 'nvarchar') or \
            data_type in ('tinytext','mediumtext','text','longtext') : 
            if isinstance(value, (float, int, Decimal)) and len(str(value))>prec or \
                VALID.isString(value, length=prec)[0]<1:
                return "'%s' must be %s "%(value,attrs[2])
        elif data_type in ('varbinary','binary'): 
            if not isinstance(value, bytes) or len(value)>prec:
                return "'%s' must be %s "%(value,attrs[2])        
        elif data_type in ('date','time','datetime'):
            if VALID.check(value, data_type)[0]<1:
                return "'%s' must be %s "%(value,attrs[2])
    
    _table_columns_ = None    
    @ValidMethod(['self:','table:true','data:true', 'uique_fields:fields','ignore_fields:fields', 'raise_exception:', 'use_cahce:', 'debug:'])     
    def valid(self, table, data, uique_fields=None, ignore_fields=None, raise_exception=False, use_cahce=True, debug=False):
        columnd = {} 
        uniqued = {}
        isI = uique_fields and ('*' in uique_fields or 'I' in uique_fields) #insert
        isU = uique_fields and 'U' in uique_fields #update
        if use_cahce:
            if self._table_columns_ is None: self._table_columns_={}
            if isinstance(table, str) and table in self._table_columns_:
                columnd = self._table_columns_[table]
        
        if columnd: pass
        elif isinstance(table, dict):
            columnd = table
        else:
            if isinstance(table, str):
                columns = self._get_columns(table)
            elif isinstance(table, (tuple,list)):
                columns = table
            for e in columns: columnd[e[:2]] = e[2:]
            if use_cahce and isinstance(table, str):
                self._table_columns_[table] = columnd
                
        for k,v in columnd.items():
            if v[3] in ('PK','PRI', 'UQ','UNI'):
                uniqued[k[1]] = []
                
        if isinstance(data, dict): data=[data]
        msg = None
        line = 0
        for d in data:
            line += 1
            for k,v in d.items():
                if ignore_fields and k in ignore_fields: continue
                if isinstance(v, f_str): continue
                if (table,k) not in columnd:
                    msg = '%s column not find'%k
                else:
                    msg = self._check_field(v, columnd[(table,k)])
                if not msg:
                    if k in uniqued:
                        if v in uniqued[k]:
                            msg = '%s value same'%k
                            break
                        else:
                            uniqued[k].append(v)
                if msg:
                    break

            if msg:
                if debug or self.debug: 
                    bcolors.warn(d)
                    bcolors.warn(msg)
                msg = '[line:%s]'%line+k+':'+msg    
                if raise_exception:
                    raise DBError(msg)
                return {'error':{'message':msg}, 'key':k, 'line':line}
            
        
    def extractTableSql(self, table, columns=None, scheme='mysql'):
        columns = columns or self.columns 
        sqls = ["CREATE TABLE if not exists %s("%table]
        for k in columns:
            if k[0]==table:
                v =  columns[k]
                if _py[0]==2: v = [ str(e) if isinstance(e,unicode) else e  for e in v]
                #print(v)
                sql=self.add_field(table, 
                    k[1], 
                    field_type=v[2],  
                    required= v[1]=='NO', 
                    default=v[0], 
                    comment=v[4],  
                    unique=v[3] in ('UQ','UNI'), 
                    primary=v[3] in ('PK','PRI'), 
                    to_sql='short', 
                    scheme=scheme,
                    debug=0)
                if len(sqls)>1:
                    sqls.append('\t,'+k[1]+' '+sql)
                else:
                    sqls.append('\t'+k[1]+' '+sql)
        sqls.append(')')
        sql = '\n'.join(sqls)
        return sql
        
    def extractInsertSql(self, table, data, insert_mode=None):
        table = str(table)
        _keys,_args = [], []
        for k, v in data.items():
            _keys.append(k)
            _args.append(v)
            
        _keys = ','.join(str(v) for v in _keys)
        _vals = []
        for v in  _args:
            if v is None: v='null'
            elif isinstance(v,str) or isinstance(v,(datetime.datetime,datetime.date)) or isinstance(v,unicode):
                if _py[0]==2 and isinstance(v,unicode):
                    v = v.encode('utf-8')
                v = '"%s"'%escape_string(str(v))
            else:
                v = str(v)
            _vals.append(v)    
        _vals =  ','.join(_vals)       
        #_vals = ','.join( '\'' +str(v) +'\'' if isinstance(v,str) or isinstance(v,datetime.datetime) or isinstance(v,unicode) else str(v) for v in _args)
        if insert_mode and insert_mode.lower()=='replace':
            sql="REPLACE INTO %s(%s) VALUES (%s)"%(table, _keys, _vals)
        elif insert_mode and insert_mode.lower()=='ignore':
            sql="INSERT IGNORE %s(%s) VALUES (%s)"%(table, _keys, _vals)
        else:
            sql="INSERT INTO %s(%s) VALUES (%s)"%(table, _keys, _vals)
        return sql
        
    def extractAll(self, out_dir, cache=True, is_cover=False, tables=None, use_db=None, insert_mode=None):
        def callback(data, fp):
            i = 0
            for d in data:
                fp.write(self.dumps(d)+'\n')
                with open(cachefile,'w') as f :
                   f.write(json.dumps(cacheDict))                
                if i and i%10000==0: print(i)
                i += 1
                
        if not os.path.isdir(out_dir):
            print(out_dir, 'Not Dir.....')
            return
        if use_db is True: use_db = self.DEFAULT_DATABASE   
        cacheDict = {} 
        cachefile = None         
        if cache:
            cachefile = os.path.join(out_dir, '.cache.json')
            if not os.path.isfile(cachefile) or is_cover:
                with open(cachefile,'w') as fp: fp.write('{}')
                cacheDict = {}
            else:
                cacheDict = json.loads(open(cachefile,'r').read())
                
        if tables:
            if isinstance(tables, str): tables=[tables]
        else:
            tables = self.tables
        tables.sort()
        if len(tables)==1:
            columns = self.get_table_columns(tables[0])
        else:
            columns = self.columns
        dPK = {}
        for table in tables:
            print(table)
            _fields = {}
            pkname = None
            pktype = None
            cacheTable = cacheDict.setdefault(table, {})
            for k,v in columns.items():
                if k[0]!=table:continue
                if v[3] in ('PK','PRI'):
                    pkname = dPK[table]=k[1]
                    pktype = v[2]
                _fields[k[1]] = v[2]
                
            if table not in dPK: 
                for k,v in columns.items():
                    if k[0]!=table:continue
                    if v[3] in ('UQ','UNI'):
                        pkname = dPK[table]=k[1]
                        pktype = v[2]
                        if re.search('int',pktype): break
                    
            out_file = os.path.join(out_dir, '%s.sql'%table)
            if is_cover or not cache:
                fp = open(out_file, 'wb')
            else:
                if cache and os.path.isfile(out_file):
                    st_size = os.stat(out_file).st_size
                    if st_size:
                        fp = open(out_file, 'rb')
                        if fp.read(17)==b'-- -- start -- --':
                            cacheTable['initSQL'] = 1
                        fp.seek(0)
                        if st_size>100:
                            fp.seek(st_size-100)                         
                        if fp.read().split(b'\n')[-1][:15] == b'-- -- end -- --':
                            cacheTable['endSQL'] = 1
                            continue
                if table not in dPK:
                    fp = open(out_file, 'wb')
                    cacheTable.clear()
                else:    
                    fp = open(out_file, 'ab+') 
            if not cacheTable.get('initSQL'):
                startmemo = '-- -- start -- --'+time.ctime()+'----\n'
                fp.write(startmemo.encode('utf-8'))
                
                if use_db:
                    fp.write(b'use '+use_db.encode('utf-8')+b'          ;\n')
                    
                sql = self.extractTableSql(table, columns)
                try:
                    fp.write(sql.encode('utf-8'))
                except:
                    if _py[0]==2: fp.write(sql)                    
                #fp.write(sql.encode('utf-8'))
                fp.write(b';\n')
                if cache:
                    cacheTable['initSQL'] = 1
                    with open(cachefile,'w') as f :
                        f.write(json.dumps(cacheDict))
                print(table, 'initSQL', 'saved...')

            count = self.count(table)    
            initROW = cacheTable.setdefault('initROW',0)
            if re.search('char',pktype):
                initPK = cacheTable.setdefault('initPK','')
            else:
                initPK = cacheTable.setdefault('initPK',-count)
            
            if isinstance(count, (str,tuple,list,dict)):
                print(count)
                continue
            #print(count)    
            if count > initROW:
                if table in dPK:
                    pk = initPK
                    n = initROW
                    while n<count:
                        _data = self.query(table, total=False, page_size=10000, where={dPK[table]+'__gt':pk}, orderby=dPK[table])
                        if _data.get('error'): 
                            raise
                        data = _data['result']
                        if not data: break
                        
                        pk = max([d[dPK[table]] for d in data])
                        for d in data:
                            sql = self.extractInsertSql(table, d, insert_mode=insert_mode)
                            try:
                                fp.write(sql.encode('utf-8'))
                            except:
                                if _py[0]==2:
                                    fp.write(sql)
                                else:
                                    print(sql, d)
                                    raise
                            fp.write(b';\n')
                            n += 1
                            if cache:
                                cacheTable['initPK']  = d[dPK[table]]
                                cacheTable['initROW'] = n
                                try:
                                    with open(cachefile,'w') as f :
                                        f.write(json.dumps(cacheDict)) 
                                except KeyboardInterrupt:
                                    with open(cachefile,'w') as f :
                                        f.write(json.dumps(cacheDict))
                                    raise    
                            if n and n%10000==0: print(table, 'initROW', n, cacheTable['initPK'], count)
                else:
                    raise
                    
                '''        
                elif count>10000 and table not in dPK:
                    data = self.query(table, page_size=10000)['result']
                    callback(data)      
                else:
                    data = self.select(table)['result']
                    callback(data)
                '''
                
                endtmemo = '-- -- end -- --'+time.ctime()+'----\n'
                fp.write(endtmemo.encode('utf-8'))
                cacheTable['endSQL'] = 1
                if cache:
                    with open(cachefile,'w') as f :
                        f.write(json.dumps(cacheDict))    
            fp.close()        
    
    @classmethod
    def django_create_model(cls, model, db_table=None, using='default', _instance={}):
        '''
        class cMoofei(models.Model):
            class Meta:
                abstract = True
                app_label = 'logmodels' #app_label需要
        '''
        class Meta:
            app_label='' 
        Meta.db_table = db_table
        new_cls_name = db_table and db_table.title().replace('_', '')
        from django.db import models, connections, connection
        class NewDynamicModel(object):
            def __new__(cls, base_cls, tb_name):
                if new_cls_name not in _instance:
                    new_meta_cls = getattr(base_cls, 'Meta', None) or Meta
                    new_meta_cls.db_table = tb_name
                    model_cls = type(str(new_cls_name), (models.Model,),
                                    {'__tablename__': tb_name, 'Meta': new_meta_cls, '__module__': cls.__module__})
                    _instance[new_cls_name] = model_cls
                    model_cls._meta.parents = {} 
                    #model_cls._meta.pk = base_cls._meta.pk    
                    model_cls._meta.local_fields =  base_cls._meta.local_fields
                    #model_cls._meta.db_table =  db_table
                return _instance[new_cls_name]
        if db_table:
            model = NewDynamicModel(model, db_table)
        
        with connections[using].schema_editor() as schema_editor:
            try:
                exists = model.objects.exists()
            except:
                exists = False                
            if not exists:
                schema_editor.create_model(model) #create_model         
        return model
        
    @classmethod
    def session_field2Column(cls, field_name, field_type, length=None, point=0, required=False, 
                  default=None, comment=None, unsigned=False, zerofill=False, 
                  unique=False, index=False, primary=False, auto_increment=None,
                  strict=False):
        '''
        def alter_column(table, field_name, *args, **awgs):
            meta = MetaData()
            meta.bind = engine
            otb = Table(table, meta, autoload=True)
            if isinstance(field_name, str):
                column = self.session_field2Column(field_name, *args, **awgs)
            else:
                column = field_name   
            if not hasattr(otb.c, column.name):
                #otb.create_column(column) #???
                column.create(otb)
            else:
                getattr(otb.c, column.name).alter(name=column.name, type=String(255))
                
        '''
        import sqlalchemy as sa
        #from migrate.versioning.schema import Table, Column    
        if (unique or index) and strict and length and length>191:
            raise DBError('unique field_length Must < 191')
        ColumnTypes = {
                        'tinyint':'SmallInteger','mediumint':'SmallInteger','tinyint':'SmallInteger',
                        'int':'Integer','integer':'Integer','bigint':'BigInteger',
                        'double':'Float','float':'Float',
                        'decimal':'Numeric','numeric':'Numeric','number':'Numeric',
                        'char':'String','varchar':'String','str':'String',
                        'nvarchar':'Unicode','varchar2':'Unicode',
                        'tinytext':'Text','mediumtext':'Text','text':'Text','long':'Text',
                        'longtext':'Text','clob':'Text','nclob':'UnicodeText',
                        'varbinary':'Binary','binary':'Binary',
                        'raw':'Binary','blob':'Binary','bfile':'LargeBinary',
                        'date':'Date','time':'Time','datetime':'DateTime',
                       }        
        
        if not isinstance(point, int): raise DBError('Point Must Be Int')
        if isinstance(field_type, str):
            field_type = field_type.lower()
            if field_type not in  ColumnTypes:
                raise DBError('field_type Must Be str')
            nullcall = False
            _type = ColumnTypes[field_type]    
            if _type in ('SmallInteger','Integer','BigInteger','Float','Date','DateTime'): 
                nullcall = True
            field_type = getattr(sa,ColumnTypes[field_type])
            if nullcall: pass
            elif length and point:
                field_type = field_type(length, point)
            elif length:
                field_type = field_type(length)
                
        param = {}
        if primary: param['primary_key'] = True
        if auto_increment: param['autoincrement'] = True
        if unique: param['unique'] = True
        elif index: param['index'] = True
        #server_default, onupdate
        if default is not None: param['default'] = default
        param['nullable'] = not required
        if comment: 
            param['comment'] = comment
            param['doc'] = comment
        return sa.Column(field_name, field_type, **param)      
        
    def get_field_max_length(self, table, field):
        "获取查询某个字段长度最大的记录"
        assert self._scheme.startswith(('mysql','mssql','postgresql','oracle','sqlite'))
        if self._scheme.startswith(('mysql','oracle','sqlite', 'postgresql')):
            c = "length"              
        elif 'mssql' in self._scheme:
            c = "DATALENGTH"
        sql="SELECT max(length(%s)) FROM %s;"%(field,table)
        return self.fetchone(sql)['result'][0]
        
    def var(self, field, ttype, rename=None):
        'date,week,month,year'
        s = field
        if ttype=='date': #日
            if 'sqlite' in self._scheme:
                s = "strftime('%%Y-%%m-%%d',%s)"%field
            else:
                s = "date_format(%s,'%%Y-%%m-%%d')"%field
        elif ttype=='week': #周
            if 'sqlite' in self._scheme:
                s = "strftime('%%W',%s)"%field
            else:
                s = "week(%s)"%field        
        elif ttype=='month': #月
            if 'sqlite' in self._scheme:
                s = "strftime('%%Y-%%m',%s)"%field
            else:
                s = "date_format(%s,'%%Y-%%m')"%field
        elif ttype=='quarter': #季
            if 'sqlite' in self._scheme:
                s = "strftime('%%m',%s)/3"%field
            else:
                s = "quarter(%s)"%field                
        elif ttype=='year': #年
            if 'sqlite' in self._scheme:
                s = "strftime('%%Y',%s)"%field
            else:
                s = "date_format(%s,'%%Y')"%field
        elif ttype=='hour': #时
            if 'sqlite' in self._scheme:
                s = "strftime('%%Y-%%m-%%d %%H',%s)"%field
            else:
                s = "date_format(%s,'%%Y-%%m-%%d %%H')"%field
        elif ttype=='minute': #分
            if 'sqlite' in self._scheme:
                s = "strftime('%%Y-%%m-%%d %%H:%%M',%s)"%field
            else:
                s = "date_format(%s,'%%Y-%%m-%%d %%H:%%I')"%field
        elif ttype=='second': #秒
            if 'sqlite' in self._scheme:
                s = "strftime('%%Y-%%m-%%d %%H:%%M:%%S',%s)"%field
            else:
                s = "date_format(%s,'%%Y-%%m-%%d %%H:%%I:%%S')"%field        
        if rename: s=s+' as '+rename
        return s        
        
    def extract_test(self, out_file, limit_nums=30000, empty_out=False, tables=None):
        def callback(data):
            i = 0
            for d in data:
                #print(d)
                fp.write(self.dumps(d)+'\n') 
                if i and i%10000==0: print(i)
                i += 1
                
        fp = open(out_file,'w')
        if tables:
            if isinstance(tables, str): tables=[tables]
        else:
            tables = self.tables
        tables.sort()
        columns = self.columns
        dPK = {}
        for table in tables:
            for k,v in columns.items():
                if k[0]!=table:continue
                if v[3] in ('PK','PRI'):
                    dPK[k[0]]=k[1]
                fp.write(str(k)+':'+str(v)+'\n')
        fp.write('\n')
        
        for table in tables:
            count = self.count(table)
            if isinstance(count, (str,tuple,list,dict)):
                print(count)
                continue
            if not empty_out and not count: continue
            if count>limit_nums: continue
            fp.write('\n')
            fp.write('-'*10+table+'-'*10+'\n')
            print('start save....',table, count, dPK.get(table,''))
            data=[]
            if count>10000 and table in dPK:
                pk = 0
                n = 0
                while n<count: 
                    #sql = "select top 10000 * from %s where %s>%s order by %s"%(table, dPK[table],pk, dPK[table])
                    #data = self.fetchallDict(sql)['result']
                    data = self.query(table, page_size=10000, where={dPK[table]+'__gt':pk}, orderby=dPK[table])['result']
                    if not data: break
                    pk = max([d[dPK[table]] for d in data])
                    callback(data)
                    print('pk=', pk)
            elif count>10000 and table not in dPK:
                data = self.query(table, page_size=10000)['result']
                callback(data)      
            else:
                data = self.select(table)['result']
                callback(data)
            
        fp.close()
            