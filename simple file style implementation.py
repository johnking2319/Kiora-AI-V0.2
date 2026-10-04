import json
from pathlib import Path
from datetime import datetime
FILE=Path("conversation.json")

def save_messages(role,content):
    if FILE.exists():
        with open(FILE,"r") as file:
            history=json.load(file)
    else:
        history=[]
        
        messages={datetime.now().isoformat()}
        
        history.append(messages)
        
        with open(FILE,"w") as file:
            json.dump(history,file,indent=4)
            
while True:
    command=input("You :")
    save_messages("user",command)
    response=command()
    print("Kiora AI :",response)
    
    save_messages("Assistant",response)