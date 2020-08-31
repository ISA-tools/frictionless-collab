from datapackage import Package
from goodtables import validate
import os

LOCAL="../datascriptor-fldatapackages"
# package_definition = os.path.join(LOCAL,'ekrt/elife-key-resource-table.json')
# file_to_test = os.path.join(LOCAL,'ekrt/elife-key-resources-example.csv')

# package_definition = os.path.join(LOCAL,'4-factor-tms/4-factor-treatment-mean-sem-table.json')
# file_to_test = os.path.join(LOCAL,'4-factor-tms/4-factor-treatment-mean-sem-table-example.csv')

# package_definition = os.path.join(LOCAL,'3-factor-tms/3-factor-treatment-mean-sem-table.json')
# file_to_test = os.path.join(LOCAL,'3-factor-tms/3-factor-treatment-mean-sem-table-example.csv')

# package_definition = os.path.join(LOCAL,'2-factor-tms/2-factor-treatment-mean-sem-table.json')
# file_to_test = os.path.join(LOCAL,'2-factor-tms/3-factor-treatment-mean-sem-table-example.csv')



def dpackage_validate():
	input_json = input("provide path to json package definition file:")
	input_tab = input("provide path the tabular package file to validate")

	try:

		#"covid-19-counts/covid-19-case-tally-report-table.json"

		if input_json.endswith(".json") and input_tab.endswith(".csv"):
			package_definition = os.path.join(LOCAL, input_json)
			print("package:", package_definition)
			pack = Package(package_definition)
			pack.valid
			print(pack.valid)
			pack.errors
			print(pack.errors)
			for e in pack.errors:
				print("error:",e)

			file_to_test = os.path.join(LOCAL, input_tab)
			print("csv file being tested:", file_to_test)
			#validating a csv files with GoodTables package
			report = validate(file_to_test, checks=['schema'])
			print(report)
			if report['valid'] is True:
				print("Success! \n")
				print(
					"\'" + file_to_test + "\'" + " is a valid Frictionless Tabular Data Package\n" + "It complies with its datapackage.json definition\n")
			else:
				print("hmmm, something went wrong. Please, see the validation report for tracing the fault")
				print(report)
		else:
				print("invalid input")

	except IOError as e:
	    print(e)


if __name__ == "__main__":
	print("running from main:")
	# print("JSON data package definition:", input_json)
	# print("csv file to evaluate:", input_tab)
	dpackage_validate()
