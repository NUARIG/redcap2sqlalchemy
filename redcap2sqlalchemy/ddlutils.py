import sqlalchemy as _sa
from .rcproject import RCProject, REDCapError

"""
The following classes and functions are structural components (connection, Table, ...)
"""

def tablegen_rcform(myrcproject, myformname, mytablename, mymetadata):
    """Generates a SQL Alchemy Table from a project, a form name, and Metada object"""
    if myformname not in map( lambda x:x['instrument_name'], myrcproject.exportInstruments() ):
        raise REDCapError('Form name is not in the given project')

    return _sa.Table(mytablename, mymetadata)


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
    """This matching function always returns True, good to keep at the end of a queue as catchall"""
    return True

def colgen_string (fieldinfo):
    _sa.DDL
    raise NotImplementedError('Column generation function colgen_string not implemented yet')

def transform_asis_str (value):
    return(str(value))
