import os
from dotenv import load_dotenv
load_dotenv()

w = os.getenv("MYNAME")
x = os.getenv("FAVORITEICECREAM")
y = os.getenv("DBSECRET")
z = os.getenv("ADMINEMAIL")
print(w, x, y, z)
