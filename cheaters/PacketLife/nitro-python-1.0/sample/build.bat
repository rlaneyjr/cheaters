@echo off

python -m py_compile set_config.py
python -m py_compile get_config.py
python -m py_compile stat_config.py
python -m py_compile rm_config.py
python -m py_compile CreateCluster.py
python -m py_compile MyFirstNitroApplication.py