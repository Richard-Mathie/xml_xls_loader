# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:14:11 2017

@author: richard
"""
from future.utils import iteritems
from xml.sax import ContentHandler
from defusedxml.sax import parse
from namedlist import namedlist, FACTORY, NO_DEFAULT
from collections import defaultdict
import pandas as pd

Data = namedlist('Data', [('attr', NO_DEFAULT),
                          ('data', FACTORY(list))])

Cell = namedlist('Cell', [('attr', NO_DEFAULT),
                          ('data', None)])

Row = namedlist('Row', [('attr', NO_DEFAULT),
                        ('cells', FACTORY(list))])

Table = namedlist('Table', [('attr', NO_DEFAULT),
                            ('name', None),
                            ('rows', FACTORY(list))])

conversions = {None: lambda x: x,
               'DateTime': lambda x: pd.to_datetime(x, utc=True),
               'String': lambda x: x,
               'Number': pd.to_numeric}


def get_methods(obj):
    methods = ((method, getattr(obj, method)) for method in dir(obj))
    return ((m, f) for m, f in methods if callable(f))


def get_tag_methods(methods, tag):
    return dict((m.replace(tag, ''), f) for m, f in methods if tag in m)


# Reference https://goo.gl/KaOBG3
class ExcelHandler(ContentHandler):
    def __init__(self):
        self.data = None
        self.cell = None
        self.row = None
        self.table = None
        self.tables = []
        self.worksheet = None

        methods = list(get_methods(self))
        self.start_methods = get_tag_methods(methods, '_start')
        self.end_methods = get_tag_methods(methods, '_end')

        self.start_methods.update(self.__format_method(self.start_methods))
        self.end_methods.update(self.__format_method(self.end_methods))

    def __format_method(self, methods):
        return dict(('ss:{}'.format(m), f) for m, f in iteritems(methods))

    def characters(self, content):
        if self.data:
            self.data.data.append(content)

    def _startData(self, atts):
        self.data = Data(atts)

    def _startCell(self, atts):
        self.cell = Cell(atts)

    def _startRow(self, atts):
        self.row = Row(atts)

    def _startTable(self, atts):
        self.table = Table(atts)

    def _startWorksheet(self, atts):
        self.worksheet = atts

    def nullfunc(self, *args, **kwargs):
        pass

    def _endData(self):
        self.data.data = "".join(self.data.data).strip()
        self.cell.data = self.data
        self.data = None

    def _endCell(self):
        self.row.cells.append(self.cell)

    def _endRow(self):
        self.table.rows.append(self.row)

    def _endTable(self):
        self.tables.append(self.table)

    def _endWorksheet(self):
        self.table.name = self.worksheet.get("ss:Name")

    def startElement(self, name, atts):
        atts = dict(atts)
        self.start_methods.get(name, self.nullfunc)(atts)

    def endElement(self, name):
        self.end_methods.get(name, self.nullfunc)()


def xmlxls_to_pd(attachment,
                 table=0,
                 header=0,
                 skiprows=None,
                 skip_footer=0,
                 merge_down=True):
    if skiprows is None:
        skiprows = header+1

    excelHandler = ExcelHandler()
    if isinstance(attachment, str):
        with open(attachment, 'r') as attachment:
            parse(attachment, excelHandler)
    else:
        parse(attachment, excelHandler)

    table = excelHandler.tables[table]

    header = table.rows[header]

    columns_index = {c.data.data: c.attr["ss:Index"] for c in header.cells}
    index_columns = {v: k for k, v in columns_index.items()}

    # print sorted(index_columns.items(), key=lambda x: int(x[0]))
    rows = table.rows[skiprows:]
    rows = rows[:(len(rows) - skip_footer)]

    coll_dtype = {}

    def row_gen(cells):
        for cell in cells:
            index = cell.attr["ss:Index"]
            if index in index_columns:
                column = index_columns[index]
                if cell.data is not None:
                    data = cell.data.data
                    dtype = cell.data.attr.get("ss:Type", None)
                    if column in coll_dtype:
                        assert(coll_dtype[column] == dtype)
                    else:
                        coll_dtype[column] = dtype
                    yield column, data

    def item_gen(rows):
        rows = iter(rows)

        while True:
            row = next(rows)
            cells = row.cells

            item = dict(row_gen(cells))

            merge_down = max(int(c.attr.get("ss:MergeDown", 0)) for c in cells)
            if merge_down > 0:
                merger = defaultdict(list)
                for i in range(merge_down):
                    # consumer rows to be merged
                    cells = next(rows).cells
                    for k, v in row_gen(cells):
                        merger[k].append(v)
                for k, v in merger.items():
                    v.insert(0, item[k])
                    item[k] = '\n'.join(v)
            yield item

    # make data frame
    df = pd.DataFrame(item_gen(rows))

    # apply data types
    for col in df.columns:
        df[col] = conversions[coll_dtype[col]](df[col])
    return df
