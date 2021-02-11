import asyncio
import aiomysql
from base import Base

class MysqlDriver:
	async def create_connectivity_pool(self):
		pool = await aiomysql.create_pool(host=self.host, port=self.port,
                  						  user=self.username, password=self.password,
                                          db=self.databasename, loop=loop)
		pool.close()
		await pool.wait_closed()