import sys
import os
import json


DIRPATHS = 0
DIRNAMES = 1
FILENAMES = 2

print(next(os.walk('.'))[DIRPATHS])
print(next(os.walk('.'))[DIRNAMES])
print(next(os.walk('.'))[FILENAMES])

result = { }

song_directories = next(os.walk('.'))[DIRNAMES]

for song_direcory in song_directories:
    if song_direcory.startswith("."):
        continue

    files = next(os.walk(song_direcory))[FILENAMES]

    for file in files:

        if file.startswith(".") or file.endswith(".meta"):
            continue

        file_path = f"{song_direcory}/{file}"
        
        result[file_path] = { }

        # check modified time
        # check path
        # audio
        result[file_path]["ModificationDate"] = os.path.getmtime(file_path)
        result[file_path]["Size"] = os.path.getsize(file_path)

y = json.dumps(result, indent=4)

with open("catalog.json", "w") as index:
    index.write(y)