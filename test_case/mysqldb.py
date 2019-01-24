#coding=utf-8
import MySQLdb  
#数据库操作类  
class DB():  
    conn=None;#这里的None相当于其它语言的NULL  
    def __init__(self):#构造函数  
        self.conn=MySQLdb.connect(host="116.204.14.248",user="root",passwd="Dfs@168",db="dfs168",port=56000);  
        #数据库连接，localhost python不认  
    def getBySql(self,sql,*param):  
        cursor=self.conn.cursor();#初始化游标  
        result=cursor.fetchmany(cursor.execute(sql,param));  
        self.conn.commit();#提交上面的sql语句到数据库执行  
        return result; 
    def getBySql1(self,sql,*param):  
        cursor=self.conn.cursor();#初始化游标  
        result=cursor.fetchmany(cursor.execute(sql,param));  
        self.conn.commit();#提交上面的sql语句到数据库执行  
        return result;           
    def getBySql_result_unique(self,sql,*param):  
        cursor=self.conn.cursor();#初始化游标  
        result=cursor.fetchmany(cursor.execute(sql,param));  
        self.conn.commit();#提交上面的sql语句到数据库执行  
        return result[0][0];  
    def setBySql(self,sql,*param):  
        cursor=self.conn.cursor();#初始化游标  
        cursor.execute(sql,param);  
        self.conn.commit();#提交上面的sql语句到数据库执行  
    def __del__(self):#析构函数  
        self.conn.close();#关闭数据库连接  
  
#主程序          
# db=DB();  
# print "usertable中的条目数："  
# print db.getBySql_result_unique("select member_name from shopnc_member where member_phone='18620369112'");
# print db.getBySql("select * from shopnc_member where member_phone='18620369112'")  
# print "usertable中id大于4的结果："  
# result=db.getBySql("select * from usertable where id>%s",4)  
# for row in result:  
#     for cell in row:  
#         print str(cell)+",",  
#     print;  
  
#增删改实例：db.setBySql("insert into usertable(username,password) values(%s,%s)","ff","s");  

host="116.204.14.248",user="root",passwd="Dfs@168",db="dfs168",port=56000