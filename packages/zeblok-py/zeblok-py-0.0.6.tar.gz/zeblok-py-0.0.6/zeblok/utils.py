"""
This module implements a progress printer while communicating with MinIO server
:copyright: (c) 2018 by MinIO, Inc.
:license: Apache 2.0, see LICENSE for more details.
"""

import sys
import time
from queue import Empty, Queue
from threading import Thread
from pathlib import Path
from os import walk
import os
from .errors import AuthenticationError, ServerError, InvalidCredentialsError, InvalidBaseURL, InvalidStorageURL

_BAR_SIZE = 20
_KILOBYTE = 1024
_FINISHED_BAR = '#'
_REMAINING_BAR = '-'

_UNKNOWN_SIZE = '?'
_STR_MEGABYTE = ' MB'

_HOURS_OF_ELAPSED = '%d:%02d:%02d'
_MINUTES_OF_ELAPSED = '%02d:%02d'

_RATE_FORMAT = '%5.2f'
_PERCENTAGE_FORMAT = '%3d%%'
_HUMANINZED_FORMAT = '%0.2f'

_DISPLAY_FORMAT = '|%s| %s/%s %s [elapsed: %s left: %s, %s MB/sec]'

_REFRESH_CHAR = '\r'


def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in walk(directory):
        for filename in files:
            file_paths.append(Path(root).joinpath(filename))
    return file_paths


def seconds_to_time(seconds):
    """
    Consistent time format to be displayed on the elapsed time in screen.
    :param seconds: seconds
    """
    minutes, seconds = divmod(int(seconds), 60)
    hours, m = divmod(minutes, 60)
    if hours:
        return _HOURS_OF_ELAPSED % (hours, m, seconds)
    else:
        return _MINUTES_OF_ELAPSED % (m, seconds)


def format_string(current_size, total_length, elapsed_time):
    """
    Consistent format to be displayed on the screen.
    :param current_size: Number of finished object size
    :param total_length: Total object size
    :param elapsed_time: number of seconds passed since start
    """

    n_to_mb = current_size / _KILOBYTE / _KILOBYTE
    elapsed_str = seconds_to_time(elapsed_time)

    rate = _RATE_FORMAT % (
            n_to_mb / elapsed_time) if elapsed_time else _UNKNOWN_SIZE
    frac = float(current_size) / total_length
    bar_length = int(frac * _BAR_SIZE)
    bar = (_FINISHED_BAR * bar_length +
           _REMAINING_BAR * (_BAR_SIZE - bar_length))
    percentage = _PERCENTAGE_FORMAT % (frac * 100)
    left_str = (
        seconds_to_time(
            elapsed_time / current_size * (total_length - current_size))
        if current_size else _UNKNOWN_SIZE)

    humanized_total = _HUMANINZED_FORMAT % (
            total_length / _KILOBYTE / _KILOBYTE) + _STR_MEGABYTE
    humanized_n = _HUMANINZED_FORMAT % n_to_mb + _STR_MEGABYTE

    return _DISPLAY_FORMAT % (bar, humanized_n, humanized_total, percentage,
                              elapsed_str, left_str, rate)


def api_error(status_code: int, message: str):
    if status_code == 401:
        raise AuthenticationError("User not authenticated. Please check your __api_access_key and api_access_secret")
    else:
        raise ServerError(f"Status code = {status_code}\n{message}")


class Progress(Thread):
    """
        Constructs a :class:`Progress` object.
        :param interval: Sets the time interval to be displayed on the screen.
        :param stdout: Sets the standard output
        :return: :class:`Progress` object
    """

    def __init__(self, interval=1, stdout=sys.stdout):
        Thread.__init__(self)
        self.daemon = True
        self.total_length = 0
        self.interval = interval
        self.object_name = None

        self.last_printed_len = 0
        self.current_size = 0

        self.display_queue = Queue()
        self.initial_time = time.time()
        self.stdout = stdout
        self.start()
        self.prefix = None

    def set_meta(self, total_length, object_name):
        """
        Metadata settings for the object. This method called before uploading
        object
        :param total_length: Total length of object.
        :param object_name: Object name to be showed.
        """
        self.total_length = total_length
        self.object_name = object_name
        self.prefix = self.object_name + ': ' if self.object_name else ''

    def run(self):
        displayed_time = 0
        while True:
            try:
                # display every interval secs
                task = self.display_queue.get(timeout=self.interval)
            except Empty:
                elapsed_time = time.time() - self.initial_time
                if elapsed_time > displayed_time:
                    displayed_time = elapsed_time
                self.print_status(current_size=self.current_size,
                                  total_length=self.total_length,
                                  displayed_time=displayed_time,
                                  prefix=self.prefix)
                continue

            current_size, total_length = task
            displayed_time = time.time() - self.initial_time
            self.print_status(current_size=current_size,
                              total_length=total_length,
                              displayed_time=displayed_time,
                              prefix=self.prefix)
            self.display_queue.task_done()
            if current_size == total_length:
                # once we have done uploading everything return
                self.done_progress()
                return

    def update(self, size):
        """
        Update object size to be showed. This method called while uploading
        :param size: Object size to be showed. The object size should be in
                     bytes.
        """
        if not isinstance(size, int):
            raise ValueError('{} type can not be displayed. '
                             'Please change it to Int.'.format(type(size)))

        self.current_size += size
        self.display_queue.put((self.current_size, self.total_length))

    def done_progress(self):
        self.total_length = 0
        self.object_name = None
        self.last_printed_len = 0
        self.current_size = 0

    def print_status(self, current_size, total_length, displayed_time, prefix):
        formatted_str = prefix + format_string(
            current_size, total_length, displayed_time)
        self.stdout.write(_REFRESH_CHAR + formatted_str + ' ' *
                          max(self.last_printed_len - len(formatted_str), 0))
        self.stdout.flush()
        self.last_printed_len = len(formatted_str)


def validate_secret_key(key_name: str, secret_key: str):
    if type(secret_key) is not str:
        raise InvalidCredentialsError(f'{key_name} can only be of type String')
    if secret_key == '':
        raise InvalidCredentialsError(f'{key_name} cannot empty')


def validate_username(username: str):
    if type(username) is not str:
        raise InvalidCredentialsError('username can only be of type String')
    if username == '':
        raise InvalidCredentialsError('username cannot empty')


def validate_url(url_name: str, url: str):
    if type(url) is not str:
        raise InvalidBaseURL(f'{url_name} can only be of type String')
    if url == '':
        raise InvalidBaseURL(f'{url_name} cannot empty')


def validate_base_url(base_url: str):
    if type(base_url) is not str:
        raise InvalidBaseURL('base_url can only be of type String')
    if base_url == '':
        raise InvalidBaseURL('base_url cannot empty')


def validate_storage_url(storage_url: str):
    if type(storage_url) is not str:
        raise InvalidBaseURL('storage_url can only be of type String')
    if storage_url == '':
        raise InvalidBaseURL('storage_url cannot empty')


def validate_deployment_name(deployment_name: str):
    if type(deployment_name) is not str:
        raise ValueError('deployment_name can only be of type String')
    if deployment_name == '':
        raise ValueError('deployment_name cannot empty')


def validate_model_version(model_version: str):
    if type(model_version) is not str:
        raise ValueError('model_version can only be of type String')
    if model_version == '':
        raise ValueError('model_version cannot empty')


def validate_namespace_id(namespace_id: str):
    if type(namespace_id) is not str:
        raise ValueError('namespace_id can only be of type String')
    if namespace_id == '':
        raise ValueError('namespace_id cannot empty')


def validate_platform_id(platform_id: list[str]):
    if type(platform_id) is not list[str]:
        raise ValueError('platform_id can only be of type List')
    if platform_id == '':
        raise ValueError('platform_id cannot empty')


def validate_model_pipeline(model_pipeline: str):
    if type(model_pipeline) is not str:
        raise ValueError('image_name can only be of type String')
    if model_pipeline == '':
        raise ValueError('image_name cannot empty')


def validate_model_folder(model_folder_path: Path):
    if model_folder_path == Path(''):
        raise ValueError(f"Model folder path is empty")

    if not model_folder_path.exists():
        raise FileNotFoundError(f"{model_folder_path} does not exist")

    if not model_folder_path.is_dir():
        raise NotADirectoryError(f"{model_folder_path} is not a folder")

    if not os.access(model_folder_path, os.W_OK):
        raise PermissionError(f"Folder doesn't have write permission: {model_folder_path}")


def validate_envs_args(name: str, val: list[str]):
    assert all([len(kv.split("=")) == 2 for kv in val]), f"{name} should be a string with comma-separated key value pairs. For e.g. 'k1=v1, k2=v2, k3=v3'"
