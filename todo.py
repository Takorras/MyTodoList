from datetime import datetime,timedelta

class Todoitem(object):

	def __init__(self,title,description,duedate,addeddate=None):
		#todoの項目を初期化

		if not addeddate:
			addeddate=datetime.now()
		self.title=title
		self.description=description
		self.duedate=duedate
		self.addeddate=addeddate
		self.finished=False
		self.finisheddate=None

	def finish(self,date=None):
		#todo項目の終了
		self.finished=True
		if not date:
			date=datetime.now()
		self.finisheddate=date

		def __repr__(self):
			#todo項目の表示形式文字列をつくる
			return "<ToDoItem{},{}>".format(self.title,self.duedate.strftime('%Y/%m/%d %H:%M'))
	
