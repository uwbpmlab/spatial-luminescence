import numpy as np
import matplotlib.pyplot as plt


d = np.arange(0, 3, 0.01)


Ds = [1.5e-4, 2.4e-4, 4.5e-4]
D = 1e-4
def one_d_diffusion(d):
    t = ((d**2)/(2*D))/3600
    return t

# for D in Ds:
#     t = one_d_diffusion(d)
#     plt.plot(d, t, label=f"D = {D}")
# plt.title("Glucose diffusion times")
# plt.xlabel("Distance (mm)")
# plt.ylabel("Time (hr)")
# plt.legend()
# plt.show()
print(one_d_diffusion(0.25), one_d_diffusion(3))
