import os,sys
os.system("git pull")
try:
    __import__("swag").swag()
except Exception as e:
    exit(str(e))
