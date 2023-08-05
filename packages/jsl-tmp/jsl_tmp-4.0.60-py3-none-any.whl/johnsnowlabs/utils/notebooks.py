import os
import shutil
import urllib
from pathlib import Path

import nbformat
import pandas as pd
from nbconvert import PythonExporter

from johnsnowlabs import settings
from johnsnowlabs.utils.file_utils import str_to_file
from johnsnowlabs.utils.py_process import str_to_file, execute_py_script_as_new_proc, log_multi_run_status


def clean_workshop_notebook(py_script_path, out_path, suc_print=settings.success_worker_print, work_dir=os.getcwd(),
                            model_cache_dir=None):
    prefix = f"""
import os 
os.chdir('{work_dir}')
from johnsnowlabs import *
"""
    if model_cache_dir:
        prefix = prefix + f"""
jsl.start(model_cache_folder='{model_cache_dir}')
        """
    else :
        prefix = prefix + f"""
jsl.start()
        """

    suffix = f"""
print('{suc_print}')    
"""

    # Substring matches
    bad_sub_strings = [
        'files.upload()',
        # 'get_ipython',
        'pip install',
        'from google',
        'google.',
        'colab',
        'jsl.install',
        '#',
        'license_keys',

    ]

    # Hard matches
    bad_lines = [  # '\n',
        'jsl.install()',
    ]
    new_file = []
    with open(py_script_path, "r") as f:
        for l in f:
            if any(s in l for s in bad_sub_strings): continue
            if l in bad_lines: continue
            # if 'get_ipython().system' in l:
            #     l = l.replace('get_ipython()', 'os')
            # if 'get_ipython().run_line_magic' in l:
            #     continue

            new_file.append(l)
    new_file = prefix + ''.join(new_file) + suffix
    # print(new_file)
    str_to_file(new_file, out_path)


def get_all_nb_in_local_folder(p):
    ## filter all files ending in .ipynb
    return [f'{p}/{f}' for f in os.listdir(p) if '.ipynb' in f]


def convert_notebook(notebookPath, out_py_path):
    with open(notebookPath) as fh:
        nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)
    exporter = PythonExporter()
    source, meta = exporter.from_notebook_node(nb)
    str_to_file(source, out_py_path)


def convert_all_notebooks(nb_folder):
    # Convert a folder which contains .ipynb into .py
    store_folder = f'{nb_folder}/nb_converted/'
    Path(store_folder).mkdir(parents=True, exist_ok=True)
    for nb_path in get_all_nb_in_local_folder(nb_folder):
        save_path = store_folder + nb_path.split('/')[-1] + '.py'
        convert_notebook(nb_path, save_path)


def test_ipynb(file_path_or_url, work_dir=os.getcwd(), use_i_py=True, model_cache_dir=None):
    if 'http' and '//' in file_path_or_url:
        file_name = file_path_or_url.split('/')[-1]

        print(f'Downloading {file_path_or_url} to  {file_name}')
        # Download the file from `url` and save it locally under `file_name`:
        with urllib.request.urlopen(file_path_or_url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            file_path_or_url = file_name

    file_name = work_dir + '/' + file_path_or_url.split('/')[-1]
    convert_notebook(file_path_or_url, file_name)
    final_py_script = file_name + '___CLEANED.py'
    clean_workshop_notebook(py_script_path=file_name, out_path=final_py_script, work_dir=work_dir,
                            model_cache_dir=model_cache_dir)

    succ, proc = execute_py_script_as_new_proc(py_script_path=final_py_script, use_i_py=True)
    return make_log(file_path_or_url, succ, proc, final_py_script)


def test_ipynb_folder(nb_folder, work_dir=os.getcwd(), log=True):
    return pd.DataFrame(test_list_of_ipynb(get_all_nb_in_local_folder(nb_folder), work_dir, log))


def test_list_of_ipynb(nb_paths_or_urls, work_dir=os.getcwd(), log=True, model_cache_dir=None):
    df = pd.DataFrame(test_ipynb(nb_path, work_dir, model_cache_dir=model_cache_dir) for nb_path in nb_paths_or_urls)
    if log:
        log_multi_run_status(df)
    return df


def make_log(nb_file, suc, proc, final_py_script):
    return {
        'notebook': nb_file,
        'success': suc,
        'stdout': proc.stdout.decode(),
        'stderr': proc.stderr.decode(),
        'test_script': final_py_script}
