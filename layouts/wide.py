from pprint import pprint
from dataflows import Flow, load, unpivot

# Select unpivoing fields
unpivoting_fields = [{'name': 'treatment_(\w)', 'keys': {'treatment': r'\1'}}]

# A newly created column header would be 'year' with type 'year':
extra_keys = [{'name': 'treatment', 'type': 'string'}]

# And values will be placed in the 'result' column with type 'string':
extra_value = {'name': 'result', 'type': 'string'}

# Run flow
flow = Flow(load('layouts/wide.csv'), unpivot(unpivoting_fields, extra_keys, extra_value))
results, package, stats = flow.results()
print('[Data]\n')
pprint(results[0])
print('\n[Meta]\n')
pprint(package.descriptor)
