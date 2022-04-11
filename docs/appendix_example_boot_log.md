# Example boot log

```
Xilinx Zynq MP First Stage Boot Loader
Release 2020.1   Jan  5 2021  -  13:57:20
SYZYGY - Voltage Handshake START
No pods are present
PMIC3: VIO setting not changed
?ê
  UjT'$HPª£ running on XCZU5EG/EV/silicon v4/RTL5.1 at 0xfffea000
NOTICE:  BL31: v2.2(release):xilinx_rebase_v2.2_2020.1
NOTICE:  BL31: Built : 13:59:23, Jan  5 2021


U-Boot 2020.01 (Jan 05 2021 - 13:55:09 +0000)

Model: TUL PYNQ-ZU RevB
Board: Xilinx ZynqMP
DRAM:  4 GiB
PMUFW:  v1.1
EL Level:       EL2
Chip ID:        zu5
NAND:  0 MiB
MMC:   mmc@ff160000: 0, mmc@ff170000: 1
In:    serial@ff000000
Out:   serial@ff000000
Err:   serial@ff000000
Bootmode: SD_MODE
Reset reason:   SOFT
Net:   No ethernet found.
Hit any key to stop autoboot:  0
switch to partitions #0, OK
mmc0 is current device
Scanning mmc 0:1...
Found U-Boot script /boot.scr
1636 bytes read in 12 ms (132.8 KiB/s)
## Executing script at 20000000
17471764 bytes read in 1163 ms (14.3 MiB/s)
## Loading kernel from FIT Image at 10000000 ...
   Using 'conf@1' configuration
   Trying 'kernel@0' kernel subimage
     Description:  Linux Kernel
     Type:         Kernel Image
     Compression:  uncompressed
     Data Start:   0x100000d4
     Data Size:    17428992 Bytes = 16.6 MiB
     Architecture: AArch64
     OS:           Linux
     Load Address: 0x00080000
     Entry Point:  0x00080000
     Hash algo:    sha1
     Hash value:   caea54708b8b69b44ac004f7e6f8c0725e688344
   Verifying Hash Integrity ... sha1+ OK
## Loading fdt from FIT Image at 10000000 ...
   Using 'conf@1' configuration
   Trying 'fdt@0' fdt subimage
     Description:  Flattened Device Tree blob
     Type:         Flat Device Tree
     Compression:  uncompressed
     Data Start:   0x1109f3cc
     Data Size:    40945 Bytes = 40 KiB
     Architecture: AArch64
     Hash algo:    sha1
     Hash value:   6ad0ddf680e7cd2d162315cb5f7f4e8518c0f538
   Verifying Hash Integrity ... sha1+ OK
   Booting using the fdt blob at 0x1109f3cc
   Loading Kernel Image
   Loading Device Tree to 000000000fff3000, end 000000000ffffff0 ... OK

Starting kernel ...

[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
[    0.000000] Linux version 5.4.0-xilinx-v2020.1 (oe-user@oe-host) (gcc version 9.2.0 (GCC)) #1 SMP Tue Jan 5 13:40:43 UTC 2021
[    0.000000] Machine model: TUL PYNQ-ZU RevB
[    0.000000] efi: Getting EFI parameters from FDT:
[    0.000000] efi: UEFI not found.
[    0.000000] Reserved memory: created CMA memory pool at 0x000000005fc00000, size 512 MiB
[    0.000000] OF: reserved mem: initialized node linux,cma, compatible id shared-dma-pool
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: PSCIv1.1 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: MIGRATE_INFO_TYPE not supported.
[    0.000000] psci: SMC Calling Convention v1.1
[    0.000000] percpu: Embedded 22 pages/cpu s50392 r8192 d31528 u90112
[    0.000000] Detected VIPT I-cache on CPU0
[    0.000000] CPU features: detected: ARM erratum 845719
[    0.000000] Speculative Store Bypass Disable mitigation not required
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1031940
[    0.000000] Kernel command line: root=/dev/mmcblk0p2 rw earlyprintk rootfstype=ext4 rootwait devtmpfs.mount=1 uio_pdrv_genirq.of_id="generic-uio" clk_ignore_unused
[    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] software IO TLB: mapped [mem 0x5bc00000-0x5fc00000] (64MB)
[    0.000000] Memory: 3505052K/4193280K available (11964K kernel code, 700K rwdata, 3568K rodata, 704K init, 533K bss, 163940K reserved, 524288K cma-reserved)
[    0.000000] rcu: Hierarchical RCU implementation.
[    0.000000] rcu:     RCU event tracing is enabled.
[    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] GIC: Adjusting CPU interface base to 0x00000000f902f000
[    0.000000] GIC: Using split EOI/Deactivate mode
[    0.000000] random: get_random_bytes called from start_kernel+0x2a8/0x3cc with crng_init=0
[    0.000000] arch_timer: cp15 timer(s) running at 100.00MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x171024e7e0, max_idle_ns: 440795205315 ns
[    0.000003] sched_clock: 56 bits at 100MHz, resolution 10ns, wraps every 4398046511100ns
[    0.000298] Console: colour dummy device 80x25
[    0.000509] printk: console [tty0] enabled
[    0.000531] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=400000)
[    0.000545] pid_max: default: 32768 minimum: 301
[    0.000690] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.000711] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.001645] ASID allocator initialised with 32768 entries
[    0.001706] rcu: Hierarchical SRCU implementation.
[    0.001852] EFI services will not be available.
[    0.001982] smp: Bringing up secondary CPUs ...
[    0.002314] Detected VIPT I-cache on CPU1
[    0.002347] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
[    0.002696] Detected VIPT I-cache on CPU2
[    0.002716] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
[    0.003043] Detected VIPT I-cache on CPU3
[    0.003062] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
[    0.003110] smp: Brought up 1 node, 4 CPUs
[    0.003151] SMP: Total of 4 processors activated.
[    0.003160] CPU features: detected: 32-bit EL0 Support
[    0.003169] CPU features: detected: CRC32 instructions
[    0.003205] CPU: All CPU(s) started at EL2
[    0.003222] alternatives: patching kernel code
[    0.004318] devtmpfs: initialized
[    0.008627] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.008646] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.020564] xor: measuring software checksum speed
[    0.060059]    8regs     :  2375.000 MB/sec
[    0.100089]    32regs    :  2725.000 MB/sec
[    0.140121]    arm64_neon:  2365.000 MB/sec
[    0.140129] xor: using function: 32regs (2725.000 MB/sec)
[    0.140143] pinctrl core: initialized pinctrl subsystem
[    0.140749] NET: Registered protocol family 16
[    0.141753] DMA: preallocated 256 KiB pool for atomic allocations
[    0.141778] audit: initializing netlink subsys (disabled)
[    0.141899] audit: type=2000 audit(0.140:1): state=initialized audit_enabled=0 res=1
[    0.142194] cpuidle: using governor menu
[    0.142384] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[    0.153808] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.153821] HugeTLB registered 32.0 MiB page size, pre-allocated 0 pages
[    0.153831] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.153841] HugeTLB registered 64.0 KiB page size, pre-allocated 0 pages
[    1.229036] DRBG: Continuing without Jitter RNG
[    1.304892] raid6: neonx8   gen()  1549 MB/s
[    1.372929] raid6: neonx8   xor()  1467 MB/s
[    1.440965] raid6: neonx4   gen()  1492 MB/s
[    1.509021] raid6: neonx4   xor()  1430 MB/s
[    1.577094] raid6: neonx2   gen()  1135 MB/s
[    1.645114] raid6: neonx2   xor()  1189 MB/s
[    1.713143] raid6: neonx1   gen()   739 MB/s
[    1.781207] raid6: neonx1   xor()   896 MB/s
[    1.849226] raid6: int64x8  gen()  1166 MB/s
[    1.917270] raid6: int64x8  xor()   763 MB/s
[    1.985377] raid6: int64x4  gen()   984 MB/s
[    2.053392] raid6: int64x4  xor()   740 MB/s
[    2.121454] raid6: int64x2  gen()   683 MB/s
[    2.189491] raid6: int64x2  xor()   600 MB/s
[    2.257593] raid6: int64x1  gen()   452 MB/s
[    2.325564] raid6: int64x1  xor()   460 MB/s
[    2.325572] raid6: using algorithm neonx8 gen() 1549 MB/s
[    2.325580] raid6: .... xor() 1467 MB/s, rmw enabled
[    2.325588] raid6: using neon recovery algorithm
[    2.326109] iommu: Default domain type: Translated
[    2.326361] SCSI subsystem initialized
[    2.326502] usbcore: registered new interface driver usbfs
[    2.326533] usbcore: registered new interface driver hub
[    2.326565] usbcore: registered new device driver usb
[    2.326614] mc: Linux media interface: v0.10
[    2.326639] videodev: Linux video capture interface: v2.00
[    2.326661] pps_core: LinuxPPS API ver. 1 registered
[    2.326669] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    2.326688] PTP clock support registered
[    2.326708] EDAC MC: Ver: 3.0.0
[    2.327053] zynqmp-ipi-mbox mailbox@ff990400: Registered ZynqMP IPI mbox with TX/RX channels.
[    2.327217] FPGA manager framework
[    2.327348] Advanced Linux Sound Architecture Driver Initialized.
[    2.327621] Bluetooth: Core ver 2.22
[    2.327645] NET: Registered protocol family 31
[    2.327653] Bluetooth: HCI device and connection manager initialized
[    2.327664] Bluetooth: HCI socket layer initialized
[    2.327674] Bluetooth: L2CAP socket layer initialized
[    2.327690] Bluetooth: SCO socket layer initialized
[    2.328057] clocksource: Switched to clocksource arch_sys_counter
[    2.328149] VFS: Disk quotas dquot_6.6.0
[    2.328196] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    2.332169] NET: Registered protocol family 2
[    2.332504] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
[    2.332557] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    2.332769] TCP bind hash table entries: 32768 (order: 7, 524288 bytes, linear)
[    2.333158] TCP: Hash tables configured (established 32768 bind 32768)
[    2.333226] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    2.333305] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    2.333466] NET: Registered protocol family 1
[    2.333723] RPC: Registered named UNIX socket transport module.
[    2.333733] RPC: Registered udp transport module.
[    2.333740] RPC: Registered tcp transport module.
[    2.333747] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    2.334376] hw perfevents: no interrupt-affinity property for /pmu, guessing.
[    2.334530] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
[    2.335282] Initialise system trusted keyrings
[    2.335368] workingset: timestamp_bits=46 max_order=20 bucket_order=0
[    2.336115] NFS: Registering the id_resolver key type
[    2.336134] Key type id_resolver registered
[    2.336142] Key type id_legacy registered
[    2.336154] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
[    2.336178] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
[    2.349427] NET: Registered protocol family 38
[    2.349438] Key type asymmetric registered
[    2.349446] Asymmetric key parser 'x509' registered
[    2.349470] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
[    2.349542] io scheduler mq-deadline registered
[    2.349551] io scheduler kyber registered
[    2.374730] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
[    2.377638] cacheinfo: Unable to detect cache hierarchy for CPU 0
[    2.381833] brd: module loaded
[    2.386112] loop: module loaded
[    2.386763] mtdoops: mtd device (mtddev=name/number) must be supplied
[    2.388130] libphy: Fixed MDIO Bus: probed
[    2.389087] tun: Universal TUN/TAP device driver, 1.6
[    2.389177] CAN device driver interface
[    2.390475] usbcore: registered new interface driver cdc_acm
[    2.390484] cdc_acm: USB Abstract Control Model driver for USB modems and ISDN adapters
[    2.390512] usbcore: registered new interface driver cdc_wdm
[    2.390546] usbcore: registered new interface driver usb-storage
[    2.390601] usbcore: registered new interface driver usbserial_generic
[    2.390625] usbserial: USB Serial support registered for generic
[    2.390651] usbcore: registered new interface driver usb_serial_simple
[    2.390673] usbserial: USB Serial support registered for carelink
[    2.390694] usbserial: USB Serial support registered for zio
[    2.390713] usbserial: USB Serial support registered for funsoft
[    2.390735] usbserial: USB Serial support registered for flashloader
[    2.390756] usbserial: USB Serial support registered for google
[    2.390776] usbserial: USB Serial support registered for libtransistor
[    2.390797] usbserial: USB Serial support registered for vivopay
[    2.390817] usbserial: USB Serial support registered for moto_modem
[    2.390837] usbserial: USB Serial support registered for motorola_tetra
[    2.390860] usbserial: USB Serial support registered for novatel_gps
[    2.390881] usbserial: USB Serial support registered for hp4x
[    2.390900] usbserial: USB Serial support registered for suunto
[    2.390921] usbserial: USB Serial support registered for siemens_mpi
[    2.391060] gadgetfs: USB Gadget filesystem, version 24 Aug 2004
[    2.391145] mousedev: PS/2 mouse device common for all mice
[    2.391559] rtc_zynqmp ffa60000.rtc: registered as rtc0
[    2.391614] i2c /dev entries driver
[    2.393567] device-mapper: ioctl: 4.41.0-ioctl (2019-09-16) initialised: dm-devel@redhat.com
[    2.393627] Bluetooth: HCI UART driver ver 2.3
[    2.393637] Bluetooth: HCI UART protocol H4 registered
[    2.393645] Bluetooth: HCI UART protocol BCSP registered
[    2.393669] Bluetooth: HCI UART protocol LL registered
[    2.393677] Bluetooth: HCI UART protocol ATH3K registered
[    2.393697] Bluetooth: HCI UART protocol Three-wire (H5) registered
[    2.393738] Bluetooth: HCI UART protocol Intel registered
[    2.393758] Bluetooth: HCI UART protocol QCA registered
[    2.393788] usbcore: registered new interface driver bcm203x
[    2.393817] usbcore: registered new interface driver bpa10x
[    2.393847] usbcore: registered new interface driver bfusb
[    2.393877] usbcore: registered new interface driver btusb
[    2.393917] usbcore: registered new interface driver ath3k
[    2.394030] EDAC MC: ECC not enabled
[    2.394170] EDAC DEVICE0: Giving out device to module zynqmp-ocm-edac controller zynqmp_ocm: DEV ff960000.memory-controller (INTERRUPT)
[    2.394467] pwrseq_simple sdio_pwrseq: mmc failed to get default resetn GPIO
[    2.394486] pwrseq_simple sdio_pwrseq: mmc failed to get default chip_en GPIO
[    2.394612] sdhci: Secure Digital Host Controller Interface driver
[    2.394620] sdhci: Copyright(c) Pierre Ossman
[    2.394627] sdhci-pltfm: SDHCI platform and OF driver helper
[    2.394973] ledtrig-cpu: registered to indicate activity on CPUs
[    2.395020] zynqmp_firmware_probe Platform Management API v1.1
[    2.395031] zynqmp_firmware_probe Trustzone version v1.0
[    2.418788] alg: No test for xilinx-zynqmp-aes (zynqmp-aes)
[    2.418929] zynqmp_aes zynqmp_aes: AES Successfully Registered
[    2.418929]
[    2.419094] alg: No test for xilinx-keccak-384 (zynqmp-keccak-384)
[    2.419320] alg: No test for xilinx-zynqmp-rsa (zynqmp-rsa)
[    2.419562] usbcore: registered new interface driver usbhid
[    2.419571] usbhid: USB HID core driver
[    2.419759] xlnk xlnk: Major 242
[    2.419846] xlnk xlnk: xlnk driver loaded
[    2.419855] xlnk xlnk: xlnk_pdev is not null
[    2.421780] fpga_manager fpga0: Xilinx ZynqMP FPGA Manager registered
[    2.422067] usbcore: registered new interface driver snd-usb-audio
[    2.422829] pktgen: Packet Generator for packet performance testing. Version: 2.75
[    2.423316] IPVS: Registered protocols (TCP, UDP)
[    2.423336] IPVS: Connection hash table configured (size=4096, memory=64Kbytes)
[    2.423431] IPVS: ipvs loaded.
[    2.423440] IPVS: [rr] scheduler registered.
[    2.423568] Initializing XFRM netlink socket
[    2.423651] NET: Registered protocol family 10
[    2.424104] Segment Routing with IPv6
[    2.424216] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    2.424555] NET: Registered protocol family 17
[    2.424572] NET: Registered protocol family 15
[    2.424594] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[    2.424607] can: controller area network core (rev 20170425 abi 9)
[    2.424640] NET: Registered protocol family 29
[    2.424649] can: raw protocol (rev 20170425)
[    2.424657] can: broadcast manager protocol (rev 20170425 t)
[    2.424667] can: netlink gateway (rev 20190810) max_hops=1
[    2.424745] Bluetooth: RFCOMM TTY layer initialized
[    2.424757] Bluetooth: RFCOMM socket layer initialized
[    2.424775] Bluetooth: RFCOMM ver 1.11
[    2.424787] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
[    2.424794] Bluetooth: BNEP filters: protocol multicast
[    2.424804] Bluetooth: BNEP socket layer initialized
[    2.424812] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
[    2.424822] Bluetooth: HIDP socket layer initialized
[    2.424934] 9pnet: Installing 9P2000 support
[    2.424956] Key type dns_resolver registered
[    2.425258] registered taskstats version 1
[    2.425266] Loading compiled-in X.509 certificates
[    2.425662] Btrfs loaded, crc32c=crc32c-generic
[    2.433775] ff000000.serial: ttyPS0 at MMIO 0xff000000 (irq = 40, base_baud = 6249999) is a xuartps
[    3.803524] printk: console [ttyPS0] enabled
[    3.808215] ff010000.serial: ttyPS1 at MMIO 0xff010000 (irq = 41, base_baud = 6249999) is a xuartps
[    3.817545] of-fpga-region fpga-full: FPGA Region probed
[    3.823980] xilinx-dpdma fd4c0000.dma: Xilinx DPDMA engine is probed
[    3.830569] xilinx-zynqmp-dma fd500000.dma: ZynqMP DMA driver Probe success
[    3.837671] xilinx-zynqmp-dma fd510000.dma: ZynqMP DMA driver Probe success
[    3.844779] xilinx-zynqmp-dma fd520000.dma: ZynqMP DMA driver Probe success
[    3.851879] xilinx-zynqmp-dma fd530000.dma: ZynqMP DMA driver Probe success
[    3.858982] xilinx-zynqmp-dma fd540000.dma: ZynqMP DMA driver Probe success
[    3.866083] xilinx-zynqmp-dma fd550000.dma: ZynqMP DMA driver Probe success
[    3.873184] xilinx-zynqmp-dma fd560000.dma: ZynqMP DMA driver Probe success
[    3.880290] xilinx-zynqmp-dma fd570000.dma: ZynqMP DMA driver Probe success
[    3.887458] xilinx-zynqmp-dma ffa80000.dma: ZynqMP DMA driver Probe success
[    3.894563] xilinx-zynqmp-dma ffa90000.dma: ZynqMP DMA driver Probe success
[    3.901668] xilinx-zynqmp-dma ffaa0000.dma: ZynqMP DMA driver Probe success
[    3.908772] xilinx-zynqmp-dma ffab0000.dma: ZynqMP DMA driver Probe success
[    3.915868] xilinx-zynqmp-dma ffac0000.dma: ZynqMP DMA driver Probe success
[    3.922976] xilinx-zynqmp-dma ffad0000.dma: ZynqMP DMA driver Probe success
[    3.930082] xilinx-zynqmp-dma ffae0000.dma: ZynqMP DMA driver Probe success
[    3.937188] xilinx-zynqmp-dma ffaf0000.dma: ZynqMP DMA driver Probe success
[    3.944481] xilinx-psgtr fd400000.zynqmp_phy: Lane:1 type:8 protocol:4 pll_locked:yes
[    3.958691] zynqmp_clk_divider_set_rate() set divider failed for pl3_ref_div1, ret = -13
[    3.968391] xilinx-dp-snd-codec fd4a0000.zynqmp-display:zynqmp_dp_snd_codec0: Xilinx DisplayPort Sound Codec probed
[    3.979050] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm0: Xilinx DisplayPort Sound PCM probed
[    3.987079] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm1: Xilinx DisplayPort Sound PCM probed
[    3.995353] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: xilinx-dp-snd-codec-dai <-> xilinx-dp-snd-codec-dai mapping ok
[    4.007798] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: xilinx-dp-snd-codec-dai <-> xilinx-dp-snd-codec-dai mapping ok
[    4.020239] zynqmp_pll_disable() clock disable failed for dpll_int, ret = -13
[    4.027674] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: Xilinx DisplayPort Sound Card probed
[    4.037849] OF: graph: no port node found in /amba/zynqmp-display@fd4a0000
[    4.044823] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    4.051439] [drm] No driver support for vblank timestamp query.
[    4.057435] xlnx-drm xlnx-drm.0: bound fd4a0000.zynqmp-display (ops 0xffffffc010cf5a80)
[    4.198928] random: fast init done
[    8.185314] [drm] Cannot find any crtc or sizes
[    8.190065] [drm] Initialized xlnx 1.0.0 20130509 for fd4a0000.zynqmp-display on minor 0
[    8.198178] zynqmp-display fd4a0000.zynqmp-display: ZynqMP DisplayPort Subsystem driver probed
[    8.207481] xilinx-axipmon ffa00000.perf-monitor: Probed Xilinx APM
[    8.213993] xilinx-axipmon fd0b0000.perf-monitor: Probed Xilinx APM
[    8.220483] xilinx-axipmon fd490000.perf-monitor: Probed Xilinx APM
[    8.226972] xilinx-axipmon ffa10000.perf-monitor: Probed Xilinx APM
[    8.233842] dwc3 fe200000.dwc3: Failed to get clk 'ref': -2
[    8.239619] xilinx-psgtr fd400000.zynqmp_phy: Lane:2 type:0 protocol:3 pll_locked:yes
[    8.250748] dwc3 fe300000.dwc3: Failed to get clk 'ref': -2
[    8.256523] xilinx-psgtr fd400000.zynqmp_phy: Lane:3 type:1 protocol:3 pll_locked:yes
[    8.266669] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
[    8.272162] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 1
[    8.279919] xhci-hcd xhci-hcd.0.auto: hcc params 0x0238f625 hci version 0x100 quirks 0x0000000202010010
[    8.289337] xhci-hcd xhci-hcd.0.auto: irq 51, io mem 0xfe300000
[    8.295483] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
[    8.303757] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    8.310978] usb usb1: Product: xHCI Host Controller
[    8.315853] usb usb1: Manufacturer: Linux 5.4.0-xilinx-v2020.1 xhci-hcd
[    8.322467] usb usb1: SerialNumber: xhci-hcd.0.auto
[    8.327608] hub 1-0:1.0: USB hub found
[    8.331394] hub 1-0:1.0: 1 port detected
[    8.335506] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
[    8.341005] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 2
[    8.348661] xhci-hcd xhci-hcd.0.auto: Host supports USB 3.0 SuperSpeed
[    8.355238] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
[    8.363412] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.04
[    8.371685] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    8.378911] usb usb2: Product: xHCI Host Controller
[    8.383783] usb usb2: Manufacturer: Linux 5.4.0-xilinx-v2020.1 xhci-hcd
[    8.390398] usb usb2: SerialNumber: xhci-hcd.0.auto
[    8.395503] hub 2-0:1.0: USB hub found
[    8.399281] hub 2-0:1.0: 1 port detected
[    8.668067] usb 1-1: new high-speed USB device number 2 using xhci-hcd
[    8.714481] i2c i2c-0: Added multiplexed i2c bus 3
[    8.719487] i2c i2c-0: Added multiplexed i2c bus 4
[    8.724417] i2c i2c-0: Added multiplexed i2c bus 5
[    8.729339] i2c i2c-0: Added multiplexed i2c bus 6
[    8.734259] i2c i2c-0: Added multiplexed i2c bus 7
[    8.739173] i2c i2c-0: Added multiplexed i2c bus 8
[    8.744138] i2c i2c-0: Added multiplexed i2c bus 9
[    8.749046] i2c i2c-0: Added multiplexed i2c bus 10
[    8.753937] pca954x 0-0075: registered 8 multiplexed busses for I2C switch pca9548
[    8.761529] cdns-i2c ff020000.i2c: 400 kHz mmio ff020000 irq 30
[    8.767869] cdns-i2c ff030000.i2c: 400 kHz mmio ff030000 irq 31
[    8.774145] cdns-wdt fd4d0000.watchdog: Xilinx Watchdog Timer with timeout 60s
[    8.781584] cdns-wdt ff150000.watchdog: Xilinx Watchdog Timer with timeout 10s
[    8.789345] pwrseq_simple sdio_pwrseq: mmc succesfully got gpio_resetn
[    8.795884] pwrseq_simple sdio_pwrseq: mmc succesfully got gpio_chip_en
[    8.832529] usb 1-1: New USB device found, idVendor=0424, idProduct=2744, bcdDevice= 2.08
[    8.840725] usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    8.847862] usb 1-1: Product: USB2744
[    8.851523] usb 1-1: Manufacturer: Microchip Tech
[    8.856344] mmc0: SDHCI controller on ff160000.mmc [ff160000.mmc] using ADMA 64-bit
[    8.864745] sdhci-arasan ff170000.mmc: allocated mmc-pwrseq
[    8.905415] mmc0: new high speed SDHC card at address aaaa
[    8.911268] mmcblk0: mmc0:aaaa SL16G 14.8 GiB
[    8.916264] mmc1: SDHCI controller on ff170000.mmc [ff170000.mmc] using ADMA 64-bit
[    8.926844] input: gpio-keys as /devices/platform/gpio-keys/input/input0
[    8.933802] hub 1-1:1.0: USB hub found
[    8.937550] rtc_zynqmp ffa60000.rtc: setting system clock to 2021-01-22T14:36:58 UTC (1611326218)
[    8.937553] of_cfs_init
[    8.937577] of_cfs_init: OK
[    8.946484]  mmcblk0: p1 p2
[    8.948989] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    8.951831] hub 1-1:1.0: 4 ports detected
[    8.982946] mmc1: new high speed SDIO card at address 0001
[    9.095575] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    9.102104] clk: Not disabling unused clocks
[    9.106374] ALSA device list:
[    9.109341]   #0: DisplayPort monitor
[    9.113268] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
[    9.121886] cfg80211: failed to load regulatory.db
[    9.168363] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
[    9.176491] VFS: Mounted root (ext4 filesystem) on device 179:2.
[    9.187104] devtmpfs: mounted
[    9.190241] Freeing unused kernel memory: 704K
[    9.194743] Run /sbin/init as init process
[    9.339278] random: crng init done
[    9.742638] systemd[1]: systemd 237 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
[    9.764224] systemd[1]: Detected architecture arm64.

Welcome to PYNQ Linux, based on Ubuntu 18.04!

[    9.821528] systemd[1]: Set hostname to <pynq>.
[   10.426119] systemd[1]: Reached target Remote File Systems.
[  OK  ] Reached target Remote File Systems.
[   10.444166] systemd[1]: Reached target Swap.
[  OK  ] Reached target Swap.
[   10.460246] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[  OK  ] Started Dispatch Password Requests to Console Directory Watch.
[   10.484612] systemd[1]: Created slice User and Session Slice.
[  OK  ] Created slice User and Session Slice.
[   10.500137] systemd[1]: Reached target System Time Synchronized.
[  OK  ] Reached target System Time Synchronized.
[   10.516214] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[  OK  ] Started Forward Password Requests to Wall Directory Watch.
[   10.540114] systemd[1]: Reached target Local Encrypted Volumes.
[  OK  ] Reached target Local Encrypted Volumes.
[  OK  ] Created slice System Slice.
[  OK  ] Reached target Slices.
[  OK  ] Listening on /dev/initctl Compatibility Named Pipe.
[  OK  ] Listening on Journal Audit Socket.
[  OK  ] Listening on Journal Socket.
         Mounting Kernel Debug File System...
         Starting Remount Root and Kernel File Systems...
[  OK  ] Listening on Journal Socket (/dev/log).
         Starting Create Static Device Nodes in /dev...
         Starting Load Kernel Modules...
[  OK  ] Created slice system-serial\x2dgetty.slice.
[  OK  ] Listening on udev Control Socket.
         Mounting Huge Pages File System...
[  OK  ] Listening on udev Kernel Socket.
         Starting udev Coldplug all Devices...
[   10.753338] wilc_sdio: loading out-of-tree module taints kernel.
         Starting Nameserver information manager...
[   10.762692] wifi_pm : 0
[   10.766734] wifi_pm : 1
[   10.769290] wilc_sdio mmc1:0001:1: Driver Initializing success
[  OK  ] Created slice system-getty.slice.
         Starting Restore / save the current clock...
[  OK  ] Listening on Syslog Socket.
         Starting Journal Service...
         Mounting POSIX Message Queue File System...
[  OK  ] Started ntp-systemd-netif.path.
[  OK  ] Mounted Kernel Debug File System.
[  OK  ] Started Remount Root and Kernel File Systems.
[  OK  ] Started Create Static Device Nodes in /dev.
[  OK  ] Started Load Kernel Modules.
[  OK  ] Mounted Huge Pages File System.
[  OK  ] Started Journal Service.
[  OK  ] Started Restore / save the current clock.
[  OK  ] Mounted POSIX Message Queue File System.
[  OK  ] Started Nameserver information manager.
[  OK  ] Reached target Network (Pre).
         Mounting Kernel Configuration File System...
         Starting Apply Kernel Variables...
[  OK  ] Reached target Local File Systems (Pre).
         Starting Flush Journal to Persistent Storage...
         Starting udev Kernel Device Manager...
         Starting Load/Save Random Seed...
[  OK  ] Mounted Kernel Configuration File System.
[  OK  ] Started Apply Kernel Variables.
[  OK  ] Started Load/Save Random Seed.
[  OK  ] Started udev Coldplug all Devices.
[  OK  ] Started Flush Journal to Persistent Storage.
[  OK  ] Started udev Kernel Device Manager.
[   11.855788] uio_pdrv_genirq 800e0000.audio-codec-ctrl: IRQ index 0 not found
[   11.900112] zocl-drm amba:zyxclmm_drm: IRQ index 0 not found
[  OK  ] Reached target Sound Card.
[  OK  ] Found device /dev/ttyPS0.
[  OK  ] Found device /dev/mmcblk0p1.
         Mounting /boot...
[  OK  ] Listening on Load/Save RF Kill Switch Status /dev/rfkill Watch.
[  OK  ] Mounted /boot.
[  OK  ] Reached target Local File Systems.
         Starting Enable support for additional executable binary formats...
         Starting Create Volatile Files and Directories...
         Starting Raise network interfaces...
         Starting Load/Save RF Kill Switch Status...
[  OK  ] Started Enable support for additional executable binary formats.
[  OK  ] Started Load/Save RF Kill Switch Status.
[  OK  ] Started Create Volatile Files and Directories.
         Starting Network Time Synchronization...
         Starting Update UTMP about System Boot/Shutdown...
[  OK  ] Started Entropy daemon using the HAVEGE algorithm.
         Starting Network Name Resolution...
[  OK  ] Started Update UTMP about System Boot/Shutdown.
[  OK  ] Started Network Time Synchronization.
[  OK  ] Reached target System Initialization.
[  OK  ] Listening on UUID daemon activation socket.
[  OK  ] Started Message of the Day.
[  OK  ] Started Discard unused blocks once a week.
[  OK  ] Started resolvconf-pull-resolved.path.
[  OK  ] Reached target Paths.
[  OK  ] Started Daily apt download activities.
[  OK  ] Started Daily apt upgrade and clean activities.
[  OK  ] Started Daily Cleanup of Temporary Directories.
[  OK  ] Reached target Timers.
[  OK  ] Listening on D-Bus System Message Bus Socket.
[  OK  ] Reached target Sockets.
[  OK  ] Reached target Basic System.
[  OK  ] Started Set the CPU Frequency Scaling governor.
         Starting Resize Filesystem on SD card...
         Starting Jupyter Notebook Server...
         Starting PYNQ PL Server...
         Starting System Logging Service...
[  OK  ] Started ntp-systemd-netif.service.
         Starting USB3.0 VBus Detection...
         Starting LSB: Load kernel modules needed to enable cpufreq scaling...
         Starting Login Service...
[  OK  ] Started Regular background program processing daemon.
         Starting Dispatcher daemon for systemd-networkd...
         Starting resolvconf-pull-resolved.service...
         Starting LSB: automatic crash report generation...
[  OK  ] Started D-Bus System Message Bus.
[  OK  ] Started Login Service.
         Starting WPA supplicant...
[  OK  ] Started Network Name Resolution.
[  OK  ] Started System Logging Service.
[  OK  ] Started Raise network interfaces.
[  OK  ] Started PYNQ PL Server.
[  OK  ] Started USB3.0 VBus Detection.
[  OK  ] Started resolvconf-pull-resolved.service.
         Starting USB Gadget for Networking...
[  OK  ] Reached target Host and Network Name Lookups.
[  OK  ] Found device /dev/ttyGS0.
[  OK  ] Started LSB: automatic crash report generation.
[  OK  ] Started USB Gadget for Networking.
[  OK  ] Started WPA supplicant.
[  OK  ] Reached target Network.
         Starting Permit User Sessions...
[  OK  ] Reached target Network is Online.
[  OK  ] Started ISC DHCP IPv4 server.
[  OK  ] Started ISC DHCP IPv6 server.
         Starting Samba NMB Daemon...
         Starting OpenBSD Secure Shell server...
[  OK  ] Started Unattended Upgrades Shutdown.
[  OK  ] Started Permit User Sessions.
[  OK  ] Started PYNQ X11 Server.
[  OK  ] Started Serial Getty on ttyGS0.
[  OK  ] Started Serial Getty on ttyPS0.
[  OK  ] Started Getty on tty1.
[  OK  ] Reached target Login Prompts.
[  OK  ] Started LSB: Load kernel modules needed to enable cpufreq scaling.

PYNQ Linux, based on Ubuntu 18.04 pynq ttyPS0

pynq login: xilinx (automatic login)

Welcome to PYNQ Linux, based on Ubuntu 18.04 (GNU/Linux 5.4.0-xilinx-v2020.1 aarch64)


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

xilinx@pynq:~$ logo         Stopping Session 1 of user xilinx.
[  OK  ] Stopped target Timers.
[  OK  ] Stopped Discard unused blocks once a week.
[  OK  ] Closed Load/Save RF Kill Switch Status /dev/rfkill Watch.
         Stopping Jupyter Notebook Server...
[  OK  ] Stopped Daily apt upgrade and clean activities.
         Stopping Session 4 of user xilinx.
[  OK  ] Stopped target Host and Network Name Lookups.
[  OK  ] Stopped Daily apt download activities.
         Stopping User Manager for UID 1000...
[  OK  ] Stopped target Graphical Interface.
[  OK  ] Stopped Message of the Day.
         Stopping Session c1 of user root.
         Stopping User Manager for UID 0...
         Stopping PYNQ PL Server...
[  OK  ] Stopped target Multi-User System.
[  OK  ] Stopped target Login Prompts.
         Stopping Getty on tty1...
         Stopping Serial Getty on ttyPS0...
         Stopping Regular background program processing daemon...
         Stopping Samba SMB Daemon...
         Stopping LSB: set CPUFreq kernel parameters...
         Stopping LSB: automatic crash report generation...
         Stopping Dispatcher daemon for systemd-networkd...
         Stopping PYNQ X11 Server...
         Stopping ISC DHCP IPv4 server...
         Stopping Unattended Upgrades Shutdown...
         Stopping System Logging Service...
[  OK  ] Stopped Daily Cleanup of Temporary Directories.
         Stopping Serial Getty on ttyGS0...
         Stopping OpenBSD Secure Shell server...
[  OK  ] Stopped System Logging Service.
[  OK  ] Stopped Regular background program processing daemon.
[  OK  ] Stopped Dispatcher daemon for systemd-networkd.
[  OK  ] Stopped ISC DHCP IPv4 server.
[  OK  ] Stopped Serial Getty on ttyGS0.
[  OK  ] Stopped Serial Getty on ttyPS0.
[  OK  ] Stopped Getty on tty1.
[  OK  ] Stopped User Manager for UID 0.
[  OK  ] Stopped OpenBSD Secure Shell server.
[  OK  ] Stopped User Manager for UID 1000.
[  OK  ] Stopped Samba SMB Daemon.
[  OK  ] Stopped PYNQ X11 Server.
[  OK  ] Stopped Session 4 of user xilinx.
[  OK  ] Stopped Session 1 of user xilinx.
[  OK  ] Stopped Jupyter Notebook Server.
[  OK  ] Stopped target Sound Card.
         Stopping Samba NMB Daemon...
[  OK  ] Removed slice User Slice of xilinx.
[  OK  ] Removed slice system-getty.slice.
[  OK  ] Removed slice system-serial\x2dgetty.slice.
[  OK  ] Stopped target System Time Synchronized.
         Stopping USB Gadget for Networking...
[  OK  ] Stopped Samba NMB Daemon.
[  OK  ] Stopped LSB: set CPUFreq kernel parameters.
[  OK  ] Stopped LSB: automatic crash report generation.
[  OK  ] Stopped USB Gadget for Networking.
[  OK  ] Stopped USB3.0 VBus Detection.
         Stopping LSB: Load kernel modules needed to enable cpufreq scaling...
[  OK  ] Stopped target Network is Online.
[  OK  ] Stopped LSB: Load kernel modules needed to enable cpufreq scaling.
[  OK  ] Unmounted /run/user/1000.
[  OK  ] Stopped Unattended Upgrades Shutdown.
[  OK  ] Stopped PYNQ PL Server.
[  OK  ] Stopped Session c1 of user root.
[  OK  ] Removed slice User Slice of root.
         Stopping Permit User Sessions...
         Stopping Login Service...
[  OK  ] Stopped Permit User Sessions.
[  OK  ] Stopped target Network.
         Stopping Raise network interfaces...
         Stopping Network Name Resolution...
         Stopping WPA supplicant...
[  OK  ] Stopped target Remote File Systems.
[  OK  ] Stopped Network Name Resolution.
[  OK  ] Stopped Login Service.
[  OK  ] Stopped WPA supplicant.
[  OK  ] Stopped Raise network interfaces.
[  OK  ] Stopped target Network (Pre).
         Stopping D-Bus System Message Bus...
[  OK  ] Stopped D-Bus System Message Bus.
[  OK  ] Stopped target Basic System.
[  OK  ] Stopped target Sockets.
[  OK  ] Closed UUID daemon activation socket.
[  OK  ] Closed Syslog Socket.
[  OK  ] Stopped target Slices.
[  OK  ] Removed slice User and Session Slice.
[  OK  ] Stopped target Paths.
[  OK  ] Stopped resolvconf-pull-resolved.path.
[  OK  ] Closed D-Bus System Message Bus Socket.
[  OK  ] Stopped target System Initialization.
         Stopping Restore / save the current clock...
[  OK  ] Stopped target Local Encrypted Volumes.
[  OK  ] Stopped Dispatch Password Requests to Console Directory Watch.
[  OK  ] Stopped Forward Password Requests to Wall Directory Watch.
         Stopping Load/Save Random Seed...
         Stopping Network Time Synchronization...
[  OK  ] Stopped Apply Kernel Variables.
         Stopping Update UTMP about System Boot/Shutdown...
[  OK  ] Stopped Load Kernel Modules.
[  OK  ] Stopped Network Time Synchronization.
[  OK  ] Stopped Restore / save the current clock.
[  OK  ] Stopped Load/Save Random Seed.
[  OK  ] Stopped Update UTMP about System Boot/Shutdown.
[  OK  ] Stopped Create Volatile Files and Directories.
[  OK  ] Stopped target Local File Systems.
         Unmounting /run/user/0...
         Unmounting /boot...
[  OK  ] Unmounted /run/user/0.
[  OK  ] Unmounted /boot.
[  OK  ] Stopped target Local File Systems (Pre).
[  OK  ] Stopped Create Static Device Nodes in /dev.
[  OK  ] Stopped Remount Root and Kernel File Systems.
[  OK  ] Stopped target Swap.
[  OK  ] Reached target Shutdown.
         Deactivating swap /var/swap...
[  OK  ] Deactivated swap /var/swap.
[  OK  ] Reached target Unmount All Filesystems.
[  OK  ] Reached target Final Step.
         Starting Power-Off...
[ 5738.699726] systemd-shutdown[1]: Failed to wait for process: Protocol error
[ 5738.868764] reboot: Power down


U-Boot 2020.01 (Jan 05 2021 - 13:55:09 +0000)

Model: TUL PYNQ-ZU RevB
Board: Xilinx ZynqMP
DRAM:  4 GiB
PMUFW:  v1.1
EL Level:       EL2
Chip ID:        zu5
NAND:  0 MiB
MMC:   mmc@ff160000: 0, mmc@ff170000: 1
In:    serial@ff000000
Out:   serial@ff000000
Err:   serial@ff000000
Bootmode: SD_MODE
Reset reason:   EXTERNAL
Net:   No ethernet found.
Hit any key to stop autoboot:  0
switch to partitions #0, OK
mmc0 is current device
Scanning mmc 0:1...
Found U-Boot script /boot.scr
1636 bytes read in 13 ms (122.1 KiB/s)
## Executing script at 20000000
17471764 bytes read in 1163 ms (14.3 MiB/s)
## Loading kernel from FIT Image at 10000000 ...
   Using 'conf@1' configuration
   Trying 'kernel@0' kernel subimage
     Description:  Linux Kernel
     Type:         Kernel Image
     Compression:  uncompressed
     Data Start:   0x100000d4
     Data Size:    17428992 Bytes = 16.6 MiB
     Architecture: AArch64
     OS:           Linux
     Load Address: 0x00080000
     Entry Point:  0x00080000
     Hash algo:    sha1
     Hash value:   caea54708b8b69b44ac004f7e6f8c0725e688344
   Verifying Hash Integrity ... sha1+ OK
## Loading fdt from FIT Image at 10000000 ...
   Using 'conf@1' configuration
   Trying 'fdt@0' fdt subimage
     Description:  Flattened Device Tree blob
     Type:         Flat Device Tree
     Compression:  uncompressed
     Data Start:   0x1109f3cc
     Data Size:    40945 Bytes = 40 KiB
     Architecture: AArch64
     Hash algo:    sha1
     Hash value:   6ad0ddf680e7cd2d162315cb5f7f4e8518c0f538
   Verifying Hash Integrity ... sha1+ OK
   Booting using the fdt blob at 0x1109f3cc
   Loading Kernel Image
   Loading Device Tree to 000000000fff3000, end 000000000ffffff0 ... OK

Starting kernel ...

[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
[    0.000000] Linux version 5.4.0-xilinx-v2020.1 (oe-user@oe-host) (gcc version 9.2.0 (GCC)) #1 SMP Tue Jan 5 13:40:43 UTC 2021
[    0.000000] Machine model: TUL PYNQ-ZU RevB
[    0.000000] efi: Getting EFI parameters from FDT:
[    0.000000] efi: UEFI not found.
[    0.000000] Reserved memory: created CMA memory pool at 0x000000005fc00000, size 512 MiB
[    0.000000] OF: reserved mem: initialized node linux,cma, compatible id shared-dma-pool
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: PSCIv1.1 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: MIGRATE_INFO_TYPE not supported.
[    0.000000] psci: SMC Calling Convention v1.1
[    0.000000] percpu: Embedded 22 pages/cpu s50392 r8192 d31528 u90112
[    0.000000] Detected VIPT I-cache on CPU0
[    0.000000] CPU features: detected: ARM erratum 845719
[    0.000000] Speculative Store Bypass Disable mitigation not required
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1031940
[    0.000000] Kernel command line: root=/dev/mmcblk0p2 rw earlyprintk rootfstype=ext4 rootwait devtmpfs.mount=1 uio_pdrv_genirq.of_id="generic-uio" clk_ignore_unused
[    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] software IO TLB: mapped [mem 0x5bc00000-0x5fc00000] (64MB)
[    0.000000] Memory: 3505052K/4193280K available (11964K kernel code, 700K rwdata, 3568K rodata, 704K init, 533K bss, 163940K reserved, 524288K cma-reserved)
[    0.000000] rcu: Hierarchical RCU implementation.
[    0.000000] rcu:     RCU event tracing is enabled.
[    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] GIC: Adjusting CPU interface base to 0x00000000f902f000
[    0.000000] GIC: Using split EOI/Deactivate mode
[    0.000000] random: get_random_bytes called from start_kernel+0x2a8/0x3cc with crng_init=0
[    0.000000] arch_timer: cp15 timer(s) running at 100.00MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x171024e7e0, max_idle_ns: 440795205315 ns
[    0.000003] sched_clock: 56 bits at 100MHz, resolution 10ns, wraps every 4398046511100ns
[    0.000301] Console: colour dummy device 80x25
[    0.000510] printk: console [tty0] enabled
[    0.000532] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=400000)
[    0.000547] pid_max: default: 32768 minimum: 301
[    0.000692] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.000714] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
[    0.001648] ASID allocator initialised with 32768 entries
[    0.001709] rcu: Hierarchical SRCU implementation.
[    0.001854] EFI services will not be available.
[    0.001985] smp: Bringing up secondary CPUs ...
[    0.002321] Detected VIPT I-cache on CPU1
[    0.002353] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
[    0.002702] Detected VIPT I-cache on CPU2
[    0.002721] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
[    0.003047] Detected VIPT I-cache on CPU3
[    0.003066] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
[    0.003114] smp: Brought up 1 node, 4 CPUs
[    0.003154] SMP: Total of 4 processors activated.
[    0.003163] CPU features: detected: 32-bit EL0 Support
[    0.003172] CPU features: detected: CRC32 instructions
[    0.003208] CPU: All CPU(s) started at EL2
[    0.003225] alternatives: patching kernel code
[    0.004326] devtmpfs: initialized
[    0.008627] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.008646] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.020543] xor: measuring software checksum speed
[    0.060060]    8regs     :  2375.000 MB/sec
[    0.100090]    32regs    :  2725.000 MB/sec
[    0.140122]    arm64_neon:  2365.000 MB/sec
[    0.140130] xor: using function: 32regs (2725.000 MB/sec)
[    0.140144] pinctrl core: initialized pinctrl subsystem
[    0.140754] NET: Registered protocol family 16
[    0.141763] DMA: preallocated 256 KiB pool for atomic allocations
[    0.141788] audit: initializing netlink subsys (disabled)
[    0.141909] audit: type=2000 audit(0.140:1): state=initialized audit_enabled=0 res=1
[    0.142206] cpuidle: using governor menu
[    0.142395] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[    0.153839] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.153854] HugeTLB registered 32.0 MiB page size, pre-allocated 0 pages
[    0.153864] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.153873] HugeTLB registered 64.0 KiB page size, pre-allocated 0 pages
[    1.229068] DRBG: Continuing without Jitter RNG
[    1.304881] raid6: neonx8   gen()  1548 MB/s
[    1.372933] raid6: neonx8   xor()  1467 MB/s
[    1.440989] raid6: neonx4   gen()  1489 MB/s
[    1.509015] raid6: neonx4   xor()  1430 MB/s
[    1.577097] raid6: neonx2   gen()  1135 MB/s
[    1.645092] raid6: neonx2   xor()  1189 MB/s
[    1.713182] raid6: neonx1   gen()   740 MB/s
[    1.781195] raid6: neonx1   xor()   895 MB/s
[    1.849237] raid6: int64x8  gen()  1166 MB/s
[    1.917272] raid6: int64x8  xor()   763 MB/s
[    1.985354] raid6: int64x4  gen()   984 MB/s
[    2.053400] raid6: int64x4  xor()   740 MB/s
[    2.121443] raid6: int64x2  gen()   683 MB/s
[    2.189463] raid6: int64x2  xor()   600 MB/s
[    2.257541] raid6: int64x1  gen()   451 MB/s
[    2.325554] raid6: int64x1  xor()   459 MB/s
[    2.325562] raid6: using algorithm neonx8 gen() 1548 MB/s
[    2.325570] raid6: .... xor() 1467 MB/s, rmw enabled
[    2.325577] raid6: using neon recovery algorithm
[    2.326106] iommu: Default domain type: Translated
[    2.326355] SCSI subsystem initialized
[    2.326495] usbcore: registered new interface driver usbfs
[    2.326526] usbcore: registered new interface driver hub
[    2.326556] usbcore: registered new device driver usb
[    2.326606] mc: Linux media interface: v0.10
[    2.326633] videodev: Linux video capture interface: v2.00
[    2.326655] pps_core: LinuxPPS API ver. 1 registered
[    2.326663] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    2.326680] PTP clock support registered
[    2.326701] EDAC MC: Ver: 3.0.0
[    2.327047] zynqmp-ipi-mbox mailbox@ff990400: Registered ZynqMP IPI mbox with TX/RX channels.
[    2.327214] FPGA manager framework
[    2.327345] Advanced Linux Sound Architecture Driver Initialized.
[    2.327618] Bluetooth: Core ver 2.22
[    2.327642] NET: Registered protocol family 31
[    2.327649] Bluetooth: HCI device and connection manager initialized
[    2.327661] Bluetooth: HCI socket layer initialized
[    2.327670] Bluetooth: L2CAP socket layer initialized
[    2.327686] Bluetooth: SCO socket layer initialized
[    2.328068] clocksource: Switched to clocksource arch_sys_counter
[    2.328163] VFS: Disk quotas dquot_6.6.0
[    2.328210] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    2.332178] NET: Registered protocol family 2
[    2.332506] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
[    2.332558] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    2.332769] TCP bind hash table entries: 32768 (order: 7, 524288 bytes, linear)
[    2.333156] TCP: Hash tables configured (established 32768 bind 32768)
[    2.333225] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    2.333304] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
[    2.333464] NET: Registered protocol family 1
[    2.333722] RPC: Registered named UNIX socket transport module.
[    2.333731] RPC: Registered udp transport module.
[    2.333739] RPC: Registered tcp transport module.
[    2.333746] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    2.334384] hw perfevents: no interrupt-affinity property for /pmu, guessing.
[    2.334539] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
[    2.335288] Initialise system trusted keyrings
[    2.335369] workingset: timestamp_bits=46 max_order=20 bucket_order=0
[    2.336110] NFS: Registering the id_resolver key type
[    2.336126] Key type id_resolver registered
[    2.336134] Key type id_legacy registered
[    2.336146] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
[    2.336171] jffs2: version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
[    2.349006] NET: Registered protocol family 38
[    2.349017] Key type asymmetric registered
[    2.349025] Asymmetric key parser 'x509' registered
[    2.349050] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
[    2.349121] io scheduler mq-deadline registered
[    2.349130] io scheduler kyber registered
[    2.374060] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
[    2.376979] cacheinfo: Unable to detect cache hierarchy for CPU 0
[    2.381179] brd: module loaded
[    2.385454] loop: module loaded
[    2.386103] mtdoops: mtd device (mtddev=name/number) must be supplied
[    2.387460] libphy: Fixed MDIO Bus: probed
[    2.388431] tun: Universal TUN/TAP device driver, 1.6
[    2.388520] CAN device driver interface
[    2.389816] usbcore: registered new interface driver cdc_acm
[    2.389825] cdc_acm: USB Abstract Control Model driver for USB modems and ISDN adapters
[    2.389854] usbcore: registered new interface driver cdc_wdm
[    2.389888] usbcore: registered new interface driver usb-storage
[    2.389941] usbcore: registered new interface driver usbserial_generic
[    2.389964] usbserial: USB Serial support registered for generic
[    2.389990] usbcore: registered new interface driver usb_serial_simple
[    2.390013] usbserial: USB Serial support registered for carelink
[    2.390033] usbserial: USB Serial support registered for zio
[    2.390053] usbserial: USB Serial support registered for funsoft
[    2.390075] usbserial: USB Serial support registered for flashloader
[    2.390096] usbserial: USB Serial support registered for google
[    2.390116] usbserial: USB Serial support registered for libtransistor
[    2.390136] usbserial: USB Serial support registered for vivopay
[    2.390156] usbserial: USB Serial support registered for moto_modem
[    2.390176] usbserial: USB Serial support registered for motorola_tetra
[    2.390199] usbserial: USB Serial support registered for novatel_gps
[    2.390219] usbserial: USB Serial support registered for hp4x
[    2.390239] usbserial: USB Serial support registered for suunto
[    2.390259] usbserial: USB Serial support registered for siemens_mpi
[    2.390397] gadgetfs: USB Gadget filesystem, version 24 Aug 2004
[    2.390481] mousedev: PS/2 mouse device common for all mice
[    2.390897] rtc_zynqmp ffa60000.rtc: registered as rtc0
[    2.390951] i2c /dev entries driver
[    2.392908] device-mapper: ioctl: 4.41.0-ioctl (2019-09-16) initialised: dm-devel@redhat.com
[    2.392969] Bluetooth: HCI UART driver ver 2.3
[    2.392979] Bluetooth: HCI UART protocol H4 registered
[    2.392987] Bluetooth: HCI UART protocol BCSP registered
[    2.393011] Bluetooth: HCI UART protocol LL registered
[    2.393019] Bluetooth: HCI UART protocol ATH3K registered
[    2.393038] Bluetooth: HCI UART protocol Three-wire (H5) registered
[    2.393080] Bluetooth: HCI UART protocol Intel registered
[    2.393100] Bluetooth: HCI UART protocol QCA registered
[    2.393129] usbcore: registered new interface driver bcm203x
[    2.393158] usbcore: registered new interface driver bpa10x
[    2.393189] usbcore: registered new interface driver bfusb
[    2.393218] usbcore: registered new interface driver btusb
[    2.393259] usbcore: registered new interface driver ath3k
[    2.393372] EDAC MC: ECC not enabled
[    2.393512] EDAC DEVICE0: Giving out device to module zynqmp-ocm-edac controller zynqmp_ocm: DEV ff960000.memory-controller (INTERRUPT)
[    2.393810] pwrseq_simple sdio_pwrseq: mmc failed to get default resetn GPIO
[    2.393829] pwrseq_simple sdio_pwrseq: mmc failed to get default chip_en GPIO
[    2.393954] sdhci: Secure Digital Host Controller Interface driver
[    2.393963] sdhci: Copyright(c) Pierre Ossman
[    2.393970] sdhci-pltfm: SDHCI platform and OF driver helper
[    2.394315] ledtrig-cpu: registered to indicate activity on CPUs
[    2.394363] zynqmp_firmware_probe Platform Management API v1.1
[    2.394373] zynqmp_firmware_probe Trustzone version v1.0
[    2.418157] alg: No test for xilinx-zynqmp-aes (zynqmp-aes)
[    2.418288] zynqmp_aes zynqmp_aes: AES Successfully Registered
[    2.418288]
[    2.418452] alg: No test for xilinx-keccak-384 (zynqmp-keccak-384)
[    2.418680] alg: No test for xilinx-zynqmp-rsa (zynqmp-rsa)
[    2.418924] usbcore: registered new interface driver usbhid
[    2.418932] usbhid: USB HID core driver
[    2.419123] xlnk xlnk: Major 242
[    2.419210] xlnk xlnk: xlnk driver loaded
[    2.419219] xlnk xlnk: xlnk_pdev is not null
[    2.421140] fpga_manager fpga0: Xilinx ZynqMP FPGA Manager registered
[    2.421428] usbcore: registered new interface driver snd-usb-audio
[    2.422192] pktgen: Packet Generator for packet performance testing. Version: 2.75
[    2.422676] IPVS: Registered protocols (TCP, UDP)
[    2.422697] IPVS: Connection hash table configured (size=4096, memory=64Kbytes)
[    2.422793] IPVS: ipvs loaded.
[    2.422802] IPVS: [rr] scheduler registered.
[    2.422928] Initializing XFRM netlink socket
[    2.423012] NET: Registered protocol family 10
[    2.423451] Segment Routing with IPv6
[    2.423564] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    2.423904] NET: Registered protocol family 17
[    2.423921] NET: Registered protocol family 15
[    2.423943] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[    2.423957] can: controller area network core (rev 20170425 abi 9)
[    2.423989] NET: Registered protocol family 29
[    2.423998] can: raw protocol (rev 20170425)
[    2.424006] can: broadcast manager protocol (rev 20170425 t)
[    2.424016] can: netlink gateway (rev 20190810) max_hops=1
[    2.424101] Bluetooth: RFCOMM TTY layer initialized
[    2.424114] Bluetooth: RFCOMM socket layer initialized
[    2.424132] Bluetooth: RFCOMM ver 1.11
[    2.424143] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
[    2.424151] Bluetooth: BNEP filters: protocol multicast
[    2.424161] Bluetooth: BNEP socket layer initialized
[    2.424169] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
[    2.424179] Bluetooth: HIDP socket layer initialized
[    2.424297] 9pnet: Installing 9P2000 support
[    2.424320] Key type dns_resolver registered
[    2.424628] registered taskstats version 1
[    2.424636] Loading compiled-in X.509 certificates
[    2.425030] Btrfs loaded, crc32c=crc32c-generic
[    2.433140] ff000000.serial: ttyPS0 at MMIO 0xff000000 (irq = 40, base_baud = 6249999) is a xuartps
[    3.802922] printk: console [ttyPS0] enabled
[    3.807605] ff010000.serial: ttyPS1 at MMIO 0xff010000 (irq = 41, base_baud = 6249999) is a xuartps
[    3.816934] of-fpga-region fpga-full: FPGA Region probed
[    3.823359] xilinx-dpdma fd4c0000.dma: Xilinx DPDMA engine is probed
[    3.829949] xilinx-zynqmp-dma fd500000.dma: ZynqMP DMA driver Probe success
[    3.837053] xilinx-zynqmp-dma fd510000.dma: ZynqMP DMA driver Probe success
[    3.844164] xilinx-zynqmp-dma fd520000.dma: ZynqMP DMA driver Probe success
[    3.851261] xilinx-zynqmp-dma fd530000.dma: ZynqMP DMA driver Probe success
[    3.858363] xilinx-zynqmp-dma fd540000.dma: ZynqMP DMA driver Probe success
[    3.865465] xilinx-zynqmp-dma fd550000.dma: ZynqMP DMA driver Probe success
[    3.872565] xilinx-zynqmp-dma fd560000.dma: ZynqMP DMA driver Probe success
[    3.879664] xilinx-zynqmp-dma fd570000.dma: ZynqMP DMA driver Probe success
[    3.886835] xilinx-zynqmp-dma ffa80000.dma: ZynqMP DMA driver Probe success
[    3.893935] xilinx-zynqmp-dma ffa90000.dma: ZynqMP DMA driver Probe success
[    3.901032] xilinx-zynqmp-dma ffaa0000.dma: ZynqMP DMA driver Probe success
[    3.908144] xilinx-zynqmp-dma ffab0000.dma: ZynqMP DMA driver Probe success
[    3.915239] xilinx-zynqmp-dma ffac0000.dma: ZynqMP DMA driver Probe success
[    3.922348] xilinx-zynqmp-dma ffad0000.dma: ZynqMP DMA driver Probe success
[    3.929451] xilinx-zynqmp-dma ffae0000.dma: ZynqMP DMA driver Probe success
[    3.936551] xilinx-zynqmp-dma ffaf0000.dma: ZynqMP DMA driver Probe success
[    3.943845] xilinx-psgtr fd400000.zynqmp_phy: Lane:1 type:8 protocol:4 pll_locked:yes
[    3.958067] zynqmp_clk_divider_set_rate() set divider failed for pl3_ref_div1, ret = -13
[    3.967763] xilinx-dp-snd-codec fd4a0000.zynqmp-display:zynqmp_dp_snd_codec0: Xilinx DisplayPort Sound Codec probed
[    3.978423] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm0: Xilinx DisplayPort Sound PCM probed
[    3.986454] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm1: Xilinx DisplayPort Sound PCM probed
[    3.994734] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: xilinx-dp-snd-codec-dai <-> xilinx-dp-snd-codec-dai mapping ok
[    4.007170] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: xilinx-dp-snd-codec-dai <-> xilinx-dp-snd-codec-dai mapping ok
[    4.019609] zynqmp_pll_disable() clock disable failed for dpll_int, ret = -13
[    4.027049] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: Xilinx DisplayPort Sound Card probed
[    4.037219] OF: graph: no port node found in /amba/zynqmp-display@fd4a0000
[    4.044196] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    4.050811] [drm] No driver support for vblank timestamp query.
[    4.056807] xlnx-drm xlnx-drm.0: bound fd4a0000.zynqmp-display (ops 0xffffffc010cf5a80)
[    4.196691] random: fast init done
[    8.179132] [drm] Cannot find any crtc or sizes
[    8.183895] [drm] Initialized xlnx 1.0.0 20130509 for fd4a0000.zynqmp-display on minor 0
[    8.192012] zynqmp-display fd4a0000.zynqmp-display: ZynqMP DisplayPort Subsystem driver probed
[    8.201309] xilinx-axipmon ffa00000.perf-monitor: Probed Xilinx APM
[    8.207828] xilinx-axipmon fd0b0000.perf-monitor: Probed Xilinx APM
[    8.214315] xilinx-axipmon fd490000.perf-monitor: Probed Xilinx APM
[    8.220802] xilinx-axipmon ffa10000.perf-monitor: Probed Xilinx APM
[    8.227670] dwc3 fe200000.dwc3: Failed to get clk 'ref': -2
[    8.233454] xilinx-psgtr fd400000.zynqmp_phy: Lane:2 type:0 protocol:3 pll_locked:yes
[    8.244591] dwc3 fe300000.dwc3: Failed to get clk 'ref': -2
[    8.250367] xilinx-psgtr fd400000.zynqmp_phy: Lane:3 type:1 protocol:3 pll_locked:yes
[    8.260529] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
[    8.266022] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 1
[    8.273778] xhci-hcd xhci-hcd.0.auto: hcc params 0x0238f625 hci version 0x100 quirks 0x0000000202010010
[    8.283198] xhci-hcd xhci-hcd.0.auto: irq 51, io mem 0xfe300000
[    8.289337] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
[    8.297610] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    8.304830] usb usb1: Product: xHCI Host Controller
[    8.309705] usb usb1: Manufacturer: Linux 5.4.0-xilinx-v2020.1 xhci-hcd
[    8.316320] usb usb1: SerialNumber: xhci-hcd.0.auto
[    8.321458] hub 1-0:1.0: USB hub found
[    8.325242] hub 1-0:1.0: 1 port detected
[    8.329369] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
[    8.334863] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 2
[    8.342523] xhci-hcd xhci-hcd.0.auto: Host supports USB 3.0 SuperSpeed
[    8.349107] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
[    8.357279] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.04
[    8.365554] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    8.372776] usb usb2: Product: xHCI Host Controller
[    8.377656] usb usb2: Manufacturer: Linux 5.4.0-xilinx-v2020.1 xhci-hcd
[    8.384267] usb usb2: SerialNumber: xhci-hcd.0.auto
[    8.389375] hub 2-0:1.0: USB hub found
[    8.393156] hub 2-0:1.0: 1 port detected
[    8.664079] usb 1-1: new high-speed USB device number 2 using xhci-hcd
[    8.708253] i2c i2c-0: Added multiplexed i2c bus 3
[    8.713240] i2c i2c-0: Added multiplexed i2c bus 4
[    8.718161] i2c i2c-0: Added multiplexed i2c bus 5
[    8.723095] i2c i2c-0: Added multiplexed i2c bus 6
[    8.728026] i2c i2c-0: Added multiplexed i2c bus 7
[    8.732934] i2c i2c-0: Added multiplexed i2c bus 8
[    8.737891] i2c i2c-0: Added multiplexed i2c bus 9
[    8.742803] i2c i2c-0: Added multiplexed i2c bus 10
[    8.747693] pca954x 0-0075: registered 8 multiplexed busses for I2C switch pca9548
[    8.755286] cdns-i2c ff020000.i2c: 400 kHz mmio ff020000 irq 30
[    8.761624] cdns-i2c ff030000.i2c: 400 kHz mmio ff030000 irq 31
[    8.767888] cdns-wdt fd4d0000.watchdog: Xilinx Watchdog Timer with timeout 60s
[    8.775333] cdns-wdt ff150000.watchdog: Xilinx Watchdog Timer with timeout 10s
[    8.783096] pwrseq_simple sdio_pwrseq: mmc succesfully got gpio_resetn
[    8.789643] pwrseq_simple sdio_pwrseq: mmc succesfully got gpio_chip_en
[    8.824547] usb 1-1: New USB device found, idVendor=0424, idProduct=2744, bcdDevice= 2.08
[    8.832737] usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    8.839878] usb 1-1: Product: USB2744
[    8.843534] usb 1-1: Manufacturer: Microchip Tech
[    8.848347] mmc0: SDHCI controller on ff160000.mmc [ff160000.mmc] using ADMA 64-bit
[    8.856753] sdhci-arasan ff170000.mmc: allocated mmc-pwrseq
[    8.897423] mmc0: new high speed SDHC card at address aaaa
[    8.903276] mmcblk0: mmc0:aaaa SL16G 14.8 GiB
[    8.908304] mmc1: SDHCI controller on ff170000.mmc [ff170000.mmc] using ADMA 64-bit
[    8.916425]  mmcblk0: p1 p2
[    8.921833] input: gpio-keys as /devices/platform/gpio-keys/input/input0
[    8.928797] rtc_zynqmp ffa60000.rtc: setting system clock to 2021-01-22T16:13:06 UTC (1611331986)
[    8.928814] hub 1-1:1.0: USB hub found
[    8.937677] of_cfs_init
[    8.937700] of_cfs_init: OK
[    8.941916] hub 1-1:1.0: 4 ports detected
[    8.943982] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    8.962725] mmc1: new high speed SDIO card at address 0001
[    9.087268] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    9.093803] clk: Not disabling unused clocks
[    9.098074] ALSA device list:
[    9.101041]   #0: DisplayPort monitor
[    9.104967] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
[    9.113586] cfg80211: failed to load regulatory.db
[    9.187203] EXT4-fs (mmcblk0p2): recovery complete
[    9.193040] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
[    9.201160] VFS: Mounted root (ext4 filesystem) on device 179:2.
[    9.210581] devtmpfs: mounted
[    9.213710] Freeing unused kernel memory: 704K
[    9.218212] Run /sbin/init as init process
[    9.265388] random: crng init done
[    9.764851] systemd[1]: systemd 237 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
[    9.786395] systemd[1]: Detected architecture arm64.

Welcome to PYNQ Linux, based on Ubuntu 18.04!

[    9.861579] systemd[1]: Set hostname to <pynq>.
[   10.469300] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[  OK  ] Started Forward Password Requests to Wall Directory Watch.
[   10.492650] systemd[1]: Created slice User and Session Slice.
[  OK  ] Created slice User and Session Slice.
[   10.508125] systemd[1]: Reached target Remote File Systems.
[  OK  ] Reached target Remote File Systems.
[   10.524498] systemd[1]: Created slice System Slice.
[  OK  ] Created slice System Slice.
[   10.540265] systemd[1]: Listening on udev Kernel Socket.
[  OK  ] Listening on udev Kernel Socket.
[   10.556122] systemd[1]: Reached target Slices.
[  OK  ] Reached target Slices.
[   10.572123] systemd[1]: Reached target System Time Synchronized.
[  OK  ] Reached target System Time Synchronized.
[  OK  ] Started Dispatch Password Requests to Console Directory Watch.
[  OK  ] Started ntp-systemd-netif.path.
[  OK  ] Listening on udev Control Socket.
[  OK  ] Created slice system-getty.slice.
[  OK  ] Created slice system-serial\x2dgetty.slice.
[  OK  ] Reached target Local Encrypted Volumes.
[  OK  ] Listening on Syslog Socket.
[  OK  ] Listening on Journal Audit Socket.
[  OK  ] Listening on /dev/initctl Compatibility Named Pipe.
[  OK  ] Listening on Journal Socket (/dev/log).
[  OK  ] Listening on Journal Socket.
         Mounting Kernel Debug File System...
         Starting Remount Root and Kernel File Systems...
         Starting Load Kernel Modules...
         Mounting POSIX Message Queue File System...
         Mounting Huge Pages File System...
         Starting udev Coldplug all Devices...
[   10.807826] wilc_sdio: loading out-of-tree module taints kernel.
[   10.817182] wifi_pm : 0
[   10.819622] wifi_pm : 1
[   10.822180] wilc_sdio mmc1:0001:1: Driver Initializing success
         Starting Nameserver information manager...
         Starting Create Static Device Nodes in /dev...
         Starting Journal Service...
         Starting Restore / save the current clock...
[  OK  ] Mounted Kernel Debug File System.
[  OK  ] Started Remount Root and Kernel File Systems.
[  OK  ] Started Load Kernel Modules.
[  OK  ] Mounted POSIX Message Queue File System.
[  OK  ] Mounted Huge Pages File System.
[  OK  ] Started Journal Service.
[  OK  ] Started Create Static Device Nodes in /dev.
[  OK  ] Started Restore / save the current clock.
[  OK  ] Started Nameserver information manager.
[  OK  ] Reached target Network (Pre).
         Mounting Kernel Configuration File System...
         Starting Apply Kernel Variables...
         Starting Flush Journal to Persistent Storage...
         Starting Load/Save Random Seed...
         Starting udev Kernel Device Manager...
         Activating swap /var/swap...
[  OK  ] Reached target Local File Systems (Pre).
[  OK  ] Mounted Kernel Configuration File System.
[  OK  ] Started Load/Save Random Seed.
[  OK  ] Started Apply Kernel Variables.
[  OK  ] Started udev Coldplug all Devices.
[  OK  ] Activated swap /var/swap.
[  OK  ] Reached target Swap.
[  OK  ] Started udev Kernel Device Manager.
[  OK  ] Started Flush Journal to Persistent Storage.
[   11.582721] uio_pdrv_genirq 800e0000.audio-codec-ctrl: IRQ index 0 not found
[  OK  ] Reached target Sound Card.
[   11.613316] zocl-drm amba:zyxclmm_drm: IRQ index 0 not found
[  OK  ] Found device /dev/ttyPS0.
[  OK  ] Found device /dev/mmcblk0p1.
         Mounting /boot...
[  OK  ] Listening on Load/Save RF Kill Switch Status /dev/rfkill Watch.
         Starting Load/Save RF Kill Switch Status...
[  OK  ] Mounted /boot.
[  OK  ] Started Load/Save RF Kill Switch Status.
[  OK  ] Reached target Local File Systems.
         Starting Raise network interfaces...
         Starting Create Volatile Files and Directories...
         Starting Enable support for additional executable binary formats...
[  OK  ] Started Enable support for additional executable binary formats.
[  OK  ] Started Create Volatile Files and Directories.
[  OK  ] Started Entropy daemon using the HAVEGE algorithm.
         Starting Network Name Resolution...
         Starting Update UTMP about System Boot/Shutdown...
         Starting Network Time Synchronization...
[  OK  ] Started Update UTMP about System Boot/Shutdown.
[  OK  ] Started Raise network interfaces.
[  OK  ] Started Network Time Synchronization.
[  OK  ] Started Network Name Resolution.
[  OK  ] Reached target Host and Network Name Lookups.
[  OK  ] Reached target System Initialization.
[  OK  ] Listening on UUID daemon activation socket.
[  OK  ] Started Message of the Day.
[  OK  ] Started Daily Cleanup of Temporary Directories.
[  OK  ] Started resolvconf-pull-resolved.path.
[  OK  ] Reached target Paths.
[  OK  ] Listening on D-Bus System Message Bus Socket.
[  OK  ] Reached target Sockets.
[  OK  ] Started Daily apt download activities.
[  OK  ] Started Daily apt upgrade and clean activities.
[  OK  ] Reached target Basic System.
         Starting Jupyter Notebook Server...
         Starting Resize Filesystem on SD card...
         Starting LSB: Load kernel modules needed to enable cpufreq scaling...
[  OK  ] Started D-Bus System Message Bus.
         Starting WPA supplicant...
         Starting LSB: automatic crash report generation...
[  OK  ] Started ntp-systemd-netif.service.
[  OK  ] Started Regular background program processing daemon.
[  OK  ] Started Set the CPU Frequency Scaling governor.
         Starting resolvconf-pull-resolved.service...
         Starting PYNQ PL Server...
         Starting Login Service...
         Starting Dispatcher daemon for systemd-networkd...
[  OK  ] Started Discard unused blocks once a week.
[  OK  ] Reached target Timers.
         Starting USB3.0 VBus Detection...
         Starting System Logging Service...
[  OK  ] Started Resize Filesystem on SD card.
[  OK  ] Started resolvconf-pull-resolved.service.
[  OK  ] Started PYNQ PL Server.
[  OK  ] Started USB3.0 VBus Detection.
[  OK  ] Started Login Service.
         Starting USB Gadget for Networking...
[  OK  ] Started WPA supplicant.
[  OK  ] Reached target Network.
         Starting Permit User Sessions...
         Starting OpenBSD Secure Shell server...
[  OK  ] Reached target Network is Online.
[  OK  ] Started ISC DHCP IPv6 server.
         Starting Samba NMB Daemon...
[  OK  ] Started Unattended Upgrades Shutdown.
[  OK  ] Started System Logging Service.
[  OK  ] Started LSB: automatic crash report generation.
[  OK  ] Started USB Gadget for Networking.
[  OK  ] Started Permit User Sessions.
[  OK  ] Found device /dev/ttyGS0.
[  OK  ] Started Serial Getty on ttyGS0.
[  OK  ] Started PYNQ X11 Server.
[  OK  ] Started Serial Getty on ttyPS0.
[  OK  ] Started Getty on tty1.
[  OK  ] Reached target Login Prompts.
[  OK  ] Started ISC DHCP IPv4 server.
[  OK  ] Started LSB: Load kernel modules needed to enable cpufreq scaling.
         Starting LSB: set CPUFreq kernel parameters...
[  OK  ] Started LSB: set CPUFreq kernel parameters.
[  OK  ] Created slice User Slice of root.
         Starting User Manager for UID 0...
[  OK  ] Started Session c1 of user root.
[  OK  ] Started OpenBSD Secure Shell server.
[  OK  ] Started User Manager for UID 0.
[  OK  ] Started Dispatcher daemon for systemd-networkd.
[  OK  ] Started Samba NMB Daemon.
         Starting Samba SMB Daemon...
[  OK  ] Started Samba SMB Daemon.
[  OK  ] Reached target Multi-User System.
[  OK  ] Reached target Graphical Interface.
         Starting Update UTMP about System Runlevel Changes...
[  OK  ] Started Update UTMP about System Runlevel Changes.

PYNQ Linux, based on Ubuntu 18.04 pynq ttyPS0

pynq login: xilinx (automatic login)

Last login: Fri Jan 22 14:37:36 UTC 2021 on ttyGS0
Welcome to PYNQ Linux, based on Ubuntu 18.04 (GNU/Linux 5.4.0-xilinx-v2020.1 aarch64)

xilinx@pynq:~$
```

