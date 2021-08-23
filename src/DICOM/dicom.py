
# 20210120，Python读取影像DICOM文件  
########安装pydicom包：pip install pydicom
#Pydicom支持DICOM格式的读取：可以将dicom文件读入python结构，同时支持修改后的数据集可以再次写入DICOM格式文件。但需要注意，它不是被设计为查看图像，主要是用来操作DICOM文件的各种数据元素。
import pydicom
import os

########安装matplotlib绘图库：pip install matplotlib  -i https://pypi.tuna.tsinghua.edu.cn/simple
#镜像安装：-i https://pypi.tuna.tsinghua.edu.cn/simple
import matplotlib.pyplot as plt

#1.调用dicom文件
file_path="DICOM\dome.dcm"

#2.显示dicom图像
ds = pydicom.dcmread(file_path)
plt.figure(figsize=(10, 10))
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
plt.show() 

#3.读取dicom文件信息
dcm =pydicom.read_file(file_path)
info={}
info["PatientID"] = dcm.PatientID               # 患者ID
info["PatientName"] = dcm.PatientName           # 患者姓名
# info["PatientBirthData"] = dcm.PatientBirthData # 患者出生日期
info["PatientAge"] = dcm.PatientAge             # 患者年龄
info['PatientSex'] = dcm.PatientSex             # 患者性别
info['StudyID'] = dcm.StudyID                   # 检查ID
info['StudyDate'] = dcm.StudyDate               # 检查日期
info['StudyTime'] = dcm.StudyTime               # 检查时间
info['InstitutionName'] = dcm.InstitutionName   # 机构名称
info['Manufacturer'] = dcm.Manufacturer         # 设备制造商
info['StudyDescription']=dcm.StudyDescription   # 检查项目描述 """
print(info)
