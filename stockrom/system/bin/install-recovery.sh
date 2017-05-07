#!/system/bin/sh
if [ -f /system/etc/recovery-transform.sh ]; then
  exec sh /system/etc/recovery-transform.sh 10047488 ef2d3d6c4ad32de867b84ce0c4234ffb2b9656ef 7374848 e041534e485a7814c51c446d2c1eeaf51e3a1236
fi

if ! applypatch -c EMMC:/dev/block/bootdevice/by-name/recovery:10047488:ef2d3d6c4ad32de867b84ce0c4234ffb2b9656ef; then
  applypatch -b /system/etc/recovery-resource.dat EMMC:/dev/block/bootdevice/by-name/boot:7374848:e041534e485a7814c51c446d2c1eeaf51e3a1236 EMMC:/dev/block/bootdevice/by-name/recovery ef2d3d6c4ad32de867b84ce0c4234ffb2b9656ef 10047488 e041534e485a7814c51c446d2c1eeaf51e3a1236:/system/recovery-from-boot.p && log -t recovery "Installing new recovery image: succeeded" || log -t recovery "Installing new recovery image: failed"
else
  log -t recovery "Recovery image already installed"
fi
