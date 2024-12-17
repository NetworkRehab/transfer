
import argparse
import paramiko

def parse_args():
    parser = argparse.ArgumentParser(description='SFTP CLI Client')
    parser.add_argument('host', help='SFTP server hostname or IP address')
    parser.add_argument('username', help='Username for SFTP server')
    parser.add_argument('password', help='Password for SFTP server')
    parser.add_argument('action', choices=['upload', 'download'], help='Action to perform')
    parser.add_argument('local_path', help='Path to the local file')
    parser.add_argument('remote_path', help='Path on the remote server')
    return parser.parse_args()

def sftp_transfer(host, username, password, action, local_path, remote_path):
    transport = paramiko.Transport((host, 22))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    if action == 'upload':
        sftp.put(local_path, remote_path)
    elif action == 'download':
        sftp.get(remote_path, local_path)
    sftp.close()
    transport.close()

if __name__ == '__main__':
    args = parse_args()
    sftp_transfer(args.host, args.username, args.password, args.action, args.local_path, args.remote_path)