**feedie** is a simple easy-to-use iRC RSS FEED bot written in Python.

## Features

* Easy configuration
* Supports multiple Feeds and Channels
* Supports short urls
* IRC Colors


## Required:
```
apt-get install python3-pip libffi-dev
pip3 install pyopenssl feedparser irc requests sgmllib3k
```

*Note*
*In case of following issue:*
```bash
The following packages have unmet dependencies:
 python3-pip : Depends: python-pip-whl (= 8.1.1-2) but 8.1.1-2ubuntu0.4 is to be installed
               Recommends: python3-dev (>= 3.2) but it is not going to be installed
               Recommends: python3-wheel but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```
*Please uninstall* ***python-pip-whl***
`apt-get remove python-pip-whl` *and try* `apt-get install python3-pip` *again, it should run!*

## Installation:
```
$ cd /home/<username>  
$ git clone https://github.com/meigrafd/feedie.git
$ cd feedie
```

Edit the config.py file to suit your needs, then:

```
$ bash start.sh
```
