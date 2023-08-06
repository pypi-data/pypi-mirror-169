# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:07:27 2022

@author: Darshan Rathod
"""

import os as _os


def make_dir(path1):
    '''
    makes the directory in path1. path1 should include the directory name to make. If directory already exists then nothing is done.
    '''
    try:
        _os.mkdir(path1)
    except FileExistsError as e:
        pass

def get_dir_path(fname):
    '''
    returns the list of paths of all the directories in the fname path.
    '''
    return [_os.path.join(fname,x) for x in _os.listdir(fname) if _os.path.isdir(_os.path.join(fname,x))]

def get_file_path(fname):
    '''
    returns the list of paths of all the files in the fname path.
    '''
    return [_os.path.join(fname,x) for x in _os.listdir(fname) if _os.path.isfile(_os.path.join(fname,x))]

def get_dir_name(fname):
    '''
    returns the list of names of all the directories in the fname path.
    '''
    return [x for x in _os.listdir(fname) if _os.path.isdir(_os.path.join(fname,x))]

def get_file_name(fname):
    '''
    returns the list of names of all the files in the fname path.
    '''
    return [x for x in _os.listdir(fname) if _os.path.isfile(_os.path.join(fname,x))]

