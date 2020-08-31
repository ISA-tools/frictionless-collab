from datapackage import Package
from goodtables import validate
import os

__author__ = 'proccaserra (Philippe Rocca-Serra)'

# author: philippe rocca-serra (philippe.rocca-serra@oerc.ox.ac.uk)
# ontology: http://www.stato-ontology.org

cwd = os.getcwd()
os.chdir('./covid19-case-counts')

print("from:", cwd)

dpsch1 = 'nhsn-covid-19-patient-module-denominator-table.json'
dpsch2 = 'covid-19-case-tally-spain-report-table.json'

packages = [dpsch1, dpsch2]

file1 = 'nhsn-covid-19-patient-module-denominator-table.csv'
file2 = 'serie_historica_acumulados.csv'

files = [file1, file2]

try:
    for counter in range(len(packages)):
        print('json:', packages[counter])
        print('csv:', files[counter])
        try:
            pack = Package(packages[counter])
            pack.valid
            print("really?", pack.valid)
            pack.errors
            for e in pack.errors:
                print(e)
            print(pack.profile.name)

            report = validate(files[counter])
            print(report)

        except IOError as e:
            print(e)

except IOError as e:
    print(e)
