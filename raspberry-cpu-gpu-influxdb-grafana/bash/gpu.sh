#!/bin/bash
gpu="$(/opt/vc/bin/vcgencmd measure_temp | cut -c 6-)"
echo ${gpu}

# Dependendo do Raspberry, o arquivo de execucao podera estar em outro diretorio
# gpu="$(/usr/bin/vcgencmd measure_temp | cut -c 6-)"