
import json 
  
# Data to be written 
dictionary ={ 
    "none" : "0",
} 
  
with open("sample.json", "w") as outfile: 
    json.dump(dictionary, outfile) 
