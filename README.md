# kasa-smart-plug-web_interface
#### This is a simple web interface to allow you to turn on/off a TP-Link Kasa smart plug from a browser. 
:warning: NOTE:
Requries at least Python 3.7 or newer

## Setup:
1. Install [python-kasa](https://github.com/python-kasa/python-kasa) and [pywebio](https://github.com/pywebio/PyWebIO). You can use the pip requirements.txt file in this repo to help if needed. You can use a virtual environment if you wish. 
2. Change line 13 of test.py to have the desired plug IP address e.g.

    ` PLUG = SmartPlug("192.168.0.2")`

3. Run the following in your terminal (you may need to start your virtual environment if you used one)

    `python3 test.py`
    
4. Navigate to the URL printed in the console to toggle the plug state. The URL by default is: [http://localhost:8000/](http://localhost:8000)
    
---
If you have issues with the socket already being in use, try change line 41 to use another port. E.g. ` port=8001 `. And then instead navigate to http://localhost:8001
