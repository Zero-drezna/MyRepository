#открыть и считать файл с классом в список
#забрать название класса
#получить список всез public методов
import sys
import myMethods as utils#импортируем функции под именем utils
print ('python ver: '+sys.version[:3])#print python version
inFile = open('class.txt')#файл с классом
content = inFile.readlines()
inFile.close()
className = utils.getClassName(content)#получаем имя класса
print('Class_Name = '+className)
methods = utils.getPublicMethodsList(content)
for x in methods:
	print(x)
print('count methods = '+str(len(methods)))