import os
union = os.environ.get
version = union("UB_VER")
ver = "0.1"
async def checkup():
  if version != ver:
    print ("Version Can't Match Please Update the bot or contact support")
    sys.exit()
  else:
    pass

SESSION = union("SESSION")
APP_ID = union("APP_ID")
API_HASH = union("API_HASH")
