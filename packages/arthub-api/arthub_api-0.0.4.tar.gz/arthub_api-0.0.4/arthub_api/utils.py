"""
arthub_api.utils
~~~~~~~~~~~~~~

This module provides utilities that are used within API
"""
import logging
import os
import shutil
import time
import random
import string
import requests
from . import models


def _path_preprocess(path):
    path = path.strip()
    path = path.rstrip("\\/")
    return path


def create_empty_file(path):
    try:
        open(path, "w").close()
        return True
    except Exception:
        return False


def mkdir(path):
    path = _path_preprocess(path)
    if os.path.isdir(path):
        return True
    if os.path.isfile(path):
        return False
    try:
        os.makedirs(path)
    except Exception as e:
        return False
    return True


def remove(path):
    path = _path_preprocess(path)
    if not os.path.exists(path):
        return True
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
    except Exception as e:
        return False
    return True


def current_milli_time():
    return (lambda: int(round(time.time() * 1000)))()


def get_random_string(length):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


class UploadFilePartReader(object):
    def __init__(self, file_, offset, length):
        self._file = file_
        self._file.seek(offset)
        self._total_size = length
        self._completed_size = 0
        self._finished = False

    def read(self, size=-1):
        if size == -1:
            self._finished = True
            return ""
        uncompleted_size = self._total_size - self._completed_size
        size_to_read = min(uncompleted_size, size)
        if size_to_read == 0:
            self._finished = True
            return ""
        content = self._file.read(size_to_read)
        self._completed_size += len(content)
        return content


def upload_part_of_file(url, file_path, offset, length):
    try:
        if not os.path.isfile(file_path):
            return models.Result(False, error_message="file \"%s\" not exist" % file_path)
        with open(file_path, 'rb') as file_:
            res = requests.put(url, data=UploadFilePartReader(file_, offset, length), headers={
                "Accept": "application/json",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Content-Type": "application/octet-stream",
                "Content-Length": str(length)
            })
            if not res.ok:
                return models.Result(False, error_message="status code: %d" % res.status_code)
            return models.Result(True, data=res)
    except Exception as e:
        error_message = "send request \"%s\" exception" % url
        logging.error("[UploadPart] %s" % error_message)
        return models.Result(False, error_message=error_message)


def download_file(url, file_path):
    try:
        # get file capacity
        res_length = requests.get(url, stream=True)
        if not res_length:
            return models.Result(False, error_message="request \"%s\" failed" % url)
        total_size = int(res_length.headers['Content-Length'])
        existing_size = 0
        if os.path.exists(file_path):
            existing_size = os.path.getsize(file_path)
            if existing_size > total_size:
                remove(file_path)
                existing_size = 0
        else:
            if not create_empty_file(file_path):
                return models.Result(False, error_message="create \"%s\" failed" % file_path)

        if existing_size == total_size:
            return models.Result(True)

        # download file
        download_dir_path = os.path.dirname(file_path)
        if not mkdir(download_dir_path):
            return models.Result(False, error_message="create directory \"%s\" failed" % download_dir_path)
        res_left = requests.get(url, stream=True, headers={'Range': 'bytes=%d-' % existing_size})
        if not res_left:
            return models.Result(False, error_message="request \"%s\" failed" % url)
        with open(file_path, "ab") as f:
            for chunk in res_left.iter_content(chunk_size=1024):
                existing_size += len(chunk)
                f.write(chunk)
                f.flush()
                done = float(existing_size / total_size)
        return models.Result(True)

    except Exception as e:
        return models.Result(False, error_message=e)


def splite_path(path_):
    path_list = []
    while path_:
        l = os.path.split(path_)
        path_ = l[0]
        if l[1]:
            path_list.insert(0, l[1])
    return path_list


def rename_path_text(path_):
    path_ = _path_preprocess(path_)
    path_without_ext, ext = os.path.splitext(path_)
    suffix_number = 1
    while os.path.exists(path_):
        path_ = "%s (%d)%s" % (path_without_ext, suffix_number, ext)
        suffix_number += 1
    return path_
