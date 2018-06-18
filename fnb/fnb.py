import argparse
import time

import fnb

parser = argparse.ArgumentParser()
parser.add_argument("number", type=int)
args = parser.parse_args()

since = time.time()
result = fnb.fnb(args.number)
time_used = time.time() - since
print("fnb({})={}".format(args.number, result))
print("Time used: {:.0f}m:{:.0f}s".format(time_used//60, time_used % 60))
