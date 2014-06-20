#получаем имя класса, на вход список строк всего класса
def getClassName(content):
	classNameLine = ''
	for line in content:
		if 'class' in line:
			classNameLine = line
	pos1 = classNameLine.find('class') + 5
	pos2 = classNameLine.find('{')
	className = classNameLine[pos1:pos2]
	className = className.strip()
	return className
#Получаем список имен всех public методов класса, на вход список строк всего класса
def getPublicMethodsList(content):
	nameMethodLineList = ['']
	nameMethodList = ['']
	for line in content:
		if 'public' in line.lower():
			if '(' in line:
				if ')' in line:
					if '{' in line:
						nameMethodLineList.append(line.lower())
	name = ''
	for item in nameMethodLineList:
		if '(' in item:
			if ')' in item:
				bracketspos1 = item.find('(')
				bracketspos2 = item.find(')')
				sizeBetweenBrackets = bracketspos2 - bracketspos1
				if sizeBetweenBrackets > 2:
					pass
					#обработка случая метода с аргументами(если есть что-то между скобками)
					#возможно вернуть массив с аргументами??
				else:
					pos1 = item.find('public') + 6
					pos2 = item.find('{')
					name = item[pos1:pos2]
					name = name.rstrip()#удаляем пробелы в конце строки
					if (len(name) > 1):
						i = len(name) - 1
						nameMethod = ''
						while i != 0:
							if name[i] == ' ':
								nameMethod = name[i:]
							i = i - 1
						nameMethod = nameMethod.strip()#удаляем пробелы в начале и в конце строки
						nameMethodList.append(nameMethod)
						name = ''
						pos1 = 0
						pos2 = 0
	#удаляем пустые елементы списка
	nameMethodList = filter(None,nameMethodList)#быстрое удаление
	nameMethodList = list(nameMethodList)
	return nameMethodList
