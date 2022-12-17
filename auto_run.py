import os
import time

os.system('{command}')

loop = True
while loop:
    time.sleep(2.5)
    with open(os.path.abspath('logs/latest.log'), 'r') as file:
        line = file.readlines()[-1]
    if line.find('Server shut down correctly, ending gracefully') == 79:
        print("Restarting the server")
        os.system('{command}')
print("Arrêt complet du serveur")
