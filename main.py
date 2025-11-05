import numpy as np 
import scipy.integrate as spi 

#---Example kernal functions---

# this example shows a polynomial function
def kernel_polynomial(x):
    return x**3 + x

# This example represents the normal distribution
def kernel_normal(x):
    return np.exp(-x**2)

#---End of example kernal functions---


#---Helpers for transformations of kernal fxn to probability fxn ---
def normalize_kernel(kernel, lower_bound, upper_bound):
    (integral, abs_error) = spi.quad(kernel, lower_bound, upper_bound)
    def normalized_density(x):
        return kernel(x)/ integral
    return normalized_density

def main():
    poly_density = normalize_kernel(kernel, lower_bound, upper_bound):
    print(poly_densityl)

if __name__ == "__main__":
    main()
