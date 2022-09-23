import subprocess
import sys

from pcscp.config import setup


def build_local(
        file: str,
        local_path: str
) -> str:
    return local_path + '\\' + file


def build_remote(
        file: str,
        remote_user: str,
        remote_host: str,
        remote_path: str
) -> str:
    return f'{remote_user}@{remote_host}:{remote_path}/{file}'


def scp(
        local: str,
        remote: str,
        upload: bool
) -> list[str]:
    if upload:
        return ['scp', local, remote]
    return ['scp', remote, local]


def main():
    relative_file_path: str = sys.argv[1]

    conf = setup(sys.argv[2] + '\\pcscp.json')

    command = scp(
        local=build_local(
            file=relative_file_path,
            local_path=conf['mapping']['local_project_path'],),
        remote=build_remote(
            file=relative_file_path.replace('\\', '/'),
            remote_user=conf['login']['user'],
            remote_host=conf['login']['host'],
            remote_path=conf['mapping']['remote_project_path']),
        upload=True)

    subprocess.run(command, check=True)
