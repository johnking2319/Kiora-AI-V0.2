from pathlib import Path
file_path=Path("data.txt")

with open("data.txt","r") as file:
    content=file.read()
    
if file_path.exists():
    print("File Exists")
    
else:
    print("File doesnt exist")
    
