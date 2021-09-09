from PyQt5.QtWidgets import QMainWindow,QSizePolicy,QLabel,QApplication,QCheckBox,QListWidgetItem,QWidget,QHBoxLayout
from ui_mainwindow import Ui_MainWindow
from PyQt5 import QtCore,QtGui
import sqlite3
import sys
import datetime
import time 


class Task(QWidget):
	def __init__(self,title,status,timestamp,id_,item):
		super().__init__()
		self.title = title
		self.status = status
		self.timestamp = timestamp
		self.id = id_
		self.item = item

		self.title_widget = QLabel(self)
		self.title_widget.setGeometry(QtCore.QRect(20, -10, 380, 41))
		self.title_widget.setStyleSheet("color:rgb(184, 184, 184);font-size:18px")

		self.status_widget = QCheckBox(self)
		self.status_widget.setGeometry(QtCore.QRect(0, -10, 20, 41))


		self.settings()

		# Signals 
		self.status_widget.stateChanged.connect(self.checked_task)


	def settings(self):
		""" Set The Configurations """
		self.title_widget.setText(self.title)
		self.status_widget.setChecked(self.status)

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

		# ui
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.settings()


		# Signals
		self.ui.insert.clicked.connect(self.insert_task)
		
		self.fetch_tasks()


	def settings(self):
		""" Set the Configuration """
		self.ui.task.setPlaceholderText('your task to do')
		self.setWindowTitle(self.title)
		self.setFixedSize(500,500)
		self.setWindowIcon(QtGui.QIcon('../tick.png'))



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

		item = QListWidgetItem()
		item_widget = Task(title,status,datetime,id_,item)
		item.setSizeHint(item_widget.sizeHint())
		self.ui.list.addItem(item)
		self.ui.list.setItemWidget(item,item_widget)


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
		for task in tasks:
			id_ = task[0]
			title = task[1]
			status = bool(task[2])
			datetime = task[3]

			item = QListWidgetItem()
			item_widget = Task(title,status,datetime,id_,item)
			item.setSizeHint(item_widget.sizeHint())
			self.ui.list.addItem(item)
			self.ui.list.setItemWidget(item,item_widget)


	def fetch_tasks(self):
		""" Get All Active Tasks """
		query = 'SELECT * FROM Task WHERE status=0 ORDER BY datetime;'
		self.cursor.execute(query)
		tasks = self.cursor.fetchall()
		self.display_tasks(tasks)


	def remove_task(self,row_item):
		""" Remove task from list """
		self.ui.list.takeItem(row_item)


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



if __name__ == '__main__':
	app = QApplication(sys.argv)
	todo_app = Todo()
	todo_app.show() 
	app.exec_()