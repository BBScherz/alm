import argparse
import math
import os
from time import sleep
import csv

from pythonosc import dispatcher
from pythonosc import osc_server

# muse-io --device 00:06:66:65:92:94 --osc osc.udp://localhost:5000

#theta = []
#alpha = []
#beta  = []
#gamma = []
#theta.append([])
#alpha.append([])
#beta.append([])

count = 0

def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4):

#    os.system('clear')
#    print("EEG (uV) per channel: ", unused_addr, args, ch1, ch2, ch3, ch4)

    average = (ch1 + ch2 + ch3 + ch4) / 4
#    print("Average: ", average)
#    count = count + 1
#    if count % 1000 == 0:
    if average < 800.0:
        print("feeling calm.")
    else:
        print("STRESSED!!!")


def acc_handler(unused_addr, args, ch1, ch2, ch3):
    print("Accelerometer Data per channel:", ch1, ch2, ch3)


def gamma_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    
    print("GAMMA per channel: ", unused_addr, args, ch1, ch2, ch3, ch4)


def beta_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    print("BETA per channel:    ", unused_addr, args, ch1, ch2, ch3, ch4)

def alpha_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    print("ALPHA per channel: ", unused_addr, args, ch1, ch2, ch3, ch4)


def theta_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    print("THETA per channel: ", unused_addr, args, ch1, ch2, ch3, ch4)


if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
#    dispatcher.map("/debug", print)
    dispatcher.map("/muse/eeg", eeg_handler, "EEG")
#    dispatcher.map("/muse/acc", acc_handler, "ACC")

#    dispatcher.map("/muse/elements/gamma_absolute", gamma_handler, "GAMMA")
#    dispatcher.map("/muse/elements/beta_absolute",  beta_handler,  "BETA" )
#    dispatcher.map("/muse/elements/alpha_absolute", alpha_handler, "ALPHA")
#    dispatcher.map("/muse/elements/theta_absolute", theta_handler, "THETA")

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()

#    with open('brainwaves.csv',newline='')as File:
#        reader = csv.reader(File)
#        for row in reader:
#            print(row)
