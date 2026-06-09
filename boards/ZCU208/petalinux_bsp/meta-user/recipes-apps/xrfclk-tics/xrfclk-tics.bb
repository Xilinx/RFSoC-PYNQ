SUMMARY = "On-target xrfclk TICS register files (ZCU208)"
DESCRIPTION = "Installs this board's LMK/LMX TICS register files into /usr/share/xrfclk \
so the PYNQ.remote xrfclk server can program clocks from on-target files when the host \
provides no local file for the requested frequency."
SECTION = "PETALINUX/apps"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://LMK04828_245.76.txt \
           file://LMK04828_500.0.txt \
           file://LMX2594_491.52.txt \
           file://LMX2594_4000.0.txt"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${datadir}/xrfclk
    install -m 0644 ${WORKDIR}/*.txt ${D}${datadir}/xrfclk/
}

FILES:${PN} += "${datadir}/xrfclk"
