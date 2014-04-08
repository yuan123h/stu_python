'''
Created on 2014-4-8

@author: yuanhuan
'''

class SchoolMember:
    '''
    Represents any school member
    '''


    def __init__(self, name, age):
        '''
        Constructor
        '''
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s )' % self.name
        
    def tell(self):
        '''
        tell my details
        '''
        print 'Name:"%s" Age:"%s" ' % (self.name, self.age)
        
class Teacher(SchoolMember):
    '''
    represents a teacher
    '''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name
    
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary:"%d"' % self.salary
        
class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print 'Initailized Student: %s' % self.name
    
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks : %d' % self.marks
        
t = Teacher('wangli', 19, 5000)
s = Student('LiLei', 12, 69)
print # print a blank line

memners = [t,s]

for member in memners:
    member.tell()



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        