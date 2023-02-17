# python -c "import examples.rest.get_candles_hist"

from bfxapi.client import Client, REST_HOST

bfx = Client(
    REST_HOST=REST_HOST
)

print(f"Candles: {bfx.rest.public.get_candles_hist(symbol='tBTCUSD')}")

# Be sure to specify a period or aggregated period when retrieving funding candles.
# If you wish to mimic the candles found in the UI, use the following setup to aggregate all funding candles: a30:p2:p30
print(f"Candles: {bfx.rest.public.get_candles_hist(tf='15m', symbol='fUSD:a30:p2:p30')}")