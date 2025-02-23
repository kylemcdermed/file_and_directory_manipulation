import os, shutil

try:
    if not os.path.exists("logs"):
        os.mkdir("logs")
        print("Successfully created logs dir")
    else:
        print("logs dir already exists")

    if not os.path.exists("backup_logs"):
        os.mkdir("backup_logs")
        print("Successfully created backup_logs dir")
    else:
        print("backup_logs already exists")
except FileExistsError as e:
    print(f"The {e} directory already exists")

try:
    if os.path.exists("logs.csv"):
        shutil.move("logs.csv","logs")
        print("Successfully moved logs.csv to logs dir")
    else:
        print("logs.csv not moved to logs dir")

    if os.path.exists("sample.txt"):
        os.remove("sample.txt")
        print("Successfully deleted sample.txt file")
    else:
        print("sample.txt file does not exist")
except FileNotFoundError as e:
    print(f"The {e} file does not exist")

    
