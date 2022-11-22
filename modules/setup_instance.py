from os import path, mkdir, getcwd,listdir

dirs = ["logs"]
print(getcwd())
for dir in dirs:
    print(path.exists(dir))
    if not path.exists(dir):
        mkdir(path.join(getcwd(), dir))
print(listdir())
with open('logs/app.log', 'w+') as fp:
    fp.close()
