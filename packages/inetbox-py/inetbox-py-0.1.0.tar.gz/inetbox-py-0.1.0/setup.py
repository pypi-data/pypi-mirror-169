# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['inetbox']

package_data = \
{'': ['*']}

install_requires = \
['bitstruct>=8.15.1,<9.0.0', 'miqro>=1.1,<1.2', 'pyserial>=3.5,<4.0']

extras_require = \
{'truma_service': ['paho-mqtt>=1.6.1,<2.0.0']}

entry_points = \
{'console_scripts': ['truma_service = '
                     'inetbox:truma_service.run[truma_service]']}

setup_kwargs = {
    'name': 'inetbox-py',
    'version': '0.1.0',
    'description': '',
    'long_description': '# inetbox.py\n\nThis is a software implementation of a Truma iNet box, a device for controlling mobile heater and AC units by Truma and Alde.\n\nThis software is not provided, endorsed, supported, or sponsored by Truma or Alde. It may or may not be working with their products. Please read the [license](./LICENSE) file, in particular:\n\nIN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING\nWILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS\nTHE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY\nGENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE\nUSE OR INABILITY TO USE THE PROGRAM.\n\nThat said, it is working for me, and I hope it will work for you, too.\n\n## Hardware Requirements\n\nThis has been tested with a Truma Combi 4 and the CP Plus control panel (inet ready). I don\'t see why this wouldn\'t be working with the Combi 6 and E models as well.\n\nThe software runs on a Raspberry Pi, any newer model should do. This could also be ported to a Pi Pico Microcontroller, but I haven\'t done that yet.\n\nYou need a [LIN to UART Transceiver](https://amzn.to/3E1qITr) (Affiliate Link!) for connecting the Raspberry Pi to the LIN bus. On the transceiver module, the connections are as follows:\n\n * **LIN** connects to Pin 4 on an RJ12 connector (the one with the 6 pins) going into any port on the Truma Combi heating, or using a [splitter module](https://amzn.to/3dL4bzT) (Affiliate Link!) into the existing connection between Combi and the control panel. The cable for Pin 4 should be colored green.\n * **GND** (any of the two) connects to a ground connection - e.g. on the power supply.\n * **12V** connects to a 12V power supply that also powers the Combi and CP Plus.\n * **TX** connects to pin 15 on the Raspberry Pi.\n * **RX** connects to pin 14 on the Raspberry Pi (14/15 might be the other way round, not sure).\n\nThe other pins (**INH**, **SLP**, second **GND**) are not used.\n\n## Installation\n\n`pip3 install inetbox[truma_service]` is what you normally want to do.\n\n`pip3 install inetbox` installs just the library in case you want to develop your own code using it. \n\n## Usage\n\nIn the following, only the MQTT service will be explained. You need an MQTT broker running (e.g. [Mosquitto](https://mosquitto.org/)) for this to work and you should be familiar with basic MQTT concepts.\n\nTo run the service:\n```\ntruma_service\n```\n\nIf you want to enable debugging, you can set the environment variables `DEBUG_LIN=1`, `DEBUG_PROTOCOL=1`, and `DEBUG_APP=1`, to debug the LIN bus (byte level communication), the protocol layer (handing LIN bus specifics), and the application layer (handling the actual data), respectively.\n\nExample:\n\n`DEBUG_LIN=1 truma_service`\n\nIf you want to define a different MQTT broker or define a log level for the MQTT messages, create a file `/etc/miqro.yml` as described here: https://github.com/danielfett/miqro#configuration-file (note that there is no service-specific configuration for the truma service as of now).\n\n## Initializing\n\nThis script plays the role of the inet box. You might need to initialize CP Plus again to make the fake inet box known to the system. This is an easy step that can safely be repeated (no settings are lost): After starting the software, go to the settings menu on the CP Plus and select "PR SET". The display will show "Init..." and after a few seconds, the initialization will be completed.\n\n## MQTT Topics\n\nWhen started, the service will connect to the LIN bus and publish any status updates acquired from there. When you send a command to modify a setting (e.g., to turn on the heating), the service will send the command to the LIN bus and publish the new status once the setting has been confirmed.\n\n### MQTT topics for receiving status\n\n`service/truma/error` - some error messages are published here\n\n`service/truma/display_status/#` - frequent updates from CP Plus, similar to what is shown on the display. Note that not all values have been decoded yet.\n\n`service/truma/control_status/#` - less frequent updates, but includes values that can be modified. These are the values that would otherwise be available in the Truma inet app.\n\n### Changing settings\n\nIn general, publish a message to `service/truma/set/<setting>` with the value you want to set. After restarting the service, wait a minute or so until the first set of values has been published before changing settings.\n\nFor example:\n\n```bash\nmosquitto_pub -t \'service/truma/set/target_temp_water\' -m \'40\'\n```\nor\n\n```bash\nmosquitto_pub -t \'service/truma/set/target_temp_room\' -m \'10\'; mosquitto_pub -t \'service/truma/set/heating_mode\' -m \'eco\'\n```\n\nThere are some specifics for certain settings:\n\n * `target_temp_room` and `heating_mode` must both be enabled for the heating to work. It\'s best to set both together as in the example above.\n * `target_temp_room` can be set to 0 to turn off the heating, and 5-30 degrees otherwise.\n * `heating_mode` can be set to `off`, `eco` and `high` and defines the fan intensity for room heating.\n * `target_temp_water` must be set to one of `0` (off), `40` (equivalent to selecting \'eco\' on the display), `60` (\'high\'), or `200` (boost)\n * `energy_mix` can be one of `none`/`gas`/`electricity`/`mix`\n * `el_power_level` can be set to `0`/`900`/`1800` when electric heating or mix is enabled\n\n## Acknowledgements\n\nThis project is based on the work of the [WomoLIN project](https://github.com/muccc/WomoLIN), especially the initial protocol decoding and the inet box log files.\n',
    'author': 'Daniel Fett',
    'author_email': 'fett@danielfett.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
