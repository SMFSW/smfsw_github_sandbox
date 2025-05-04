# -*- coding: utf-8 -*-
import os
import subprocess
import argparse

def recursive_git_repository_command(root, cmd):
    for current_dir, sub_dirs, files in os.walk(root):
        if '.git' in sub_dirs:
            print(f"\n📁 Git repository : {current_dir}")
            try:
                result = subprocess.run(cmd, shell=True, cwd=current_dir,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.stdout:
                    print("🟢 Output:", result.stdout.strip())
                if result.stderr:
                    print("🔴 Error:", result.stderr.strip())
            except Exception as e:
                print(f"⚠️ Error in {current_dir} : {e}")

def main():
    parser = argparse.ArgumentParser(description="Execute a command in all folders including a Git repository.")
    parser.add_argument("--root", required=True, help="Root path")
    parser.add_argument("--cmd", required=True, help="Command to execute (between quotes if command contains spaces)")

    args = parser.parse_args()
    recursive_git_repository_command(args.root, args.cmd)
    os.system("PAUSE")

if __name__ == "__main__":
    main()
