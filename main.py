from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

def sample_numpy(e):
    document.getElementById('output').innerHTML = " "

    months =  np.array(['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    waffles_eaten = np.array([10, 22, 42, 50, 31, 53, 17, 29, 17, 46, 44, 59])
    sample_graph = plt.plot(months, waffles_eaten)
    plt.show(sample_graph)

    plt.title("Waffles eaten per month")
    plt.xlabel('Months')
    plt.ylabel('Number of Waffles')