file_name = input("File name: ").strip().lower()
file_ext = file_name.split(".")

if file_ext[-1] == "gif":
    print("image/gif")
elif file_ext[-1] == "jpg" or file_ext[-1] == "jpeg":
    print("image/jpeg")
elif file_ext[-1] == "png":
    print("image/png")
elif file_ext[-1] == "pdf":
    print("application/pdf")
elif file_ext[-1] == "txt":
    print("text/plain")
elif file_ext[-1] == "zip":
    print("application/zip")
else:
    print("application/octet-stream")