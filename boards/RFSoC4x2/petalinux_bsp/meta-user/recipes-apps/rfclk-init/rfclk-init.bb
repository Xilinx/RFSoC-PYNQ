SUMMARY = "RFSoC4x2 LMK clock select/reset at boot"
DESCRIPTION = "Sets the RFSoC4x2 LMK clk_sel lines and pulses the LMK reset via \
sysfs GPIO before the PYNQ.remote server starts. Replaces the classic on-board \
boot.py GPIO step, which the minimal PYNQ.remote image does not run."
SECTION = "PETALINUX/apps"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://rfclk-init.sh \
           file://rfclk-init.service"

S = "${WORKDIR}"

inherit systemd

SYSTEMD_AUTO_ENABLE = "enable"
SYSTEMD_SERVICE:${PN} = "rfclk-init.service"

do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${WORKDIR}/rfclk-init.sh ${D}${bindir}/rfclk-init.sh

    install -d ${D}${systemd_system_unitdir}
    install -m 0644 ${WORKDIR}/rfclk-init.service ${D}${systemd_system_unitdir}/rfclk-init.service
}

FILES:${PN} += "${bindir}/rfclk-init.sh ${systemd_system_unitdir}/rfclk-init.service"
