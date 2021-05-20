from worldmap.worldmap import (
    plot,
    code2county,
    county2code,
    list_county_names,
    list_map_names,
    )

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '0.1.7'

# module level doc-string
__doc__ = """
worldmap
=====================================================================

Description
-----------
worldmap is to plot and color countries or specific regions in a country using offline approaches.

Example
-------
>>> import worldmap
>>> county_names = ['zeeland','Overijssel', 'flevoland']
>>> opacity = [0.4, 0.6, 0.9]
>>> out = worldmap.plot(county_names,opacity=opacity, cmap='Set1', map_name='netherlands', filename='Netherlands_map.svg')

References
----------
* https://github.com/erdogant/worldmap
* http://www.amcharts.com/svg-maps/

"""
