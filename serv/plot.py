import matplotlib

matplotlib.use('agg') # setup matplotlib in write-only mode

import matplotlib.pyplot as plt
import matplotlib.colors as colors

colors_list = list(colors._colors_full_map.values()) # Obtain color list to preven flickering

from collections import defaultdict


def _transpose(data): # Func forms data for plots
    data.sort(key=lambda x: x['tstamp']) # Sort data by timestamp to avoid inconsistence
    x = [i['tstamp'] for i in data]
    y = defaultdict(list)
    res_y = []
    for item in data:
        for counter in item['data']:
            y[counter['cid']].append(counter['value'])
    for key in sorted(y.keys()):
        res_y.append(y[key])
    return x, res_y


def generate_plot(data, id):
    x, y = _transpose(data)
    for index, p in enumerate(y):
        plt.plot(x, p, c=colors_list[index], label=str(index)) # Plotting obtained dots one point at a time (we have several data points at one tstamp)

    plt.legend()
    plt.grid()

    path = f"img/{id}"
    plt.savefig(path, format='png')
    plt.close()
    return path # Return path to file so it can be returned to user
