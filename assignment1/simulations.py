import numpy as np

from assignment1.hodgkinhuxley import HodgkinHuxleyModel


def simulation1(a, at, b, bt, c, ct, d, dt):
    def inj_current(t):
        cur_start = 0
        for val, tm in zip([a,b,c,d], [at,bt,ct,dt]):
            if cur_start <= t < cur_start + 50:
                return 0
            cur_start += 50
            if cur_start <= t < cur_start + tm:
                return val
            cur_start += val
        return 0

    steps = 10000
    time_ms = np.linspace(0, 50 * 5 + sum([at,bt,ct,dt]), steps)
    v0 = 0

    hh = HodgkinHuxleyModel()
    vm, n, m, h = hh(inj_current, time_ms, v0)

    inj_array = np.array([inj_current(t) for t in time_ms])

    return vm, n, m, h, inj_array


def simulation2(a, b):
    time_ms = np.linspace(0, 200, 10000)
    

