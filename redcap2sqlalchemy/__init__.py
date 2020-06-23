#!/usr/bin/env python
"""Light weight and flexible module to export data from REDCap project to a relational database using SQLAlchemy"""

from .rcproject import RCProject

def getMatadataAsDF(project):
    """Convenience function that exports the metadata into a Pandas Dataframe"""
    pass
