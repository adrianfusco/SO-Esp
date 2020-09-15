#!/usr/bin/python3

# Thanks to this S.O question: https://es.stackoverflow.com/questions/363681/como-acceder-a-unidad-compartida-pide-user-y-pass-desde-linux-con-python/363847

# With help of this smb docker: https://hub.docker.com/r/sixeyed/samba/

###### Add users ######
# adduser usuarioprueba
# smbpasswd -a usuarioprueba

###### SMB CONFIG #####
# [music]
#    path = /mnt/audio/music
#    browsable = yes
#    read only = no
#    guest ok = yes
#    valid users = usuarioprueba


from smb.SMBConnection import SMBConnection

usuario = 'usuarioprueba'
password = 'abc123.'
server = 'localhost'

conexion = SMBConnection(usuario, password, server, server)
conexion.connect(server)

shares = conexion.listShares()

for share in shares:
    if not share.isSpecial and share.name not in ['NETLOGON', 'SYSVOL']:
        sharedfiles = conexion.listPath(share.name, '/')
        for sharedfile in sharedfiles:
            print(sharedfile)

# Result:

#   fichero_ejemplo_1
#   fichero_ejemplo_3
#   fichero_ejemplo_2