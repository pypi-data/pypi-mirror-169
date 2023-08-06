"""
    This module provides utility functions for other modules in the SDK.
"""


from functools import wraps
import json
import logging
import time
import os
import platform
from urllib.parse import urlparse

import boto3


LOGGER = logging.getLogger(__name__)
CANONICAL = os.getenv('CANONICAL', 'org-prod-canonical-use1')


def retry(tries=4, delay=3, backoff=2):
    """Retry calling the decorated function using an exponential backoff.

    Originally sourced from https://tinyurl.com/yb9crvtw.

    Args:
        tries: Number the number of times to retry.
        delay: How long to sleep between tries.
        backoff: The backoff rate.

    Returns:
        None
    """
    def deco_retry(findings):
        @wraps(findings)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return findings(*args, **kwargs)
                except:  # pylint: disable=bare-except
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return findings(*args, **kwargs)
        return f_retry  # true decorator
    return deco_retry


def get_cloudformation_export(name) -> str:
    """I lookup the cloudformation export value.

    Args:
        name: str form of the export we are looking up

    Returns:
        The value of the export.
    """
    client = boto3.client('cloudformation')
    response = client.list_exports()
    while response['NextToken']:
        for record in response['Exports']:
            if record['Name'] == name:
                return record['Value']
        response = client.list_exports(NextToken=response['NextToken'])
    return None


def get_canonical_object(key):
    """I return the a dictionary version of a canonical object.

    Args:
        key: The object key to fetch and convert.

    Returns:
        dict: A dictionary reprensentation of the data in the object file.
    """
    client = boto3.client('s3')
    obj = client.get_object(Bucket=CANONICAL, Key=key)
    return json.loads(obj['Body'].read().decode('utf8'))


def set_no_proxy(url):
    """Set the no_proxy variable to skip proxy for our push endpoint.

    Args:
        url: the url we'll be posting data to

    Returns:
        None
    """
    hostname = urlparse(url).netloc
    system =  platform.system()
    if system in ['Linux', 'Darwin']:
        key = 'no_proxy'
    else:
        # Windows
        key = 'NO_PROXY'
    LOGGER.debug('Setting %s to %s', key, hostname)
