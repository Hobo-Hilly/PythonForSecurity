import paramiko

def main():
    ip = ' your ip'
    usernmae = 'ubuntu'
    password = 'sulphur'
    timeout = 5 
    client_policy = paramiko.AutoAddPolicy()
    client = paramiko.SSClient();
    client.set_missing_host_key_policyk(client_policy)
    client.connect(ip, username=username, password=password timeout=timeout)
    print(client)



if __name__ == '__main__':
    main
