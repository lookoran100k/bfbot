import os
import sys
from dotenv import load_dotenv
# Load your environment variables
load_dotenv('keys3.env')  # ovo cu ti dati 
sys.path.append('../../../')
from bfxapi import Client
from bfxapi.constants import WS_HOST, REST_HOST

API_KEY=os.getenv("BFX_KEY")
API_SECRET=os.getenv("BFX_SECRET")

# Checking wallet balances requires private hosts
bfx = Client(
  API_KEY=API_KEY,
  API_SECRET=API_SECRET,
  logLevel='INFO',
  ws_host=WS_HOST,
  rest_host=REST_HOST,
  #channel_filter=['wallet']  #Ako ovo otkomentiram onda dobijam samo wallet update. 
  
)
#ovo sve skupa ispod je nepotrebno , ali ako komentiram Chanel Filter onda dobijam 
# wallet snapshot sa ovim ispod na jedan ili drugi nacin. zapravo ne znam. brljam
""" 
#prvi nacin
@bfx.ws.on('wallet_snapshot')
def log_snapshot(wallets):
  for wallet in wallets:
    print (wallet)  """

#drugi nacin  
  # or bfx.ws.wallets.get_wallets()   - ovo radi isto ko ovo gore
# bfx.ws.wallets.get_wallets()


@bfx.ws.on('error')
def log_error(msg):
  print ("Error: {}".format(msg))

bfx.ws.run()
