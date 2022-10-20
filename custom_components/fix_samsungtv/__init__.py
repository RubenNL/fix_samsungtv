from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "fix_samsungtv"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    with open("/usr/src/homeassistant/homeassistant/components/samsungtv/media_player.py", "a") as myfile:
      myfile.write("\n    async def async_select_source(self, source: str) -> None:\n      await self._async_send_keys(source.split(','))\n")
    return True
