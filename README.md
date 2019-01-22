# Python Uptime

Python script to get statistics on uptime and response time for a particular URL

## Requirements

The following librairies are required for the script to work :

+ requests
+ matplotlib

You can install them with these commands
```bash
python3.7 -m pip install requests
python3.7 -m pip install matplotlib 
```

## Usage

```bash
python3.7 Uptime.py URL
```
## Example

```bash
python3.7 Uptime.py https://www.google.fr/
```

### Result

```
100% up time during 0:00:05
Minimum response time: 117ms
Maximum response time : 137ms
Mean response time : 127ms
```

![alt text](https://github.com/Baennon/python-uptime/raw/master/result.png "Resultant graph")



