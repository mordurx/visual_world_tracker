#-*- coding:utf-8 -*-


import xlrd
import xlwt
class LeerExcel():
	
	
	def leer(self,path): #ruta del archivo a leer
		print path
		xl_workbook = xlrd.open_workbook(path)
		