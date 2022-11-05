from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "fix_ibeacon"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    with open("/usr/src/homeassistant/homeassistant/components/ibeacon/device_tracker.py", "a") as myfile:
      myfile.write('\n    @property\n    def state(self) -> str:\n        """Return the state of the device."""\n        return self._ibeacon_advertisement.source if self._active else STATE_NOT_HOME\n')
    with open("/usr/src/homeassistant/homeassistant/components/ibeacon/const.py", "a") as myfile:
      myfile.write('\nUNAVAILABLE_TIMEOUT = 30\nUPDATE_INTERVAL = timedelta(seconds=10)\nMIN_SEEN_TRANSIENT_NEW=2 #2 because it initializes with 1, and 1 more. TODO: just make this 1, and change the other code.\n')
    with open("/usr/src/homeassistant/homeassistant/components/bluetooth/const.py", "a") as myfile:
      myfile.write('\nUNAVAILABLE_TRACK_SECONDS: Final = 60\n')
    return True


#TODO; this line is also interesting for multi-room detection: https://github.com/home-assistant/core/blob/0311063c4417e70b566eef8e4156c362fec1a199/homeassistant/components/ibeacon/coordinator.py#L87
