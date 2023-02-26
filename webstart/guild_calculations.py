def check_permissions(guild):
    return (int(guild.permissions) & 0x20) == 0x20