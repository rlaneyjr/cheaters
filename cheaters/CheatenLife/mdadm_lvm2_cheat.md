mdadm
=====

Glossary:
* md: multiple devices

| command | description |
|---------|-------------|
| `cat /proc/mdstat` | show status of all raids |
| `mdadm --detail /dev/md0` | detailed status of raid md0 |
| `mdadm --create /dev/md0 -n2 -l1 /dev/sda1 /dev/sdb1` | new raid `/dev/md0` with 2 disks, raid level 1 on `/dev/sda1` and `/dev/sda2`
| `mdadm --fail /dev/md0 /dev/sda1 ; mdadm --remove /dev/md0 /dev/sda1` | remove `/dev/sda1` from `/dev/md0`
| `mdadm --add /dev/md0 /dev/sda1` | add `/dev/sda1` to `/dev/md0`
| `mdadm --grow /dev/md0 -n3` | use 3 disks in raid `/dev/md0` (e.g. add an additional disk, so a damaged drive can be removed later-on)
| `mdadm --assemble /dev/md0` | Assemble `/dev/md0` (e.g. when running live system)
| `mdadm --detail --scan >> /etc/mdadm/mdadm.conf` | Update list of arrays in `/etc/mdadm/mdadm.conf` ; you should remove old list by hand first!
| `mdadm --examine /dev/sda1` | What is this disk / partition?
| `sysctl -w dev.raid.speed_limit_min=10000` | Set minimum raid rebuilding speed to 10000 kiB/s (default 1000)
| <code>sfdisk -d /dev/sda &#124; sfdisk /dev/sdb</code> | Copy partition table from sda to sdb

* To boot a machine even with a degraded array, modify `/etc/initramfs-tools/conf.d/mdadm` and run `update-initramfs -c -kall` (Use with caution!)

lvm
===

Glossary:
* *pv*: physical device (e.g. `/dev/md0` or `/dev/sda1`)
* *vg*: volume group (consists of 1 or more *pv*s, contains *lv*s); has a name (e.g. `lvm`)
* *lv*: logical volume (has a name which defines its path, e.g. `/dev/lvm/root` which equals `dev/mapper/lvm-root`)

| command | description |
|---------|-------------|
| `pvcreate /dev/md0` | initializes `/dev/md0` as phys device for a volume group
| `vgcreate lvm /dev/md0` | create volume group `lvm` with phys device `/dev/md0`
| `lvcreate -L30G -nroot lvm ; mkfs.ext4 /dev/lvm/root` | create logical volume `root`, sized 30G in volume group `lvm`; format with ext4
| `lvextend -L60G -nroot lvm ; resize2fs /dev/lvm/root` | extend `/dev/lvm/root` to 60G; also resize file system to new size
| `pvs`, `vgs`, `lvs` | show short info about pv, vg and lv
| `pvdisplay`, `vgdisplay`, `lvdisplay` | show long info
| `pvscan /dev/md0` | scan disks for physical volumes (e.g. when running live system)
| `vgextend lvm /dev/md1` | add phys device `/dev/md1` to volume group `lvm` (need pvcreate first!)
| `pvmove /dev/md0 ; vgreduce lvm /dev/md0` | move all logical volumes from `/dev/md0` and remove phys device from volume group

Other
=====
create bios grub partition
--------------------------
```sh
parted
mklabel gpt
unit s
mkpart bios 64s 2047s
set 1 bios_grub on
mkpart NAME 2048s [end]
```