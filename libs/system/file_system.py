import os
import shutil


def list_dir_files_as_absolute_paths(dir_path):
    return [os.path.join(dir_path, x) for x in os.listdir(dir_path)]


def ensure_directory_does_not_exist(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)


def ensure_directory_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def ensure_empty_directory(dir_path):
    ensure_directory_does_not_exist(dir_path)
    ensure_directory_exists(dir_path)


def ensure_directory_exists_for_path(path):
    dirname = os.path.dirname(path)
    ensure_directory_exists(dirname)
