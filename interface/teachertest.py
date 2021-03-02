import requests
import unittest

class testteacher(unittest.TestCase):

    def testlogin(self):
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet"
        data = {
            "method" : "login",
            "loginname" : "wrm",
            "password" : "123456",
        }
        expect = "菜单"
        response = requests.post(url=url,data=data)
        response.encoding = "utf-8"
        data = response.text
        self.assertIn(expect,data)


    def testFindAllTeacher(self):
        #准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllTeacher"
        data = {}
        expect = 200 #期望数据
        # 调用被测接口
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        # 取出状态码和响应数据
        code = response.status_code
        txt = response.text
        # 断言
        print(txt)
        self.assertEqual(expect,code)


    def testfindAllMenu(self):

        url = "http://www.jasonisoft.cn:8080/HKR/MenuServlet?method=findAllMenu"
        data = {}
        expect = 200 #期望结果
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        # 取出状态码和响应数据
        code = response.status_code
        txt = response.text
        # 断言
        print(txt)
        self.assertEqual(expect, code)

    def testfindAllPicture(self):
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllPicture"
        data = {}
        expect = 200 # 期望结果
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        # 取出状态码和响应数据
        code = response.status_code
        txt = response.text
        # 断言
        print(txt)
        self.assertEqual(expect,code)

    def testfindAllStudent(self):
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllStudent"
        data = {}
        expect = 200
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        code = response.status_code
        txt = response.text
        print(txt)
        self.assertEqual(expect,code)

    def testfindAllCourse(self):
        url = "http://www.jasonisoft.cn:8080/HKR/CourseServlet?method=findAllCourse"
        data = {}
        expect = 200 # 期望结果
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        code = response.status_code
        txt = response.text
        print(txt)
        self.assertEqual(expect,code)

    def testindAllTeacherMenu(self):
        url = "http://www.jasonisoft.cn:8080/HKR/MenuServlet?method=findAllTeacherMenu"
        data = {}
        expect = 200
        response = requests.post(url=url, data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        print(txt)
        self.assertEqual(expect, code)

    def testgetTodeAllEvaluate(self):
        url = "http://www.jasonisoft.cn:8080/HKR/EvaluateServlet?method=getTodayAllEvaluate"
        data = {}
        expect = 200
        response = requests.post(url=url, data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        print(txt)
        self.assertEqual(expect, code)

    def testreportAll(self):
        url = "http://www.jasonisoft.cn:8080/HKR/EvaluateServlet?method=reportAll"
        data = {}
        expect = 200
        response = requests.post(url=url, data=data)
        response.encoding = "utf-8"
        code = response.status_code
        txt = response.text
        print(txt)
        self.assertEqual(expect, code)