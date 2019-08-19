class DatabaseConnectivity:
	database_name = ""
	database_type = ""
	def connect_database(self, database_name, database_type):
		self.database_name = database_name
		self.database_type = database_type
		return (self.database_name, self.database_type)

