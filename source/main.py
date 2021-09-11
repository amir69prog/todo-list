import sqlite3
import sys
import datetime
import time 
from PyQt5.QtWidgets import (
	QMainWindow,
	QLayout,
	QSizePolicy,
	QLabel,
	QApplication,
	QCheckBox,
	QListWidgetItem,
	QWidget,
	QHBoxLayout,
	QDesktopWidget
)
from PyQt5 import QtCore,QtGui
from ui_mainwindow import Ui_MainWindow
from ui_itemwidget import Ui_Form


class TaskWindow(QWidget):
	def __init__(self,item):
		super(TaskWindow,self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.item = item
		self.task = todo_app.ui.list.itemWidget(self.item)
		self.set_data()
		self.settings()

		# Signals
		self.ui.delete_2.clicked.connect(self.delete)
		self.ui.done.clicked.connect(self.done)
		self.ui.save.clicked.connect(self.update)


	def settings(self):
		self.setFixedSize(457,148)


	def get_date(self,date,format_):
		""" Get the date from str """
		datetime_ = datetime.datetime.strptime(date,format_)
		return datetime_.date()


	def get_time(self,date,format_):
		""" Get the time from str """
		datetime_ = datetime.datetime.strptime(date,format_)
		return datetime_.time()


	def set_data(self):
		""" Set The Data in widgets """
		self.ui.task.setText(self.task.title)
		date = self.get_date(self.task.timestamp[:19],'%Y-%m-%d %H:%M:%S')
		time = self.get_time(self.task.timestamp[:19],'%Y-%m-%d %H:%M:%S')
		self.ui.time.setTime(QtCore.QTime(time))
		self.ui.date.setDate(QtCore.QDate(date))


	def delete(self):
		""" Send request to remove and delete task """
		self.hide()
		todo_app.delete_task(self.item)


	def done(self):
		""" Done Task """
		self.hide()
		todo_app.done_task(self.task)


	def update(self):
		""" Update the Task's data """
		self.hide()
		title = self.ui.task.text()
		time = self.ui.time.time()
		date = self.ui.date.date()
		datetime_ = datetime.datetime.combine(date.toPyDate(),time.toPyTime())
		todo_app.update_task(self.item,title,datetime_)


class Task(QWidget):
	def __init__(self,title,status,timestamp,id_,item):
		super().__init__()
		self.title = title
		self.status = status
		self.timestamp = timestamp
		self.id = id_
		self.item = item


		self.title_widget = QLabel(self)
		self.title_widget.setStyleSheet("color:rgb(184, 184, 184);font-size:18px;background:none;")
		self.title_widget.setGeometry(QtCore.QRect(20, 0, 120, 41))
		
		self.status_widget = QCheckBox(self.title,self)
		self.status_widget.setGeometry(QtCore.QRect(0, -10, 20, 41))

		self.settings()

		# Signals 
		self.status_widget.stateChanged.connect(self.checked_task)


	def settings(self):
		""" Set The Configurations """
		self.title_widget.setText(self.title)
		self.status_widget.setChecked(self.status)
		self.title_widget.adjustSize()

	def checked_task(self):
		""" Set Done Task """
		todo_app.done_task(self)



class Todo(QMainWindow):
	def __init__(self):
		super().__init__()
		# Attrs
		self.title = 'Todo List'

		# database
		self.db = 'todo.db'
		self.connection = sqlite3.connect(self.db)
		self.cursor = self.connection.cursor()
		self.create_table()
		
		# ui
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.settings()


		# Signals
		self.ui.insert.clicked.connect(self.insert_task)
		self.ui.list.itemDoubleClicked.connect(self.item_clicked)
		
		self.fetch_tasks()


	def settings(self):
		""" Set the Configuration """
		self.ui.task.setPlaceholderText('your task to do')
		self.setWindowTitle(self.title)
		self.setFixedSize(500,500)
		self.setWindowIcon(QtGui.QIcon('../images/tick.png'))


	def create_table(self):
		""" Creation The Task Table on data base """
		query = """
			CREATE TABLE IF NOT EXISTS Task(
				id integer PRIMARY KEY,
				title varchar(255) NOT NULL,
				status boolean DEFAULT 0,
				datetime timestamp
			)
		"""
		self.cursor.execute(query)
		self.connection.commit()



	def make_task_widget(self,title,status,datetime,id_,item):
		task = Task(title,status,datetime,id_,item)
		return task


	def get_task(self,id):
		""" Get the Task from Data Base """
		query = f'SELECT * FROM Task WHERE id={id}'
		self.cursor.execute(query)
		return self.cursor.fetchone()


	def insert_to_list(self,task_id):
		""" Inserting The Task in Front-End """
		task = self.get_task(task_id)
		id_ = task[0]
		title = task[1]
		status = bool(task[2])
		datetime = task[3]

		# item = QListWidgetItem()
		# item_widget = self.make_task_widget(title,status,datetime,id_,item)
		# item.setSizeHint(item_widget.sizeHint())
		# self.ui.list.addItem(item)
		# self.ui.list.setItemWidget(item,item_widget)
		self.fetch_tasks()


	def insert_to_database(self,title,datetime):
		""" Inserting The Task in Back-End """
		query = 'INSERT INTO Task(id,title,datetime) VALUES(NULL,?,?)'
		self.cursor.execute(query,(title,datetime))
		self.connection.commit()
		self.ui.task.setText('')

		task_id = self.cursor.lastrowid
		return task_id


	def insert_task(self):
		''' Insert Task to List and Table '''
		title = self.ui.task.text()
		datetime_ = datetime.datetime.now()
		if title:
			# insert to table
			task_id = self.insert_to_database(title,datetime_)

			# insert to list
			self.insert_to_list(task_id)


	def display_tasks(self,tasks):
		""" Display All Task in Front-End """
		self.ui.list.clear()
		if tasks:
			for task in tasks:
				id_ = task[0]
				title = task[1]
				status = bool(task[2])
				datetime = task[3]

				item = QListWidgetItem()
				item_widget = self.make_task_widget(title,status,datetime,id_,item)
				item.setSizeHint(item_widget.sizeHint())
				self.ui.list.addItem(item)
				self.ui.list.setItemWidget(item,item_widget)
		else:
			item = QListWidgetItem('You Have no tasks')
			self.ui.list.addItem(item)

	def fetch_tasks(self):
		""" Get All Active Tasks """
		query = 'SELECT * FROM Task WHERE status=0 ORDER BY datetime DESC;'
		self.cursor.execute(query)
		tasks = self.cursor.fetchall()
		self.display_tasks(tasks)


	def remove_task(self,row_item):
		""" Remove task from list """
		self.ui.list.takeItem(row_item)
		if self.ui.list.count() == 0:
			item = QListWidgetItem('You Have no tasks')
			self.ui.list.addItem(item) 


	def disable_task(self,task_id):
		""" Set disabled the task """
		query = f'UPDATE Task SET status=1 WHERE id={task_id}'
		self.cursor.execute(query)
		self.connection.commit()


	def done_task(self,task):
		""" Remove From List View And Set Disabled Task in Back-end """
		row_item = self.ui.list.row(task.item)
		self.remove_task(row_item)

		task_id = task.id
		self.disable_task(task_id)


	def item_clicked(self,item):
		try:
			self.task_window = TaskWindow(item)
			fg = self.task_window.frameGeometry()
			desktop_center = QDesktopWidget().availableGeometry().center() 
			fg.moveCenter(desktop_center)
			self.task_window.move(fg.topLeft())
			self.task_window.show()
		except Exception as err:
			print(err)

	def delete_task_db(self,task_id):
		""" Delete task from databse """
		query = f'DELETE From Task WHERE id={task_id}'
		self.cursor.execute(query)
		self.connection.commit()


	def delete_task(self,item):
		""" Delete Task from list and data base """
		task = self.ui.list.itemWidget(item)
		row_item = self.ui.list.row(item)

		# delete from database
		self.delete_task_db(task.id)

		# delete from list
		self.remove_task(row_item)


	def update_task_db(self,task_id,title,datetime):
		query = f'UPDATE Task SET title=\'{title}\',datetime=\'{datetime}\' WHERE id={task_id}'
		self.cursor.execute(query)
		self.connection.commit()


	def update_task(self,item,title,datetime):
		""" Update Task """
		task = self.ui.list.itemWidget(item)
		# update from database
		self.update_task_db(task.id,title,datetime)
		# edit item in list

		# get the new task information and set widget to item
		# new_task = self.get_task(task.id)
		# # data
		# id_ = new_task[0]
		# title = new_task[1]
		# status = bool(new_task[2])
		# datetime = new_task[3]
		# # new widget
		# new_widget = self.make_task_widget(title,status,datetime,id_,item)
		# self.ui.list.setItemWidget(item,new_widget)
		self.fetch_tasks()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	todo_app = Todo()
	todo_app.show() 
	app.exec_()