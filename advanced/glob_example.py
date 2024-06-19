import glob
import os

if __name__ == '__main__':
    print('GLOB USAGE')
    print(glob.glob('*.py'))
    print(glob.glob('?sserts.py'))
    # [] match any character in the sequence
    print(glob.glob('[ac]*.py'))
    # [!] match any character in the sequence
    print(glob.glob('[!ac]*.py'))
    print(glob.glob('**/*.py', root_dir="C:/Users/luisf/Desktop/CODE/python/mastering_python/medium",
                    recursive=True,
                    include_hidden=True)) # 3.11

    globs = glob.iglob('**/*.py', recursive=True, include_hidden=True)
    for i, glob in enumerate(globs):
        print(i,glob, sep="). ")
