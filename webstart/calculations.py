def permissions(guild):
    return (int(guild.permissions) & 0x20) == 0x20

def iscasesin(guild):
    return True # until next line is fixed
    # return 'botname' in guild.members
