from base import Base
from database_connectivity_bridge import DatabaseConnectivity
from errors import Errors

class Transform(Base, DatabaseConnectivity, Errors):
	def transform_database(self):
		self.database_name = database_name
		self.username = username
		self.password = password
		self.host = host


