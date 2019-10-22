import pymysql,os,time,csv
from faker import Faker

BASEPATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CASEPATH = os.path.join(BASEPATH,'case')
DATAPATH = os.path.join(BASEPATH,'data')
DRIVERPATH = os.path.join(BASEPATH,'driver')
IMGPATH = os.path.join(BASEPATH,'img')
REPORTPATH = os.path.join(BASEPATH,'report')

BASEURL = 'http://127.0.0.1:8000/api'
Add_EventURL = BASEURL+'/add_event/'
Add_GuestURL = BASEURL+'/add_guest/'
Get_Guest_ListURL = BASEURL+'/get_guest_list/'
User_SignURL = BASEURL+'/user_sign/'
Sec_Get_Event_ListURL = BASEURL+'/sec_get_event_list/'

#生成测试数据
class Create_Data():
    fake = Faker(locale='zh_CN')
    def get_num(self,m,n):
        #随机生成一个指定范围内的数字
        return self.fake.random_int(min=m,max=n)
    def get_address(self):
        #随机生成一个城市名
        return self.fake.city()
    def get_future_time(self):
        #随机生成一个未来时间
        return self.fake.future_datetime()
    def get_email(self):
        #随机生成一个email地址
        return self.fake.email()
    def get_phone(self):
        #随机生成一个电话号码
        return self.fake.phone_number()
    def get_name(self):
        #随机生成一个名字
        return self.fake.name()
    def get_password(self,l,s,d,u,lo):
        #随机生成一个密码
        return self.fake.password(length=l,special_chars=s,digits=d,upper_case=u,lower_case=lo)


#数据库操作方法
class Execute_Mysql():
    def con_mysql(self):
        #连接数据库
        self.con,self.cur = '',''
        try:
            self.con = pymysql.connect('localhost','root','123456','learn',3306,charset='utf8')
        except:
            print('数据库连接失败')
        else:
            self.cur = self.con.cursor()
    def execute_sql(self,sql):
        #执行一条sql语句
        return self.cur.execute(sql)
    def get_sql_result(self):
        #获得一条sql语句执行结果
        return self.cur.fetchone()
    def get_allsql_result(self):
        # 获得sql语句执行所有结果
        return self.cur.fetchall()
    def close_mysql(self):
        #关闭数据库连接
        self.cur.close()
        self.con.close()

def get_time():
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())

def get_data(file):
    l = []
    with open(file) as f:
        data = csv.reader(f)
        for i in data:
            l.append(i)
    return l