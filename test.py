import asyncio
from kasa import SmartPlug

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import info as session_info
PLUG = None

async def plug_setup():
	global PLUG
	# the plug IP address
	PLUG = SmartPlug("192.168.0.26")
	await PLUG.update()
	
async def toggle_plug_state():
	if PLUG.is_on:
		print("now turning off")
		await(PLUG.turn_off())
	else:
		print("now turning on")
		await PLUG.turn_on()
	await PLUG.update()

async def get_btn_status():
	await PLUG.update()
	return PLUG.is_on
	
async def main():
	await plug_setup()
	while (1):
		clear()
		alias = PLUG.alias
		put_text(alias)
		btn_is_on = await get_btn_status()
		text = "Click to turn OFF" if btn_is_on else "Click to turn ON"
		await actions(buttons=[text])
		await toggle_plug_state()

if __name__ == '__main__':
    start_server(main, debug=True, port=8000)