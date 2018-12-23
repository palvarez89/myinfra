General
=======

Installing roles needed
-----------------------

    ansible-galaxy install -r requirements.yml -p roles/

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
