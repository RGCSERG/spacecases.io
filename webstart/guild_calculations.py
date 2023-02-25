def check_permissions(guild):
    print(guild.members)
    if guild.permissions == str(4398046511103) or guild.owner == True:
        return True