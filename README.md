# Python Projects

This repository contains a collection of Python programs for various purposes.

## Table of Contents

- [IpInfo](#ipinfo)
- [Lock_Unlock](#lock_unlock)
- [PingWebsite](#pingwebsite)

## IpInfo

The `ipInfo.py` script uses the `ipinfo` library to retrieve the location details of a given IP address. It fetches the IP address from the `api.ipify.org` service and then uses the `ipinfo` API to get the corresponding location information, such as city, region, country, latitude, longitude, and timezone. The location details are saved in a JSON file located in the `Output` folder.

## Lock_Unlock

This folder contains two Python scripts, `lock.py` and `unlock.py`, that provide functionality to lock and unlock files and folders, respectively.

### lock.py

The `lock.py` script recursively traverses a specified directory and performs the following actions:

1. Removes all permissions for directories.
2. Renames directories with a leading dot (`.`) to hide them.
3. Removes all permissions for files.
4. Renames files with a leading dot (`.`) to hide them.

The script assumes the presence of a `Lock_Unlock` folder containing a `Lock` folder in the current working directory.

### unlock.py

The `unlock.py` script is designed to reverse the actions performed by the `lock.py` script. It recursively traverses the hidden `Lock` folder and performs the following actions:

1. Restores original permissions for directories (set to 0o755 by default, but you can adjust it according to your needs).
2. Removes the leading dot (`.`) from directory names to unhide them.
3. Restores original permissions for files (set to 0o644 by default, but you can adjust it according to your needs).
4. Removes the leading dot (`.`) from file names to unhide them.

After unhiding all files and folders, the script renames the `Lock` folder back to its original name.

## PingWebsite

The `pingloop.py` script continuously pings a specified website using the `ping` command from the operating system. It demonstrates how to execute system commands from within a Python script.

The `WebsitePing` class encapsulates the functionality of pinging a website. It takes a URL as input and provides methods to ping the website and run the pinger in a loop.

When executed, the script prompts the user to enter the URL to ping, creates an instance of the `WebsitePing` class, and starts the pinger loop. The loop continuously pings the specified website and prints a message indicating whether the website is reachable or not.

## Prerequisites

To run these programs, you need to have Python installed on your system. Additionally, the `ipInfo.py` script requires the `ipinfo` library, which can be installed using `pip`: 
```bash
pip install ipinfo.io
```
## Project Structure

The project is organized as follows:

```md
.
├───IpINFO
├───Lock_Unlock
│   └───Lock
│       └───Folder
├───Output
└───PingWebsite
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/python-projects.git
```

2. Navigate to the desired project folder.
3. Follow the specific instructions for each project as mentioned in the respective sections above.

For example, to run the `pingloop.py` script:
```bash
cd PingWebsite
python pingloop.py
```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.