import json
from os.path import exists
import unreadable


# encode the password
def encode_pwd(set_pwd):
    return unreadable.encode(set_pwd)


# decode the password
def decode_pwd(get_pwd):
    return unreadable.decode(get_pwd)


def get_json_length():
    n = 0
    if exists('data.json'):
        data = json.load(open('data.json'))
        n = len(data)
    return n


# Setting the data in local variables
def set_data(s_host, s_username, s_pwd):
    pwd = encode_pwd(s_pwd)
    host = s_host
    username = s_username
    write_to_json(host, username, pwd)


# Method to write user data to file in Json format
def write_to_json(host, username, pwd):
    d_list = []
    data = {
        'host': host,
        'username': username,
        'password': pwd
    }
    if exists('data.json'):
        print('if')
        with open('data.json') as fp:
            d_list = json.load(fp)
            for x in d_list:
                if x['host'] == host:
                    print('Host already exists')
                    return

            d_list.append(data)
            with open('data.json', 'w+') as json_file:
                json.dump(d_list, json_file,
                          indent=4,
                          separators=(',', ': '))
    else:
        print('else')
        d_list.append(data)
        open('data.json', 'w')
        with open('data.json', 'w+') as json_file:
            json.dump(d_list, json_file,
                      indent=4,
                      separators=(',', ': '))


# implement read json method here also add it to TKinter


def read_json(entry):
    data = json.load(open('data.json'))
    host = data[entry]['host']
    username = data[entry]['username']
    pwd = decode_pwd(data[entry]['password'])
    return host, username, pwd







