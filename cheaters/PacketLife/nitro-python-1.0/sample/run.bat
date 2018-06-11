setlocal
set PYTHONPATH=../lib/nitro_python-1.0-py2.7.egg
python set_config.py %1 %2 %3
python get_config.py %1 %2 %3
python stat_config.py %1 %2 %3
python rm_config.py %1 %2 %3
python CreateCluster.py %1 %2 %3
python MyFirstNitroApplication.py %1 %2 %3
endlocal