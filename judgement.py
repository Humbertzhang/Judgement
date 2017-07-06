import os

File_Address = raw_input("File Address:")

#Open File that need be tested
f = open(File_Address,'r')
AllLines = f.readlines()

#new Open Test File
if os.path.isdir("testByJudgement"):
	pass
else:
	os.mkdir("testByJudgement")

if os.path.isfile("testByJudgement/test.py"):
	pass
else:
	os.mknod("testByJudgement/test.py")

ftest = open("./testByJudgement/test.py","w+")

#import things
ListOfImport=\
			["import unittest\n",
			  "from flask import current_app, url_for,jsonify\n",
			  "from flask_sqlalchemy import SQLAlchemy\n",
			  "mport random\n",
			  "import json\n"]
ftest.writelines(ListOfImport)

ListOfThings=\
			["class BasicTestCase(unittest.TestCase):\n\n",
			 "    def setUp(self):\n",
			 "        self.app = create_app()\n",
			 "        self.app_context = self.app.app_context()\n",
			 "        self.app_context.push()\n",
			 "        self.client = self.app.test_client()\n",
			 "        db.create_all()\n\n",
			 "    def tearDown(self):\n",
			 "        db.session.remove()\n",
			 "        db.drop_all()\n",
			 "        self.app_context.pop()\n\n",
			 "    def test_app_exist(self):\n",
			 "        self.assertFalse(current_app is None)\n\n"]
ftest.writelines(ListOfThings)

for i in range(len(AllLines)):
	if "@api.route" in AllLines[i]:
		index1 = AllLines[i+1].find("def")
		index2 = AllLines[i+1].find("()")
		str = AllLines[i+1][index1+4:index2]

		#special api
		if "register" or "signup" in str:
			ftest.writelines(["    def test_a_"+str+"(self):\n"])
		elif "signin" or "login" in str:
			ftest.writelines(["    def test_b_"+str+"(self):\n"])
		else:
			ftest.writelines(["    def test_c_"+str+"(self):\n"])
		###End special api


		#find out methods
		if "POST" in AllLines[i]:
			ftest.writelines(
							["        response = self.client."+"post"+"(self):\n"]
			)

			ftest.writelines(
				["          url_for('api." + str + "',_external=True),\n",
				 "          data = json.dump({\n #Need complete}),\n",
				 "          content_type = 'application/json')\n",
				 "        self.assertTrue(response.status_code == 200)\n"]
			)

		elif "GET" in AllLines[i]:
			ftest.writelines(
							["        response = self.client."+"get"+"(self):\n"]
			)

			ftest.writelines(
					["          url_for('api."+str+"',_external=True),\n",
					 "          content_type = 'application/json')\n",
					 "        self.assertTrue(response.status_code == 200)"]
			)
		else:
			ftest.writelines(
							["        response = self.client."+"XXXX"+"(self):\n"]
			)
			ftest.writelines(
			["          url_for('api." + str + "',_external=True),\n",
			 "          content_type = 'application/json')\n",
			 "        self.assertTrue(response.status_code == 200)"]
			)
		#End Of find out methods

















