# redcap2sqlalchemy

Generic methods for extracting data from REDCap and pushing into a relational DB using SQLAlchemy

## Classes

### RCProject

Local mirror of a REDCap Project instantiated via a URL and Token.

To instantiate a project.

```python
>>> import redcap2sqlalchemy as r2sa
>>> myproject = r2sa.RCProject('https://redcap.example.edu/api/', 'ABCDE12345')
```

The constructor will automatically do a call to the REDCap Export Project Information API Method. This will set some information about the project which will be placed in the `info` attribute of the project.

You can then use any of the bound methods to make specific API calls. For example to get the metadata associated with a project, you can call the following method.

```python
>>> myproject.exportMetaData()
[{'field_name': 'record_id',
  'form_name': 'my_first_instrument',
  'section_header': '',
  'field_type': 'text',
  'field_label': 'Record ID',
  'select_choices_or_calculations': '',
  'field_note': '',
  'text_validation_type_or_show_slider_number': '',
  'text_validation_min': '',
  'text_validation_max': '',
  'identifier': '',
  'branching_logic': '',
  'required_field': '',
  'custom_alignment': '',
  'question_number': '',
  'matrix_group_name': '',
  'matrix_ranking': '',
  'field_annotation': ''},
 {...
```


