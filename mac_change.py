import subprocess
try:
    subprocess.run(["ifconfig","-s"])
    my_interface=input("Enter interface name : \n")
    my_new_mac=input("Enter new mac address : \n")
    print("Interface DOWN ...\n")
    subprocess.run(["ifconfig",my_interface,"down"])
    print("Changing mac ...\n")
    subprocess.run(["ifconfig",my_interface,"hw","ether" ,my_new_mac])
    print("Interface UP ...\n")
    subprocess.run(["ifconfig",my_interface,"up"])
except:
    print ("We have error ... ! ")
