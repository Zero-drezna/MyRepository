#открыть и считать файл с классом в список
#забрать название класса
#получить список всез public методов
import sys
import myMethods as utils#импортируем функции под именем utils
import output as output#импортируем модуль вывода в файл как тест
print ('python ver: '+sys.version[:3])#print python version
inFile = open('class.txt')#файл с классом
content = inFile.readlines()
inFile.close()
className = utils.getClassName(content)#получаем имя класса
print('Class_Name = '+className)
methods = utils.getPublicMethodsList(content)#получаем список методов класса
for x in methods:
	print(x)
print('count methods = '+str(len(methods)))
output.writeTest(className, methods)#выводим в файл(пишем сам тест)