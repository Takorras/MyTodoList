#!/usr/bin/env python
#! coding:utf-8

from datetime import datetime,timedelta
from pickle import dump,load
from todocontainer import Todocontainer
from todo import Todoitem

DUMPFILE="todo.dat"

class Todoapp:
	def __init__(self):
		self.load()

	def main(self):
		while True:
			print("\n[1]show tasks、[2]add task、[3]exit")
			operation=int(input("enter number :"))
			if operation==1:
				self.itemconfirmation()
			elif operation==2:
				self.createitem()
			else:
				print("Thanks! bye!")
				break

	# 未消化todoitemの表示
	def itemconfirmation(self):
		self.todos.sort()
		for todo in self.todos.get_remaining_todos():
			d=todo.duedate
			t=todo.title
			if todo.duedate<datetime.now():
				t='*!* '+t
			print("{0}\n-->{1}\n-->...{2}".format(d,t,todo.description))

	# todoitemを生成する
	def createitem(self):
		todo=Todoitem("","",datetime.now())
		self.entry_item(todo)
		self.todos+=todo
		self.save()

	# 入力した内容をtodoitemに反映
	def entry_item(self,todo):
		todo.title=input("enter task's title :")
		todo.description=input("enter task's description :")
		while True:
			try:
				todo.duedate=datetime.strptime(input("entry duedate...(year/month/date) :"),"%Y/%m/%d")
			except ValueError:
				print("please enter year/month/date :")
			else:
				break

	# データのロード
	def load(self):
		try:
			f=open(DUMPFILE,'rb')
			self.todos=load(f)
			f.close()
		except IOError:
			self.todos=Todocontainer()

	# データの保存
	def save(self):
		f=open(DUMPFILE,'wb')
		dump(self.todos,f)
		f.close()

if __name__=="__main__":
	app=Todoapp()
	app.main()
