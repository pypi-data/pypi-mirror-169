#!/usr/bin/env bash

w=${1:?"${ME} workRID  [ workDIR  | . ] : workRID required, not given"}

marcURL="https://purl.bdrc.io/resource/"
gbparam="style=google_books"

workDir=${2-"."}
metadataDir="${workDir}/META"
errorLog="${workDir}/error.txt"

echo "****************************************************"
echo "*** FETCHING METADATA FOR ${w}"
echo "****************************************************"

if [ ! -w "${metadataDir}" ]; then
  mkdir -p $metadataDir
fi

  marcXMLdest="${metadataDir}/marc-${w}.xml"
  curl -s -o $marcXMLdest "${marcURL}${w}.mrcx?${gbparam}"
# IGRID metadata
