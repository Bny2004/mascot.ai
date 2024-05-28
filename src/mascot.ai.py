import asyncio
import pyvts

from utils import tts_engine, yt_chat
from dotenv import load_dotenv

load_dotenv()


plugin_info = {
    "plugin_name": "mascot.ai",
    "developer": "Cheap Nightbot",
    # "plugin_icon": "",
    "authentication_token_path": "./src/.env"
}

async def main():

    vts = pyvts.vts(plugin_info=plugin_info)

    await vts.connect()
    await vts.request_authenticate_token()
    await vts.request_authenticate()

    response = await vts.request(vts.vts_request.requestHotKeyList())

    hotkey_list = []
    for hotkey in response["data"]["availableHotkeys"]:
        hotkey_list.append(hotkey["name"])

    send_hotkey_request = vts.vts_request.requestTriggerHotKey(hotkey_list[1])
    print("First Animation")
    await vts.request(send_hotkey_request)
    await vts.close()


if __name__ == "__main__":
    
    asyncio.run(main())
