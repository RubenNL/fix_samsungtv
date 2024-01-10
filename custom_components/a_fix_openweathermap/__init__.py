from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
import subprocess
import os
import logging
_LOGGER = logging.getLogger(__name__)

DOMAIN = "a_fix_openweathermap"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    currentpath = os.path.dirname(__file__)
    _LOGGER.debug(currentpath)
    diff_file = os.path.join(currentpath, "diff")
    _LOGGER.debug(diff_file)
    p = subprocess.Popen(["git","apply",diff_file], cwd="/usr/src/homeassistant/homeassistant/components", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    stderr=p.stderr.read().decode()
    stdout=p.stdout.read().decode()
    exitcode=p.returncode
    _LOGGER.debug("stderr: "+stderr)
    _LOGGER.debug("stdout: "+stdout)
    _LOGGER.debug("exit code:"+str(exitcode))
    return True