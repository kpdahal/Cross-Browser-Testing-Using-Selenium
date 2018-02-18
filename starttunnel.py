
import os

#start local tunnel to active local connection to crossbrowser testing site
def start_cbt_tunnel():
    try:
        os.system('cbt_tunnels --username <<user_name>> --authkey <<password>>')
        print("Local tunnel opened sucessfully.")
    except Exception as e:
        print("An error occured during tunnel setup.",format(e))