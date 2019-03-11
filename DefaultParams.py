
class DenudationParameters:
	# Surface Area of a cubic mineral grain
	#As = 4*np.pi*(0.5*Ds)**2 #spherical 
	As = 6*Ds**2 #cubic
	Ds = .001
	dz = 0.1 # m, Thickness of saprolite layer in which mineral dissolution is accounted for.
	M = 263.02
	ralb = 0.5 # Percent of saprolite composed of mineral for which dissolution is accounted for.
	rho = 2.62*10**6
	R_dis = 2* 10**-9 # mol/m^2/s Mineral dissolution rate for chem denudation estimates.

	kwargs_array = [As, Ds, dz, M, ralb, rho, R_dis]	


	