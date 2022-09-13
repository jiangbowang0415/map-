
import sys
sys.path.append('D:\王江波')
import pytest
from day4.yewu.modify_password import Modify_Password
from day4.common.excel import Excel




class Test_Modify_Password():

    modify_password_testdata = r'D:\王江波\day4\testdata\modifypassword_testdata.xlsx'
    ex = Excel()
    testcase_number = ex.get_testcase_number(modify_password_testdata)

    def setup(self): # 定义前置方法
        self.mp = Modify_Password() #实例化修改密码业务类对象
        self.driver = self.mp.driver_browser() # 驱动浏览器
    
    def teardown(self): # 定义后置方法
        self.driver.quit()


    @pytest.mark.parametrize('testcase_number',testcase_number) # 测试用例参数化
    def test_modify_password(self,testcase_number):
        try:
            func_name = sys._getframe().f_code.co_name # 获取当前函数名称
            td_dic = self.ex.get_testdata_by_id(self.modify_password_testdata, testcase_number)
            self.mp.login_oa_and_modify_password(self.driver, td_dic['旧密码'], td_dic['新密码'], td_dic['密码确认'])
            tip_info = self.mp.find_element_and_get_text(self.driver,self.mp.tip_element)
            if testcase_number == '004':
                print(tip_info)
                print(td_dic['断言'])
            assert tip_info == td_dic['断言']
        except:
            self.mp.get_web_img(self.driver, r'D:\王江波\day4\test_img', f'{func_name}_{testcase_number}')
            raise #抛出一次异常

    


if __name__ == '__main__':
    pytest.main(['-s',r'D:\王江波\day4\testcase\test_modify_password.py'])

