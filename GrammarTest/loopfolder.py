import os
rootdir = 'e:/GitCode/Python/GrammarTest/'
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print os.path.join(subdir, file)
