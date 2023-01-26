import pysftp
import paramiko

videoFile = ''
destinationPath = ''
host = ''
username = ''
password = ''


def set_variables(set_file, set_path, set_host, set_username, set_password):
    global videoFile, destinationPath, host, username, password

    videoFile = set_file
    destinationPath = set_path
    host = set_host
    username = set_username
    password = set_password


def send_video():
    print('test')
