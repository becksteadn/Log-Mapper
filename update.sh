#!/bin/bash

sudo cp  /var/log/auth.log /home/pi/Log-Mapper/
cd /home/pi/Log-Mapper
python /home/pi/Log-Mapper/stats_map.py
python3 /home/pi/Log-Mapper/draw_map.py
python3 /home/pi/Log-Mapper/get_stats.py
sudo cp /home/pi/Log-Mapper/mymap.html /var/www/html/