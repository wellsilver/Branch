import toml
import secrets
cookies=[]
# ^ change to file
# actually dont? it only uses 32 megabytes per million people and shut downs dont happen everyday lol
class cookie:
  # a cookie in the table is [(cookie,userid),]
  def valid(cookie):
    f=False
    global cookies
    for i in cookies:
      if i == cookie:
        f=True
        ff=i[1]
        break
    if f ==True:
      return ff
    else:
      return False
  def make(userID):
    global cookies
    key=secrets.token_urlsafe(32)
    for i in cookies:
      if i[0]==key:
        return 0
    cookies.append((key,userID))
    return key
class user:
  def get(ID):
    try:
      open(f"store/user/{ID}.toml").close()
    except:
      return None
    a=toml.load(open(f"store/user/{ID}.toml"))
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