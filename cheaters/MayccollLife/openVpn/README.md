

### Debian install

```bash
  $
  wget http://swupdate.openvpn.org/as/openvpn-as-2.0.20-Debian8.amd_64.deb
  sudo dpkg -i openvpn-as-2.0.20-Debian8.amd_64.deb

  # Add password
  sudo passwd openvpn

  # Load config files
  sudo openvpn --config client.ovpn

   # To change interface or config again
   sudo /usr/local/openvpn_as/bin/ovpn-init

```
