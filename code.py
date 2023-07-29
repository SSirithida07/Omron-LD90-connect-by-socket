import socket

# กำหนดค่า Host และ Port ของหุ่นยนต์
HOST = ''  
PORT = 

# สร้าง Socket Object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# เชื่อมต่อกับหุ่นยนต์
s.connect((HOST, PORT))

# รับข้อมูลจากหุ่นยนต์
data = s.recv(1024)
print('Received:', data)

# ส่ง Password ให้กับหุ่นยนต์
password = b'admin\n'
s.sendall(password)

# รับข้อมูลจากหุ่นยนต์
data = s.recv(1024)
print('Received:', data)

while True:
    # รับคำสั่งจากผู้ใช้
    command = input("Enter ARCL command: ")

    if command == 'exit':
        break

    if command == 'd':
        command = b'dock\n'
    elif command == 'ud':
        command = b'undock\n'
    elif command == 'go':
            i = input("Goal where?: ")
            command = b'goto goal' + i.encode() + b'\n'
    elif command == 's':
            command = b' stopped\n'

    else:
        print("Invalid command")
        continue

    # ส่งคำสั่ง ARCL ให้กับหุ่นยนต์
    print(command)
    s.sendall(command)

    # รับข้อมูลจากหุ่นยนต์
    data = s.recv(1024)
    print('Received:', data.decode())



