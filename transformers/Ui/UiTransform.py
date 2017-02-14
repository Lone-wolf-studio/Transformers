from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('transformers', 'templates'))

class BootstrapTransform:
	def create_template(self, template_name, title=None):
		self.template_name = template_name
		self.title = title
		if ".html" not in self.template_name:
			self.template_name = self.template_name + ".html"
		template = env.get_template('bootstrap_template.html')
		return template


	def create_layout(self, rows):
		pass

	