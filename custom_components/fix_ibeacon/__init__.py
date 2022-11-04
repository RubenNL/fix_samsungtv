from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "fix_ibeacon"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    with open("/usr/src/homeassistant/homeassistant/components/ibeacon/device_tracker.py", "a") as myfile:
      myfile.write('\n    @property\n    def state(self) -> str:\n        """Return the state of the device."""\n        return self._ibeacon_advertisement.source if self._active else STATE_NOT_HOME\n')
    with open("/usr/src/homeassistant/homeassistant/components/ibeacon/const.py", "a") as myfile:
      myfile.write('\nUNAVAILABLE_TIMEOUT = 30\nUPDATE_INTERVAL = timedelta(seconds=10)\n')
    with open("/usr/src/homeassistant/homeassistant/components/bluetooth/const.py", "a") as myfile:
      myfile.write('\nUNAVAILABLE_TRACK_SECONDS: Final = 60\n')
    return True
