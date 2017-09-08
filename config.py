conf_file = 'config.cfg'
host_file = 'host_list'

with open(host_file) as fl:
    host_list = fl.readlines()
    
with open(conf_file) as fl:
    config_file = fl.readlines()
    