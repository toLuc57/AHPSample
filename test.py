import itertools
import pytest

from ahpy import ahpy

price_comparisons = {('mobie1', 'mobie2'): 3/2, ('mobie1', 'mobie3'): 4/3, 
          ('mobie2', 'mobie3'): 3/2}

storage_comparisons = {('mobie1', 'mobie2'): 5/4, ('mobie1', 'mobie3'): 4/3, 
          ('mobie2', 'mobie3'): 3/2}

camera_comparisons = {('mobie1', 'mobie2'): 5/4, ('mobie1', 'mobie3'): 3/2, 
          ('mobie2', 'mobie3'): 5/3}

look_comparisons = {('mobie1', 'mobie2'): 9/7, ('mobie1', 'mobie3'): 7/5, 
          ('mobie2', 'mobie3'): 5/3}

criteria_comparisons = {('Price', 'Storage'): 5, ('Price', 'Camera'): 4, ('Price', 'Look'): 7,
          ('Storage', 'Camera'): 1/2, ('Storage', 'Look'): 3,
          ('Camera', 'Look'): 3}

price = ahpy.Compare('Price', price_comparisons, precision=3, random_index='saaty')
storage = ahpy.Compare('Storage', storage_comparisons, precision=3, random_index='saaty')
camera = ahpy.Compare('Camera', camera_comparisons, precision=3, random_index='saaty')
look = ahpy.Compare('Look', look_comparisons, precision=3, random_index='saaty')
criteria = ahpy.Compare('Criteria', criteria_comparisons, precision=3, random_index='saaty')

criteria.add_children([price, storage, camera, look])

report = criteria.report(show=True)