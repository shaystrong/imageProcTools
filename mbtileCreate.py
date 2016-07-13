import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import logging
from landez import MBTilesBuilder
from landez import ImageExporter
from landez import GoogleProjection
from landez import TilesManager,TileDownloader
from landez import ImageExporter
from PIL import Image, ImageEnhance
from cStringIO import StringIO
from landez.sources import MBTilesReader
from numpy import array
import os, glob, time, re, sys
import argparse

# Use:
#    python mbtileCreate.py --llong -97.321757 --llat 32.847790 --ulong -97.318813 --ulat 32.854694 --zoom 21 --mbtilePath "/Data/collect_zoom21.mbtiles"
#    

#Uses 'MBTilesBuilder' function to download imagery at a specified zoom level and create an mbtiles file. Provide bounding box.

#MBTilesBuilder
#Keyword arguments:
#        cache -- use a local cache to share tiles between runs (default True)
#        tiles_dir -- Local folder containing existing tiles if cache is
#                     True, or where temporary tiles will be written otherwise
#                     (default DEFAULT_TMP_DIR)
#        tiles_url -- remote URL to download tiles (*default DEFAULT_TILES_URL*)
#        tiles_headers -- HTTP headers to send (*default empty*)
#        stylefile -- mapnik stylesheet file (*to render tiles locally*)
#        mbtiles_file -- A MBTiles file providing tiles (*to extract its tiles*)
#        wms_server -- A WMS server url (*to request tiles*)
#        wms_layers -- The list of layers to be requested
#        wms_options -- WMS parameters to be requested (see ``landez.reader.WMSReader``)
#        tile_size -- default tile size (default DEFAULT_TILE_SIZE)
#        tile_format -- default tile format (default DEFAULT_TILE_FORMAT)


parser = argparse.ArgumentParser()
parser.add_argument('--ulong', '-ulo', help="bounding box, upper longitude value")
parser.add_argument('--ulat', '-ula', help="bounding box, upper latitude value")
parser.add_argument('--llong', '-llo', help="bounding box, lower longitude value")
parser.add_argument('--llat', '-lla', help="bounding box, lower latitude value")
parser.add_argument('--zoom', '-z', help="zoom levels")
parser.add_argument('--mbtilePath', '-p',help="where to put the mbtile file")
parser.add_argument('--url', '-p',help="full api call/url to server")

args = parser.parse_args()

ulong=args.ulong
ulat=args.ulat
llong=args.llong
llat=args.llat
zoom=args.zoom
mbtilePath=args.mbtilePath

logging.basicConfig(level=logging.DEBUG)

mb = MBTilesBuilder(cache=False,tiles_url=urlMe,filepath=mbtilePath)   #really only seems to be jpeg or png options
mb.add_coverage(bbox=(float(llong),float(llat),float(ulong),float(ulat)),zoomlevels=[int(zoom)])          
mb.run(force=True)

