import os
Folders=["Images","PDFs","Videos"]

for Folder in Folders:
    if not os.path.exists(Folder):
        os.mkdir(Folder)
        print(f"{Folder} created Successfully")
    else:
        print(f"{Folder} are already existed")
