Disable ssh by password (TODO)

To configure new users (once installed)
---------------------------------------

Run the following command and following the instructions:

    cd /etc/easy-rsa/
    sudo . ./vars ./build-key <keyname>

will generate various files needed to configure OpenVPN:

- `<keyname>.crt` (User certificate)
- `ca.crt` (CA certificate)
- `<keyname>.key` (Private key)

The client must configure the following options:

- Port 8010
- LZO compression
- TCP connection
