# WiFi Connection Script For Raspberry Pi 

This script is designed with the purpose of connecting to Wi-Fi network on a 4-inch Raspberry Pi touchscreen. The system dialog 
to configure a Wifi is too big for small touchscreens. 

## Prerequisites

The script is written in Python 3, thus requires `python3` and `python3-tk` to run.

## How To Run The Script

1. Ensure you have the required tools installed. 

    ```bash
    sudo apt-get install python3 python3-tk
    ```

2. Download/Clone the repository containing the script or directly download the script.

3. Run the script using python3

    ```bash
    python3 your_script.py
    ```

The script's GUI will appear on your Raspberry Pi's touchscreen, you can then proceed to select your WiFi network and enter the password to establish connection.