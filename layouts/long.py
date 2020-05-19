from pprint import pprint
from dataflows import Flow, load
from processors.pivot import pivot

# Run flow
flow = Flow(
    load('layouts/long.csv'),
    pivot(join_field='name', key_field='treatment', value_field='result'),
)
results, package, stats = flow.results()
print('[Data]\n')
pprint(results[0])
print('\n[Meta]\n')
pprint(package.descriptor)
