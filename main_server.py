from web_server import DataBase

class MainDatabase(DataBase.Model):
    _id = DataBase.Column("_id", DataBase.Integer, primary_key=True)
    username = DataBase.Column("username", DataBase.String, nullable=False)
    hashedPassword = DataBase.Column("password", DataBase.String, nullable=False)
    
    def __init__(self, username, hashedPassword):
        self.username = username
        self.hashedPassword = hashedPassword

def GetDatabaseData():
    for user in DataBase.query.All():
        m_user = user.username
        m_password = user.hashedPassword
        print("USER: ", m_user, " | PASS:", m_password)

def QueryDatabase(QueryType, ToQuery):
    if QueryType == "Username":
        queryResult = DataBase.query.filter_by(username=ToQuery).First()
    
    return queryResult
