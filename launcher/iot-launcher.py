#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import subprocess
import os
import shutil
import random
import signal
import time

spawns=[] #list of subprocesses spawned 

def usage():
    print( "iot-launcher.py <clients_configuration_file> <server_ip> <server_sensor_port> <server_client_port> <sim_time> <num_of_sensors> <num_of_clients> <all_reliable>")

def signal_handler(signal, frame):
  print( 'Shutting down Launcher...')
  #probably need to close all the forked subprocesses?
  sys.exit(0)

def main(argv):
  ipaddr="localhost"
  port="5000"
  client_port="5001"
  client_config="../iot/conf/test.conf"
  sim_time=10 #seconds
  N=4 #or >4 (number of sensors)
  M=1 # number of clients
  all_reliable = "-a"
  
  if(len(argv)>=1):
     client_config=argv[0]
     if(len(argv)>=3):
       ipaddr=argv[1]
       port=argv[2]
       if(len(argv)>=4):
         client_port=argv[3]
         if(len(argv)>=5):
           sim_time=int(argv[4])
           if(len(argv)>=6):
             N=int(argv[5])
             if(len(argv)>=7):
               M=int(argv[6])
               if(len(argv)==8):
                 all_reliable="-A"
  if len(argv)!=0:
    if (argv[0] == "-h" or argv[0]=="--help"):
      usage()
      sys.exit(0)
  else:
    print( "using Launcher defaults =>")

  print( "ip",ipaddr,"and port:",port)
  print( "sim_time",sim_time)
  print( "number of sensors",N)
  print( "number of clients",M)
  print( "clients configuration file",client_config)
  
  start_time = round(time.time(), 3)
  #[STEP0]:
  #creating sensor.list
  sensorFile = open('./sensor.list', 'wb')

  sensors=["device", "temp", "gps", "camera"]
  
  print( range(N))
  for i in range(N): 
    #choose randomly a sensor from the list
    if (N>4):
      sensor_type=random.choice(sensors)
      sid=str(random.randint(10000,99999))
    else:
      sensor_type=sensors[i]
      sid=str(i)
    
    sensorFile.write(str(sensor_type+"_"+sid+"\n").encode('utf-8'))

  #[STEP1]: starting IoT Server to handle input from sensors
  # NOTE: depending on your coding language the values in the list will change
  # Also implement SIGINT (Ctrl+C), so that we can kill them. 
  FNULL = open(os.devnull, 'w')
  spawns.append(subprocess.Popen(["../iot/application/iotserver", "-i"+ipaddr, "-p"+port, "-s"+client_port,
    "-l./sensor.list","-c"+client_config],shell=False,stdout=FNULL))
  #spawns.append(subprocess.Popen(["python","iot-server.py", ipaddr, port],stdout=False,shell=False))

  #[STEP2]: starting sensors
  sensorFile.close
  sensorFile = open('./sensor.list', 'r')
  for i in range(N): 
    sensor_type, sid = sensorFile.readline().strip().split('_')
    print( "starting",(sensor_type+sid),"...")
    #forking a subprocess 
    spawns.append(subprocess.Popen(["python3","sensor.py", sensor_type, ipaddr, port, sid],stdout=False,shell=False))
    #print( spawns[i].pid
    #spawns[i].wait()
  
  #close sensor.list file
  sensorFile.close
  
  #[STEP3]: start your clients here
  #NOTE: depending on your coding language the values in the list will change
  #Also implement SIGINT (Ctrl+C), so that we can kill them. 
  for i in range(M): # where M is the number of clients.
    spawns.append(subprocess.Popen(["../iot/application/iotclient","-l../iot/application/client"+str(i+1)+"_sensor_log","-s"+ipaddr,"-p"+client_port, all_reliable],stdout=FNULL,shell=False))
  time.sleep(sim_time)
  print( "killing processes after", (time.time()-start_time))
  for s in spawns:
    #print( s.pid
    os.kill(s.pid, signal.SIGINT)

if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)
  main(sys.argv[1:])
