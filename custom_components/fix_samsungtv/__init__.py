from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
import subprocess

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "fix_samsungtv"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    subprocess.call("/config/fix_samsungtv.sh")
    return True
