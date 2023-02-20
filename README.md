# How to use the mitm and dnspoison scripts

## How to clone
Please clone this link: https://github.com/ninjawill543/reseau.git

Once you have used the cd command to move to reseau/TP5-MITM/Scripts, please follow the next steps.

## MITM:
To launch the mitm.py script, simply run
```
sudo python3 mitm.py
```

Steps to start the attack:

- Enter the ip address of your network followed by the subnet mask
- Chose a victim ip from the list by typing the number at the beginning of the line
- Enter the router's ip address

The attack has now started, you may open wireshark and view the traffic passing from the victim to you, and then from you to the router, and vice versa.

## DNS poison:
The dns poison script does not currently work

