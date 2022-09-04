import pathlib

def twelve_point_two():

    pathlib.Path.home() / 'ubuntu-sistemas'
    cwd_path = pathlib.Path.cwd()

    path = pathlib.Path('root/')

    list(cwd_path.parents)

    path = pathlib.Path.home() / 'development'
    #print(f'{path} exist {path.exists()}')

    #print(f'{path} is directory: {path.is_dir()}')

    path = path / 'docker-compose.yml'
    #print(f'{path} is file: {path.is_file()}')

    file_path = pathlib.Path.home() / 'my_folder/my_file.txt'
    print(file_path.exists())
    print(file_path.name)
    print(file_path.parent.name)

def twelve_point_three():
    new_dir = pathlib.Path.home() / 'new_directory'
    new_dir.mkdir(exist_ok=True)

    nested_dir = new_dir / 'folder_a' / 'folder_b'
    nested_dir.mkdir(parents=True, exist_ok=True)

    file_path = new_dir / 'file1.txt'
    #print(file_path.exists())
    file_path.touch()
    #print(file_path.exists())

    '''  for path in new_dir.iterdir():
        print(path)

    for path in new_dir.glob("*.txt"):
        print(path) '''

    
    paths = [
        new_dir / "program1.py",
        new_dir / "program2.py",
        new_dir / "folder_a" / "program3.py",
        new_dir / "folder_a" / "folder_b" / "image1.jpg",
        new_dir / "folder_a" / "folder_b" / "image2.png",
        ]
    
    for path in paths:
        path.touch()
    
    #print(list(new_dir.glob("*1*")))
    #print(list(new_dir.glob("program?.py")))
    #print(list(new_dir.glob("program[13].py")))

    print(list(new_dir.rglob("*.py")))

    source = new_dir / 'file1.txt'
    destination = new_dir / 'folder_a' / 'file1.txt'
    if not destination.exists():
        source.replace(destination)

twelve_point_three()