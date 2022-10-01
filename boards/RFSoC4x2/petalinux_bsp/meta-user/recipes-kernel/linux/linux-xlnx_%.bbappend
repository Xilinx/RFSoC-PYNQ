SRC_URI += " file://i2c.cfg"

FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI:append = " \
		file://0001-power-supply-irps-Add-support-for-irps-supply.patch \
		file://0002-i2c-cadence-Implement-timeout.patch \
		file://0003-drivers-misc-add-support-for-DDR-memory-management.patch \
"
