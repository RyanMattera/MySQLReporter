#autoreport.py
#Working to take the data from a csv file and create a report that is then emailed to relevant parties

from jinja2 import FileSystemLoader, Environment

#content to be put in the report
content = "Hello, World!"

#Configures Jinja and ready the template
env = Environment (
	loader=FileSystemLoader(searchpath="templates")
	)
template = env.get_template("report.html")

def main():
	"""
	Entry Point for the script
	Render a template and write to file
	:return:
	"""
	with open("outputs/report.html", "w") as f:
	f.write(template.render(content=content))
	
	if __name__ == "__main__":
		main()
		
		