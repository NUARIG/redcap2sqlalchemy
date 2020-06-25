import sqlalchemy as _sa

class RC2SARule:
    """A rule used to match and act based on patterns"""
    
    def __init__(self, name, matchfn, colgenfn, transformfn, description = ''):
        self.name = name
        self.description = description
        self.matchfn = matchfn
        self.colgenfn = colgenfn
        self.transformfn = transformfn

    def __repr__(self):
        return('<redcap2sqlalchemy::RC2SARule {0}>'.format(self.name))



class RC2SARuleQueue:
    """Ordered set of Rules"""
    pass

def match_always (fieldinfo):
    return True

def colgen_string (fieldinfo):
    raise NotImplementedError('Column generation function colgen_string not implemented yet')

def transform_asis_str (value):
    return(str(value))

class RC2SATable(_sa.Table):
    pass