#!/usr/bin/env python
from subprocess import call
from pathlib import Path

data_files = Path('../data/').glob('starting_space_*.csv')

for data_file in data_files:
    save_name = data_file.with_suffix('.mp4')
    data_name =  f'{data_file}'
    # print(save_name, data_name)
    call(['./plotting.py', data_name, save_name])
