from datetime import date
today = str(date.today())

from jinja2 import FileSystemLoader, Environment

# Configure Jinja and ready the template
env = Environment(
    loader=FileSystemLoader(searchpath="templates")
)

#Assemble the templates we will use
base_template = env.get_template("report.html")
table_section_template = env.get_template("table_section.html")

# Content to be published
title = "Daily Report For %s" %today
sections = list()
sections.append(table_section_template.render(
department ="Curing",
dataset = "CuringReport.csv",
table ="Table Goes here."
))
sections.append(table_section_template.render(
deparment = "Deboning",
dataset = "DeboningReport.csv",
table = "Table Goes Here."
))



def main():
    """
    Entry point for the script.
    Render a template and write it to file.
    :return:
    """
    with open("outputs/report.html", "w") as f:
        f.write(base_template.render(
		title = title,
		sections = sections
		))


if __name__ == "__main__":
    main()
