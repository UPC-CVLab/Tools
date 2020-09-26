import os
import re
import sys
import csv
import pandas as pd

# 根据csv文件中的内容对pdf文件进行批量重命名
def renameall():
	"""
	① 请先安装好相应依赖库
	② 确保pdf文件和csv文件在同一路径，且pdf文件按原始序号升序排列
	③ 指定info_path 与 file_path,路径前的r请保留，否则可能会报错
	"""
	
	# csv 文件存放路径。如：
	# info_path = r"D:\200-Study-学习文件\240-Learning-Master\01-论文\03-最新\2020\IJCAI 2020\test\IJCAI2020-Paper_Info.csv"
	info_path = r"[TODO]"

	# pdf 文件存放路径。如：
	# file_path = r"D:\200-Study-学习文件\240-Learning-Master\01-论文\03-最新\2020\IJCAI 2020\test"
	file_path = r"[TODO]"
	
	# 获取文件标题信息
	data = pd.read_csv(info_path,encoding="ISO-8859-1")           	#读取csv文件
	titleList = data['Title'].tolist()
	# print(titleList) # print title list

	# 获取pdf文件列表
	fileList = os.listdir(file_path)#待修改文件夹
	# print("修改前："+str(fileList))		#输出文件夹中包含的文件
	currentpath = os.getcwd()		#得到进程当前工作目录
	os.chdir(file_path)		#将当前工作目录修改为待修改文件夹的位置
	
	# 批量修改文件名
	for idx in range(len(titleList)):
			pat=".+\.(pdf)"		#匹配文件名正则表达式
			pattern = re.findall(pat,fileList[idx])		#进行匹配
			os.rename(fileList[idx],(str(idx+1).zfill(4)+'-'+titleList[idx].replace(':','_').replace('?','').replace('/','_')+'.'+pattern[0]))		#文件重新命名
	print("------------------------------------------------")
	os.chdir(currentpath)		#改回程序运行前的工作目录
	sys.stdin.flush()		#刷新
	# print("修改后："+str(os.listdir(file_path)))		#输出修改后文件夹中包含的文件
	print("OK")
renameall()