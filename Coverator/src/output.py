﻿def writeTest(className, methodsList):
	pass
	#className - имя класса
	#methodsList - список методов
	testFile = open('apexTest.txt','w')#открываем/создаем файл с тестом
	testFile.write('@isTest\n')#первой строчкой аннотрируем файл как тест Apex
	testFile.write('public class Test_'+ className + '{\n')#определяем класс теста
	#тут реализуем тестовый метод с вызовом методов из methodsList
	testFile.write('static testMethod void myUnitTest() {\n')#сам тестовый метод
	for item in methodsList:
		testFile.write(item + ';\n')#методы из списка методов
	testFile.write('}\n')#закрываем определение тестового метода
	testFile.write('}')#закрываем определение тестового класса
	testFile.close()