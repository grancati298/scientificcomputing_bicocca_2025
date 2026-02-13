import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cycler
from functools import wraps

def myplot(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d', '#666666']
        styles = ['-', '--', ':', '-.'] * 2
        markers = ['o', 's', '^', 'D', '*', 'p', 'h', 'v']

        my_cycler = (cycler(color=colors[:8]) + cycler(linestyle=styles[:8]) + cycler(marker=markers[:8]))

        xlab = kwargs.pop('xlabel', None)
        ylab = kwargs.pop('ylabel', None)
        title = kwargs.pop('title', None)
        xsc = kwargs.pop('xscale', None)
        ysc = kwargs.pop('yscale', None)

        plt.rcParams.update({
            'figure.figsize': (8, 8),
            'figure.dpi': 100,
            
            'axes.prop_cycle': my_cycler,
            'axes.labelsize': 14,
            'axes.labelpad': 12,
            
            'lines.linewidth': 2,
            'lines.markersize': 7,
            
            'legend.frameon': True,
            'legend.framealpha': 0.8,
            'legend.fancybox': True,
            'legend.edgecolor': '0.8',

            'font.family': 'serif',
            'axes.labelsize': 14,
            'xtick.labelsize': 12,
            'ytick.labelsize': 12,
        })

        fig = func(*args, **kwargs)

        for ax in fig.get_axes():
            if xlab: ax.set_xlabel(xlab)
            if ylab: ax.set_ylabel(ylab)
            if title: ax.set_title(title)
            if xsc: ax.set_xscale(xsc)
            if ysc: ax.set_yscale(ysc)
        
        filename = f"{func.__name__}.pdf"
        fig.savefig(filename, format='pdf', bbox_inches='tight')
        plt.show()
        plt.close(fig)
        
        return fig
    return wrapper
