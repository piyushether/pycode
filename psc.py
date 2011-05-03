#!/usr/bin/env python
#encoding: utf-8

'''
Useful function for studying PSCs
'''

ID_ALL = 0b1111
ID_STS = 0b0001
ID_NAT = 0b0010
ID_ICE = 0b0100
ID_UNKNOWN = 0b1000

psc_id = {'unknown':ID_UNKNOWN, 'all':ID_ALL, 'STS':ID_STS, 'NAT':ID_NAT, 'Ice':ID_ICE}

def classify_psc_type(r, depol):
    '''
    give a type to a psc layer according to its r and depol coefficients.
    r = ratio between b532 and bmol, with b532 the total volume backscatter and bmol the molecular backscatter
    depol = particle-only depolarization ratio
    (cf Pitts et al 2009)
    '''
    
    if (r >= 4.5) and (depol >= 0.035) and (depol < 0.9):
        psc_type = psc_id['Ice']
    elif (r >= 1.25) and (depol < 0.035) and (depol >= -0.2):
        psc_type = psc_id['STS']
    elif (depol > 0.035) and (depol < 0.9) and (r < 4.5) and (r > 0.8):
        psc_type = psc_id['NAT']
    elif (depol < 0.035) and (depol >= -0.2) and (r < 1.25) and (r > 0.8):
        psc_type = psc_id['NAT']
    else:
        psc_type = psc_id['unknown']
        
    return psc_type

def _plot_type_colors():
    colors = ['#000033', '#0000FF', '#00FF00', '#FF0000']
    return colors

def plot_type_cmap():
    from matplotlib.colors import ListedColormap
    colors = _plot_type_colors()
    cmap = ListedColormap(colors)
    return cmap
    
def plot_type_legend():
    from matplotlib.patches import Rectangle
    import matplotlib.pyplot as plt
    colors = _plot_type_colors()
    liste_rec = [Rectangle((0, 0), 1, 1, fc=color) for color in colors]
    labels = [types[i] for i in types]
    plt.legend(liste_rec, labels)