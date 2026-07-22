import os

file_types={
    "Images": [".jpg", ".jpeg", ".png"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Text": [".txt"],
    "Python": [".py"]
}

for item in os.listdir():
    if os.path.isfile(item):
        name, extension=os.path.splitext(item)
        
        print(f"\nchecking: {item}")
        
        for category, extensions in file_types.items():
            
            if extension in extensions:
                print(f"category: {category}")
                break
                