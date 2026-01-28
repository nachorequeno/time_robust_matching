from setuptools import find_packages, setup, Extension
import pybind11
# from pybind11.setup_helpers import Pybind11Extension

libraries = ['ppl', 'gmp', 'gmpxx']

# ext_instance_int = Pybind11Extension(
#     'timedrel_ext_int',
#     sources=['querytre/boost/timedrel_ext_int.cpp'],
#     include_dirs=['include', '/usr/include'],
#     cxx_std=11,
#     # language = 'c++',
#     libraries=libraries,
#     library_dirs=['/usr/lib'],
# )
#
# ext_instance_float = Pybind11Extension(
#     'timedrel_ext_float',
#     sources=['querytre/boost/timedrel_ext_float.cpp'],
#     include_dirs=['include', '/usr/include'],
#     cxx_std=11,
#     # language = 'c++',
#     libraries=libraries,
#     library_dirs=['/usr/lib'],
# )
#
# ext_instance_rational = Pybind11Extension(
#     'timedrel_ext_rational',
#     sources=['querytre/boost/timedrel_ext_rational.cpp'],
#     include_dirs=['include', '/usr/include'],
#     cxx_std=11,
#     # language = 'c++',
#     libraries=libraries,
#     library_dirs=['/usr/lib', '/usr/lib/x86_64-linux-gnu'],
#     extra_link_args=['-lgmp', '-lgmpxx'],
# )
#
# ext_instance_diag = Pybind11Extension(
#     'timedrel_ext_diag',
#     sources=['querytre/boost/timedrel_ext_diag.cpp'],
#     include_dirs=['include', '/usr/include'],
#     cxx_std=11,
#     # language = 'c++',
#     libraries=libraries,
#     library_dirs=['/usr/lib', '/usr/lib/x86_64-linux-gnu'],
#     extra_link_args=['-lgmp', '-lgmpxx'],
# )

# robusttre_module = Pybind11Extension(
robusttre_module = Extension(
    'robustTRE',
    sources=['robustTRE/robusttre.cpp'],
    include_dirs=['include', '/usr/include', pybind11.get_include()],
    language = 'c++',
    libraries=libraries,
    library_dirs=['/usr/lib', '/usr/lib/x86_64-linux-gnu'],
    extra_link_args=['-std=c++11', '-lppl', '-lgmp', '-lgmpxx'],
)
# '-stdlib=libc++',

setup(
    name='robustTRE',
    packages=find_packages(),
    version='0.1.0',
    description='A library for time-robust pattern matching of Timed Regular Expressions (TRE)',
    author='Akshay Mambakam',
    license='GPLv3+',
    python_requires='>=3',
    install_requires=[#'antlr4-python3-runtime==4.7.1',
                      'pybind11>=2.11'],
    #ext_package='robusttre',
    # ext_modules=[ext_instance_int, ext_instance_float, ext_instance_rational, ext_instance_diag, ext_instance_robust]
    ext_modules=[robusttre_module]
)
