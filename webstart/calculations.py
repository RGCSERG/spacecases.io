def permissions(guilds):
    return [guild for guild in guilds if int(guild.permissions) & 0x20 == 0x20] # returns True if User has Manage Server privilages

def iscasesin(guilds, Client_guilds):
    return [guild for guild in guilds if guild.id in [guild.id for guild in Client_guilds]] # returns servers if server is in discord bot server list

def updateLD(Client, get_leaderboard, db):
    get_leaderboard()

    if type(db.leaderboard[0]) == str:
        return db.leaderboard, False # returns false iteration if index[0] is an error message
    if type(db.leaderboard[0][0]) != str:
        leaderboard = []
        for id in db.leaderboard[:10]:
            user_data = db.user_data.find_one({"_id": id[0]})
            if len(user_data['inventory']) > 0:
                leaderboard.append((Client.users.get_user(id[0]).username, id[1], id[2], Client.users.get_user(id[0]).avatar_url, user_data['inventory'][0]['name']))
            else:
                leaderboard.append((Client.users.get_user(id[0]).username, id[1], id[2], Client.users.get_user(id[0]).avatar_url))
        with open('leaderboard.py', 'w') as f: # if leaderboard is updated it rewrites the saved leaderboard in the file - probaly should change this to a local db
            f.write(f'Leaderboard = {leaderboard}\nunfiltered_Leaderboard = {db.leaderboard}')
            f.close()
        return leaderboard, True # returns updated leaderboard # not needed right now
    
    return db.leaderboard[:10], True

def get_user_inv(db, datetime, id):
    user = db.user_data.find_one({"_id": id})
    user['inventory'] = [{'name': item['name'], 'float': item['float'] , 'image_url': db.skin_data["skins"][item['name']]['image_url']} for item in user['inventory']]
    user['balance'] = user['balance']/100
    user['return'] = round((user['stats']['total_return']/user['stats']['total_spent'])*100, 2)
    user['join_date'] = datetime.utcfromtimestamp(user['join_date']).strftime('%Y-%m-%d')
    for i, item in enumerate(db.unfiltered_leaderboard):
        if item[0] == user['_id']:
            user['rank'] = i + 1
            user['networth'] = item[1]/100
            break
    return user # returns user inventory with image_url as well as name and float