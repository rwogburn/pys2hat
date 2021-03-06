from distutils.core import setup, Extension
import numpy as np

module1 = Extension('pys2hat.pures2hat',
                    sources = ['pys2hat/pyc_pures2hat.c'],
                    include_dirs = ['s2hat','pure_s2hat','mpi_stubs'],
                    library_dirs = ['s2hat','pure_s2hat','mpi_stubs'],
                    libraries = ['s2hat','s2hat_pure','mpi_stubs','gfortran','fftw3'])

module2 = Extension('pys2hat._s2hat_types',
                    sources = ['pys2hat/s2hat_types.c'],
                    include_dirs = ['s2hat','pure_s2hat','mpi_stubs'],
                    library_dirs = ['s2hat','pure_s2hat','mpi_stubs'],
                    libraries = ['s2hat','s2hat_pure','mpi_stubs','gfortran','fftw3'])

setup (name = 'pys2hat',
       packages = ['pys2hat'],
       version = '0.1',
       description = 's2hat with pure-s2hat E/B separation for CMB polarization maps',
       include_dirs = [np.get_include()],
       ext_modules = [module1,module2])
