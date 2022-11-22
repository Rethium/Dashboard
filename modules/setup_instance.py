from os import getcwd, mkdir, path

dirs = ["logs"]
for dir in dirs:
    if not path.exists(dir):
        mkdir(path.join(getcwd(), dir))

with open('logs/app.log', 'w+') as fp:
    fp.close()
