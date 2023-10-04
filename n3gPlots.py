import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import matplotlib.font_manager as fontmg
from matplotlib.ticker import ScalarFormatter, FixedLocator, FuncFormatter

def plottingImg(fileName, delimiterChar, numSkipRows, axisXLabel, axisYLabel, numYColums = 4, fontSize = 22, columnLabel=["a","b"], xLims=[0,1], yLims=[0,1], customTicksLim=[0,1]):
  # Importing the data from a file
  data = np.loadtxt(fileName, delimiter = delimiterChar, skiprows = numSkipRows)

  # Extract the data columns from the loaded data
  x = data[:, 0]
  # Separating x and y data for clearness
  y = [0] * numYColums
  yerr = [0] * numYColums;
  for i in range(1, numYColums+1):
    y[i-1] = data[:, i]
    yerr[i-1] = 0.1 #If there are error bars yerr[i-1] = data[:, i+numYColums]

  # Configurations of the plot
  font = {'fontname':'Liberation Sans'}
  # Create a figure and axes object
  fig, ax = plt.subplots(figsize=(7, 7))
  # Set the axis labels and title
  ax.set_xlabel(axisXLabel, loc='right', **font, fontsize = fontSize, fontweight="bold")
  ax.set_ylabel(axisYLabel, loc='top', **font, fontsize = fontSize, fontweight="bold")
  #color list
  colorList = ["#000000","#FF0000","#FFD23F","#266DD3","#E0ACD5","#CC00CC","#9999FF","#339933"]

  # Adding data to the graphics
  for i in range (0, numYColums):
    ax.errorbar(x, y[i], yerr = yerr[i], fmt='-s', markersize = 5, label = columnLabel[i], color = colorList[i] )

  # Add legend in the top right corner
  fontDef = fontmg.FontProperties(family="Liberation Sans", size=18)
  ax.legend(loc='upper left', prop=fontDef)

  #Axis
  ax.set_xscale("log")
  ax.set_yscale("log")
  ax.minorticks_on()
  ax.tick_params(direction='in',which="both", size=8, labelsize=20)
  ax.grid(which='Major', axis='both',color="#EDEDED")
  ax.grid(which='Minor', axis='both',color="#EDEDED")
  # Limits
  ax.set_xlim(xLims[0], xLims[1])
  ax.set_ylim(yLims[0], yLims[1])
  # Ticks formating
  ax.xaxis.set_major_formatter(ticker.NullFormatter())
  ax.xaxis.set_minor_formatter(ticker.NullFormatter())
  custom_ticksx = [customTicksLim[0], customTicksLim[1]]
  ax.xaxis.set_major_locator(FixedLocator(custom_ticksx))
  formatterx = ScalarFormatter(useMathText=True)
  ax.xaxis.set_major_formatter(formatterx)
  formattery = ScalarFormatter(useMathText=True)
  ax.yaxis.set_major_formatter(formattery)
  ax.xaxis.offsetText.set_visible(True)
  ax.yaxis.offsetText.set_visible(False)
  ax.xaxis.offsetText.set_fontsize(20)
  ax.xaxis.offsetText.set_x(1)
  ax.xaxis.offsetText.set(va="bottom")
  # Y-axis
  custom_ticksy = [1,5,10]
  ax.yaxis.set_major_locator(FixedLocator(custom_ticksy))
  def integer_formatter(x, pos):
    return f"{int(x):,}"  # Format the tick value as an integer with comma separation

  # Set the custom formatter for the x-axis tick labels
  ax.yaxis.set_major_formatter(FuncFormatter(integer_formatter))
  plt.show()
  return 1

plottingImg("/content/flux160", ",", 0, "neutrons / cm$^2$", "FWHM (keV)", 4, 22,["seg1","seg2","seg9","seg10"], (3E8, 2E9), (0.9, 11), (5e8, 1e9) )

plottingImg("/content/flux120", ",", 0, "neutrons / cm$^2$", "FWHM (keV)", 4, 22,["seg1","seg2","seg9","seg10"], (3E8, 2E9), (0.9, 11), (5e8, 1e9) )

plottingImg("/content/flux80", ",", 0, "neutrons / cm$^2$", "FWHM (keV)", 4, 22,["seg1","seg2","seg9","seg10"], (3E8, 2E9), (0.9, 11), (5e8, 1e9) )
