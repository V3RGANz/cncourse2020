import numpy as np

from assignment1.hodgkinhuxley import HodgkinHuxleyModel


def simulation1(a, at, b, bt, c, ct, d, dt):
    def inj_current(t):
        cur_start = 0
        for val, tm in zip([0,a,0,b,0,c,0,d,0], [50,at,50,bt,50,ct,50,dt,50]):
            if cur_start <= t < cur_start + tm:
                return val
            cur_start += tm
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

    def inj_current(t):
        period = int(t) % 4
        if period == 0 or period == 2:
            return 0
        elif period == 1:
            return a
        return b

    v0 = 0
    hh = HodgkinHuxleyModel()
    vm, n, m, h = hh(inj_current, time_ms, v0)

    inj_array = np.array([inj_current(t) for t in time_ms])

    return vm, n, m, h, inj_array
