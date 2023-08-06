import asyncio
import logging
import getpass

from pytrutankless.api import TruTanklessApiInterface


async def main():
    email = "your@email.here"
    password = "yourSECRETpa$$word"
    # email = input("Enter your email: ").strip()
    # password = getpass.getpass(prompt="Enter your password: ")
    this_api = TruTanklessApiInterface(user=email, passwd=password)
    # this_api = TruTanklessApiInterface(token="253d0929210eede18505dfd731d15f777b0fb6aa")
    this_token = await this_api.authenticate()
    # print(api)
    await this_api.get_devices()
    await this_api.refresh_device("1061")
    # print(f"All Locations: {api._locations}")
    # print(f"Get Devices: {api._devices}")

    # await api.get_devices()

    # test_device = Device(api.devices)

    # for dev_id in api.devices.keys():
    #     await api.refresh_device(dev_id)
    #     dev_obj = api.devices[dev_id]
    #     print(dev_obj.get("serial_number"))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
