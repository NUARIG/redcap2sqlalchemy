import sqlalchemy as _sa
from .rcproject import RCProject, REDCapError
"""
The following classes and functions are structural components (connection, Table, ...)
"""

class RC2SATableFactory:
    """Generates SQLAlchemy Tables based on projects and other parameters"""

    def __init__(self, rcproject, metadata, prefix='', suffix=''):
        if not isinstance(rcproject, RCProject):
            raise REDCapError('Did not pass a RCProject object to RC2SATableFactory constructor')
        elif not isinstance(metadata, _sa.MetaData):
            raise REDCapError('Did not pass a MetaData object to RC2SATableFactory constructor')
        elif not isinstance(prefix, str) or not isinstance(suffix, str):
            raise REDCapError('Prefix and Suffix need to be string objects in RC2SATableFactory constructor')

        self._rcproject = rcproject
        self._metadata = metadata
        self._prefix = prefix
        self._suffix = suffix

    def makeTableForProject(self, projectname, identifier_col, tablename=None, overwrite=False):
        """Generates a SQL Alchemy Table based on a project name

        Warning: if the tablename already exists as a table in the metadata, it will fail
                unless the overwrite parameter is True (defauilt is False)
        """
        self._metadata.reflect()
        if not isinstance(tablename, str):
            tablename = self._prefix + projectname + self._suffix

        redcap_dict = self._rcproject.exportMetaData(data={})
        forms = self._rcproject.exportInstruments(data={})

        def generator_field_names():
            for field in redcap_dict:
                if field['field_name'] != identifier_col:
                    yield field['field_name']
        def generator_form_complete_cols():
            for form in forms:
                yield form['instrument_name'] + '_complete'


        def concat(a, b):
            yield from a
            yield from b

        if tablename in self._metadata.tables and overwrite is not True:
            raise REDCapError('Attempting to create a table {0} which exists without overwrite flag'.format(tablename))

        # todo foreign key relationship?
        # TODO USE ALLTOSTRING constant below in code here instead?
        mytable = _sa.Table(tablename, self._metadata, _sa.Column(identifier_col, _sa.String, primary_key=True),
                            *(_sa.Column(field, _sa.String) for field in concat(generator_form_complete_cols(),
                                                                                generator_field_names())))

        """
        A WHOLE BUNCH OF STUFF WITH COLUMNS NEED TO HAPPEN HERE
        """

        return mytable

    def makeTable(self, formname, tablename = None, overwrite = False):
        """Generates a SQL Alchemy Table based on a form name

        Warning: if the tablename already exists as a table in the metadata, it will fail
                unless the overwrite parameter is True (defauilt is False)
        """
        if formname not in map( lambda x:x['instrument_name'], self._rcproject.exportInstruments() ):
            raise REDCapError('Form name {0} is not in the given project'.format(formname))
        if not isinstance(tablename,str):
            tablename = self._prefix + formname + self._suffix

        if tablename in self._metadata.tables and overwrite is not True:
            raise REDCapError('Attempting to create a table {0} which exists without overwrite flag'.format(tablename))

        mytable = _sa.Table(tablename, self._metadata)

        """
        A WHOLE BUNCH OF STUFF WITH COLUMNS NEED TO HAPPEN HERE
        """

        return mytable


"""
The following classes and function address the DDL and ETL logic
"""

class RC2SARule:
    """A rule used to match and act based on patterns"""
    
    def __init__(self, name, matchfn, colgenfn, transformfn, description = ''):
        self.name = name
        self.description = description
        self.matchfn = matchfn
        self.colgenfn = colgenfn
        self.transformfn = transformfn

    def __repr__(self):
        return('<redcap2sqlalchemy::RC2SARule {0} >'.format(self.name))

class RC2SARuleQueue:
    """Ordered set of Rules"""

    def __init__(self):
        raise NotImplementedError('RC2SARuleQueue is not implemented yet')

def match_always (fieldinfo):
    """A matching function that always returns True, good to keep at the end of a queue as catchall"""
    return True

def colgen_string (fieldinfo):
    """Returns a simple string (varchar) column"""
    if 'field_name' not in fieldinfo.keys():
        raise REDCapError('Invalid REDCap field metadata definition passed to colgen_string')

    return _sa.Column(fieldinfo['field_name'], _sa.String())


def transform_asis_str (value):
    return(str(value))

R_ALLTOSTRING = RC2SARule('All to String', match_always, colgen_string, transform_asis_str)
