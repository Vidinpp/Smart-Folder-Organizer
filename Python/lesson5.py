import os

filename="image.jpg"

name,extension=os.path.splitext(filename)

print(name)
print(extension)


files = [
    "photo.jpg",
    "movie.mp4",
    "resume.pdf",
    "notes.txt",
    "song.mp3"
]

for file in files:
    name,extension=os.path.splitext(file)
    print(name)
    print(extension)
    
    
#mini challange

files = [
    "photo.jpg",
    "movie.mp4",
    "resume.pdf",
    "notes.txt",
    "song.mp3"
]

for file in files:
    name,extension=os.path.splitext(file)
    print(f"{name} -> {extension}")