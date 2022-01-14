#!/bin/bash
gpu="$(/opt/vc/bin/vcgencmd measure_temp | cut -c 6-)"
echo ${gpu}