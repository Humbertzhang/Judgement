import os

def Static_Content():


    # import things
    ListOfImport = \
        ["import unittest\n",
         "from flask import current_app, url_for,jsonify\n",
         "from flask_sqlalchemy import SQLAlchemy\n",
         "import random\n",
         "import json\n"]
    ftest.writelines(ListOfImport)

    ListOfThings = \
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


def API_Test_Content(api_add):
    # Open File that need be tested
    f = open(api_add, 'r')
    AllLines = f.readlines()

    for i in range(len(AllLines)):
        if "@api.route" in AllLines[i]:
            count = 0
            while (True):
                if "@" in AllLines[i] or "#" in AllLines[i] or AllLines[i].strip()=='':
                    count += 1
                    i += 1
                else:
                    break

            index1 = AllLines[i].find("def")
            index2 = AllLines[i].find("(")
            str = AllLines[i][index1 + 4:index2]
            
            print str

            # special api
            if "register" in str or "signup" in str:
                ftest.writelines([
                                    "    #Test " + str,
                                    "\n    def test_a_" + str + "(self):\n"
                                ])

            elif "signin" in str or "login" in str:
                ftest.writelines([
                                    "    #Test "+str,
                                    "\n    def test_b_" + str + "(self):\n"
                                ])

            else:
                ftest.writelines([
                                    "    #Test "+str,
                                    "\n    def test_c_" + str + "(self):\n"
                                ])
            ###End special api


            # find out methods
            if "POST" in AllLines[i - count]:
                ftest.writelines(
                    ["        response = self.client." + "post" + "(\n",
                     "            url_for('api." + str + "',_external=True),\n",
                     "            data = json.dumps({\n"])
                
                #POST json data
                j=0
                while("return" not in AllLines[j+i-count]):
                    if "get_json()" in AllLines[j+i-count]:
                        
                        index1 = AllLines[j+i-count].find("().get")
                        
                        if "\"" in AllLines[j+i-count][index1+8:-1]:
                            index2 = AllLines[j+i-count][index1+8:-1].find("\"")+index1+8
                        elif "\'" in AllLines[j+i-count][index1+8:-1]:
                            index2 = AllLines[j+i-count][index1+8:-1].find("\'")+index1+8
                        else:
                            index2 = -1
                        attr = AllLines[j+i-count][index1+8:index2]
                        ftest.writelines([" "*16 +"\"" + attr + "\":'test',\n"])
                    j+=1
                           

                #End of post json data
                ftest.writelines(
                    ["            }),\n",
                     "            content_type = 'application/json')\n",
                     "        self.assertTrue(response.status_code == 200)\n\n"])
                
                
            elif "PUT" in AllLines[i - count]:
                ftest.writelines(
                    ["        response = self.client." + "put" + "(\n",
                     "            url_for('api." + str + "',_external=True),\n",
                     "            data = json.dumps({\n"])
                
                #PUT json data
                j=0
                while("return" not in AllLines[j+i-count]):
                    if "get_json()" in AllLines[j+i-count]:
                        
                        index1 = AllLines[j+i-count].find("().get")
                        if "\"" in AllLines[j+i-count][index1+8:-1]:
                            index2 = AllLines[j+i-count][index1+8:-1].find("\"")+index1+8
                        elif "\'" in AllLines[j+i-count][index1+8:-1]:
                            index2 = AllLines[j+i-count][index1+8:-1].find("\'")+index1+8
                        
                        attr = AllLines[j+i-count][index1+8:index2]
                        ftest.writelines([" "*16 +"\"" + attr + "\":'test',\n"])
                    j+=1
                           

                #End of post json data
                ftest.writelines(
                    ["            }),\n",
                     "            content_type = 'application/json')\n",
                     "        self.assertTrue(response.status_code == 200)\n\n"])
                
            
            elif "DELETE" in AllLines[i - count]:
                ftest.writelines(
                    ["        response = self.client." + "delete" + "(\n",
                     "            url_for('api." + str + "',_external=True),\n",
                     "            content_type = 'application/json')\n",
                     "        self.assertTrue(response.status_code == 200)\n\n"]
                )
            elif "GET" in AllLines[i - count]:
                ftest.writelines(
                    ["        response = self.client." + "get" + "(\n",
                     "            url_for('api." + str + "',_external=True),\n",
                     "            content_type = 'application/json')\n",
                     "        self.assertTrue(response.status_code == 200)\n\n"]
                )

            else:
                ftest.writelines(
                    ["        response = self.client." + "XXXX" + "(\n"]
                )
                ftest.writelines(
                    ["            url_for('api." + str + "',_external=True),\n",
                     "            content_type = 'application/json')\n",
                     "        self.assertTrue(response.status_code == 200)\n\n"]
                )
            
            # End Of find out methods
            f.close()


if __name__ == "__main__":
    print '''

+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++
                   judgement                    
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++xxxxxxxxxxxxxxxxxx++++++++++++++++
+++++++++++++++xxxooooooooooooxxx++++++++++++++++
               xxxooooooooooooxxx               
+++++++++++++++xxxooo      oooxxx++++++++++++++++
+++++++++++++++xxxooo      oooxxx++++++++++++++++
+++++++++++++++xxxooo      oooxxx++++++++++++++++
               xxxooooooooooooxxx               
+++++++++++++++xxxxooowwwwoooxxxx++++++++++++++++
++++++++++++++++++xxxooooooxxx+++++++++++++++++++
++++++++++++++++++++++xxxx+++++++++++++++++++++++
                       xx                      
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++

    '''
#http://www.text-image.com/convert/
    
    API_Floder = raw_input("API Floder Address:")
    files = os.listdir(API_Floder)


    # new Open Test File
    if os.path.isdir("testByJudgement"):
        pass
    else:
        os.mkdir("testByJudgement")

    if os.path.isfile("testByJudgement/test.py"):
        pass
    else:
        with open("testByJudgement/test.py","w+") as f:
            f.close()

    ftest = open("./testByJudgement/test.py", "w+")
    #End Open Test File
    apis = []
    for i in range(len(files)):
        if '.py' in files[i] and '.pyc' not in files[i]:
            apis.append(files[i])


    file_addes = []
    for i in range(len(apis)):
        file_addes.append(API_Floder +'/'+apis[i])

    Static_Content()


    for i in range(len(file_addes)):
        print '\n-------------API file Name-----------'
        print file_addes[i]
        ftest.writelines(["\n"+" "*4 + "#----------API FILE NAME:"+ file_addes[i] + "-------------------\n\n"])
        print '-----------------APIS----------------'
        API_Test_Content(file_addes[i])

    ftest.close()
