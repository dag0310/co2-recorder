# CO2 Sensor MH-Z19C

- Reference: [https://github.com/UedaTakeyuki/mh-z19.git](https://github.com/UedaTakeyuki/mh-z19.git)
- `sudo raspi-config`: Enable the serial interface which is used to communicate with the MH-Z19C. This tool is asking quite a few questions… (Interface Options — Serial Port — No — Ok)
- `sudo pip3 install -r requirements.txt`
- `./co2.py`
- Set values in `config.ini` according to `config.template.ini`

## Calibration

https://github.com/UedaTakeyuki/mh-z19/wiki/CALIBRATION-&-detection-range

`sudo python3 -m mh_z19 --h`
`sudo python3 -m mh_z19 --abc_off`
`sudo python3 -m mh_z19 --detection_range_2000`
`sudo python3 -m mh_z19 --zero_point_calibration`
