class Base:
	username = ""
	password = ""
	host = ""
	def database_credentials(self, username, password, host):
		self.username = username
		self.password = password
		self.host = host
		return (self.username, self.password, self.host)

