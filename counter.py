from os import walk
import os


def count_lines(directory, ignore, file_types):
    ignored = set()
    paths = []
    lines = 0

    for (dirpath, dirnames, filenames) in walk(directory):
        for ig in ignore:
            if ig in dirpath:
                ignored.add(dirpath)

        if dirpath not in ignored:
            for name in filenames:
                if os.path.splitext(name)[1] in file_types:
                    paths.append(os.path.join(dirpath, name))
    
    for path in paths:
        with open(path, 'r') as f:
            lines += len(f.readlines())


    return lines

if __name__ == '__main__':
    directory = '../'
    ignore = ['__init__.py', '__pycache__.py', '.git', '__pycache__', 'env', 'node_modules', 'build']
    file_types = ['.js', '.py']
    print(count_lines(directory, ignore, file_types))
