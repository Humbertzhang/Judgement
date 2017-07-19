# Judgement-i---Semi-sutomatic Flask API Test Tool
***
![Markdown](http://i2.kiimg.com/1949/339853871a89da2f.jpg)
***
### Usage
    python judgement.py
    Input api's floder.
    Judgement will auto wirte static content of an api test in the ./testByJudgement/test.py file.
    ***
    ### Description of auto generated content
    1,If there are "register" or "signup" in you api's function name, it will generate `def test_a_apiname(self):`
    2,If there are "signin" or "login" in you api's name, it will generate `def test_b_apiname(self):`
    3,For Other apis, It will generate `def test_c_apiname(self):`
    4,It will Identify the method(Include `POST` `GET` `PUT` `DELETE`) witch the api need and auto generate corresponding content.
    5,For those apis which need be used by `POST` or `PUT` method,and need json.dumps({}) content, Judgement will generate `"key":"test"` json data according to the content of apis' `get_json().get('key')` statement.
    ***
    ### Demo

    [![judge_demo.gif](https://storage2.cuntuku.com/2017/07/14/judge_demo.gif)](https://cuntuku.com/image/44PCc)



    ***
    zh-ch
    ***


    # Judgement－－半自动化Flask api测试工具
    ![Markdown](http://i2.kiimg.com/1949/339853871a89da2f.jpg)
     

     ***
     ### 用法：
     python judgement.py

     根据提示输入　api所在文件夹

     程序输出自动生成了测试的api所在的文件名以及改文件下测试了什么api

     生成testByJudgement文件夹和 testByJudgement/test.py文件

     test.py文件下便有自动生成的测试


     ***

     ### 关于自动生成的测试的说明：
     1,若api中有`register`或`signup`字样，生成 def test_a_apiname(self):

     2,若api中有`signin`或`login`字样，生成 def test_b_apiname(self):

     3,其余api生成 def test_c_apiname(self):

     4,对于需要用POST或PUT方法发送 json.dumps({})的api，会根据get_json().get('content')括号中的内容自动生成json语句.如：'content':'test'

     5,仓库中testByjudgement文件夹中的test.py 为judgement.py根据test_apis文件夹生成的测试文件，以供参考

     ***
     ### 示例
     [![judge_demo.gif](https://storage2.cuntuku.com/2017/07/14/judge_demo.gif)](https://cuntuku.com/image/44PCc)

