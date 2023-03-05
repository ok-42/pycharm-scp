import subprocess
import sys
from pathlib import Path

from pcscp.config import setup
from pcscp.utils import convert_line_endings


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


def main() -> None:
    """Creates a new file with LF and sends it to remote machine using SCP.

    [1] Convert CRLF to LF (that creates a new temporary file).

    [2] Read paths mapping.

    [3] Execute SCP command.

    [4] Remove the temporary file from [1].
    """

    # [1]
    relative_file_path_crlf: str = sys.argv[1]
    relative_file_path_lf: str = relative_file_path_crlf + 'LF'
    convert_line_endings(
        input_file=relative_file_path_crlf,
        output_file=relative_file_path_lf)

    # [2]
    conf = setup(sys.argv[2] + '\\pcscp.json')

    # [3]
    command = scp(
        local=build_local(
            file=relative_file_path_lf,
            local_path=conf['mapping']['local_project_path'],),
        remote=build_remote(
            file=relative_file_path_crlf.replace('\\', '/'),
            remote_user=conf['login']['user'],
            remote_host=conf['login']['host'],
            remote_path=conf['mapping']['remote_project_path']),
        upload=True)

    subprocess.run(command, check=True)

    # [4]
    Path(relative_file_path_lf).unlink()
