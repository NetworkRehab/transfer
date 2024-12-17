# Transfer

A simple SFTP CLI client for transferring files to and from a remote SFTP server.

## Requirements

- Python 3.x
- `paramiko` library

## Installation

Install the required dependency:

```bash
pip install paramiko
```

## Usage

```bash
python sftp_client.py host username password action local_path remote_path
```

- `host`: SFTP server hostname or IP address
- `username`: Username for SFTP server
- `password`: Password for SFTP server
- `action`: `upload` or `download`
- `local_path`: Path to the local file
- `remote_path`: Path on the remote server

## Examples

### Upload a File

```bash
python sftp_client.py example.com user password upload /local/path/file.txt /remote/path/file.txt
```

### Download a File

```bash
python sftp_client.py example.com user password download /local/path/file.txt /remote/path/file.txt
```

## License

This project is licensed under the MIT License.
