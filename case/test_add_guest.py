import unittest,requests
from util.utils import Create_Data,Execute_Mysql,Add_GuestURL,DATAPATH,get_data

file = DATAPATH+'/add_guest.csv'
response_data = get_data(file)
class Test_Add_Guest(unittest.TestCase):
    '''添加嘉宾接口'''
    def setUp(self):
        self.em = Execute_Mysql()
        self.em.con_mysql()
        self.gd = Create_Data()
        self.data = {}
        sql = 'select id from sign_event where status=1;'
        self.em.execute_sql(sql)
        self.a = self.em.get_allsql_result()
        self.data['eid'] = int(self.a[-1][0])
        self.data['realname'] = self.gd.get_name()
        self.data['phone'] = self.gd.get_phone()
        self.data['email'] = self.gd.get_email()
    def tearDown(self):
        self.em.close_mysql()
    def testcase01(self):
        '''正确传入以“13”开头的phone参数添加嘉宾成功'''
        sql = 'select phone from sign_guest'
        self.em.execute_sql(sql)
        self.e_phone = self.em.get_allsql_result()
        self.error_phone = []
        for i in self.e_phone:
            self.error_phone.append(i[0])
        while True:
            self.true_phone = '13'+str(self.gd.get_num(100000000,999999999))
            if self.true_phone not in self.error_phone:
                self.data['phone'] = self.true_phone
                break
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[1][0]))
        self.assertEqual(self.res['message'],response_data[1][1])
        self.assertEqual(self.result,1)
    def testcase02(self):
        '''正确传入以“15”开头的phone参数添加嘉宾成功'''
        sql = 'select phone from sign_guest'
        self.em.execute_sql(sql)
        self.e_phone = self.em.get_allsql_result()
        self.error_phone = []
        for i in self.e_phone:
            self.error_phone.append(i[0])
        while True:
            self.true_phone = '15' + str(self.gd.get_num(100000000, 999999999))
            if self.true_phone not in self.error_phone:
                self.data['phone'] = self.true_phone
                break
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[1][0]))
        self.assertEqual(self.res['message'],response_data[1][1])
        self.assertEqual(self.result,1)
    def testcase03(self):
        '''正确传入以“17”开头的phone参数添加嘉宾成功'''
        sql = 'select phone from sign_guest'
        self.em.execute_sql(sql)
        self.e_phone = self.em.get_allsql_result()
        self.error_phone = []
        for i in self.e_phone:
            self.error_phone.append(i[0])
        while True:
            self.true_phone = '17' + str(self.gd.get_num(100000000, 999999999))
            if self.true_phone not in self.error_phone:
                self.data['phone'] = self.true_phone
                break
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[1][0]))
        self.assertEqual(self.res['message'],response_data[1][1])
        self.assertEqual(self.result,1)
    def testcase04(self):
        '''正确传入以“18”开头的phone参数添加嘉宾成功'''
        sql = 'select phone from sign_guest'
        self.em.execute_sql(sql)
        self.e_phone = self.em.get_allsql_result()
        self.error_phone = []
        for i in self.e_phone:
            self.error_phone.append(i[0])
        while True:
            self.true_phone = '18' + str(self.gd.get_num(100000000, 999999999))
            if self.true_phone not in self.error_phone:
                self.data['phone'] = self.true_phone
                break
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[1][0]))
        self.assertEqual(self.res['message'],response_data[1][1])
        self.assertEqual(self.result,1)
    def testcase05(self):
        '''正确传入以“19”开头的phone参数添加嘉宾成功'''
        sql = 'select phone from sign_guest'
        self.em.execute_sql(sql)
        self.e_phone = self.em.get_allsql_result()
        self.error_phone = []
        for i in self.e_phone:
            self.error_phone.append(i[0])
        while True:
            self.true_phone = '19' + str(self.gd.get_num(100000000, 999999999))
            if self.true_phone not in self.error_phone:
                self.data['phone'] = self.true_phone
                break
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[1][0]))
        self.assertEqual(self.res['message'],response_data[1][1])
        self.assertEqual(self.result,1)
    def testcase06(self):
        '''不传入eid参数添加嘉宾失败'''
        self.data.pop('eid')
        self.data['phone'] = '18'+str(self.gd.get_num(100000000,999999999))
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[2][0]))
        self.assertEqual(self.res['message'],response_data[2][1])
        self.assertEqual(self.result,0)
    def testcase07(self):
        '''不传入realname参数添加嘉宾失败'''
        self.data.pop('realname')
        self.data['phone'] = '17'+str(self.gd.get_num(100000000,999999999))
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[2][0]))
        self.assertEqual(self.res['message'],response_data[2][1])
        self.assertEqual(self.result,0)
    def testcase08(self):
        '''不传入phone参数添加嘉宾失败'''
        self.data.pop('phone')
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where email="%s";'
        self.result = self.em.execute_sql(sql %(self.data['email']))
        self.assertEqual(self.res['status'],int(response_data[2][0]))
        self.assertEqual(self.res['message'],response_data[2][1])
        self.assertEqual(self.result,0)
    def testcase09(self):
        '''传入不存在的eid参数添加嘉宾失败'''
        sql = 'select event_id from sign_guest'
        self.em.execute_sql(sql)
        self.e_id = self.em.get_allsql_result()
        self.error_id = []
        for i in self.e_id:
            self.error_id.append(i[0])
        while True:
            self.g_id = self.gd.get_num(0,2147483647)
            if self.g_id not in self.error_id:
                self.data['eid'] = self.g_id
                break
        self.data['phone'] = '17' + str(self.gd.get_num(100000000, 999999999))
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where event_id="%d";'
        self.result = self.em.execute_sql(sql %(self.data['eid']))
        self.assertEqual(self.res['status'],int(response_data[3][0]))
        self.assertEqual(self.res['message'],response_data[3][1])
        self.assertEqual(self.result,0)
    def testcase10(self):
        '''在status为0的发布会添加嘉宾失败'''
        sql = 'select id from sign_event where status=0;'
        self.em.execute_sql(sql)
        self.e_id = self.em.get_sql_result()
        self.data['eid'] = self.e_id
        self.data['phone'] = '18' + str(self.gd.get_num(100000000, 999999999))
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[4][0]))
        self.assertEqual(self.res['message'],response_data[4][1])
        self.assertEqual(self.result,0)
    def testcase11(self):
        '''在人数已满的发布会添加嘉宾失败'''
        self.data['eid'] = 10010
        self.data['phone'] = '19' + str(self.gd.get_num(100000000, 999999999))
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[5][0]))
        self.assertEqual(self.res['message'],response_data[5][1])
        self.assertEqual(self.result,0)
    def testcase12(self):
        '''在开始时间已过的发布会添加嘉宾失败'''
        self.data['eid'] = 1
        self.data['phone'] = '13' + str(self.gd.get_num(100000000, 999999999))
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[6][0]))
        self.assertEqual(self.res['message'],response_data[6][1])
        self.assertEqual(self.result,0)
    def testcase13(self):
        '''传入重复的phone参数添加嘉宾失败'''
        sql = 'select phone from sign_guest where event_id !=10010'
        self.em.execute_sql(sql)
        self.data['phone'] = self.em.get_sql_result()
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s" and realname="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone'],self.data['realname']))
        self.assertEqual(self.res['status'],int(response_data[7][0]))
        self.assertEqual(self.res['message'],response_data[7][1])
        self.assertEqual(self.result,0)
    def testcase14(self):
        '''传入10位长度的phone参数添加嘉宾失败'''
        self.data['phone'] = '13' + str(self.gd.get_num(10000000, 99999999))
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[8][0]))
        self.assertEqual(self.res['message'],response_data[8][1])
        self.assertEqual(self.result,0)
    def testcase15(self):
        '''传入12位长度的phone参数添加嘉宾失败'''
        self.data['phone'] = '13' + str(self.gd.get_num(1000000000, 9999999999))
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[8][0]))
        self.assertEqual(self.res['message'],response_data[8][1])
        self.assertEqual(self.result,0)
    def testcase16(self):
        '''传入非1开头的phone参数添加嘉宾失败'''
        self.data['phone'] = '3' + str(self.gd.get_num(1000000000, 9999999999))
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[8][0]))
        self.assertEqual(self.res['message'],response_data[8][1])
        self.assertEqual(self.result,0)
    def testcase17(self):
        '''传入第二位非3、5、7、8、9的phone参数添加嘉宾失败'''
        while True:
            self.p = self.gd.get_num(0,9)
            if self.p not in (3,5,7,8,9):
                self.data['phone'] = '1' + str(self.p)+str(self.gd.get_num(100000000, 999999999))
                break
        self.r = requests.post(Add_GuestURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_guest where phone="%s";'
        self.result = self.em.execute_sql(sql %(self.data['phone']))
        self.assertEqual(self.res['status'],int(response_data[8][0]))
        self.assertEqual(self.res['message'],response_data[8][1])
        self.assertEqual(self.result,0)

if __name__ == 'main':
    unittest.main()

