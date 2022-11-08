SRC_URI += "file://bsp.cfg \
            file://ethernet.cfg \
	    file://0001-read-from-at24mac402-extended-memory.patch \
            "

FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
