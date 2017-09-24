import time, multiprocessing, config, ssh_mod, getpass, sys

host_list = config.host_list
config_file = config.config_file

def worker(host,username,password,config_file, print_output):
    try:
        ssh_connect = ssh_mod.SSH_Connect(host, username, password)
        print 'connected to %s' %host
        fl = open('outputs/%s' %host, 'a')
        if print_output:
            for line in config_file:
                stdout = ssh_connect.send_command(line)
                time.sleep(1)
                fl.writelines(stdout)
                #print stdout.read()
        else:
            for line in config:
                stdout = ssh_connect.send_command(line)
                fl.writelines(stdout)
    except Exception, e:
        print 'ERROR: Could not connect to %s' %host
    

if __name__ == '__main__':
    username = raw_input('username: ')
    password = getpass.getpass('password: ')
    print_output = True
    jobs = []
    print """Going to apply below commands to host list:
    -------
    %s
    -------
    Are you sure?
    """ % config_file
    inpt = raw_input('(y/n): ')
    if inpt.lower() == 'y':
        for host in host_list:
            p = multiprocessing.Process(target=worker, args=(host.rstrip(), username, password, config_file, print_output,))
            jobs.append(p)
            p.start()
    elif inpt.lower() == 'n':
        sys.exit()
    else:
        print 'wrong input, plz. run again'
        

