#!/usr/bin/env python
"""Light weight and flexible module to exporf data from REDCap project to a relational database using SQLAlchemy
"""

import requests

class Project:
    """Sets up local configuration for calling the API scoped to a single project
    """

    supported_actions = set(['project'])
    """Supported REDCap API actions
    """

    def __init__(self, url, token):
        self._url = url
        self._token = token

    def getProject(self,data = {}):
        """Calls the 'project' REDCap API Method"""
        data['content'] = 'project'
        return self._call(data)

    def _call(self, data):
        """Checks that there is an API method specified and updates the token to reflect the Project's token

        This should not be called directly. Class methods should call this as the last step. It binds the API
        token and always sets the format to 'json'. It also checks one last time that the API method being called
        is supported
        """
        try:
            if data['content'] in self.supported_actions:
                data['token'] = self._token
                data['format'] = 'json'
                callResult = requests.post(self._url, data)
                callResult.raise_for_status()
                return callResult
            raise NotImplementedError('Your content type is not supported yet')
        except Exception as e:
            raise RuntimeError('Something went wrong when calling the REDCap Project API') from e
    
   