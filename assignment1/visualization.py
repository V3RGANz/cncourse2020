import matplotlib.pyplot as plt


def plot_simulation(time_ms, vm, n, m, h, inj_array, save_to=None, title=''):
    figure = plt.figure(figsize=(15, 10))
    ax1 = plt.subplot(511)
    ax1.set_title(title, fontSize=20)
    ax1.plot(time_ms, vm)
    ax1.set_ylabel("V (mV)")
    ax1.set_xlabel("time (ms)")

    ax2 = plt.subplot(512)
    ax2.plot(time_ms, n, color='red')
    ax2.set_ylabel("n")
    ax2.set_xlabel("time (ms)")

    ax3 = plt.subplot(513)
    ax3.plot(time_ms, m, color='green')
    ax3.set_ylabel("m")
    ax3.set_xlabel("time (ms)")

    ax4 = plt.subplot(514)
    ax4.plot(time_ms, h, color='black')
    ax4.set_ylabel("h")
    ax4.set_xlabel("time (ms)")

    ax5 = plt.subplot(515)
    ax5.plot(time_ms, inj_array)
    ax5.set_ylabel("inj current (µA/mm²)")
    ax5.set_xlabel("time (ms)")

    if save_to is not None:
        plt.savefig(save_to)

    return figure
