# RobustTRE
RobusTRE is a fork of [Timedrel] and [Montre] that computes time-robust pattern matching Timed Regular Expressions in Python. 

[Timedrel]: https://github.com/doganulus/timedrel
[Montre]: https://github.com/doganulus/montre

# Installation
In order to install RobustTRE, run the following commands
``
pip3 install .
``

# Compilation
Alternatively, you can compile and pack the library into a *.whl file.

``
python3 setup.py bdist_wheel --universal
``

``
pip3 install  --force-reinstall ./dist/robusttre-0.1.0-*.whl 
``

Then, you can install the *.whl file using the installation procedure for Python libraries.

**Remark**: On Linux/macOS you will probably need g++.

# Dependencies: 
## GMP and PPL
RobustTRE uses **Parma Polyhedra Library (PPL)** for implementing the algorithms for TRE evaluation,  diagnostics and time-robustness from a given match-set and a given robustness value. 
PPL depends on the **GNU Multiple Precision (GMP) Arithmetic Library**.
Additionally, we use **pybind11** to create **Python3** bindings.
You must install both libraries before installing RobustTRE.
On Ubuntu, you can install them running:
We provide a list of detailed commands for Ubuntu.

1. Install Parma Polyhedra Library (PPL).
```
sudo apt install ppl-dev
```
2. Install C++ compiler.
```
sudo apt install g++
```
3. Install the GNU Multiple Precision (GMP) Arithmetic Library.
```
sudo apt install libgmp-dev
```
4. Install
```
./build.sh
```
5. Run
```
python3 ./examples/robustness_example_1.py
```


# Authors and acknowledgment
This package is built on top of the work done at the VERIMAG laboratory located in the Grenoble city of France. This work is based on the theory of timed pattern matching developed by Dogan Ulus. Check out his [github page](https://github.com/doganulus).

## License
For open source projects, say how it is licensed.