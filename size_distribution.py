import os, json

files = [z for z in os.listdir(".") if z.endswith(".tsv")]

count = {}

def t(w,h):
  return "{0}_{1}".format(w,h)

def add_count(count, w, h):
  token = t(w,h)
  if token not in count:
    count[token] = 0
  count[token] += 1

for f in files:
  if f in ["unknown_plates.tsv", "unknown_medium.tsv", "unknown_small.tsv", "titlelist.tsv"]:
    continue
  with open(f, "r") as fp:
    print("{0}".format(f))
    headers = fp.readline().strip("\r\n").split("\t")
    widx = headers.index("flickr_original_width")
    hidx = headers.index("flickr_original_height")
    for img in fp:
      cols = img.strip("\r\n").split("\t")
      w = cols[widx]
      h = cols[hidx]
      add_count(count, w, h)

with open("sizecounts.json", "w") as sc:
  json.dump(count, sc)

