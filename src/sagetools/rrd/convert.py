import pandas as pd
import json
import sys
import argparse
import rrdtool

from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description='Export RRD to JSON or CSV')
    parser.add_argument('--format', choices=['json', 'csv'])
    parser.add_argument('--input-rrd',
                        required=True,
                        type=str,
                        help="Eg: DEF:UAT=path.rrd:Bucuresti:AVERAGE:step=86400 XPORT:UAT")
    parser.add_argument('--start', type=int, required=True)
    parser.add_argument('--xport', type=str, required=True, help="Export field")
    #parser.add_argument('--export-time', action='store_true', default=False, help="Export time")
    parser.add_argument('--output', required=True, type=argparse.FileType('w'))
    args = parser.parse_args()
    rrd_args = ["XPORT:"+args.xport, "--start", str(args.start),]
    export = rrdtool.xport(args.input_rrd, *rrd_args)
    start_time = export['meta']['start']
    step = export['meta']['step']
    data = export['data']
    series = []
    current_time = start_time
    for entry in data:
        current_time += step
        dt = current_time
        dt = datetime.utcfromtimestamp(dt)
        value = entry[0]
        if value is None:
            continue
        series.append([dt, value])
    df = pd.DataFrame.from_records(series, columns=["Time", "Value"])
    df.to_csv(args.output)
