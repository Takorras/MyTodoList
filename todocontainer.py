from datetime import datetime,timedelta

class Todocontainer(object):
	#todo項目のリストを保存するためのクラス

	def __init__(self):
		#todo項目のリストのインスタンスを初期化する
		self.todos=[]

	def __len__(self):
		#todo項目の数を返す
		return len(self.todos)

	def sort(self):
		#todoを締切日でソート
		self.todos.sort(key=lambda x : x.duedate)

	def __add__(self,item):
		#+演算子をエミュレートして、todo項目を追加する
		self.todos.append(item)
		self.sort()

	def __iadd__(self,item):
		#+=演算子をエミュレートして、todo項目を追加する
		self.__add__(item)
		return self

	def __getitem__(self,idx):
		#インデックスアクセスのエミュレート
		return self.todos[idx]

	def __setitem__(self,idx,item):
		#インデックスの代入をエミュレート
		self.todos[idx]=item
		self.sort()

	def __delitem__(self,idx):
		#インデックスを指定したdelをエミュレート
		del self.todos[idx]

	def get_remaining_todos(self):
		#終了していないtodo項目をリストとして返す
		return [t for t in self.todos if not t.finished]
