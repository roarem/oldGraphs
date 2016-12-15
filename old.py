import matplotlib as mpl
mpl.rc('text',usetex=True)
mpl.rcParams['legend.numpoints']=1
mpl.rcParams['font.size'] = 30
mpl.rcParams['font.weight']   = 'bold'
mpl.rcParams['text.latex.preamble']=[r'\usepackage{bm} \boldmath']
from matplotlib import ticker
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
from scipy.optimize import curve_fit
import ROOT


def fig1():
    fig1al_nf   = [2.18, 2.15, 2.18, 2.4,  3.05, 3.2, 3.29, 3.3, 3.2,  2.98, 2.75]
    fig1al_nb   = [0,    0.5,  1,    2.25, 5.25, 6,   7,    7.5, 8.12, 9,    10]
    fig1as_nf   = [2.05,2.15,2.4,2.6,2.85,3,3.2,3.3,3.4,3.5,3.4,2.8,2.65]
    fig1as_nb   = [0.1,1.75,2.25,3.25,4.25,5.25,6,7.25,8.25,9.5,10.15,11,12.15]
    fig1as_yerr = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.4,0.5,0.9,1]
    fig1ah_nf   = [2.4,2.8,3.1]
    fig1ah_nb   = [1.25,3.25,5.25]
    
    fig1al_nb_new = np.linspace(fig1al_nb[0],fig1al_nb[-1],100)
    smooth1 = spline(fig1al_nb,fig1al_nf,fig1al_nb_new)

    fig1bl_nf   = [2.60, 2.06, 2.06, 2.45, 2.45, 2.25, 2.45, 2.57, 2.63, 2.65, 2.67, 2.69, 2.69 ]
    fig1bl_nb   = [0.32, 1.20, 1.23, 1.99, 2.01, 3,    4,    5.1,  6.2,  7.1,  8,    9.09, 9.1]

    fig1bs_nf   = [2.6,2.05,2.4,2.25,2.5,2.65,2.75,2.87,2.79,2.83]
    fig1bs_nb   = [0.1,1.2, 2,  3,   4,  5.1, 6.2, 7.1, 8,   9.1]

    fig1bs_yerr = [0.1,0.1,0.1,0.1,0.1,0.1,0.2,0.4,0.57,1.1]
    fig1bh_nf   = [2.2,2.53,2.75]
    fig1bh_nb   = [1.2,3,5.1]

    fig1bl_nb_new = np.linspace(fig1bl_nb[0],fig1bl_nb[-1],100)
    smooth2 = spline(fig1bl_nb,fig1bl_nf,fig1bl_nb_new)

    fig,axs = plt.subplots(1,2,sharey=True,figsize=(5,5))
    fig.subplots_adjust(wspace=0)
    DPI = fig.get_dpi()
    fig.set_size_inches(2000/DPI,1000/DPI)

    for ax in axs:
        ax.set_xlim([-1,13])
        ax.set_ylim(1.5,4)
        [ylabel.set_visible(False) for ylabel in ax.get_yticklabels()]
        [ylabel.set_fontsize(40) for ylabel in ax.get_yticklabels()]
        [xlabel.set_fontsize(40) for xlabel in ax.get_xticklabels()]
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
        ax.xaxis.set_tick_params(which='major',length=14,width=2)
        ax.yaxis.set_tick_params(which='major',length=14,width=2)
        ax.xaxis.set_tick_params(which='minor',length=8 ,width=2)
        ax.yaxis.set_tick_params(which='minor',length=8 ,width=2)

        ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
        ax.get_xticklabels()[-1].set_visible(False)
    [ylabel.set_visible(True) for ylabel in axs[0].get_yticklabels()[2:-2:2]]

    markcolor = 'blue'
    linecolor = 'red'
    linewidth = 4
    markersize= 18

    axs[0].plot(fig1al_nb_new,smooth1,linewidth=linewidth,color=linecolor,
                label='QGSM')
    axs[0].plot(fig1ah_nb,fig1ah_nf,marker='o',linestyle='',color='green',
                markersize=markersize,label='nondiffractive')
    axs[0].text(11,3.8,'a)')
    axs[0].errorbar(fig1as_nb,fig1as_nf,fig1as_yerr,
                    marker='o',linestyle='',color=markcolor,
                    markersize=markersize,label='inelastic')

    axs[1].plot(fig1bl_nb_new,smooth2,linewidth=linewidth,color=linecolor,
                label='QGSM')
    axs[1].plot([],[],linestyle='',label='Experimental:')
    axs[1].plot(fig1bh_nb,fig1bh_nf,marker='o',linestyle='',color='green',
                markersize=markersize,label='nondiffractive')
    axs[1].text(11,3.8,'b)')
    axs[1].errorbar(fig1bs_nb,fig1bs_nf,fig1bs_yerr,
                    marker='o',linestyle='',color=markcolor,
                    markersize=markersize,label='inelastic')
    fig.text(0.50,0.02,'$n_B$',ha='center',size=40)
    fig.text(0.1,0.92,r'$\langle n_F \rangle$',ha='center',size=40)
    plt.legend(loc='best',frameon=False)
    #plt.show()
    fig.savefig('fig1.pdf', bbox_inches='tight')

def fig4():
    fig4a_nf   = [2.9,2.9,2.8,2.7,2.59,2.42,2.53,2.4,2.7]
    fig4a_nb   = [0,1,2,3,4,5,6,7,8]
    fig4a_yerr = [0,0,0,0,0,0,0.1,0.1,0.1]

    fig4b_nf   = [1.7,1.95,1.79,1.73,1.8,2,1.98]
    fig4b_nb   = [0,1,2,3,4,5,6]
    fig4b_yerr = [0,0,0,0.5,1,1.5,2]

    fig4c_nf   = [1.59,1.25,1]
    fig4c_nb   = [1,3,5]
    fig4c_yerr = [0,0.2,0.4]

    fig4d_nf   = [3.7,4,4.1,3.93,3.96,3.91,3.82,3.83,3.3]
    fig4d_nb   = [0,1,2,3,4,5,6,7,8]
    fig4d_yerr = [0.05,0.2,0.1,0.1,0.1,0.1,0.13,0.13,0.13]

    fig4e_nf   = [1.95,2,2.05,2.08,2.05,2.19,2.16]
    fig4e_nb   = [0,1,2,3,4,5,6]
    fig4e_yerr = [0.1,0.03,0.03,0.03,0.1,0.22,0.3]

    fig4_nf = [fig4a_nf,fig4b_nf,fig4c_nf,fig4d_nf,fig4e_nf]
    fig4_nb = [fig4a_nb,fig4b_nb,fig4c_nb,fig4d_nb,fig4e_nb]
    fig4_yerr = [fig4a_yerr,fig4b_yerr,fig4c_yerr,fig4d_yerr,fig4e_yerr]

    height_ratios = [1,1,1,1,1]
    fig, axs = plt.subplots(5,1,sharex=True,figsize=(5,5),gridspec_kw={'height_ratios':height_ratios})
    fig.subplots_adjust(hspace=0)
    DPI = fig.get_dpi()
    fig.set_size_inches(1000/DPI,2000/DPI)
    ylimits = [[2.2,3.2],[1.6,2.2],[0.6,1.8],[3,4.2],[1.6,2.4]]
    labels = ['a)','b)','c)','d)','e)']
    texts  = ['cylindrical','undeveloped\ncylinder','diffraction\ndiagrams','annihilation','planar']
    fig.text(0.5,0.06,'$n_B$',ha='center',size=40)
    fig.text(0.1,0.91,r'$\langle n_F \rangle$',ha='center',size=40)

    for i,ax in enumerate(axs):
        ax.set_ylim(ylimits[i])
        ax.set_xlim([-1,10])
        [ylabel.set_visible(False) for ylabel in ax.get_yticklabels()]
        [ylabel.set_fontsize(40) for ylabel in ax.get_yticklabels()]
        [xlabel.set_fontsize(40) for xlabel in ax.get_xticklabels()]
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
        ax.xaxis.set_tick_params(which='major',length=14,width=2)
        ax.yaxis.set_tick_params(which='major',length=14,width=2)
        ax.xaxis.set_tick_params(which='minor',length=8,width=2)
        ax.yaxis.set_tick_params(which='minor',length=8,width=2)
        ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))

    #  a
    axs[0].errorbar(fig4_nb[0],fig4_nf[0],fig4_yerr[0],
                marker='o',linestyle='',
                markersize='14', color='black')
    [ylabel.set_visible(True) for ylabel in axs[0].get_yticklabels()[2:-2:2]]
    axs[0].text(8.2,ylimits[0][1]-0.19,labels[0])
    axs[0].text(7.4,ylimits[0][1]-0.31,texts[0])

    #   b
    axs[1].errorbar(fig4_nb[1],fig4_nf[1],fig4_yerr[1],
                marker='o',linestyle='',
                markersize='14', color='black')
    [ylabel.set_visible(True) for ylabel in axs[1].get_yticklabels()[2:-2]]
    axs[1].text(7.7,ylimits[1][1]-0.25,labels[1])
    axs[1].text(7.0,ylimits[1][1]-0.4,texts[1])


    #  c 
    axs[2].errorbar(fig4_nb[2],fig4_nf[2],fig4_yerr[2],
                marker='o',linestyle='',
                markersize='14', color='black')
    [ylabel.set_visible(True) for ylabel in axs[2].get_yticklabels()[2:-1:2]]
    axs[2].text(8,ylimits[2][1]-0.44,labels[2])
    axs[2].text(7.3,ylimits[2][1]-0.75,texts[2])

    #  d 
    axs[3].errorbar(fig4_nb[3],fig4_nf[3],fig4_yerr[3],
                marker='o',linestyle='',
                markersize='14', color='black')
    [ylabel.set_visible(True) for ylabel in axs[3].get_yticklabels()[2:-1:2]]
    axs[3].text(8,ylimits[3][1]-0.28,labels[3])
    axs[3].text(7.3,ylimits[3][1]-0.45,texts[3])


    #  e 
    axs[4].errorbar(fig4_nb[4],fig4_nf[4],fig4_yerr[4],
                marker='o',linestyle='',
                markersize='14', color='black')
    [ylabel.set_visible(True) for ylabel in axs[4].get_yticklabels()[2:-1:2]]
    axs[4].text(8,ylimits[4][1]-0.25,labels[4])
    axs[4].text(7.5,ylimits[4][1]-0.35,texts[4])

    #plt.show()
    fig.savefig('fig4.pdf', bbox_inches='tight')

fig1()
fig4()
