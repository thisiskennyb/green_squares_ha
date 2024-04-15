import subprocess


with open('green.txt', 'a') as file:

    file.write("I will not fake green squares so recruiters will notice me\n")


commands = [
    "git add .",               
    "git commit -m 'plus one green square ftw'",
    "git push origin master"       
]

for cmd in commands:
    subprocess.run(cmd, shell=True)