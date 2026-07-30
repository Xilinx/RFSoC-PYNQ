# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

PREBUILT_ROOTFS_DST := ${CURDIR}/pynq/sdbuild/prebuilt/pynq_rootfs.aarch64.tar.gz
PREBUILT_SDIST_DST := ${CURDIR}/pynq/sdbuild/prebuilt/pynq_sdist.tar.gz

BASE_OVERLAY_PATH := ${CURDIR}/boards/${BOARD}/base
# Boards without an in-repo base overlay build nothing here.
ifneq ($(wildcard $(BASE_OVERLAY_PATH)),)
BASE_OVERLAY := ${BASE_OVERLAY_PATH}/base.bit
else
BASE_OVERLAY :=
endif

# Minimal PS-only design for the boot BSP/SDT (custom-SDT boards only).
BSP_PATH := ${CURDIR}/boards/${BOARD}/bsp
ifneq ($(wildcard $(BSP_PATH)),)
BSP_XSA := ${BSP_PATH}/bsp.xsa
else
BSP_XSA :=
endif

VERSION := 4.0.0
IMAGE := ${BOARD}-${VERSION}.img

all: checkenv_rfsocpynq gitsubmodule ${PREBUILT_SDIST_DST} ${PREBUILT_ROOTFS_DST} checkenv_pynq ${BASE_OVERLAY} ${BSP_XSA} ${IMAGE}
	@echo ""
	@echo "  RFSoC-PYNQ completed building image: ${IMAGE}"
	@echo ""

gitsubmodule:
	git submodule update --init --recursive

checkenv_rfsocpynq:
ifeq ($(BOARD),)
	$(error Please set board variable BOARD when calling this Makefile)
endif

${PREBUILT_SDIST_DST}:
	wget https://download.amd.com/opendownload/pynq/pynq-4.0.0.tar.gz -O ${PREBUILT_SDIST_DST}

${PREBUILT_ROOTFS_DST}:
	wget https://download.amd.com/opendownload/pynq/noble.aarch64.4.0.0.tar.gz -O ${PREBUILT_ROOTFS_DST}

checkenv_pynq:
	${CURDIR}/pynq/sdbuild/scripts/check_env.sh

${BASE_OVERLAY}:
ifneq ($(wildcard $(BASE_OVERLAY_PATH)),)
	cd ${CURDIR}/boards/${BOARD}/base && make
endif

${BSP_XSA}:
ifneq ($(wildcard $(BSP_PATH)),)
	cd ${CURDIR}/boards/${BOARD}/bsp && make
endif

${IMAGE}:
	cd ${CURDIR}/pynq/sdbuild && make BOARDDIR=${CURDIR}/boards BOARDS=${BOARD}
	mv ${CURDIR}/pynq/sdbuild/output/${BOARD}*.img ${IMAGE}

pynqremote: ${BSP_XSA}
	cd ${CURDIR}/pynq/sdbuild && make pynqremote BOARDDIR=${CURDIR}/boards BOARDS=${BOARD}
	mv ${CURDIR}/pynq/sdbuild/output/${BOARD}*.img ${IMAGE}
