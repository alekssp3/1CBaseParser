# -*- coding: utf-8 -*-

def load(filename, coding='cp1251'):
	try:
		f = open(filename, 'rb+')
	except:
		print('Can\'t open file %s' % (filename))
	unicode_string = unicode(union(f.readlines()), coding)
	f.close()
	return unicode_string

def show(filename, size=32, seek=0):
	l = load(filename).readlines()
	print('Type: %s\nSize: %d' % (type(l), len(l)))
	return l

def del_nulls(l):
	ll = []
	for i in l:
		ll.append(i.replace('\0', ''))
	return ll

def union(ll):
	string = ''
	for i in ll:
		string += i
	return string

def clean(string, coding='cp1251'):
	tmp = u''
	abc = u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
	num = u'0123456789'
	smb = u'.,:; {}[]<>-\t'
	alphabet = abc + num + smb + abc.upper()

	for ch in string.lower():
		if unicode(ch, coding) in alphabet:
			tmp += unicode(ch, coding)

	tmp = tmp.replace(u'\tАШя', '\n')
	tmp = tmp.replace(u'в1Ья', '\t')
	tmp = tmp.replace(u'\tШяс ', '\t')
	tmp = tmp.replace(u'г\tШя', '\t')
	tmp = tmp.replace(u'зШя', ' ')
	tmp = tmp.replace(u'гШя', '\t')

	#tmp = tmp.replace(unicode(parse('{', tmp.encode('utf-8'), '}г'), coding), '')
	#tmp = tmp.replace(u'{}г', '')

	return tmp.encode('utf-8')

def save(string, filename, coding='utf-8'):
	f = open(filename, 'wb+')
	f.write(string)
	f.close()

def parse(what, where, stop_bit):
	tmp = ''
	start = 0
	stop = -1
	if where.find(what) > -1:
		start = where.find(what) + len(what)
	else:
		print('Not find %s', (what))
		return

	if type(stop_bit) == type(0):
		stop = start + stop_bit
	elif type(stop_bit) == type(''):
			if stop_bit.isalnum():
				stop = start + int(stop_bit)
			else:
				stop = where.find(stop_bit, start)

	if stop == -1:
		print('Stop bit not found')
		return

	#print ('Start: %d Stop: %d' % (start, stop))

	tmp = where[start:stop]
	return tmp

def cut(string, start_bit, stop_bit):
	start = string.find(start_bit)
	stop = string.find(stop_bit)
	return string.replace(string[start:stop + 1], '')