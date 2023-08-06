import pandas as pd
import os
from scipy.spatial import cKDTree
import pickle
from tqdm import tqdm
tqdm.pandas()


from glam.utils import utils
from glam.matching.embedded._model import make_embeddings


def upgrade_linz(linz_path, outpath, pc_path = None):
    """
    
    """

    linz = utils.load_linz(linz_path)
    linz['suburb_town_city'] = (linz['suburb_locality_ascii'].fillna('') + ', ' + linz['town_city_ascii'].fillna(''))
    linz['suburb_town_city'] = linz['suburb_town_city'].str.replace('^, |, $', '', regex=True) # remove leading and trailing commas and spaces

    # join on postcodes 
    if pc_path is not None:
        pass

    argmap = {
        'first_number' : 'address_number',
        'street_name' : 'full_road_name_ascii',
        'suburb_town_city' : 'suburb_town_city',
        'postcode' : 'POSTCODE',
    }

    embedding_combinations = [
        [
            'first_number',
            'street_name',
            'suburb_town_city',
            # 'postcode'
        ],
        # [
        #     'first_number',
        #     'street_name',
        #     'suburb_town_city',
        # ],
        [
            'first_number',
            'street_name'
        ]
    ]

    for i, embedding_combination in enumerate(embedding_combinations):
        print(f'building tree {i+1}/{len(embedding_combinations)}...')
        embeddings = linz.progress_apply(lambda x: make_embeddings(
                {ac : x[argmap[ac]] for ac in embedding_combination}
            ), axis=1
        )

        tree = cKDTree(embeddings.to_list())    

        pickle_loc = os.path.join(outpath,f'tree{i}.pkl')
        pickle.dump(tree,open(pickle_loc,'wb'))

    