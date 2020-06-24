# redcap2sqlalchemy

Generic methods for extracting data from REDCap and pushing into a relational DB using SQLAlchemy

## Classes

### RCProject

Local mirror of a REDCap Project instantiated via a URL and Token. Example usage below.

```python
>>> import redcap2sqlalchemy as r2sa
>>> myproject = r2sa.RCProject('https://redcap.example.edu/api/', 'ABCDE12345')
```




