'''
export 2 sets of windows shares as such:
net share >> <servername>-net-share.txt

edit the <servername>-net-share.txt to remove line breaks

copy files to the same folder as this parse-shares.py file and
update the file_1, file_2 variables below

set the root_drive variable for the shares
'''

# TODO: fix need to do manual fix for wrapped file lines
# TODO: make root_drive a dictionary item to allow for differing roots
# TODO: provide an array of dictionary items to handle > 2 servers at a time

file_1 = 'fs-net-share.txt'
file_2 = 'adp-net-share.txt'
root_drive = 'D:\\'

def read_files(file_name=None):
    from io import open

    assert file_name

    with open(file_name) as f:
        file_contents = f.readlines()
    f.closed

    return file_contents

def parse_shares(file_contents=None):

    assert file_contents

    file_line_split = []
    for file_line in file_contents:
        if ' D:\\' in file_line and file_line[1] != '$':
            file_line_split.append((file_line.split(root_drive)[0]).strip())

    return file_line_split

# do the stuff
file_1_contents = read_files(file_1)
file_2_contents = read_files(file_2)

file_1_shares = parse_shares(file_1_contents)
file_2_shares = parse_shares(file_2_contents)

share_union = set(file_1_shares).intersection(file_2_shares)
print(share_union)




