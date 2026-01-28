import robustTRE
from robustTRE import zone_set, zone, lower_bound, upper_bound

import matplotlib.pyplot as plt
import numpy as np

def zone_converter(values: list[int], signs: list[bool]) -> zone:
	args = [lower_bound(*item) if i % 2 == 0 else upper_bound(*item) for i, item in enumerate(zip(values, signs))]
	return zone.make(*args)

# Function that returns the time robustness (translation) oracle from the match set
def gen_rob_oracle(zset: zone_set) -> callable:
	return lambda x,y: robustTRE.trobustness(zset,x,y)

# Function that returns the optimal robustness (translation) oracle from the match set
def gen_rob_oracle_opt(zset: zone_set, start_scope: float, end_scope: float) -> callable:
	return lambda x,y: robustTRE.trobustness_opt(zset,x,y,start_scope,end_scope)

# Initialize scaling factor
scaling = 1000

# Initialize heat map display scope
start_scope = 0.0
# end_scope = 20.0
end_scope_x = 15.0
end_scope_y = 18.0
end_scope = max(end_scope_x, end_scope_y)

# Define the duration of signal
# duration = end_scope - start_scope

# Create a match set of choice
zset = robustTRE.zone_set()

# zone1 = (0, 2, 4, 5, 3, 4)
values1 = [0, 2, 4, 5, 3, 4]
signs1 = [False, True, False, True, True, True]

# zone2 = (12.0, 15.0, 15.0, 19.0, 3.0, 4.0)
values2 = [12, 15, 15, 19, 3, 4]
signs2 = [True, False, False, False, True, True]

zone1 = zone_converter(values1, signs1)
zone2 = zone_converter(values2, signs2)

zset = robustTRE.zone_set()
zset.add(zone1)
zset.add(zone2)
# zset.add_from_period([("0", "5"), ("12", "15")])
# zone_set_q = zset.from_periods([("0", "2"), ("4", "5"), ("8/1", "12"), ("15", "18")])

robustTRE.zsetprint(zset)

# Filter out points where robustness is less than rob_bound = 0.1
rob_bound = 0.1
zset_rob = robustTRE.trmtrans(zset, rob_bound)

# Print the robust zone set
robustTRE.zsetprint(zset_rob)

# Get the time robustness (translation) oracle
# rob_oracle = gen_rob_oracle_opt(zset, start_scope, end_scope)
rob_oracle = gen_rob_oracle(zset)

# generate 2 2d grids for the x & y bounds
y, x = np.meshgrid(np.linspace(start_scope, end_scope_y, scaling), np.linspace(start_scope, end_scope_x, scaling))

# Map the time robustness with respect to translation
z = np.zeros((scaling,scaling))
for i in range(scaling):
	for j in range(scaling):
		# xi, yi = float(x[i,j]), float(y[i,j])
		# zi = rob_oracle(xi, yi)
		# z[i,j] = np.float64(zi) # Convert to numpy float64
		# print(f"{i},{j}: x={x[i,j]}, y={y[i,j]}, type={type(x[i,j])},{type(y[i,j])}, type={type(xi)},{type(yi)}")
		z[i,j] = rob_oracle(x[i,j], y[i,j])

# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

fig, ax = plt.subplots()

c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
ax.set_title('Time Robustness (translation) map')
# set the limits of the plot to the limits of the data
corners = (x.min(), x.max(), y.min(), y.max())
ax.axis(corners)
fig.colorbar(c, ax=ax)

plt.show()