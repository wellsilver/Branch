import secrets
cookies=[]
# ^ change to file
class cookie:
  def valid(cookie):
    f=False
    global cookies
    for i in cookies:
      if i == cookie:
        f=True
        break
    if f ==True:
      return True
    else:
      return False
  def make(userID):
    pass
class user:
  def get(ID):
    try:
      file=open(f"store/user/{ID}.toml")
    except:
      return None
    
  def create(user,passw):
    pass
  def change(mode):
    pass