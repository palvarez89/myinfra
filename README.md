General
=======

Installing roles needed
-----------------------

    ansible-galaxy install -r requirements.yml -p roles/

For paparajotes y bellotas
==========================

    ansible-playbook -i hosts wedsite.yml  -e ansible_user=pedroalvarez


For Quassel
===========

    ansible-playbook -i hosts quasselcore.yml  -e ansible_user=pedroalvarez


For OpenVPN
===========

To configure new users (once installed)
---------------------------------------

Run the following command and following the instructions:

    cd /etc/easy-rsa/
    sudo ./easyrsa gen-req <keyname> nopass
    sudo ./easyrsa sign-req client <keyname>

will generate various files needed to configure OpenVPN:

- `<keyname>.crt` (User certificate)
- `ca.crt` (CA certificate)
- `<keyname>.key` (Private key)

The client must configure the following options:

- Port 8010
- LZO compression
- TCP connection

VPN won't connect? Renew the CRL
--------------------------------
Check this is the issue by trying to connect and:

    sudo journalctl -u openvpn-server@server.service  -f

You will see:

    VERIFY ERROR: depth=0, error=CRL has expired: CN=foobar-2019

Regenerate CRL

    cd /etc/easy-rsa
    sudo ./easyrsa gen-crl
    sudo cp /etc/easy-rsa/keys/crl.pem crl.pem /etc/openvpn/server
