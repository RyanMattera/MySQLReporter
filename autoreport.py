import pandas as pd
from jinja2 import FileSystemLoader, Environment

from datetime import date
today = str(date.today())

#Allow for very wide columns - otherwise columns are spaced and ellipse'd
pd.set_option("display.max_colwidth", 200)

def csv_to_html(filepath):
	"""
	Open a .csv and put in a HTML format.
	:param filepath: Filepath to a .csv to be read
	:return: String of HTML to be published.
	"""
	df = pd.read_csv(filepath, index_col=0)
	html = df.to_html()
	return html

# Configure Jinja and ready the template
env = Environment(
    loader=FileSystemLoader(searchpath="templates")
)

#Assemble the templates we will use
base_template = env.get_template("report.html")
table_section_template = env.get_template("table_section.html")

def main():
    """
    Entry point for the script.
    Render a template and write it to file.
    :return:
    """

# Content to be published
title = "Daily Report For %s" %today
sections = list()
sections.append(table_section_template.render(
department ="Curing",
dataset = "CuringReport.csv",
table =csv_to_html("datasets/CuringReport.csv")
))
sections.append(table_section_template.render(
department ="Deboning",
dataset = "DeboningReport.csv",
table =csv_to_html("datasets/DeboningReport.csv")
))
sections.append(table_section_template.render(
department ="Slicing",
dataset = "SliReport.csv",
table =csv_to_html("datasets/SlicingReport.csv")
))
with open("outputs/report.html", "w") as f:
    f.write(base_template.render(
	title = title,
	sections = sections
	))


if __name__ == "__main__":
    main()
