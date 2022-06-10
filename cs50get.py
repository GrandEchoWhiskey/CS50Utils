import sys
import subprocess

"""
To make it even easier to use - just type alias
find a row where -> HOME="workspaces/YOUR_CODESPACE_NUMBER",
select and rightclick to copy. Now create your own alias:
alias cs50get='python workspaces/YOUR_CODESPACE_NUMBER/cs50get.py'
or if you dont have it in your main directory:
alias cs50get='python workspaces/YOUR_CODESPACE_NUMBER/YOUR_PATH/cs50get.py'
be free and use this programm in every directory you want.
Remember that the directory made by the zip file,
is gonna be placed in your current console path
"""

def command(string):

    p = subprocess.Popen(string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print(line[:-1])
    p.wait()


def main():

    if len(sys.argv) != 2: return

    commands = {
        'wget': f"wget {sys.argv[1]}",
        'unzip': f"unzip {sys.argv[1].split('/')[-1]}",
        'remove': f"rm {sys.argv[1].split('/')[-1]}"
    }

    for key in commands:
        command(commands[key])


if __name__ == "__main__":
    main()