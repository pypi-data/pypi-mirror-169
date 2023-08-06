import os
import asyncio
from shlex import quote

import aiofiles

from . import  const, utils, parser


async def exec():
    args = parser.parse_args()

    project_dir = args.dir

    print('Checking project directory...')

    if not os.path.exists(project_dir):
        print('Project directory not found, creating project directory')

        os.mkdir(project_dir)
    else:
        print('Project directory found')

    name = args.name 

    print('Creating Django project...')

    await utils.run_cmd(('django-admin', 'startproject', name, project_dir))

    print('Django project created')

    venv_dir = os.path.join(project_dir, 'venv/')

    print('Creating files...')

    tasks = [
        utils.write_file(
            os.path.join(project_dir, '.gitignore'),
            const.GITIGNORE
        ),
        utils.write_file(
            os.path.join(project_dir, '.env'),
            utils.generate_env(args.debug, args.hosts)
        ),
        utils.write_file(
            os.path.join(project_dir, 'env.example'),
            const.ENV_EXAMPLE
        ),
        utils.run_cmd([args.python, '-m', 'venv', quote(venv_dir)])
    ]

    if args.git:
        tasks.append(utils.run_cmd(['git', 'init', project_dir]))  

    await asyncio.gather(*tasks)

    print('Created files')

    bin_path = os.path.join(venv_dir, 'bin')

    pip_path = os.path.join(bin_path, 'pip') 

    print('Installing required packages...')

    packages = map(quote, frozenset((*const.REQUIRED_PACKAGES, *args.packages)))

    await utils.install_packages(pip_path, packages)

    print('Installed required packages')

    print('Writing requirements...')

    requirements_path = os.path.join(project_dir, 'requirements.txt')

    with open(requirements_path, 'w') as file:
        await utils.run_cmd((pip_path, 'freeze'), stdout=file)

    print('Added requirements')

    print('Editing settings file...')

    settings_dir = os.path.join(project_dir, args.name, 'settings.py')

    async with aiofiles.open(settings_dir, 'r+') as file:
        lines = await file.readlines()

        result = utils.edit_settings(lines)

        await file.seek(0)

        await file.writelines(result)

    print('Edited settings file')
    
    tasks = []

    if args.git and args.commit:
        tasks.append(utils.run_cmd((
            'cd',
            quote(project_dir),
            '&&',
            'git',
            'add',
            '-v',
            '.',
            '&&'
            'git',
            'commit',
            '-v',
            '-m',
            f'"{args.commit_message}"'
        )))

    if args.migrate:
        python_path = os.path.join(bin_path, 'python')

        manage_path = os.path.join(project_dir, 'manage.py')

        tasks.append(utils.run_cmd((
            python_path,
            quote(manage_path),
            'migrate',
            '--no-input'
        )))

    await asyncio.gather(*tasks)

    
def main():
    asyncio.run(exec())

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
