import os


filename = 'project_file_map.txt'
with open(filename, 'w') as file_map:
    for root, dirs, files in os.walk("."):
        path = root.split(os.sep)
        print(path)
        if os.path.basename(root) in ('__pycache__', '.'):
            continue
        file_map.write(f'{(len(path) - 1) * "---"} {os.path.basename(root)}\n')
        for file in files:
            line = f'{len(path) * "----"} {file}\n'
            file_map.write(line)

print(f'Project map write in {filename}')
