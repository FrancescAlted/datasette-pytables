import tables

def inspect(path):
    "Open file and return tables info"
    h5tables = {}
    views = []
    h5file = tables.open_file(path)

    for table in filter(lambda node: not(isinstance(node, tables.group.Group)), h5file):
        colnames = []
        if isinstance(table, tables.table.Table):
            colnames = table.colnames

        h5tables[table._v_pathname] = {
            'name': table._v_pathname,
            'columns': colnames,
            'primary_keys': [],
            'count': table.nrows,
            'label_column': None,
            'hidden': False,
            'fts_table': None,
            'foreign_keys': {'incoming': [], 'outgoing': []},
        }

    h5file.close()
    return h5tables, views
