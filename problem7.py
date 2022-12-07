class Dir:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.files = []
        self.directories = []
        self.size = 0

    def __str__(self) -> str:
        return f'-------------\nDir: {self.name} \n' +\
            f'Directories: {[dir.name for dir in self.directories]}\n'+\
            f'Files: {[f for f in self.files]}\n'+\
            f'Size: {self.size}\n-----------------\n'

# once file tree is constructed, traverse and calculate sizes
def compute_sizes(cwd):
    # recursive call for each dir in cwd
    sum = 0
    for dir in cwd.directories:
        sum += compute_sizes(dir)
    # add files in dir
    for file in cwd.files:
        sum += file[0]
    cwd.size = sum
    return sum

def get_target_dirs(dir, found_dirs):
    if dir.size <= 100000:
        found_dirs.append(dir)
    for child in dir.directories:
        get_target_dirs(child, found_dirs)

    

with open('problem7.txt', 'r') as input:
    root = Dir(None, '/')
    cwd = root
    for line in input.readlines()[1:]:
        command = line[:-1].split(' ')
        if command[1] == 'cd':
            if command[2] == '..':
                cwd = cwd.parent
            else:
                # cd <dir>
                new_dir = Dir(cwd, command[2])
                cwd.directories.append(new_dir)
                cwd = new_dir
        elif command[0] != 'dir' and command[0] != '$':
            # file
            cwd.files.append((int(command[0]), command[1]))

    
    compute_sizes(root) # calculate size of each directory
    target_dirs = []
    get_target_dirs(root, target_dirs)
    print("Sum of sizes of dirs with at most 100.000 size is: ", sum([dir.size for dir in target_dirs]))
    
    # ================ PART TWO ===================
    total_disk = 70000000
    required_disk = 30000000
    free_disk = total_disk - root.size
    required_deletion = required_disk - free_disk
    print(f'Disk stats:\n--> Free disk: {free_disk}\n--> Required deletion: {required_deletion}')

    targets_for_removal = []
    def get_target_dirs_v2(dir, found_dirs):
        if dir.size >= required_deletion:
            found_dirs.append(dir)
        for child in dir.directories:
            get_target_dirs_v2(child, found_dirs)

    get_target_dirs_v2(root, targets_for_removal)
    print(f'Size of smallest target directory is {min([dir.size for dir in targets_for_removal])}')

    
    
