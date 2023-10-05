import socket

def main():
    server_ip = "127.0.0.1"  # Địa chỉ IP của server
    server_port = 8890       # Cổng của server

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        print("Danh sách dịch vụ:")
        print("1. Đảo ngược chuỗi đồng thời in hoa ký tự đầu của mỗi từ")
        print("2. Tính tổng chuỗi các số nguyên (khoảng trắng)")
        print("3. Thoát")
        choice = input("Chọn dịch vụ (1/2/3): ")

        if choice == "1" or choice == "2" or choice == "3":
            client.send(choice.encode())

            if choice == "3":
                client.close()
                break
            
            response = client.recv(1024).decode()
            print(response)
            
            if choice == "1":
                data = input("Nhập dữ liệu: ")
                client.send(data.encode())
                result = client.recv(1024).decode()
                print(result)
                
            elif choice == "2":
                data = input("Nhập chuỗi số nguyên (cách nhau bởi khoảng trắng): ")
                client.send(data.encode())
                result = client.recv(1024).decode()
                print(result)
                
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()