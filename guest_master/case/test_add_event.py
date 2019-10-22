import unittest,sys,requests
sys.path.append('../')
from util.utils import Create_Data,Execute_Mysql,Add_EventURL,DATAPATH,get_data,get_time

file = DATAPATH+'/add_event.csv'
response_data = get_data(file)
class Test_Add_Event(unittest.TestCase):
    '''添加发布会接口'''
    def setUp(self):
        self.gd = Create_Data()
        self.data = {}
        self.data['eid'] = self.gd.get_num(0,2147483647)
        self.data['name'] = '华为'+str(self.data['eid'])+'发布会'
        self.data['limit'] = self.gd.get_num(1,5000)
        self.data['status'] = self.gd.get_num(0,1)
        self.data['address'] = self.gd.get_address()
        self.data['start_time'] = self.gd.get_future_time()
        self.em = Execute_Mysql()
        self.em.con_mysql()
    def tearDown(self):
        self.em.close_mysql()
    def testcase01(self):
        '''正确传入所有参数添加发布会成功'''
        sql = 'select id from sign_event'
        self.em.execute_sql(sql)
        self.e_id = self.em.get_allsql_result()
        self.error_id = []
        for i in self.e_id:
            self.error_id.append(i[0])
        while True:
            self.true_id = self.gd.get_num(0,2147483647)
            if self.true_id not in self.error_id:
                self.data['eid'] = self.true_id
                break
        self.r = requests.post(Add_EventURL,self.data)
        self.em.con.autocommit(True)
        self.res = self.r.json()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        self.result = self.em.execute_sql(sql %(self.data['eid'],self.data['name']))
        self.assertEqual(self.res['status'],int(response_data[1][0]))
        self.assertEqual(self.res['message'],response_data[1][1])
        self.assertEqual(self.result,1)
    def testcase02(self):
        '''不传入eid参数添加发布会失败'''
        self.data.pop('eid')
        self.r = requests.post(Add_EventURL,self.data)
        self.res = self.r.json()
        sql = 'select * from sign_event where name="%s";'
        self.result = self.em.execute_sql(sql %(self.data['name']))
        self.assertEqual(self.res['status'],int(response_data[2][0]))
        self.assertEqual(self.res['message'],response_data[2][1])
        self.assertEqual(self.result,0)
    def testcase03(self):
        '''传入11位长度且不重复的eid添加发布会失败'''
        self.data['eid'] = int(self.gd.get_password(11,0,1,0,0,))
        self.r = requests.post(Add_EventURL,self.data)
        self.res = self.r.json()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        self.result = self.em.execute_sql(sql %(self.data['eid'],self.data['name']))
        self.assertEqual(self.res['status'],int(response_data[7][0]))
        self.assertEqual(self.res['message'],response_data[7][1])
        self.assertEqual(self.result,0)
    def testcase04(self):
        '''传入重复的eid参数添加发布会失败'''
        sql = 'select id from sign_event'
        self.em.execute_sql(sql)
        self.data['eid'] = self.em.get_sql_result()[0]
        self.r = requests.post(Add_EventURL,self.data)
        self.res = self.r.json()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        self.result = self.em.execute_sql(sql %(self.data['eid'],self.data['name']))
        self.assertEqual(self.res['status'],int(response_data[3][0]))
        self.assertEqual(self.res['message'],response_data[3][1])
        self.assertEqual(self.result,0)
    def testcase05(self):
        '''不传入name参数添加发布会失败'''
        self.data.pop('name')
        self.r = requests.post(Add_EventURL,self.data)
        self.res = self.r.json()
        sql = 'select * from sign_event where id="%d";'
        self.result = self.em.execute_sql(sql %(self.data['eid']))
        self.assertEqual(self.res['status'],int(response_data[2][0]))
        self.assertEqual(self.res['message'],response_data[2][1])
        self.assertEqual(self.result,0)
    def testcase06(self):
        '''传入长度为21位的name参数添加发布会失败'''
        self.data['name'] = self.gd.get_password(21,1,1,1,1)
        self.r = requests.post(Add_EventURL,self.data)
        self.res = self.r.json()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        self.result = self.em.execute_sql(sql %(self.data['eid'],self.data['name']))
        self.assertEqual(self.res['status'],int(response_data[6][0]))
        self.assertEqual(self.res['message'],response_data[6][1])
        self.assertEqual(self.result,0)
    def testcase07(self):
        '''传入重复的name参数添加发布会失败'''
        sql = 'select name from sign_event'
        self.em.execute_sql(sql)
        self.data['name'] = self.em.get_sql_result()[0]
        self.r = requests.post(Add_EventURL,self.data)
        self.res = self.r.json()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        self.result = self.em.execute_sql(sql %(self.data['eid'],self.data['name']))
        self.assertEqual(self.res['status'],int(response_data[4][0]))
        self.assertEqual(self.res['message'],response_data[4][1])
        self.assertEqual(self.result,0)
    def testcase08(self):
        '''不传入limit参数添加发布会失败'''
        self.data.pop('limit')
        self.r = requests.post(Add_EventURL,self.data)
        self.res = self.r.json()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        self.result = self.em.execute_sql(sql %(self.data['eid'],self.data['name']))
        self.assertEqual(self.res['status'],int(response_data[2][0]))
        self.assertEqual(self.res['message'],response_data[2][1])
        self.assertEqual(self.result,0)
    def testcase09(self):
        '''传入错误的status添加发布会失败'''
        self.data['status'] = self.gd.get_num(2,10)
        self.r = requests.post(Add_EventURL,self.data)
        self.res = self.r.json()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        self.result = self.em.execute_sql(sql %(self.data['eid'],self.data['name']))
        self.assertEqual(self.res['status'],int(response_data[8][0]))
        self.assertEqual(self.res['message'],response_data[8][1])
        self.assertEqual(self.result,0)
    def testcase10(self):
        '''不传入status参数添加发布会失败'''
        self.data.pop('status')
        self.r = requests.post(Add_EventURL,self.data)
        self.res = self.r.json()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        self.result = self.em.execute_sql(sql %(self.data['eid'],self.data['name']))
        self.assertEqual(self.res['status'],int(response_data[2][0]))
        self.assertEqual(self.res['message'],response_data[2][1])
        self.assertEqual(self.result,0)
    def testcase11(self):
        '''不传入address参数添加发布会失败'''
        self.data.pop('address')
        self.r = requests.post(Add_EventURL,self.data)
        self.res = self.r.json()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        self.result = self.em.execute_sql(sql %(self.data['eid'],self.data['name']))
        self.assertEqual(self.res['status'],int(response_data[2][0]))
        self.assertEqual(self.res['message'],response_data[2][1])
        self.assertEqual(self.result,0)
    def testcase12(self):
        '''不传入start_time参数添加发布会失败'''
        self.data.pop('start_time')
        self.r = requests.post(Add_EventURL,self.data)
        self.res = self.r.json()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        self.result = self.em.execute_sql(sql %(self.data['eid'],self.data['name']))
        self.assertEqual(self.res['status'],int(response_data[2][0]))
        self.assertEqual(self.res['message'],response_data[2][1])
        self.assertEqual(self.result,0)
    def testcase13(self):
        '''传入格式错误的start_time添加发布会失败'''
        self.data['start_time'] = get_time()
        self.r = requests.post(Add_EventURL,self.data)
        self.res = self.r.json()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        self.result = self.em.execute_sql(sql %(self.data['eid'],self.data['name']))
        self.assertEqual(self.res['status'],int(response_data[5][0]))
        self.assertIn(response_data[5][1],self.res['message'])
        self.assertEqual(self.result,0)

if __name__ == 'main':
    unittest.main()
