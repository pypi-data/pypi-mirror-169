import sys
import asyncio
import secrets
from subprocess import SubprocessError
from asyncio.subprocess import PIPE, Process
from typing import Tuple, AnyStr, List, Iterable

import aiofiles

SYS_ENCODING = sys.getdefaultencoding()


def generate_env(debug: bool=False, hosts: str='*') -> str:
    items = [
        f'SECRET_KEY={secrets.token_hex(128)}',
        f'ALLOWED_HOSTS={hosts}'
    ]

    if debug:
        items.append('DEBUG=True')

    return '\n\n'.join(items)


def edit_settings(lines: Iterable[str]) -> List[str]:
    result = []

    for line in lines:
        if line.startswith('BASE_DIR'):
            result.append('\nfrom environ import Env\n')

            result.append(f'\n{line}\n')

            result.append('\nenv = Env(DEBUG=(bool, False))\n')
            
            result.append('\nEnv.read_env(BASE_DIR / \'.env\')\n')

        elif line.startswith('SECRET_KEY'):
            result.append(f'SECRET_KEY = env(\'SECRET_KEY\')\n')
        elif line.startswith('ALLOWED_HOSTS'):
            result.append('ALLOWED_HOSTS = env.tuple(\'ALLOWED_HOSTS\')')
        elif line.startswith('DEBUG'):
            result.append('DEBUG = env(\'DEBUG\')\n')
        else:
            result.append(line)

    return result


async def write_file(path: str, content: AnyStr, mode: str='w'):
    async with aiofiles.open(path, mode) as file:
        await file.write(content)


async def run_cmd(args: Tuple[str], **kwargs) -> Process:
    cmd = ' '.join(args)

    kwargs = {
        'stdout': PIPE,
        'stderr': PIPE,
        **kwargs
    }

    result = await asyncio.create_subprocess_shell(cmd, **kwargs)

    out, err = [item.decode(SYS_ENCODING) if isinstance(item, bytes) else item for item in await result.communicate()]

    code = result.returncode

    if code != 0:
        raise SubprocessError(f'{code}: {err}')

    if out:
        print(out)

    return result


async def install_packages(pip_path: str, packages: Iterable[str]):
    tasks = [
        run_cmd((
            pip_path,
            'install',
            '--require-virtualenv',
            '-v',
            '--disable-pip-version-check',
            package
        )) for package in packages
    ]

    await asyncio.gather(*tasks)
