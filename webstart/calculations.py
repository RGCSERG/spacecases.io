def permissions(guild):
    return (int(guild.permissions) & 0x20) == 0x20

def iscasesin(guild):
    return True if 'botname' in guild.members else False