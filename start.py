import os
import sys
import signal
sys.path.append('../../../')
from dotenv import load_dotenv

# Load your environment variables
load_dotenv('keys3.env')

from bfxapi import Client
from bfxapi.constants import WS_HOST, REST_HOST

API_KEY=os.getenv("BFX_KEY")
API_SECRET=os.getenv("BFX_SECRET")

bfx = Client(
  API_KEY=API_KEY,
  API_SECRET=API_SECRET,
  logLevel='INFO',
  ws_host=WS_HOST,
  rest_host=REST_HOST,
  #dead_man_switch=False, # <-- kill all orders if this connection drops
  channel_filter=['wallet','order','position'] # <-- only receive wallet updates
)

def exit_program(signal, frame):
    print("Exiting the program gracefully...")
    bfx.ws.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_program)

@bfx.ws.on('error')
def log_error(msg):
  print ("Error: {}".format(msg))

@bfx.ws.on('authenticated')
async def Acount(auth_message):
  print ("Authenticated!!")


bfx.ws.run()