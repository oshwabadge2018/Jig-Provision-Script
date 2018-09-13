# Jig-Provision-Script

## Setup
The Pi needs to have internet access.
* Remove SD Card, insert it into a computer
* Create a file names ` ` in the BOOT partition
* Paste the following into it and edit with correct wifi info.
"""country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
	ssid="MyWiFiNetwork"
	psk="aVeryStrongPassword"
	key_mgmt=WPA-PSK
}
"""
