import json
from os.path import exists


# encode the password
def encode_pwd(set_pwd):
    return set_pwd.encode('u32')


# decode the password
def decode_pwd(get_pwd):
    return get_pwd.decode('u32')


def get_json_length():
    data = json.load(open('data.json'))
    return len(data)


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
        'password': str(pwd).replace("'", '"')
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
    host = data[entry - 1]['host']
    username = data[entry - 1]['username']
    pwd = decode_pwd(data[entry - 1]['password'])
    return host, username, pwd


