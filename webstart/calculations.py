def permissions(guild):
    return (int(guild.permissions) & 0x20) == 0x20

def iscasesin(guild):
    return True # until next line is fixed
    # return 'botname' in guild.members

def updateLD(Client, get_leaderbaord, db):
    #get_leaderbaord()
    return [('FarmerJoe', 1719305, 'https://cdn.discordapp.com/avatars/570945676632915983/cefba4f180f822f9e66de059e51b5481.png'), ('JaSaTo', 544505, 'https://cdn.discordapp.com/avatars/614450150470844427/30aa70a42438ffd4f3b91cc74a664062.png'), ('Reubenz1', 418741, 'https://cdn.discordapp.com/avatars/389813398831104003/8bc3fbd30771e992a107c02cb7623973.png'), ('sparky', 242139, 'https://cdn.discordapp.com/avatars/790570913165738016/dab4c4e15723156e3ef6ed3693d6c06c.png'), ('freddy', 95140, 'https://cdn.discordapp.com/avatars/418420102506217473/40e67487e66931e492cdc63b81d43686.png'), ('c00ckie', 1336, 'https://cdn.discordapp.com/avatars/391273931744739328/89f5273c6ed032e39e05b5cd416de43f.png'), ('samoel', 195, 'https://cdn.discordapp.com/avatars/577511899231420427/07d9efe85d0bb782a237594e59c289bf.png'), ('Roo', 11, 'https://cdn.discordapp.com/avatars/752638641087447090/13013638317eb727b7a454f5289f18d3.png'), ('thomas', 10, 'https://cdn.discordapp.com/avatars/741930167865442367/25869ef2c0cb760996844b6724795694.png'), ('carpetpoo', 0, 'https://cdn.discordapp.com/avatars/554083602581815306/e357d37e1d8b7f2c2d00d7529cd18cc1.png'), ('pooshitpisspoo', 0, None), ('Willl', 0, 'https://cdn.discordapp.com/avatars/582473067822055435/cce5cb7c4a386f7185afdcac0ee1124b.png'), ('leojacsin', 0, None), ('Alex.', 0, 'https://cdn.discordapp.com/avatars/389406845791371266/ba015738d875e22ebaed2dccf6251403.png'), ('SavestaSemen', 0, 'https://cdn.discordapp.com/avatars/632964319809765396/da1067adcf29a47ddd4f4e2bbcb2fbbe.png'), ('wil', 0, 'https://cdn.discordapp.com/avatars/486910822535135242/6a1317f37661c0311cad8ba5b9ef2428.png'), ('losvalas', 0, 'https://cdn.discordapp.com/avatars/517726160621142029/2b723aca77222a735bf21a2584aaa674.png'), ('Wöödhutt', 0, 'https://cdn.discordapp.com/avatars/555351461932957697/59b779b4e167fd4f61bde3232d9807a7.png'), ('AMNNAH', 0, 'https://cdn.discordapp.com/avatars/496696611674652672/59d5eddf4c1f09e39d5abf323ef5872a.png'), ('willredding', 0, 'https://cdn.discordapp.com/avatars/342744317955407874/5e392b9d93732378d9a9bdb110f47d44.png')]#[(Client.users.get_user(id[0]).username, id[1], Client.users.get_user(id[0]).avatar_url) for id in db.leaderboard]
