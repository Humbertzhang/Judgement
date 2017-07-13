# Judgement－－半自动化Flask api测试
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

4,对于需要用POST或PUT方法发送 json.dumps({)}的api，会根据get_json().get('content')括号中的内容自动生成json语句.如：'content':'test'

5,仓库中testByjudgement文件夹中的test.py 为judgement.py根据test_apis文件夹生成的测试文件，以供参考

***
示例
```shell
`python judgement.py`
APIS ADRESS:`test_apis`

-------------API file Name-----------
test_apis/forgive.py
-----------------APIS----------------
forgive

-------------API file Name-----------
test_apis/signin.py
-----------------APIS----------------
login

-------------API file Name-----------
test_apis/__init__.py
-----------------APIS----------------

-------------API file Name-----------
test_apis/getinfo.py
-----------------APIS----------------
get_info

-------------API file Name-----------
test_apis/signup.py
-----------------APIS----------------
signup

-------------API file Name-----------
test_apis/uploadtime.py
-----------------APIS----------------
upload_time

```
