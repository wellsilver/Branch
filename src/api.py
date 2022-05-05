import secrets
cookies=[]
# ^ change to file
# actually dont? it only uses 32 megabytes per million people and shut downs dont happen everyday lol
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
  def get(UserID):
    try:
      file=open(f"store/user/{ID}.toml")
    except:
      return None
  def getID(user):
    # return integer of ID
    pass
  def validate(user,passw):
    #return true if good
    pass
  def create(user,passw):
    pass
  def change(ID,infotochange,info):
    pass