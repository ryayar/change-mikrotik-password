import paramiko

"""
Рядом с файлом main.py должен лежать .txt файл 
с названием ips_mikrotik.txt, в котором с каждой 
новой строки написан IP микрота. По результату 
выполнения будет сформирован файл с названием logs.log"""

user = 'login'
secret = 'password' # Актуальный пароль
new_secret = 'new_secret'
port = 22
command_change_pass = f'user set [find name={user}] password={new_secret}'


def change_password():
    with open('ips_mikrotik.txt', 'r+', encoding='UTF-8') as hosts:
        with open('logs.log', 'a+', encoding='UTF-8') as log:
            for host in hosts:
                host = host.strip()
                try:
                    log.write(f'[i] Open SSH\n')
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    log.write(f'[i] Connect to {host}\n')
                    client.connect(hostname=host, username=user, password=secret, port=port)
                    log.write('[i] Connect OK\n')

                    log.write(f'[i] Send [{command_change_pass}]\n')
                    try:
                        client.exec_command(command_change_pass)
                        log.write(f'[i] Send command Success\n')
                    except Exception as err:
                        log.write(f'[Err] Send command Error\n')
                        log.write(f'[Err] {err}\n')

                except Exception as err:
                    log.write(f'[Err] {err}\n')

                log.write('[i] SSH client close\n')
                log.write(f'-' * 50 + '\n\n')
                client.close()


def main():
    change_password()


if __name__ == "__main__":
    main()
