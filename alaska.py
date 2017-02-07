import numpy as np
import matplotlib.pyplot as plt
import giapy as gp

alaska = {'area_thresh': 1000.0,
          'height': 4700000,
          'lat_0': 57,
          'lat_1': 50.0,
          'lat_2': 89.9,
          'lon_0': -144.0,
          'projection': 'aeqd',
          'resolution': 'l',
          'rsphere': (6378137.0, 6356752.3142),
          'width': 4900000}

grid = gp.maps.GridObject(mapparam=alaska)

xs = np.linspace(grid.basemap.xmin, grid.basemap.xmax)
ys = np.linspace(grid.basemap.ymin, grid.basemap.ymax)
Xs, Ys = np.meshgrid(xs, ys)
Lons, Lats = grid.basemap(Xs, Ys, inverse=True)

dx = np.mean(giapy.maps.haversine(Lats[:-1,:-1], Lats[1:,1:],
                                  Lons[:-1,:-1], Lons[1:,1:]))/np.sqrt(2)

fs = np.fft.fftfreq(N, d=dx)


# Load dhdt data

