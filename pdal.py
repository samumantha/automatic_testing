"""
Example from: https://github.com/PDAL/python
01.12.2021
"""

import pdal

data = "https://github.com/PDAL/PDAL/blob/master/test/data/las/1.2-with-color.las?raw=true"

pipeline = pdal.Reader.las(filename=data).pipeline()
print(pipeline.execute())  # 1065 points

# Get the data from the first array
# [array([(637012.24, 849028.31, 431.66, 143, 1,
# 1, 1, 0, 1,  -9., 132, 7326, 245380.78254963,  68,  77,  88),
# dtype=[('X', '<f8'), ('Y', '<f8'), ('Z', '<f8'), ('Intensity', '<u2'),
# ('ReturnNumber', 'u1'), ('NumberOfReturns', 'u1'), ('ScanDirectionFlag', 'u1'),
# ('EdgeOfFlightLine', 'u1'), ('Classification', 'u1'), ('ScanAngleRank', '<f4'),
# ('UserData', 'u1'), ('PointSourceId', '<u2'),
# ('GpsTime', '<f8'), ('Red', '<u2'), ('Green', '<u2'), ('Blue', '<u2')])
arr = pipeline.arrays[0]

# Filter out entries that have intensity < 50
intensity = arr[arr["Intensity"] > 30]
print(len(intensity))  # 704 points

# Now use pdal to clamp points that have intensity 100 <= v < 300
pipeline = pdal.Filter.range(limits="Intensity[100:300)").pipeline(intensity)
print(pipeline.execute())  # 387 points
clamped = pipeline.arrays[0]

# Write our intensity data to a LAS file and a TileDB array. For TileDB it is
# recommended to use Hilbert ordering by default with geospatial point cloud data,
# which requires specifying a domain extent. This can be determined automatically
# from a stats filter that computes statistics about each dimension (min, max, etc.).
pipeline = pdal.Writer.las(
    filename="clamped.las",
    offset_x="auto",
    offset_y="auto",
    offset_z="auto",
    scale_x=0.01,
    scale_y=0.01,
    scale_z=0.01,
).pipeline(clamped)
pipeline |= pdal.Filter.stats() | pdal.Writer.tiledb(array_name="clamped")
print(pipeline.execute())  # 387 points
