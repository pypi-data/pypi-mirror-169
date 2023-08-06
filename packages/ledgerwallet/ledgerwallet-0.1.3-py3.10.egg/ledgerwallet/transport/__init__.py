from .ble import BleDevice
from .hid import HidDevice
from .tcp import TcpDevice

DEVICE_CLASSES = [TcpDevice, HidDevice, BleDevice]


def enumerate_devices():
    devices = []
    for cls in DEVICE_CLASSES:
        devices.extend(cls.enumerate_devices())
    return devices
