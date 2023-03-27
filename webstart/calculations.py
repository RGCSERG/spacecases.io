def permissions(guilds):
    return [guild for guild in guilds if int(guild.permissions) & 0x20 == 0x20] # returns True if User has Manage Server privilages

def iscasesin(guilds, Client_guilds):
    return [guild for guild in guilds if guild.id in [guild.id for guild in Client_guilds]] # returns servers if server is in discord bot server list

def updateLD(Client, get_leaderboard, db):
    get_leaderboard()

    if type(db.leaderboard[0]) == str:
        return db.leaderboard, False
    if type(db.leaderboard[0][0]) != str:
        return ['setup leaderboard funciton'], False
    
    #[(Client.users.get_user(id[0]).username, id[1], Client.users.get_user(id[0]).avatar_url) for id in db.leaderboard[:10]] #returns updated leaderboard # not needed right now
    return db.leaderboard[:10], True