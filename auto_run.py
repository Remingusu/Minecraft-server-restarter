import os
import time

os.system('java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.18.2-40.1.80/unix_args.txt "$@"')

loop = True
while loop:
    time.sleep(2.5)
    file = open(os.path.abspath('logs/latest.log'))
    line = file.readlines()[-1]
    file.close()
    if line.find('Server shut down correctly, ending gracefully') == 79:
        print("Redémarrage du serveur")
        os.system('java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.18.2-40.1.80/unix_args.txt "$@"')
    else:
        loop = False
print("Arrêt complet du serveur")
