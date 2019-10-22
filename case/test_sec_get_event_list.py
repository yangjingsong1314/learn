import unittest,requests
from util.utils import Create_Data,Execute_Mysql,Sec_Get_Event_ListURL,DATAPATH,get_data

file = DATAPATH+'/test_sec_get_event_list.csv'
response_data = get_data(file)
file = DATAPATH+'/ifo_auth.csv'
auth_data = get_data(file)
class Test_Sec_Get_Event_List(unittest.TestCase):
    '''带用户认证的发布会查询接口'''
    def setUp(self):
        self.em = Execute_Mysql()
        self.em.con_mysql()
        self.gd = Create_Data()
        self.data = {}
        sql = 'select id from sign_event'
        self.em.execute_sql(sql)
        self.e_id = self.em.get_allsql_result()
        self.data['eid'] = self.e_id[self.gd.get_num(0,len(self.e_id)-1)][0]
        sql = 'select name from sign_event where id="%d";'
        self.em.execute_sql(sql %(self.data['eid']))
        self.data['name'] = self.em.get_sql_result()[0]
    def tearDown(self):
        self.em.con_mysql()
    def testcase01(self):
        '''正确传入所有参数查询成功'''
        self.r = requests.get(Sec_Get_Event_ListURL,self.data,auth=tuple(auth_data[1]))
        self.res = self.r.json()
        self.assertEqual(self.res['status'],int(response_data[1][0]))
        self.assertEqual(self.res['message'],response_data[1][1])
        self.assertEqual(self.res['data']['eid'],self.data['eid'])
        self.assertEqual(self.res['data']['name'],self.data['name'])
    def testcase02(self):
        '''只传eid查询成功'''
        self.data.pop('name')
        self.r = requests.get(Sec_Get_Event_ListURL,self.data,auth=tuple(auth_data[1]))
        self.res = self.r.json()
        self.assertEqual(self.res['status'],int(response_data[1][0]))
        self.assertEqual(self.res['message'],response_data[1][1])
        self.assertEqual(self.res['data']['eid'],self.data['eid'])
    def testcase03(self):
        '''只传name查询成功'''
        self.data.pop('eid')
        self.r = requests.get(Sec_Get_Event_ListURL,self.data,auth=tuple(auth_data[1]))
        self.res = self.r.json()
        self.assertEqual(self.res['status'],int(response_data[1][0]))
        self.assertEqual(self.res['message'],response_data[1][1])
        self.assertEqual(self.res['data'][0]['name'],self.data['name'])
    def testcase04(self):
        '''不传参数查询发布会失败'''
        self.data.pop('eid')
        self.data.pop('name')
        self.r = requests.get(Sec_Get_Event_ListURL,self.data,auth=tuple(auth_data[1]))
        self.res = self.r.json()
        self.assertEqual(self.res['status'],int(response_data[4][0]))
        self.assertEqual(self.res['message'],response_data[4][1])
    def testcase05(self):
        '''传入不存在的eid查询发布会失败'''
        while True:
            self.error_id = self.gd.get_num(0,2147483647)
            if self.error_id not in self.e_id:
                self.data['eid'] = self.error_id
                break
        self.r = requests.get(Sec_Get_Event_ListURL,self.data,auth=tuple(auth_data[1]))
        self.res = self.r.json()
        self.assertEqual(self.res['status'],int(response_data[5][0]))
        self.assertEqual(self.res['message'],response_data[5][1])
    def testcase06(self):
        '''传入错误的auth密码查询发布会失败'''
        self.r = requests.get(Sec_Get_Event_ListURL,self.data,auth=tuple(auth_data[2]))
        self.res = self.r.json()
        self.assertEqual(self.res['status'],int(response_data[3][0]))
        self.assertEqual(self.res['message'],response_data[3][1])
    def testcase07(self):
        '''传入错误的auth用户名查询发布会失败'''
        self.r = requests.get(Sec_Get_Event_ListURL,self.data,auth=tuple(auth_data[3]))
        self.res = self.r.json()
        self.assertEqual(self.res['status'],int(response_data[3][0]))
        self.assertEqual(self.res['message'],response_data[3][1])
    def testcase08(self):
        '''传入错误的auth用户名和密码查询发布会失败'''
        self.r = requests.get(Sec_Get_Event_ListURL,self.data,auth=tuple(auth_data[4]))
        self.res = self.r.json()
        self.assertEqual(self.res['status'],int(response_data[3][0]))
        self.assertEqual(self.res['message'],response_data[3][1])
    def testcase09(self):
        '''auth密码为空查询发布会失败'''
        self.r = requests.get(Sec_Get_Event_ListURL,self.data,auth=tuple(auth_data[5]))
        self.res = self.r.json()
        self.assertEqual(self.res['status'],int(response_data[3][0]))
        self.assertEqual(self.res['message'],response_data[3][1])
    def testcase10(self):
        '''auth用户名为空查询发布会失败'''
        self.r = requests.get(Sec_Get_Event_ListURL,self.data,auth=tuple(auth_data[6]))
        self.res = self.r.json()
        self.assertEqual(self.res['status'],int(response_data[3][0]))
        self.assertEqual(self.res['message'],response_data[3][1])
    def testcase11(self):
        '''auth用户名和密码都为空查询发布会失败'''
        self.r = requests.get(Sec_Get_Event_ListURL,self.data,auth=tuple(auth_data[7]))
        self.res = self.r.json()
        self.assertEqual(self.res['status'],int(response_data[3][0]))
        self.assertEqual(self.res['message'],response_data[3][1])
    def testcase12(self):
        '''不传auth查询发布会失败'''
        self.r = requests.get(Sec_Get_Event_ListURL,self.data)
        self.res = self.r.json()
        self.assertEqual(self.res['status'],int(response_data[2][0]))
        self.assertEqual(self.res['message'],response_data[2][1])

if __name__ == 'main':
    unittest.main()