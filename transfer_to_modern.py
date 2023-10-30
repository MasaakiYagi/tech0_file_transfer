from ftplib import FTP
import os


def upload_file_to_ftp(server_ip, file_path):
    """
    Upload a file to an FTP server.

    :param server_ip: The IP address of the FTP server.
    :param file_path: The local path of the file to be uploaded.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist. Exiting.")
        return

    try:
        # Connect to the FTP server
        ftp = FTP(server_ip)

        # Use anonymous FTP access
        ftp.login()

        # Enable Passive Mode
        ftp.set_pasv(True)

        # Upload the file
        with open(file_path, 'rb') as file:
            print(f"STOR {os.path.basename(file_path)}")
            ftp.storbinary(f"STOR {os.path.basename(file_path)}", file)

        # Close the connection
        ftp.quit()

    except Exception as e:
        print(f"An error occurred: {e}")


# Usage
file_path = "C:\\Users\\USERNAME\\Documents\\rep_dscnt\\output\\m_dscnt_data.csv"  # 送信対象ファイル
server_ip = "XXX.XXX.XXX.XXX"  # 接続先FTPサーバーのIP

upload_file_to_ftp(server_ip, file_path)
