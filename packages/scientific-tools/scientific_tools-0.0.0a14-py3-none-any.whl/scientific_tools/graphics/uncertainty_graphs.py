"""This module trace graphs to show uncertainties."""

import matplotlib.pyplot as plt
import numpy as np

from function_graphs import plot_2Dfunction
import  scientific_tools.physics.uncertainty as uncertainty

def plot_uncertainty_function() :
    raise NotImplementedError("This function is in development. Work in progress.")

def plot_uncertainty_points(x, y, u_x, u_y, title="Experimental values with error bar", x_label="", y_label="") :
    """Draw experimental values with error bar
    
    x is the list of x coordinates, y is the list of y coordinates
    u_x is the list of x uncertainties, u_y is the list of y uncertainties
    """
    plt.errorbar(x, y, xerr=u_x, yerr=u_y, fmt='bo', label='Mesures')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

def null_function(value) :
    """Return 0 for all value of 'value'.
    
    It's can use as an uncertainty calculator when the function is a reference function. (see the documentation of plot_z_score_graph).
    """
    return 0

def plot_z_score_graph(f1, u_f1, f2, u_f2, min_x, max_x, values_nb, z_score_limit=2, limit_color='red', z_score_color='blue', limit_linestyle="-", z_score_linestyle="-", title="", label_x="", label_y="", limit_label="Limits of z-score validity", z_score_label="Z-score") :
    """Trace the z-score between two functions
    
    f1 is the first function & f2 is the second one. Those functions takes only
    one argument that varies from min_x to max_x by taking values_nb values.
    u_f1 is the function that calculate the f1 uncertainty & u_f2 calculate f2 uncertainty. Those uncertainties functions take only one argument : the function value. If a function is a function reference, u_f must return 0 (you can use the null_function define in this module).

    z_score_limit is the validity limit for the z-score (usually, it's 2) 
    limit_color is color of lines that represents limits of z_score validity
    z_score_color is the color of the z_score curve
    limit_linestyle & z_score_linestyle are the line style of each curve (cf Matplotlib docs for futher information)
    title is the graph title
    label_x and label_y are texts to put on the axes
    limit_label is the text display in the legend about lines that represents limits of z_score validity
    z_score_label is the text display in the legned about the z-score curve
    """
    x_values = np.linspace(min_x, max_x, values_nb)
    
    #calculate values for f1 & f2
    f1_values = []
    u_f1_values = []
    f2_values = []
    u_f2_values = []
    for x in x_values :
        f1_value = f1(x)
        f1_values.append(f1_value)
        if u_f1 is not null_function :
            u_f1_values.append(u_f1(f1_value))
        f2_value = f2(x)
        f2_values.append(f2_value)
        if u_f2 is not null_function :
            u_f2_values.append(u_f1(f2_value))

    z_score_values = []
    #calculate z_score
    if u_f1 is null_function :
        for i in range(values_nb) :
            z_score_values.append(uncertainty.z_score_ref(f2_values[i], f1_values[i], u_f2_values[i]))
    elif u_f2 is null_function :
        for i in range(values_nb) :
            z_score_values.append(uncertainty.z_score_ref(f1_values[i], f2_values[i], u_f1_values[i]))
    else :
        for i in range(values_nb) :
            z_score_values.append(uncertainty.z_score(f1_values[i], u_f1_values[i], f2_values[i], u_f2_values[i]))

    #displaying
    plt.plot(x_values, z_score_values, color=z_score_color, linestyle=z_score_linestyle, label=z_score_label)
    plt.plot([np.min(x_values), np.max(x_values)], [z_score_limit, z_score_limit], color=limit_color,linestyle=limit_linestyle, label=limit_label)
    plt.plot([np.min(x_values), np.max(x_values)], [-z_score_limit, -z_score_limit], color=limit_color,linestyle=limit_linestyle)
    plt.legend()
    plt.title(title)
    plt.xlabel(label_x)
    plt.ylabel(label_y)


def plot_z_score_points_graph(x, y1, u_y1, y2, u_y2, z_score_limit=2, limit_color='red', z_score_color='blue', limit_linestyle="-", z_score_linestyle="-", title="", label_x="", label_y="", limit_label="Limits of z-score validity", z_score_label="Z-score") :
    """Trace the z-score between two lists of points
    
    x is the list of point abscissa
    y1 is the first list of values & f2 is the second one.
    u_y1 is the list of uncertainties of y1 points  & u_y2 is the list for y2 points uncertainties. If a list of points is a reference, u_y be a list of zero

    z_score_limit is the validity limit for the z-score (usually, it's 2) 
    limit_color is color of lines that represents limits of z_score validity
    z_score_color is the color of the z_score curve
    limit_linestyle & z_score_linestyle are the line style of each curve (cf Matplotlib docs for futher information)
    title is the graph title
    label_x and label_y are texts to put on the axes
    limit_label is the text display in the legend about lines that represents limits of z_score validity
    z_score_label is the text display in the legned about the z-score curve
    """
    z_score_values = []
    #calculate z_score
    for i in range(len(x)) :
        z_score_values.append(uncertainty.z_score(y1[i], u_y1[i], y2[i], u_y2[i]))

    #displaying
    plt.plot(x, z_score_values, color=z_score_color, linestyle=z_score_linestyle, label=z_score_label)
    plt.plot([np.min(x), np.max(x)], [z_score_limit, z_score_limit], color=limit_color,linestyle=limit_linestyle, label=limit_label)
    plt.plot([np.min(x), np.max(x)], [-z_score_limit, -z_score_limit], color=limit_color,linestyle=limit_linestyle)
    plt.legend()
    plt.title(title)
    plt.xlabel(label_x)
    plt.ylabel(label_y)

