#!/bin/bash
INPUT=$1
OUTPUT_DIR=$2
OPTIONAL=''

if [ $# -eq 3 ]; then
    echo 'Got the optional file!: '$3
    OPTIONAL=$3
fi
echo ''
echo '-----------------------------------------------------------------'
echo 'Calling job with arguments '${INPUT} ${OUTPUT_DIR} ${OPTIONAL}

/usr/bin/python /app/renamer.py $INPUT $OUTPUT_DIR ${OPTIONAL}
rc=$?

echo 'Done calling job - wrapper finished'
echo '-----------------------------------------------------------------'
echo ''
exit ${rc}