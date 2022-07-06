ROOT_PATH := $(abspath $(dir $(firstword $(MAKEFILE_LIST))))

PREBUILT_IMAGE := ${ROOT_PATH}/aarch64_prebuilt_image.tar.gz
PREBUILT_SDIST := ${ROOT_PATH}/pynq_2_7.tar.gz
BSP_PATH := ${ROOT_PATH}/board/RFSoC4x2/RFSoC4x2.bsp
BOARD_FILES := ${ROOT_PATH}/board/RFSoC4x2/board_files

all: base image
	echo ${ROOT_PATH}

image: gitsubmodule ${BSP_PATH} ${PREBUILT_SDIST} ${PREBUILT_IMAGE}
	cd ${ROOT_PATH}/PYNQ/sdbuild/ && make BOARDDIR=${ROOT_PATH}/board/ BOARDS=RFSoC4x2 PYNQ_SDIST=${PREBUILT_SDIST} PREBUILT=${PREBUILT_IMAGE}

base: ${BOARD_FILES} ${ROOT_PATH}/board/RFSoC4x2/base/base.bit
	
${ROOT_PATH}/board/RFSoC4x2/base/base.bit:
	cd ${ROOT_PATH}/board/RFSoC4x2/base && make

gitsubmodule:
	git submodule init && git submodule update

${BSP_PATH}:
	wget "https://github.com/RealDigitalOrg/RFSoC4x2-BSP/blob/master/bsp_releases/RFSoC4x2_2020_2.bsp?raw=true" -O ${BSP_PATH}

${BOARD_FILES}:
	cd ${ROOT_PATH}/board/RFSoC4x2/ && \
	wget "https://www.realdigital.org/downloads/9d2af32116d5420d25da904f6a06bb1f.zip" -O bf.zip && \
	unzip bf.zip -d board_files && rm bf.zip

${PREBUILT_IMAGE}:
	wget https://bit.ly/pynq_aarch64_2_7 -O ${PREBUILT_IMAGE}

${PREBUILT_SDIST}:
	wget https://github.com/Xilinx/PYNQ/releases/download/v2.7.0/pynq-2.7.0.tar.gz -O ${PREBUILT_SDIST}

