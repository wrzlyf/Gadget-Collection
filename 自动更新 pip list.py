#! python3

###
# 功能1：如果是 新装的python软件，自动安装必备的第三方包（预装列表）
#      *1. 对于新装的python，安装第三方包前需要对自身的pip库进行版本检查，
#           如果版本不是最新版的，则需要先对pip库进行升级
#       2. 然后根据本文件中存有的"列表清单" 依次安装第三方库 
#      *3. 安装完毕后，将当前系统中的所有 第三方库列表 覆盖到预装列表
#      *4. 将预装列表的内容从json移到本文件中
#
#
#
#
# 功能2：如果是 已有的python软件，自动更新所有已安装的包    [本功能使用频率更高]
#      *1. 更新第三方包前，需要对自身的pip库进行版本检查
#           如果版本不是最新版的，则需要先对pip库进行升级
#       2. 然后检查当前所需要升级的第三方库 （使用 python list -o）
#       3. 根据检查的结果，依次对需要升级的第三方库进行升级
#      *4. 升级完毕后，将当前系统中的所有 第三方库列表 覆盖到预装列表中
#      *5. 将预装列表的内容从json移到本文件中
# 
# 
# ###

#----------------------------------------------------------------
def Get_Dictionary_PackageList():
    ###
    # 功能： 获得预装列表
    # 输入值：\
    # 输出值：字典
    # 最后结果为 一个字典
    # 该字典的 item 为 {package：version}
    # ###

    Get_Dictionary_PackageList={}
    ## PACKAGELIST START ##

    Get_Dictionary_PackageList={
    "asn1crypto": "0.24.0",
    "astroid": "2.2.5",
    "cachetools": "3.1.0",
    "certifi": "2019.3.9",
    "cffi": "1.12.3",
    "chardet": "3.0.4",
    "colorama": "0.4.1",
    "cryptography": "2.6.1",
    "Django": "2.2.1",
    "earthengine-api": "0.1.175",
    "et-xmlfile": "1.0.1",
    "google-api-python-client": "1.7.8",
    "google-auth": "1.6.3",
    "google-auth-httplib2": "0.0.3",
    "httplib2": "0.12.3",
    "idna": "2.8",
    "isort": "4.3.20",
    "jdcal": "1.4.1",
    "lazy-object-proxy": "1.4.1",
    "mccabe": "0.6.1",
    "numpy": "1.16.3",
    "oauth2client": "4.1.3",
    "openpyxl": "2.6.2",
    "pandas": "0.24.2",
    "pip": "19.1.1",
    "pyasn1": "0.4.5",
    "pyasn1-modules": "0.2.5",
    "pycparser": "2.19",
    "pylint": "2.3.1",
    "pyOpenSSL": "19.0.0",
    "python-dateutil": "2.8.0",
    "pytz": "2019.1",
    "requests": "2.22.0",
    "rsa": "4.0",
    "setuptools": "41.0.1",
    "six": "1.12.0",
    "sqlparse": "0.3.0",
    "typed-ast": "1.3.5",
    "uritemplate": "3.0.0",
    "urllib3": "1.25.2",
    "wrapt": "1.11.1"
}   
    ## PACKAGELIST END ##
    return Get_Dictionary_PackageList

#----------------------------------------------------------------
def Insert_Command_into_cmd(Command_Lind):
    ###
    # 功能： 对 subprocess.Popen的封装
    # 输入值：命令行 （string）
    # 输出值：\
    # ###

    import subprocess
    import time
    p = subprocess.Popen(Command_Lind,shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=False)
    
    time.sleep(10)  # 等待10s

    return p
    #if p.returncode != 0:
        #p.kill()            # 关闭进程

#----------------------------------------------------------------
def Split_String(String_Unprocessed):
    ###
    # 功能： 拆分'pip list' package 与 version
    # 输入值：stirng
    # 输出值：字典
    # 最后结果为 一个字典
    # 该字典的 item 为 {package：version}
    # ###


    import re
    
    Regex_Number = re.compile(r'\d')
    mo_Number=Regex_Number.search(String_Unprocessed)
    
    try:        # 用于避免 命令行中 开头的干扰

        Number=mo_Number.group()

        re_rule_Package=r'([^(\s)]+)'
        re_rule_Version=r'(\d+)(\.)(\d+)((\.)?(\d+)?)*'

        Package = str_processed_by_Regular(String_Unprocessed,re_rule_Package)
        Version = str_processed_by_Regular(String_Unprocessed,re_rule_Version)

        dict_Package_Version={}
        dict_Package_Version['Package']=Package
        dict_Package_Version['Version']=Version

        return dict_Package_Version
        print('test')
    except:
        pass


#----------------------------------------------------------------

def str_processed_by_Regular(str_raw,re_rule):
    ###
    #
    # 功能： 通过正则表达式 从原文本中提取需要的字符
    # 输入值：
    #       str_raw:需要被正则表达式处理的原文本
    #       re_rule：需要使用到的正则表达式
    # 输出值：处理过后的字符串(一个字符串)
    #
    # ###

    
    import re

    # re_rule=re_rule.replace('\\',r'\\')     # 取消对字符串变量的转义
    Regex_Pattern = re.compile(re_rule)
    Regex_mo = Regex_Pattern.search(str_raw)
    str_after_regex=Regex_mo.group()

    return str_after_regex

#----------------------------------------------------------------
def Enter_Data_into_json(dict_data):
    ###
    # 功能：将数据存入json文件中
    # 输入值：字典
    # 输出值：/
    #  ###

    import json
    import os
    
    Path_json_file=os.getcwd() + ('\\test_data.json')
    json_str=json.dumps(dict_data,indent=4)

    with open(Path_json_file,'w') as json_file:
        json_file.write(json_str)
        json_file.close()
        return Path_json_file
#----------------------------------------------------------------

def Create_New_py_File(Path_json_file):

    ###
    # 功能：生成新的 自动更新.py 文件
    # 输入值：字典
    # 输出值：/
    #  ###

    import os
    import json
    #import pprint

    json_file=open(Path_json_file)
    current_path=os.getcwd()
    fileList=os.walk(current_path)
    for dirPath,dirNames,fileNames in fileList:
        for fileName in fileNames:
            FileFullName=os.path.join(dirPath,fileName)
            if FileFullName==current_path + '\\自动更新 pip list.py':
                FileFullName_current=FileFullName
                break

    FileFullName_New=current_path + '\\自动更新 pip list_New.py'

    file_py_current=open(FileFullName_current,'r',encoding='utf-8')
    file_py_New= open(FileFullName_New,'w',encoding='utf-8')

    bl_PACKAGELIST_START=False
    bl_PACKAGELIST_END=False

    for single_line in file_py_current.readlines():
        if bl_PACKAGELIST_START==False and bl_PACKAGELIST_END==False:
            file_py_New.writelines(single_line)
            if '## PACKAGELIST START ##' in single_line:
                bl_PACKAGELIST_START=True
                json_content=json.load(json_file)
                file_py_New.write('    Get_Dictionary_PackageList=')
                json.dump(json_content,file_py_New,indent=4)

        elif bl_PACKAGELIST_START==True and bl_PACKAGELIST_END==True:
            file_py_New.writelines(single_line)
        else:
            if '## PACKAGELIST END ##' in single_line:
                file_py_New.writelines('\n' + single_line)
                bl_PACKAGELIST_END=True

        print(single_line.rstrip())

    file_py_New.close()
    print('test')
#----------------------------------------------------------------

def Check_the_Library_Need_to_be_Upgraded():
    
    ###
    # 功能：检查当前系统下，有多少第三方库需要更新
    # 输入值：/
    # 输出值：list(需要更新的第三方库的 列表)
    #  ###

    list_Package_Need_to_be_Upgraded=[]

    p=Insert_Command_into_cmd('pip list -o')
    #p.kill()

    for eachline in iter(p.stdout.readline,b''):
        eachline_str = eachline.decode(encoding='UTF-8')
        print(eachline_str)

        try:
            each_package=str_processed_by_Regular(eachline_str,r'([^(\s)]+)')
            if 'Package' not in each_package and '---' not in each_package:
                list_Package_Need_to_be_Upgraded.append(each_package)               # 制作更新时要用到的列表
        except: 
            pass


    return list_Package_Need_to_be_Upgraded



#----------------------------------------------------------------

def Check_pip_package():
    
    ###
    # 功能：检查 pip 库是否需要更新
    # 
    # 输入：/
    # 输出：True -> 需要更新 / False -> 已是最新版
    # 
    # ###

    import subprocess


    p=Insert_Command_into_cmd('pip list -o')

    for eachline in iter(p.stdout.readline,b''):
        eachline_str = eachline.decode(encoding='UTF-8')
        print(eachline_str)

        try:
            each_package=str_processed_by_Regular(eachline_str,r'([^(\s)]+)')
            if each_package=='pip':
                return True
                pass
        except:
            pass
        
        
        

#-----------------------------------------------------------------

def Update_pip_Version():

    ###
    # 功能：在 cmd 中，输入更新pip的命令，进行更新
    # 输入：/
    # 输出：/
    # 
    # ###
    
    
    
    import subprocess
    # python -m pip install --upgrade pip

    p=Insert_Command_into_cmd('python -m pip install --upgrade pip')

    for eachline in iter(p.stdout.readline,b''):
        eachline_str = eachline.decode(encoding='UTF-8')
        print(eachline_str)     # 显示 python -m pip install --upgrade pip 的运行过程

        Installation_Result = False     # 初始化
        if eachline_str.find('Successfully installed')!= -1:        # '-1' -> 表示字符未找到
            Installation_Result = True                                # True-> 安装成功 / False -> 安装失败 
            break   # 如果已经检测到 安装成功的提示，直接退出循环
    
    
    #p.kill()
    return Installation_Result
    
def Install_Packages(list_Packages):

    ###
    # 功能：安装 list_Packages 中存在的所有 packages
    # 输入：list_Packages
    # 输出：/
    # 
    # ###

    import subprocess

    for eachpackage in list_Packages:
        Command_Statement='pip install --upgrade %s' % (eachpackage)

        p=Insert_Command_into_cmd(Command_Statement)


        for eachline in iter(p.stdout.readline,b''):
            eachline_str = eachline.decode(encoding='UTF-8')
            print(eachline_str)     # 显示 python -m pip install --upgrade pip 的运行过程




#-----------------------------------------------------------------

# Main Program #
###
# 1. 检查 pip verison
# 2. 获得当前系统中的 所有packages
# 
# ###
import subprocess
import os

## test ##

#json_test=os.getcwd() + '\\test_data.json'
#Create_New_py_File(open(json_test))
## test ##


pip_needUpdate = Check_pip_package()

if pip_needUpdate == True:        # True-> 需要更新
    Status_Update_pip=False # 初始化
    Status_Update_pip = Update_pip_Version()        # 执行更新命令
    
    if Status_Update_pip == True:
        print('pip has been updated to the latest version.')
    else:
        print('pip is not the lateset version')


dict_allPackage_current={}      # 现有系统中的 packages
list_Package_Need_to_be_Updated=[]  # 需要更新的 package 列表

p=Insert_Command_into_cmd('pip list')

#将 packages 制作成字典{packages：version}---(现有系统中的)
for eachline in iter(p.stdout.readline,b''):
   
    eachline_str = eachline.decode(encoding='UTF-8')
    if eachline_str =='':       # 防止意外的空行出现
        break  
    dict_eachPackage = Split_String(eachline_str)       # 单个package字典 {package:version}
    
    try:    # 用于避免 命令行中 开头的干扰
        if 'WARNING:' not in dict_eachPackage['Package']:   # 避免 Warning的干扰
            dict_allPackage_current[dict_eachPackage['Package']]=dict_eachPackage['Version']
    except:
        pass


# 判断 dict_allPackage_current 字典内的项目数 (<5 疑似新安装的系统,>5 非新安装的系统)

if dict_allPackage_current.__len__()<5: # 新安装，重新安装
    print("test")
    list_Package_Need_to_be_Updated=[]
    list_Package_Need_to_be_Updated=Get_Dictionary_PackageList().keys()
    Install_Packages(list_Package_Need_to_be_Updated)

else:   # >5 说明是更新现有的库，而非重新安装
    print('Updating...')
    list_Package_Need_to_be_Updated = Check_the_Library_Need_to_be_Upgraded()
    Install_Packages(list_Package_Need_to_be_Updated)



# 将字典内容写入json
Path_json_file=Enter_Data_into_json(dict_allPackage_current)   # json： 当前系统中的packages

# 生成新的 .py 文件
Create_New_py_File(Path_json_file)
    







print('DONE')
