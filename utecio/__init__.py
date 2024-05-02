import logging
from dataclasses import dataclass, asdict

logger = logging.getLogger("utecio")

logger.setLevel(logging.ERROR)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
if not logger.hasHandlers():
    logger.addHandler(ch)


@dataclass
class DeviceDefinition:
    model = ""
    lock: bool = False
    door: bool = False
    keypad: bool = False
    fingprinter: bool = False
    doublefp: bool = False
    bluetooth: bool = False
    rfid: bool = False
    rfid_once: bool = False
    rfid_twice: bool = False
    autobolt: bool = False
    autolock: bool = False
    autounlock: bool = False
    direction: bool = False
    update_ota: bool = False
    update_oad: bool = False
    update_wifi: bool = False
    alerts: bool = False
    mutemode: bool = False
    passage: bool = False
    lockout: bool = False
    manual: bool = False
    shakeopen: bool = False
    moreadmin: bool = False
    morepwd: bool = False
    timelimit: bool = False
    morelanguage: bool = False
    needregristerpwd: bool = False
    locklocal: bool = False
    havesn: bool = False
    clone: bool = False
    customuserid: bool = False
    bt264: bool = False
    keepalive: bool = False
    passageautolock: bool = False
    doorsensor: bool = False
    zwave: bool = False
    needreadmodel: bool = False
    needsycbuser: bool = False
    bt_close: bool = False
    singlelatchboltmortic: bool = False
    smartphone_nfc: bool = False
    update_2642: bool = False
    isautodirection: bool = False
    ishomekit: bool = False
    isyeeuu: bool = False
    secondsarray = []
    mtimearray = []
    adduserremovenum = 4

    def as_dict(self):
        return asdict(self)

class DeviceLockLatch5Finger(DeviceDefinition):
    model = "Latch-5-F"

    def __init__(self) -> None:
        super().__init__()

        self.bluetooth = True
        self.autolock = True
        self.update_wifi = True
        self.alerts = True
        self.mutemode = True
        self.doublefp = True
        self.keypad = True
        self.fingprinter = True
        self.needregristerpwd = True
        self.havesn = True
        self.moreadmin = True
        self.timelimit = True
        self.passage = True
        self.lockout = True
        self.bt264 = True
        self.keepalive = True
        self.passageautolock = True
        self.singlelatchboltmortic = True
        self.smartphone_nfc = True
        self.bt_close = True


class DeviceLockLatch5NFC(DeviceDefinition):
    model = "Latch-5-NFC"

    def __init__(self) -> None:
        super().__init__()

        self.bluetooth = True
        self.autolock = True
        self.update_wifi = True
        self.alerts = True
        self.mutemode = True
        self.rfid = True
        self.rfid_twice = True
        self.keypad = True
        self.needregristerpwd = True
        self.havesn = True
        self.moreadmin = True
        self.timelimit = True
        self.passage = True
        self.lockout = True
        self.bt264 = True
        self.keepalive = True
        self.passageautolock = True
        self.singlelatchboltmortic = True
        self.smartphone_nfc = True
        self.bt_close = True


class DeviceLockUL1(DeviceDefinition):
    model = "UL1-BT"

    def __init__(self) -> None:
        super().__init__()

        self.bluetooth = True
        self.rfid = True
        self.rfid_twice = True
        self.fingprinter = True
        self.autobolt = True
        self.update_ota = True
        self.update_oad = True
        self.alerts = True
        self.shakeopen = True
        self.mutemode = True
        self.passage = True
        self.lockout = True
        self.havesn = True
        self.direction = True
        self.keepalive = True
        self.singlelatchboltmortic = True


class DeviceLockBoltNFC(DeviceDefinition):
    model = "Bolt-NFC"

    def __init__(self) -> None:
        super().__init__()

        self.lock = True
        self.bluetooth = True
        self.autolock = True
        self.update_ota = True
        self.update_wifi = True
        self.direction = True
        self.alerts = True
        self.mutemode = True
        self.manual = True
        self.shakeopen = True
        self.havesn = True
        self.rfid = True
        self.keypad = True
        self.needregristerpwd = True
        self.timelimit = True
        self.moreadmin = True
        self.lockout = True
        self.bt264 = True
        self.doorsensor = True
        self.keepalive = True
        self.autounlock = True
        self.smartphone_nfc = True
        self.update_2642 = True
        self.isautodirection = True
        self.ishomekitmeKit = True


class DeviceLockLever(DeviceDefinition):
    model = "LEVER"

    def __init__(self) -> None:
        super().__init__()
        self.bluetooth = True
        self.autolock = True
        self.update_ota = True
        self.alerts = True
        self.mutemode = True
        self.shakeopen = True
        self.fingprinter = True
        self.keypad = True
        self.doublefp = True
        self.needregristerpwd = True
        self.havesn = True
        self.moreadmin = True
        self.timelimit = True
        self.passage = True
        self.lockout = True
        self.bt264 = True
        self.keepalive = True
        self.passageautolock = True
        self.singlelatchboltmortic = True


class DeviceLockUBolt(DeviceDefinition):
    model = "U-Bolt"

    def __init__(self) -> None:
        super().__init__()
        self.lock = True
        self.bluetooth = True
        self.autolock = True
        self.autounlock = True
        self.update_ota = True
        self.direction = True
        self.alerts = True
        self.mutemode = True
        self.manual = True
        self.shakeopen = True
        self.havesn = True
        self.moreadmin = True
        self.needreadmodel = True
        self.keypad = True
        self.lockout = True
        self.timelimit = True
        self.needregristerpwd = True
        self.bt264 = True
        self.keepalive = True


class DeviceLockUboltWiFi(DeviceDefinition):
    model = "U-Bolt-WiFi"

    def __init__(self) -> None:
        super().__init__()
        self.lock = True
        self.bluetooth = True
        self.autolock = True
        self.update_ota = True
        self.update_wifi = True
        self.direction = True
        self.alerts = True
        self.mutemode = True
        self.manual = True
        self.shakeopen = True
        self.havesn = True
        self.needreadmodel = True
        self.keypad = True
        self.needregristerpwd = True
        self.timelimit = True
        self.moreadmin = True
        self.lockout = True
        self.bt264 = True
        self.doorsensor = True
        self.keepalive = True
        self.autounlock = True


class DeviceLockUboltProWifi(DeviceDefinition):
    model = "U-Bolt-Pro-WiFi"

    def __init__(self) -> None:
        super().__init__()
        self.lock = True
        self.bluetooth = True
        self.autolock = True
        self.update_ota = True
        self.update_wifi = True
        self.direction = True
        self.alerts = True
        self.mutemode = True
        self.manual = True
        self.shakeopen = True
        self.havesn = True
        self.needreadmodel = True
        self.keypad = True
        self.needregristerpwd = True
        self.timelimit = True
        self.moreadmin = True
        self.lockout = True
        self.bt264 = False
        self.doorsensor = True
        self.keepalive = True
        self.autounlock = True


class DeviceLockUBoltZwave(DeviceDefinition):
    model = "U-Bolt-ZWave"

    def __init__(self) -> None:
        super().__init__()
        self.lock = True
        self.bluetooth = True
        self.autolock = True
        self.update_ota = True
        self.direction = True
        self.alerts = True
        self.mutemode = True
        self.manual = True
        self.shakeopen = True
        self.havesn = True
        self.needreadmodel = True
        self.keypad = True
        self.needregristerpwd = True
        self.timelimit = True
        self.moreadmin = True
        self.lockout = True
        self.bt264 = True
        self.doorsensor = True
        self.keepalive = True
        self.autounlocklock = True
        self.zwave = True


class DeviceLockUL3(DeviceDefinition):
    model = "SmartLockByBle"

    def __init__(self) -> None:
        super().__init__()
        self.bluetooth = True
        self.keypad = True
        self.fingprinter = True
        self.shakeopen = True
        self.morepwd = True
        self.passage = True
        self.lockout = True
        self.locklocal = True
        self.needsycbuser = True
        self.clone = True
        self.customuserid = True
        self.singlelatchboltmortic = True
        self.keepalive = True


class DeviceLockUL32ND(DeviceDefinition):
    model = "UL3-2ND"

    def __init__(self) -> None:
        super().__init__()
        self.bluetooth = True
        self.autolock = True
        self.update_ota = True
        self.alerts = True
        self.mutemode = True
        self.shakeopen = True
        self.fingprinter = True
        self.keypad = True
        self.doublefp = True
        self.needregristerpwd = True
        self.havesn = True
        self.locklocal = True
        self.needsycbuser = True
        self.moreadmin = True
        self.customuserid = True
        self.timelimit = True
        self.passage = True
        self.lockout = True
        self.bt264 = True
        self.keepalive = True
        self.passageautolock = True
        self.singlelatchboltmortic = True


class DeviceLockUL300(DeviceDefinition):
    model = "UL300"

    def __init__(self) -> None:
        super().__init__()
        self.bluetooth = True
        self.rfid = True
        self.rfid_once = True
        self.keypad = True
        self.fingprinter = True
        self.update_ota = True
        self.update_oad = True
        self.alerts = True
        self.shakeopen = True
        self.mutemode = True
        self.moreadmin = True
        self.timelimit = True
        self.passage = True
        self.lockout = True
        self.morelanguage = True
        self.locklocal = True
        self.needsycbuser = True
        self.havesn = True
        self.keepalive = True
        self.singlelatchboltmortic = True
        self.adduserremovenum = 5


class GenericLock(DeviceDefinition):
    def __init__(self) -> None:
        super().__init__()

        self.bluetooth = False
        self.autolock = True
        self.mutemode = True
        self.havesn = True
        self.timelimit = True
        self.passage = True
        self.lockout = True
        self.bt264 = True
        self.keepalive = True
        self.bt_close = True


known_devices: dict[str, DeviceDefinition] = {
    DeviceLockLatch5Finger.model: DeviceLockLatch5Finger(),
    DeviceLockLatch5NFC.model: DeviceLockLatch5NFC(),
    DeviceLockUL1.model: DeviceLockUL1(),
    DeviceLockBoltNFC.model: DeviceLockBoltNFC(),
    DeviceLockLever.model: DeviceLockLever(),
    DeviceLockUBolt.model: DeviceLockUBolt(),
    DeviceLockUboltWiFi.model: DeviceLockUboltWiFi(),
    DeviceLockUboltProWifi.model: DeviceLockUboltProWifi(),
    DeviceLockUBoltZwave.model: DeviceLockUBoltZwave(),
    DeviceLockUL3.model: DeviceLockUL3(),
    DeviceLockUL300.model: DeviceLockUL300(),
}
