#!/usr/bin/env python
#! coding:utf-8

from datetime import datetime,timedelta
from pickle import dump,load
from todocontainer import Todocontainer
from todo import Todoitem
import cmd

DUMPFILE="todo.dat"

class Todoshell(cmd.Cmd):
	intro="welcome to the todo shell. Type help or ? to list commands.\n"
	prompt=">>>"

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.app=Todoapp()

	def emptyline(self):
		pass

	def do_show(self,arg):
		"show remain your tasks"
		self.app.itemconfirmation()

	def do_showf(self,arg):
		"show finished tasks"
		self.app.itemconfirmation_finished()

	def do_add(self,arg):
		"add new task to this todo-list"
		self.app.createitem()

	def do_exit(self,arg):
		"Stop using todoapp,close the todoshell"
		print("Thank you 4 using!")
		return True

class Todoapp:
	def __init__(self):
		self.load()

	# print remaining todoitem
	def itemconfirmation(self):
		self.todos.sort()
		for todo in self.todos.get_remaining_todos():
			d=todo.duedate
			t=todo.title
			if todo.duedate<datetime.now():
				t='*!* '+t
			print("{0}\n-->{1}\n-->...{2}".format(d,t,todo.description))

	# create todoitem
	def createitem(self):
		todo=Todoitem("","",datetime.now())
		self.entry_item(todo)
		self.todos+=todo
		self.save()

	# reflect entering item to todoitem
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

	def itemconfirmation_finished(self):
		self.todos.sort()
		for todo in self.todos.get_finished_todos():
			d=todo.duedate
			t=todo.title
			print("{0}\n-->{1}\n-->...{2}".format(d,t,todo.description))

	# load date
	def load(self):
		try:
			f=open(DUMPFILE,'rb')
			self.todos=load(f)
			f.close()
		except IOError:
			self.todos=Todocontainer()

	# save date
	def save(self):
		f=open(DUMPFILE,'wb')
		dump(self.todos,f)
		f.close()

if __name__=="__main__":
	Todoshell().cmdloop()