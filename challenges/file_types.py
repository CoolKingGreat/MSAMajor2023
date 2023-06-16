file_name = input("File name: ").lower();

if file_name.find(".") != -1:
    extension = file_name.split(".")[1]
else:
    extension = "octet-stream"
prefix = ""
if extension in ["gif", "jpg", "jpeg", "png"]:
    prefix = "image"
elif extension in ["pdf", "txt"]:
    prefix = "document"
elif extension == "zip":
    prefix = "file"
else:
    prefix = "application"
    
print(prefix+"/"+extension)