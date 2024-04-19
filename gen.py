import json
import sys

def gen(pathFrom, i):
  with open(pathFrom) as input:
    data = json.load(input)

  href = data["image"].split("/")
  href[-1] = f"{i}.jpg"
  href = "/".join(href)

  data["image"] = data["external_url"] = href
  return data

for i in range(3, 2000):
  with open(f"{i}.json", "w") as outfile:
    json.dump(gen(f"{i % 3}.json", i % 3), outfile, indent=4)
