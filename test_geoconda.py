#!/usr/bin/env python

allasbucket = 'gis_courses'
rasterfile = '/appl/data/geo/landsat/lsm_19850715_sr_b1.tif'
# raster and shape need to overlap
vectorfile_shp = '/appl/data/geo/syke/asuinalueet1990/PientaloAlue90.shp'
vectorfile_gpkg = '/appl/data/geo/mml/maastotietokanta/2020/gpkg/MTK-muut_20-02-06.gpkg'
layer = "hylky"
pointcloudfile = '/appl/data/geo/mml/laserkeilaus/2008_latest/2018/W444/1/W4444G4.laz'

## ArcGIS: tools for sophisticated vector and raster analysis, geocoding, map making, routing and directions

import arcgis
print(arcgis.__version__)
# done

####################

## Cartopy: for map plotting

#-> cartopy.py
# done

####################

## Dask: advanced parallelism for analytics, enabling performance at scale

import dask
import dask-ml
import dask-labextension

print(dask.__version__)
# -> test_dask.py
# done

####################

## Descartes: use Shapely or GeoJSON-like geometric objects as matplotlib paths and patches

#-> test_descartes_shapely.py

####################

## Geoalchemy: working with spatial databases, primarily PostGIS

import geoalchemy2
print(geoalchemy2.__version__)
#done

####################

## imblearn

#-> test_imbalanced_sk.py
# done

####################

## geopandas: extends the datatypes used by pandas.

import geopandas as gpd
print(gpd.__version__)
gpd.read_file(vectorfile_gpkg, layer=layer)
#done

####################

## laspy

import laspy

print(laspy.__version__)
#might need las?
las = laspy.read(pointcloudfile)

new_file = laspy.create(point_format=las.header.point_format, file_version=las.header.version)
new_file.points = las.points[las.classification == 1]

# done

####################

## laxpy 

import laxpy
print(laxpy.__version__)
# done

####################

## lxml

# -> test_lxml.py
# done

####################

## natsort
from natsort import natsorted, ns
print(natsorted.__version__)
a = ['2 ft 7 in', '1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '7 ft 6 in']
natsorted(a)
#done

####################

## netcdf

import netcdf4
print(netcdf4.__version__)
#done

####################

## networkx: creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

import networkx as nx

print(nx.__version__)
G = nx.Graph()

nx.add_path(G, [1, 2, 3])
nx.add_path(G, [4, 2, 5])
# done

####################

## pdal:  for lidar data

#-> test_pdal.py
# done

####################

## cdo: scripting interface to climate data operator

import cdo
print(cdo.__version__)
# done

####################

## pyproj: performs cartographic transformations and geodetic computations.

from pyproj import CRS
print(CRS.__version__)
CRS.from_epsg(4326)
# done

####################

## osmnx: download spatial geometries and construct, project, visualize, and analyze street networks from OpenStreetMap's APIs

import osmnx as ox
print(ox.__version__)
# get the boundary polygon for manhattan, project it, and plot it
city = ox.geocode_to_gdf("Manhattan, New York, USA")
city_proj = ox.project_gdf(city)

#done

####################

## pysal: spatial analysis functions. 

import pysal as ps
print(ps.__version__)
ps.open(vectorfile_shp)
#done


####################

## igraph: for fast routing.

import igraph

print(igraph.__version__)
g = Graph()
g.add_vertices(3)
g.add_edges([(0,1), (1,2)])

#done

####################


## wget: download stuff

import wget
print(wget.__version__)
#done

####################

## qgis: GIS applications

import qgis
print(qgis.__version__)
# done

####################

## rasterio: access to geospatial raster data.

import rasterio
print(rasterio.__version__)
with rasterio.open(rasterfile) as dataset:
    print(dataset.name)

# done

####################

## rasterstats: summarizing geospatial raster datasets based on vector geometries.

from rasterstats import zonal_stats
print(zonal_stats.__version__)
zonal_stats(vectorfile_shp, rasterfile,
            stats="count min mean max median")
#done

####################

## rtree: spatial indexing and search.

import rtree
print(rtree.__version__)
## shapely: manipulation and analysis of geometric objects in the Cartesian plane.

#-> test_descartes_shapely.py

## scikit: machine learning for Python and algorithms for image processing

#-> test_imbalanced_sk.py
# done

## xarray: for multidimensional raster data.

import xarray
print(xarray.__version__)

## sentinelsat:downloading Sentinel images

import sentinelsat
print(sentinelsat.__version__)

## joblib

import joblib
print(joblib.__version__)
#-> https://github.com/csc-training/geocomputing/blob/master/python/puhti/04_parallel_joblib/joblib_example.py


## osgeo

from osgeo import ogr
print(ogr.__version__)
data = ogr.Open(vectorfile_gpkg)

## fiona

import fiona
print(fiona.__version__)
fiona.open(vectorfile_gpkg,layer=layer)


## gmt

import gmt
print(gmt.__version__)
####################

## Allas tools

import boto3
print(boto3.__version__)
s3 = boto3.client("s3", endpoint_url='https://a3s.fi')
s3.list_objects_v2(Bucket=allasbucket)['Contents']

####################

import python-keystoneclient
import python-swiftclient
print(python-keystoneclient.__version__)
print(python-swiftclient.__version__)
