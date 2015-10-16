"""
@San-Chuan Hung

gen_page.py reads the directory of airport location js files, and then generate html files
to show the locations on Google map. It will generate cluster_${id}.html for each cluster,
and also a index.html connecting to all cluster_${id}.html pages.

Command:

python gen_page.py ${airport_json_directory} ${google_api_id}

Example:

python gen_page.py out/ AIzaSyD3xACEruO96pXttoYtYtNKn52E2-K4zE0
"""

import os
import sys

GoogleAPI_ID = sys.argv[2]

template = """
<!--
The following code is modified from "KDD submission", whose origin author is Pedro Ribeiro.
-->
<!DOCTYPE html>
<html>
  <head>
    <title>Taboo-Decomposition</title>
    <link rel="stylesheet" type="text/css" href="layout.css">
    <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=%s"></script>
    <script type="text/javascript" src="%s"></script>
    <script type="text/javascript" src="init.js"></script>
  </head>
  <body>
    <!-- The element that will contain our Google Map. This is used in both the Javascript and CSS above. -->
    <div id="map"></div>
    <div id="title">
      <h1>Taboo-Decomposition Cluster %d</h1>
    </div>
  </body>
</html>
"""

for i, filename in enumerate(os.listdir(sys.argv[1])):
  js_path = sys.argv[1] + "/" + filename
  out_filename = "cluster_%d.html" % i
  outf = open(out_filename, "w")
  print >>outf, template % (GoogleAPI_ID, js_path, i)
  outf.close()

index_template = """
<!DOCTYPE html>
<html>
  <head>
    <title>Taboo-Decomposition</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  </head>
  <body>
    <h1>Taboo-Decomposition Cluster</h1>
    <ul>
    %s
    </ul>
  </body>
</html>
"""

outf = open("index.html", "w")
href_array = []
num_pages = len(os.listdir(sys.argv[1]))
href_html = "\n".join(
  map(lambda x: "<li><a href='cluster_%d.html'>cluster %d</a></li>" % (x, x),range(num_pages)))
print >> outf, index_template % href_html
outf.close()


