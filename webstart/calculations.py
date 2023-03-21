def permissions(guild):
    return (int(guild.permissions) & 0x20) == 0x20

def iscasesin(guild):
    return True # until next line is fixed
    # return 'botname' in guild.members

def updateLD(Client, get_leaderbaord, db):
    get_leaderbaord()
    return [(Client.users.get_user(id[0]).username, id[1], Client.users.get_user(id[0]).avatar_url) for id in db.leaderboard]
