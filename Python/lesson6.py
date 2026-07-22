file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Text": [".txt"],
    "Python": [".py"]
}

extensions=[".pdf"]

if extensions in file_types["Images"]:
    print("This is Image")
elif extensions in file_types["PDFs"]:
    print("This is PDF")
elif extensions in file_types["Videos"]:
    print("This is Videos")
elif extensions in file_types["Music"]:
    print("This is Music")
elif extensions in file_types["Text"]:
    print("This is Text")
elif extensions in file_types["Python"]:
    print("This is Python file ")
else:
    print("This something file")
    
    
    

for category, extension in file_types.items():
    if extension in extensions:
        print(f"This is {category}")
        break