# -*- coding: utf-8 -*-
import os
import subprocess

# command to execute
command = "git fetch --all"

# Access a specific environment variable, e.g., 'PATH'
path = os.environ.get('GITHUB_REPOS_ROOT')

print(f"GITHUB_REPOS_ROOT at: {path}")

# Arguments to pass
subprocess.run([
    'python', 'recursive_git_cmd_arg.py',
    '--root', path,
    '--cmd', command
], check=True)