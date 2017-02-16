import json
import MySQLdb
import pymongo
import os
from collections import OrderedDict



class MysqlTransform:
	def __init__(self, username, password, database_name):
		self.username = username
		self.password = password
		self.database_name = database_name
		self.connector = MySQLdb.connect(user=username, passwd=password, db=db)
		self.cursor = self.connector.cursor()

	def transform_to(self, database_type):
		self.database_type = database_type
		return self.database_type.lower()

	def table_getter(self, database_name=self.database_name):
		query = "SHOW TABLES;"
		self.cursor.execute(query)
		self.fetcher = self.cursor.fetchall()
		return self.fetcher
			
	def transformer(self):
		query = ""	