import numpy as np
from scipy.integrate import odeint


class HodgkinHuxleyModel:
    """
    Hodgkin-Huxley Model, described in
    "Theoretical Neuroscience Computational and Mathematical
    Modeling of Neural Systems" Peter Dayan and L.F. Abbott
    """
    gL = 0.003  # mS/mm^2
    gK = 0.36  # mS/mm^2
    gNa = 1.2  # mS/mm^2

    EL = -54.387  # mV
    EK = -77  # mV
    ENa = 50  # mV

    def __init__(self, capacity = 1.):
        self.capacity = capacity

    def get_calculate_derivatives_f(self, inj_current):
        def calculate_derivatives(y, t):
            vm, n, m, h = y

            k_current = self.gK * n ** 4 * (vm - self.EK)
            na_current = self.gNa * m ** 3 * h * (vm - self.ENa)
            leak_current = self.gL * (vm - self.EL)

            dvm_dt = (inj_current(t) - (k_current + na_current + leak_current)) / self.capacity
            dn_dt = _alpha_n(vm) * (1 - n) - _beta_n(vm) * n
            dm_dt = _alpha_m(vm) * (1 - m) - _beta_m(vm) * m
            dh_dt = _alpha_h(vm) * (1 - h) - _beta_h(vm) * h

            return np.array([dvm_dt, dn_dt, dm_dt, dh_dt])

        return calculate_derivatives

    def __call__(self, inj_current, time_ms, v0):
        calculate_derivatives = self.get_calculate_derivatives_f(inj_current)
        y0 = np.array([v0, _n_inf(v0), _m_inf(v0), _h_inf(v0)])
        result = odeint(calculate_derivatives, y0, time_ms)
        vm, n, m, h = result[:, 0], result[:, 1], result[:, 2], result[:, 3]
        return vm, n, m, h


def _alpha_n(v):
    return 0.1 * (v + 55) / (1 - np.exp(-0.1 * (v + 55)))


def _beta_n(v):
    return 0.125 * np.exp(-0.0125 * (v + 65))


def _alpha_m(v):
    return 0.1 * (v + 40) / (1 - np.exp(-0.1 * (v + 40)))


def _beta_m(v):
    return 4 * np.exp(-0.0556 * (v + 65))


def _alpha_h(v):
    return .07 * np.exp(-.05 * (v + 65))


def _beta_h(v):
    return 1. / (1 + np.exp(-0.1 * (v + 35)))


def _n_inf(v):
    return _alpha_n(v) / (_alpha_n(v) + _beta_n(v))


def _m_inf(v):
    return _alpha_m(v) / (_alpha_m(v) + _beta_m(v))


def _h_inf(v):
    return _alpha_h(v) / (_alpha_h(v) + _beta_h(v))
