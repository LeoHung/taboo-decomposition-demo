"""
@San-Chuan Hung

gen_js.py loads the cluster files (as "airport_id,airport_id,airline_id" format),
hash_id-id mapping file, and also airport data file to produce airports js, which
is used to draw the airport locations on google map. The output will directly show
on the stdout.

Command:

python gen_js.py ${airports_dat_file} ${conv_airlines_file} ${*cluster_files ...}

Usage Example:

python gen_js.py airports.dat conv_airports out.0/part*
"""

import re
class Airport:
  def __init__(self, name, city, country, code3, code4, lat, lng):
    self.name = name
    self.city = city
    self.country = country
    self.code3 = code3
    self.code4 = code4
    self.lat = float(lat)
    self.lng = float(lng)

def load_hash2airport(dat_file, conv_file):
  ind2airport = {}
  f = open(dat_file)
  for l in f:
    t = re.search(
      "(\d+),\"([^\"]*)\",\"([^\"]*)\",\"([^\"]*)\",\"([^\"]*)\",([^,]*),([^,]*),([^,]*)" ,
      l)
    ind2airport[t.group(1)] = Airport(
        t.group(2),
        t.group(3),
        t.group(4),
        t.group(5),
        t.group(6),
        t.group(7),
        t.group(8))
  f.close()

  ind2hashind = {}
  f = open(conv_file)
  for l in f:
    t = l.strip().split(" ")
    ind2hashind[t[0]] = t[1]
  f.close()

  hashind2airport = {}
  for ind, airport in ind2airport.items():
    hashind = ind2hashind[ind]
    hashind2airport[hashind] = airport

  return hashind2airport


def main(airports_dat_file, conv_airlines_file, *cluster_files):
  aid_set = set()

  for cluster_file in cluster_files:
    f = open(cluster_file)
    for l in f:
      tmp = l.split(",")[0:2]
      aid_set.add(tmp[0])
      aid_set.add(tmp[1])
    f.close()

  hashind2airport = load_hash2airport(airports_dat_file, conv_airlines_file)
  max_cid = 0
  country2cid = {}

  print "var airports = {};\n"
  for aid in aid_set:
    airport = hashind2airport[aid]
    if airport.country not in country2cid:
      cid = max_cid
      country2cid[airport.country] = max_cid
      max_cid += 1
    else:
      cid = country2cid[airport.country]

    print "airports['%s-%d'] = {center: new google.maps.LatLng(%.6lf, %.6lf), com: %s};" %(
      airport.code3,
      cid,
      airport.lat,
      airport.lng,
      cid)

if __name__ == "__main__":
  from sys import argv
  main(argv[1], argv[2], *argv[3:])


