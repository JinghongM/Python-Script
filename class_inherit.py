# -*- coding: UTF-8 -*-
class Parent:        # 定义父类
   __parentAttr = 100
   def __init__(self):
      print "father build"
 
   def parentMethod(self):
      print 'father function'
 
   def setAttr(self, attr):
      Parent.__parentAttr = attr
 
   def getAttr(self):
      print "father attribute :", Parent.__parentAttr
 
class Child(Parent): # 定义子类
   def __init__(self):
      print "son build"
 
   def childMethod(self):
      print 'child function'
   def getAttr(self):
      print "son attribute :", Parent.__parentAttr
 
c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法