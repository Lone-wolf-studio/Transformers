import json
import MySQLdb
import pymongo
import os
from collections import OrderedDict



class MysqlTransform:
	def transform_to(self, database_type):
		self.database_type = database_type
	def mysql_database_name(self, database_name):
		self.database_name = database_name	
	def mysql_username(self, user_name):
		self.username = username
	def mysql_password(self, password):
		self.password = password		