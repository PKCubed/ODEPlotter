# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math
 
mesh_width = 0.25
dir_field_x_template = np.linspace(-mesh_width / 2, mesh_width / 2, 100)
xlims = [-5, 5]
ylims = [-5, 5]

def dydx(x, y):
    try:
        return y*math.log(y+2)
    except Exception:
        return "DNE"

plt.figure(figsize=(7, 6), dpi=200)
plt.xlim(xlims)
plt.ylim(ylims)
plt.axvline(0, c=(0.8,0.8,0.8))
plt.axhline(0, c=(0.8,0.8,0.8))

for x in np.arange(xlims[0], xlims[1]+1, mesh_width):
    for y in np.arange(ylims[0], ylims[1]+1, mesh_width):
        curr_slope = dydx(x, y)
        if curr_slope != "DNE":
            curr_intercept = y - curr_slope * x
            dir_field_xs = (dir_field_x_template/(abs(curr_slope)+1) / 2)+x
            dir_field_ys = [curr_slope * dfx + curr_intercept for dfx in dir_field_xs]
            #print(dir_field_xs)
            plt.plot(dir_field_xs, dir_field_ys, color=(abs(curr_slope)/(abs(curr_slope)+1), 1-abs(curr_slope)/(abs(curr_slope)+1), 0), linewidth=1.5)

def plot_solution(xinit, yinit):
    # Plot Solution Curve
    plt.plot(xinit,yinit, 'ro', color="blue")
    plotx = xinit
    ploty = yinit
    plotres = 0.01
    sol_slope = dydx(plotx, ploty)
    while plotx < xlims[1] and ploty < ylims[1] and ploty > ylims[0] and sol_slope != "DNE":
        plt.plot([plotx, plotx + plotres], [ploty, ploty + sol_slope*plotres], color="blue", linewidth=2)
        plotx += plotres
        ploty += sol_slope*plotres
        sol_slope = dydx(plotx, ploty)
    plotx = xinit
    ploty = yinit
    sol_slope = dydx(plotx, ploty)
    while plotx > xlims[0] and ploty < ylims[1] and ploty > ylims[0] and sol_slope != "DNE":
        plt.plot([plotx, plotx - plotres], [ploty, ploty - sol_slope*plotres], color="blue", linewidth=2)
        plotx -= plotres
        ploty -= sol_slope*plotres
        sol_slope = dydx(plotx, ploty)

plot_solution(2, 4)
plot_solution(0, 1.5)
plot_solution(-2, -4)


plt.xlabel("x")
plt.ylabel("y")
plt.show()
