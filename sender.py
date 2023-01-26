import pysftp
import paramiko

videoFile = ''
destinationPath = ''
host = ''
username = ''
password = ''


def set_variables(set_host, set_username, set_password):
    global videoFile, destinationPath, host, username, password

#    destinationPath = set_path
    host = set_host
    username = set_username
    password = set_password


def set_videofile(set_file):
    global videoFile
    videoFile = set_file


def send_video():
    print(videoFile, destinationPath, host, username)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password, port=22)

    sftp = client.open_sftp()
    sftp.put(videoFile, destinationPath)

    sftp.close()