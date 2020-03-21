# RRD to JSON and CSV exporter

## Example call

```
sage-rrd-export --format json --input "DEF:UAT=wazers_bu.rrd:Bucuresti:AVERAGE:step=3600"  --output data.csv --start -645000 --xport UAT
```
