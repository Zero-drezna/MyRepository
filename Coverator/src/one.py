#открыть и считать файл с классом в список
#Забрать название класса 
#получить список всех public методов
import sys
import myMethods as utils#импортируем функции под именем Utils
inFile = open('class.txt')#файл с классом
content = inFile.readlines()
inFile.close()
className = utils.getClassName(content)#Получаем имя класса
print('Class_Name = '+className)
methods = utils.getPublicMethodsList(content)#Получаем список имен методов класса(public, non-argument)
for x in methods:
	print(x)
print('count methods = '+str(len(methods)))
