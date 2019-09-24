'''
Install VLC Media Player on your device
Make sure that you are connected to the same wifi network
Install VLC on your display device
Use Network Stream option to get view
type http://yourPiIPaddress:8160
'''
import time
import os
os.system("raspivid -o - -t 0 -hf -w 800 -h 400 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http, mux=ts, dst=:8160}' :demux=h264")

