import requests

class RCProject:
    """Sets up local class configured for API access scoped to a single project"""

    supported_actions = set(
        ['project',
        'metadata',
        'version',
        'instrument'])
    """Supported REDCap API Actions as of this implementation"""

    info = None
    rc_version = None
    _url = None
    _token = None
    """Project properties. Assigned when initializing the object"""

    def __init__(self, url, token):
        """Class constructor. Always requires a URL and TOKEN."""
        self._url = url
        self._token = token
        self._initalize()

    """The methods below are used to call the API. They typically return the payload as parsed JSON object"""

    def exportProjectInfo(self,data = {}):
        """Calls the 'project' REDCap API Method"""
        data['content'] = 'project'
        return self._call(data)

    def exportMetaData(self, data = {}, format='json'):
        """Calls the 'metadata' REDCap API Method"""
        data['content'] = 'metadata'
        return self._call(data, format)
    
    def exportREDCapVersion(self, data = {}):
        """Gets the REDCap version of the instance holding the project"""
        data['content'] = 'version'
        return self._call(data, parseJSON=False)

    def exportInstruments(self, data = {}):
        """Calls the 'instrument' REDCap API Method"""
        data['content'] = 'instrument'
        return self._call(data)

    """The methods below are internal worker methods. Not intended to be called directly."""

    def _call(self, data, format = 'json', parseJSON = True):
        """Performs the last needed modifications to the payload and does sanity checks before and after the request

        This should not be called directly. Class methods should call this as the last step.

        It does the following before the request is made
        * It binds the API token to the data payload
        * It sets the format to 'json'
        * It checks that the API method being called is supported by this Class

        It does the following after the request is made
        * Raise an HTTPError based on the status code
        * Attempts to parse the JSON payload and raises a RuntimeError if it fails
        """
        try:
            if data['content'] in self.supported_actions:
                data['token'] = self._token
                data['format'] = format
                callResult = requests.post(self._url, data)
                callResult.raise_for_status()
                if format=='json' and parseJSON: 
                    return callResult.json()
                else:
                    return callResult.text
            raise NotImplementedError('Your content type is not supported yet')
        except Exception as e:
            raise REDCapError('Something went wrong when calling the REDCap Project API') from e

    def _initalize(self):
        """Called by constructor when creating the object."""
        try:
            self.info = self.exportProjectInfo()
            self.rc_version = self.exportREDCapVersion()
        except Exception as e:
            raise REDCapError('Failed to initalize a Project class in redcap2sqlalchemy') from e

    def __repr__(self):
        """User friendly representation of project"""
        return('redcap2sqlalchemy::RCProject {0} [{1}] on {2} [v{3}]'.format(self.info['project_title'], self.info['project_id'], self._url, self.rc_version))

    
class REDCapError(RuntimeError):
    """REDCap connection related errors"""
    pass

def rcproject_from_config(myconfig):
    """Convenience function to instantiate a project using a config like object

    requires that the following keys be present
    
    * redcap.url
    * redcap.token
    """
    return RCProject(myconfig['redcap.url'], myconfig['redcap.token'])

