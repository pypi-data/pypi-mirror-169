"""
    Problems Solved:
      - We want to provide an accessible programmatic library for interacting
        with the Validator API.
      - We want to abstract the asynchronous communication form the API job
        management to be a simple method call.
"""


import hashlib
import json
import logging
import os
import time


import diskcache
import urllib3

from .utils import retry


# handlers
POOL_SIZE = int(os.getenv('POOL_SIZE', '30'))
HTTP = urllib3.PoolManager(maxsize=POOL_SIZE)
LOG = logging.getLogger(__name__)


# Configurations
# Note PRUC-2091 will setup a real dns.
URL = os.getenv(
    'VALIDATOR_URL',
    'https://validator.botthouse.net/v1'
)
HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'Validator SDK'
}
SLEEP_TIME = os.getenv('SLEEP_TIME', '0.9')


CACHE = diskcache.Cache('~/.validator')
CACHETIME = 60 * 60 * 8  # Cache for 8 hours

class Validate:
    """
        I am the object which gives the validate state.

        I turn the asynchronous nature of the validator API into a state
        refrence.
    """
    def __init__(self, **kwargs) -> object:
        """
            I initialize the Validate object to be a validation object.

            Args
            kwargs: dictionary of the object creation context.

            Reqruiremnents
            I require either a data context or filename to load the context.

            Returns
            object of type Validate class
        """
        self.logger = logging.getLogger(__name__)
        self.logger.debug('Creating Validate Object')

        # Set object context
        self.name = kwargs.get('filename')
        self.job_id = kwargs.get('job_id')

        if not self.name and not self.job_id:
            LOG.error('Missing Validate Object Context')
            raise Exception('missing filename and job_id')

        # Set delay time
        self.delay = float(kwargs.get('delay', os.getenv('SLEEP_TIME', '0.3')))

        # load date
        self.data = kwargs.get('data')
        if self.name and not self.data:
            LOG.debug('Loading data from file')
            with open(self.name, 'r', encoding='utf8') as file_handler:
                self.data = file_handler.read()

        # Set MD5
        self.md5 = hashlib.md5(self.data.encode('utf-8')).hexdigest()

        # Set user if provided
        self.user = kwargs.get('user', os.getenv('USER', 'unknown'))

    @retry()
    def validate(self) -> str:
        """
            Make the web request for evaluation.  Then return the jobId for the
            validation request.

            Args
            None

            Returns:
            The jobId for the file evaluation request.
        """
        LOG.debug('Creating validate task')
        if self.md5 in CACHE:
            self.job_id = CACHE[self.md5]
        else:
            request = {
                'name': self.name,
                'user': self.user,
                'data': self.data
            }
            encoded_data = json.dumps(
                request,
                default=str
            ).encode('utf-8')
            result = HTTP.request(
                'POST',
                f'{URL}/create',
                headers=HEADERS,
                body=encoded_data
            )
            LOG.debug('Return code is %s', result.status)
            LOG.debug('Return Data is %s', result.data)
            self.job_id = json.loads(
                    result.data
            )['job_id']

    @retry()
    def _get_validation_data(self) -> dict:
        """
            I fetch the data from a job.

            Args
            None

            Returns
            I return a dictionary of the data for the job.
        """
        lookup = {"job_id": self.job_id}
        encoded_data = json.dumps(lookup).encode('utf-8')
        LOG.debug(encoded_data)
        result = HTTP.request(
            'GET',
            f'{URL}/status?job_id={self.job_id}',
            headers=HEADERS
        )
        LOG.debug('Return code is %s', result.status)
        LOG.debug('Return Data is %s', result.data)
        return json.loads(result.data)

    def results(self) -> dict:
        """
            I fetch the data from a job.

            Args
            None

            Returns
            I return a dictionary of the data for the job.
        """
        while True:
            data = self._get_validation_data()
            CACHE.add(self.md5, self.job_id, CACHETIME)
            if data['status'] == 'complete':
                return data
            time.sleep(self.delay)
