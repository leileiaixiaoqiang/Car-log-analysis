#连接数据库
from pymongo import MongoClient


class Mongo():
    def __init__(self,file_path):
        self.file_path=file_path
        self._initDB()

    def _initDB(self):
        self.DbName = self._getDbName()
        self.CollectName = self._getCollecName()

        self.conn=MongoClient()
        self.db=self.conn[self.DbName]
        self.collect=self.db[self.CollectName]

    def _getDbName(self):
        s1=self.file_path.split('/')[-1]
        s2=s1.split('.')[0:3]
        res="D-"+"-".join(s2)
        return res

    def _getCollecName(self):
        s1 = self.file_path.split('/')[-1]
        s2 = s1.split('.')[3]
        res='T-'+s2
        return  res

    #判断数据库和数据表是否存在,如果存在就不进行插入操作
    def judge(self):
        pass

    def insert(self,datas):
        if self.judge():
            print("collection 已经存在,不需要插入")
        else:
            db=self.db
            collection=self.collect
            res=[]
            for data in datas:
                dic = {}
                for i in data:
                    if i[0][0]=='*':
                        suffix=i[0]
                    key=i[0]+"_"+i[1][0]
                    key=key.replace(".",'_dot')
                    if key in dic:
                        key=suffix+key
                    if i[1][0]=="Decimal":
                        if  isinstance(i[1][1],str):
                            dic[key] = float(i[1][1])
                        else:
                            dic[key] = int(i[1][1])
                    elif i[1][0]=="Boolean":
                        dic[key] = bool(i[1][1])
                    else:
                        dic[key] = i[1][1]
                res.append(dic)
            collection.insert_many(res)
     #组织查询语句进行查询
    def findSwitches(self):
        doc=self.collect.find_one()
        res=[]
        for k in doc:
            if k.endswith("Boolean"):
                k=k.replace("_Boolean",'').replace("_dot",'.')
                res.append(k)
        return  res

    def findAnalogs(self):
        doc=self.collect.find_one()
        res=[]
        for k in doc:
            if k.endswith("Decimal"):
                k=k.replace("_Decimal",'').replace("_dot",'.')
                res.append(k)
        return  res

    def findSearches(self):
        doc=self.collect.find_one()
        res=[]
        for k in doc:
                k=k.replace("_Decimal",'').replace("_dot",'.').replace("_Boolean",'')
                res.append(k)
        return  res






# test=Mongo(r"D:\CASCO\车载日志分析\new\WX\27.06.2018.01h59-02h09.8001c0_0000899101")
