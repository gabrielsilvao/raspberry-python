#!/bin/bash
INFLUXDB_HOST=$1
PORT=$2
NODE=`hostname`
LOCATION="home"
STREAMS="temperature:Celcius humidity:Percent"
PYTHON=/usr/bin/python3
PY_SCRIPT=/home/pi/temp-humi.py
PY_SCRIPT_TMP=/home/pi/temp-humi.tmp
PY_SCRIPT_LOG=/home/pi/temp-humi.log
EXEC_DATE=`date +%Y-%m-%d" "%H:%M:%S`
NANO="000000000"
UNIXTIME=`date -d "${EXEC_DATE}" +%s`
DATETIME=${UNIXTIME}${NANO}

## Main
RESULT=${EXEC_DATE}
${PYTHON} ${PY_SCRIPT} > ${PY_SCRIPT_TMP}
for streams in `echo ${STREAMS}`
do
    stream=`echo ${streams} | awk -F: '{print $1}'`
    VALUE=`grep ${stream} ${PY_SCRIPT_TMP} | awk '{print $3}'`
    UNIT=`echo ${streams} | awk -F: '{print $2}'`
    curl -i -XPOST "http://${INFLUXDB_HOST}:${PORT}/write?db=home&u=grafana&p=seletiva39" --data-binary "${stream},node=${NODE},location=${LOCATION},unit=${UNIT} value=${VALUE} ${DATETIME}"
    RESULT+=" ${stream}:${VALUE}"
done

echo ${RESULT} >> ${PY_SCRIPT_LOG}