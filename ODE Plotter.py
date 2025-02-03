# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
mesh_width = 0.25
dir_field_x_template = np.linspace(-mesh_width / 2, mesh_width / 2, 100)
xlims = [-5, 5]
ylims = [-5, 5]

def dydx(x, y):
    return 0.2*x**2 + y

plt.figure(figsize=(7, 6), dpi=200)
plt.xlim(xlims)
plt.ylim(ylims)
plt.axvline(0, c=(0.8,0.8,0.8))
plt.axhline(0, c=(0.8,0.8,0.8))

for x in np.arange(xlims[0], xlims[1]+1, mesh_width):
    for y in np.arange(ylims[0], ylims[1]+1, mesh_width):
        curr_slope = dydx(x, y)
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
    while plotx < xlims[1]:
        plt.plot([plotx, plotx + plotres], [ploty, ploty + dydx(plotx, ploty)*plotres], color="blue", linewidth=2)
        #print([plotx, ploty])
        plotx += plotres
        ploty += dydx(plotx, ploty)*plotres
    plotx = xinit
    ploty = yinit
    while plotx > xlims[0]:
        plt.plot([plotx, plotx - plotres], [ploty, ploty - dydx(plotx, ploty)*plotres], color="blue", linewidth=2)
        #print([plotx, ploty])
        plotx -= plotres
        ploty -= dydx(plotx, ploty)*plotres

plot_solution(0, 0.5)
plot_solution(2, -1)


plt.xlabel("x")
plt.ylabel("y")
plt.show()
