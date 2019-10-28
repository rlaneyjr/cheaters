# vmnet-shark

The ```vmnet-shark``` tool allows you to perform real-time packet capture and display for VMware Fusion networks with Wireshark.

## Prerequisites

  1. [VMware Fusion](https://www.vmware.com/products/fusion.html)
  2. [Wireshark](https://www.wireshark.org)

## Installation

```console
$ cd /usr/local/bin
$ sudo curl -Lo vmnet-shark https://raw.githubusercontent.com/mweisel/vmnet-shark/master/vmnet-shark.sh
$ sudo chmod +x ./vmnet-shark
```

## Usage

> **Note**: VMware Fusion 11 Pro added a feature for renaming custom networks. The ```vmnet-shark``` tool only supports the default vmnet (e.g., vmnet0, vmnet1, vmnet2, etc.) name format.

<img src="https://res.cloudinary.com/binarynature/image/upload/v1552871719/top-triple-ioxrv-vmnet11_yfhh7n.png" width="330" height="250">


```console
$ vmnet-shark vmnet11
```


![vmnet11 packet capture](https://res.cloudinary.com/binarynature/image/upload/v1552867714/cap-triple-ioxrv-vmnet11_lzsdht.png)

## Reference

* [VMware Fusion 11 - Creating Custom Networks](https://docs.vmware.com/en/VMware-Fusion/11/com.vmware.fusion.using.doc/GUID-C5837B81-9509-4F1B-9572-0EC0CFA87563.html)
* [Real-time vmnet packet capture and display for VMware Fusion](https://binarynature.blogspot.com/2015/05/real-time-vmnet-packet-capture-display-vmware-fusion.html)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
