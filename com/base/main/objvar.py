#!/usr/bin/python
#Filename:objvar.py

class Person:
	'''Represents a person. '''
	population = 0
	
	def __init__(self, name):
		'''Initializes the Person's data '''
		self.name = name
		print '(Initializes %s)' % self.name
		# when this Person is created , he/she adds to the population
		Person.population += 1
	def __del__(self):
		''' I am dying '''
		print '%s say goodbye. ' % self.name
		Person.population -= 1
		if Person.population == 0:
			print 'I am the last one.'
		else :
			print 'There are still %d people left.' % Person.population
	
	def sayHi(self):
		''' Greeting by the Person.
		Really, that's all it does.'''
		print 'Hi, my name is %s' % self.name

	def howMany(self):
		''' Prints the current population. '''
		if Person.population == 0:
			print 'I am the last one.'
		else :
			print 'There are still %d people left.' % Person.population
		
swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('AbKam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()









