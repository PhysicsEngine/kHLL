__author__ = 'lewuathe'

import numpy as np
import hashlib
import common

def __calc_with_hash(vec, m, target):
    for v in vec:
        m.update(v)
    if target == 'hex':
        return m.hexdigest()
    else:
        return common.hex2dec(m.hexdigest())

def md5_for_vec(vec, target = 'dec'):
    """
    Calculate hexdigest with md5 for given vector
    :param vec:
    :return string:
    """
    m = hashlib.md5()
    return __calc_with_hash(vec, m, target)

def sha1_for_vec(vec, target = 'dec'):
    """
    Calculate hexdigest with sha1 for given vector
    :param vec:
    :return string:
    """
    m = hashlib.sha1()
    return __calc_with_hash(vec, m, target)

def sha224_for_vec(vec, target = 'dec'):
    """
    Calculate hexdigest with sha224 for given vector
    :param vec:
    :return string:
    """
    m = hashlib.sha224()
    return __calc_with_hash(vec, m, target)

def sha256_for_vec(vec, target = 'dec'):
    """
    Calculate hexdigest with sha256 for given vector
    :param vec:
    :return string:
    """
    m = hashlib.sha256()
    return __calc_with_hash(vec, m, target)

def sha384_for_vec(vec, target = 'dec'):
    """
    Calculate hexdigest with sha384 for given vector
    :param vec:
    :return string:
    """
    m = hashlib.sha384()
    return __calc_with_hash(vec, m, target)

def sha512_for_vec(vec, target = 'dec'):
    """
    Calculate hexdigest with sha512 for given vector
    :param vec:
    :return string:
    """
    m = hashlib.sha512(vec)
    return __calc_with_hash(vec, m, target)
