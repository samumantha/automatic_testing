#!/usr/bin/env python

allas_bucket = ''
rasterfile = ''
# raster and shape need to overlap
vectorfile_shp = '/appl/data/geo/syke/asuinalueet1990/PientaloAlue90.shp'
vectorfile_gpkg = '/appl/data/geo/mml/maastotietokanta/2020/gpkg/MTK-muut_20-02-06.gpkg'
layer = "hylky"
pointcloudfile = '/appl/data/geo/mml/laserkeilaus/2008_latest/2018/W444/1/W4444G4.laz'
csvfile = ''

## ArcGIS: tools for sophisticated vector and raster analysis, geocoding, map making, routing and directions

import arcgis
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

# -> test_dask.py
# done

####################

## Descartes: use Shapely or GeoJSON-like geometric objects as matplotlib paths and patches

#-> test_descartes_shapely.py

####################

## Geoalchemy: working with spatial databases, primarily PostGIS

import geoalchemy2

#done

####################

## imblearn

#-> test_imbalanced_sk.py
# done

####################

## geopandas: extends the datatypes used by pandas.

import geopandas as gpd

gpd.read_file(vectorfile_gpkg, layer=layer)
#done

####################

## laspy

import laspy

#might need las?
las = laspy.read(pointcloudfile)

new_file = laspy.create(point_format=las.header.point_format, file_version=las.header.version)
new_file.points = las.points[las.classification == 1]

# done

####################

## laxpy 

import laxpy
# done

####################

## lxml

# -> test_lxml.py
# done

####################

## natsort
from natsort import natsorted, ns
a = ['2 ft 7 in', '1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '7 ft 6 in']
natsorted(a)
#done

####################

## netcdf

import netcdf4
#done

####################

## networkx: creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

import networkx as nx

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
# done

####################

## pyproj: performs cartographic transformations and geodetic computations.

from pyproj import CRS

CRS.from_epsg(4326)
# done

####################

## osmnx: download spatial geometries and construct, project, visualize, and analyze street networks from OpenStreetMap's APIs

import osmnx as ox

# get the boundary polygon for manhattan, project it, and plot it
city = ox.geocode_to_gdf("Manhattan, New York, USA")
city_proj = ox.project_gdf(city)

#done

####################

## pysal: spatial analysis functions. 

import pysal as ps

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

#done

####################

## qgis: GIS applications

import qgis

# done

####################

## rasterio: access to geospatial raster data.

import rasterio
with rasterio.open(rasterfile) as dataset:
    print(dataset.name)

# done

####################

## rasterstats: summarizing geospatial raster datasets based on vector geometries.

from rasterstats import zonal_stats
zonal_stats(vectorfile_shp, rasterfile,
            stats="count min mean max median")
#done

####################

## rtree: spatial indexing and search.

import rtree

## shapely: manipulation and analysis of geometric objects in the Cartesian plane.

#-> test_descartes_shapely.py

## scikit: machine learning for Python and algorithms for image processing

#-> test_imbalanced_sk.py
# done

## xarray: for multidimensional raster data.

import xarray

## sentinelsat:downloading Sentinel images

import sentinelsat

## joblib

import joblib

#-> https://github.com/csc-training/geocomputing/blob/master/python/puhti/04_parallel_joblib/joblib_example.py


## osgeo

from osgeo import ogr

data = ogr.Open(vectorfile_gpkg)

## fiona

import fiona

fiona.open(vectorfile_gpkg,layer=layer)


## gmt

import gmt

####################

## Allas tools

import boto3

s3 = boto3.client("s3", endpoint_url='https://a3s.fi')
s3.list_objects_v2(Bucket='name_of_your_Allas_bucket')['Contents']

####################

import python-keystoneclient
import python-swiftclient
