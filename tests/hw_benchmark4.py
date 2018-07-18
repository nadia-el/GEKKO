# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import numpy as np
from gekko import GEKKO
import test_runner

def benchmark4():
    m = GEKKO()

    nt = 101
    m.time = np.linspace(0,1,nt)

    x1 = m.Var(value=1)
    x2 = m.Var(value=0)
    T = m.Var(value = 380, lb=298, ub=398)

    final = np.zeros(nt)
    final[-1] = 1
    final = m.Param(value=final)

    k1 = m.Intermediate(4000*m.exp(-2500/T))
    k2 = m.Intermediate(6.2e5*m.exp(-5000/T))

    m.Equation(x1.dt() == -k1*x1**2)
    m.Equation(x2.dt() == k1*x1**2 - k2*x2)

    m.Obj(final*x2)

    m.options.IMODE = 6

    m.solve(disp=False)

    assert x1.value == [1.0, 0.9346326, 0.8770691, 0.8260124, 0.7804346, 0.7395115, 0.7025743, 0.6690754, 0.6385623, 0.6106578, 0.5850449, 0.5614558, 0.5396625, 0.5194695, 0.5007088, 0.4832346, 0.4669205, 0.4516555, 0.4373428, 0.4238966, 0.4112413,0.3993097, 0.3880419, 0.3773846, 0.3672898, 0.3577145, 0.3486199, 0.3399709, 0.3317359, 0.323886, 0.316395, 0.3092391, 0.3023963, 0.2958467, 0.289572, 0.2835554, 0.2777812, 0.2722354, 0.2669046, 0.2617767, 0.2568403, 0.2520851, 0.2475012, 0.2430796, 0.2388119, 0.2346903, 0.2307074, 0.2268563, 0.2231307, 0.2195245, 0.2160322, 0.2126484, 0.2093682, 0.2061869, 0.2031002, 0.2001038, 0.197194, 0.194367, 0.1916194, 0.1889478, 0.1863492, 0.1838207, 0.1813594, 0.1789628, 0.1766283, 0.1743535, 0.1721362, 0.1699742, 0.1678656, 0.1658083, 0.1638006, 0.1618406, 0.1599267, 0.1580572, 0.1562308, 0.1544458, 0.1527009, 0.1509948, 0.1493262, 0.1476939, 0.1460967, 0.1445335, 0.1430032, 0.1415048, 0.1400374, 0.1385999, 0.1371914, 0.1358112, 0.1344584, 0.133132, 0.1318315, 0.130556, 0.1293049, 0.1280774, 0.1268729, 0.1256907, 0.1245302, 0.1233909, 0.1222721, 0.1211734, 0.1200941]
    assert x2.value == [0.0, 0.06397918, 0.1189614, 0.1664073, 0.2074829, 0.2431305, 0.2741197, 0.3010855, 0.3245561, 0.3449752, 0.3627177, 0.3781024, 0.3914029, 0.4028545, 0.4126611, 0.4210001, 0.4280268, 0.4338772, 0.4386714, 0.4425156, 0.4455041, 0.4477209, 0.4492407, 0.4501309, 0.4504515, 0.4502569, 0.4495959, 0.4485128, 0.4470475, 0.4452364, 0.4431125, 0.4407058, 0.4380436, 0.4351511, 0.4320509, 0.428764, 0.4253095, 0.421705, 0.4179665, 0.4141088, 0.4101456, 0.4060893, 0.4019514, 0.3977426, 0.3934725, 0.3891501, 0.3847838, 0.3803811, 0.3759492, 0.3714945, 0.3670229, 0.3625401, 0.3580511, 0.3535607, 0.349073, 0.3445922, 0.3401219, 0.3356654, 0.3312259, 0.3268062, 0.322409, 0.3180366, 0.3136912, 0.3093749, 0.3050894, 0.3008365, 0.2966176, 0.2924342, 0.2882874, 0.2841784, 0.2801082, 0.2760777, 0.2720877, 0.2681389, 0.2642319, 0.2603673, 0.2565455, 0.2527669, 0.2490319, 0.2453407, 0.2416935, 0.2380904, 0.2345317, 0.2310174, 0.2275474, 0.2241217, 0.2207404, 0.2174033, 0.2141103, 0.2108612, 0.2076559, 0.2044942, 0.2013757, 0.1983004, 0.1952679, 0.1922779, 0.1893302, 0.1864244, 0.1835602, 0.1807372, 0.177955]
    assert T.value == [380.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0,398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0, 398.0]
    assert k1.value == [5.557244, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066,7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066, 7.483066]
    assert k2.value == [1.196715, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856,2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856, 2.169856]

test_runner.test('benchmark4', benchmark4)