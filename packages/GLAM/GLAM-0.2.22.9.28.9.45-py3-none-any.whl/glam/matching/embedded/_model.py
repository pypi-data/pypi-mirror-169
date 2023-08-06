import numpy as np
import re

# one cycle of allowing letters to appear once (unless outvoted by two new letters) - ordered by evenness of binary splits
default_letter_groups = [
    'bqt',
    'lwz',
    'ipx',
    'jlm',
    'psv',
    'chw',
    'kuy',
    'bdf',
    'gjn',
    'oqr',
    'jor',
    'dlt',
    'lrt',
    'bfz',
    'alx',
    'egl',
]

#completing two cycles of letters only being allowed to appear once (unless outvoted by two new letters) - ordered by range in count splits
default_letter_groups = [
    'dio',
    'rst',
    'cel',
    'nou',
    'adh',
    'ikv',
    'gjt',
    'lmy',
    'ipw',
    'bft',
    'nqz',
    'jnz',
    'ptv',
    'hop',
    'dkt',
    'bnx', # one cylce
    'bnz',
    'tvx',
    'fiz',
    'cgw',
    'cdu',
    'kow',
    'jlp',
    'epr',
    'alq',
    'bsy',
    'djl',
    'dlq',
    'hnp',
    'kmo',
 ]

# allowing letters to appear twice (unlesss outvoted by two new letters) - ordered by range in count splits
default_letter_groups = [
    'dio',
    'rst',
    'dno',
    'irt',
    'nos',
    'cel',
    'cls',
    'env',
    'adh',
    'adk',
    'iuv',
    'htu',
    'gjt',
    'gik',
    'djm',
    'lmy',
    'lwy',
    'ipw',
    'pqt',
    'bft',
    'bfi',
    'nqz',
    'nxz',
    'dlx',
]

default_letter_groups = [set(lg) for lg in default_letter_groups]

default_weights = {
    'first_number' : 10,
    'street_name' : 5,
    'suburb_town_city' : 1,
    'postcode' : 10
}


def make_embeddings(address_components, letter_groups = default_letter_groups, weights = default_weights):
    
    embeddings = []
    if address_components.get('first_number', 'None') != "None":
        embeddings.append(weights['first_number']*np.log(int(address_components['first_number'])))

    if address_components.get('street_name','None') != "None":
        embeddings += [weights['street_name']*(len(set(address_components['street_name'].lower()).intersection(lg))) for lg in letter_groups]

    if address_components.get('suburb_town_city','None') != "None":
        embeddings += [weights['suburb_town_city']*(len(set(address_components['suburb_town_city'].lower()).intersection(lg))) for lg in letter_groups]

    if address_components.get('postcode','None') != "None":
        embeddings.append(weights['postcode']*np.log(int(address_components['postcode'])))

    return embeddings

def make_embeddings_old(address_components, letter_groups = default_letter_groups):
    
    embeddings = []
    if 'first_number' in address_components:
        if len(address_components['first_number']) > 0:
            embeddings.append(np.log(int(address_components['first_number'])))

    if 'street_name' in address_components:
        embeddings += [len(re.sub(f'[^{lg}]','', address_components['street_name'], re.IGNORECASE)) for lg in letter_groups]

    if 'suburb_town_city' in address_components:
        embeddings += [len(re.sub(f'[^{lg}]','', address_components['suburb_town_city'], re.IGNORECASE)) for lg in letter_groups]

    if 'postcode' in address_components:
        if len(address_components['postcode']) > 0:
            embeddings.append(np.log(int(address_components['postcode'])))

    return embeddings

