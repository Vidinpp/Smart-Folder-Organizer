import os 
import shutil
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
        name, extension = os.path.splitext(item)
        extension=extension.lower()
        print(f"\nchecking: {item}")
    
        for category,extensions in file_types.items():
            
            if extension in extensions:
                
                print(f"\nCategory: {category}")
                source=item
                destination=os.path.join(category,item)
                if not os.path.exists(category):
                    os.mkdir(category)
                
                shutil.move(source,destination)
                
                print("Move succesfully")