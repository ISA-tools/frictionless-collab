from copy import deepcopy
from dataflows.helpers.resource_matcher import ResourceMatcher


def pivot(join_field, key_field, value_field, resources=None):
    def func(package):
        matcher = ResourceMatcher(resources, package.pkg)

        # Meta (pre)
        for resource in package.pkg.descriptor['resources']:
            if matcher.match(resource['name']):
                fields = resource['schema']['fields']
                fields = list(filter(lambda field: field['name'] != key_field, fields))
                fields = list(filter(lambda field: field['name'] != value_field, fields))
                resource['schema']['fields'] = fields
        package.pkg.commit()
        yield package.pkg

        # Data
        for resource in package:
            if not matcher.match(resource.res.name):
                yield resource
            if matcher.match(resource.res.name):
                groups = {}
                new_field_names = set()
                for row in resource:
                    groups.setdefault(row[join_field], {})
                    groups[row[join_field]][row[key_field]] = row[value_field]
                    new_field_names.add('_'.join([key_field, row[key_field]]))
                rows = []
                for group_name, group_data in groups.items():
                    row = {join_field: group_name}
                    for group_data_key, group_data_value in group_data.items():
                        row['_'.join([key_field, group_data_key])] = group_data_value
                    rows.append(row)
                yield iter(rows)

        # Meta (post)
        for resource in package.pkg.descriptor['resources']:
            if matcher.match(resource['name']):
                fields = resource['schema']['fields']
                for new_field_name in new_field_names:
                    fields.append(
                        {'name': new_field_name, 'type': 'string', 'format': 'default'}
                    )
                resource['schema']['fields'] = fields
        package.pkg.commit()

    return func
