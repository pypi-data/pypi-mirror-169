# gdsfactory 5.34.0

[![docs](https://github.com/gdsfactory/gdsfactory/actions/workflows/pages.yml/badge.svg)](https://gdsfactory.github.io/gdsfactory/)
[![PyPI](https://img.shields.io/pypi/v/gdsfactory)](https://pypi.org/project/gdsfactory/)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/gdsfactory.svg)](https://anaconda.org/conda-forge/gdsfactory)
[![PyPI Python](https://img.shields.io/pypi/pyversions/gdsfactory.svg)](https://pypi.python.org/pypi/gdsfactory)
[![issues](https://img.shields.io/github/issues/gdsfactory/gdsfactory)](https://github.com/gdsfactory/gdsfactory/issues)
[![forks](https://img.shields.io/github/forks/gdsfactory/gdsfactory.svg)](https://github.com/gdsfactory/gdsfactory/network/members)
[![GitHub stars](https://img.shields.io/github/stars/gdsfactory/gdsfactory.svg)](https://github.com/gdsfactory/gdsfactory/stargazers)
[![Downloads](https://pepy.tech/badge/gdsfactory)](https://pepy.tech/project/gdsfactory)
[![Downloads](https://pepy.tech/badge/gdsfactory/month)](https://pepy.tech/project/gdsfactory)
[![Downloads](https://pepy.tech/badge/gdsfactory/week)](https://pepy.tech/project/gdsfactory)
[![MIT](https://img.shields.io/github/license/gdsfactory/gdsfactory)](https://choosealicense.com/licenses/mit/)
[![codecov](https://img.shields.io/codecov/c/github/gdsfactory/gdsfactory)](https://codecov.io/gh/gdsfactory/gdsfactory/tree/master/gdsfactory)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gdsfactory/binder-sandbox/HEAD)

![logo](https://i.imgur.com/v4wpHpg.png)

gdsfactory is an EDA (electronics design automation) tool for Silicon Photonic Integrated Circuits
It combines a code driven flow (python or YAML) with visualization and simulation plugins.

Multiple Silicon Photonics foundries have gdsfactory PDKs available. Talk to your foundry to access their gdsfactory PDK.

You can also access:

- open source PDKs available on GitHub
    * [UBCPDK](https://gdsfactory.github.io/ubc/README.html)
    * [skywater130](https://gdsfactory.github.io/skywater130/README.html)
- instructions on [how to build your own PDK](https://gdsfactory.github.io/gdsfactory/notebooks/08_pdk.html)
- instructions on [how to import a PDK from a library of fixed GDS cells](https://gdsfactory.github.io/gdsfactory/notebooks/09_pdk_import.html)



gdsfactory provides you with functions that you can use to:

- define Pcells in python or YAML.
- define routes between components.
- test settings, ports and geometry for components to avoid regressions.


As input, you write python or YAML code.
As output you write a GDSII or OASIS file that can send to your foundry.
You can also write components settings (for measurement and data analysis) or netlists (for circuit simulations).

![flow](https://i.imgur.com/XbhWJDz.png)


gdsfactory provides you a common syntax for layout (klayout, gdspy, phidl), simulation (Lumerical, tidy3d, MEEP, MPB, DEVSIM, simphony, SAX, ...) and data analysis libraries.

![tool interfaces](https://i.imgur.com/9Sh8Qav.png)

![layout_to_components](https://i.imgur.com/JLsvpLv.png)



## Installation

[Download the latest installer](https://github.com/gdsfactory/gdsfactory/releases)

## Getting started

- Run notebooks on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gdsfactory/binder-sandbox/HEAD)
- [see slides](https://docs.google.com/presentation/d/1_ZmUxbaHWo_lQP17dlT1FWX-XD8D9w7-FcuEih48d_0/edit#slide=id.g11711f50935_0_5)
- [read docs](https://gdsfactory.github.io/gdsfactory/)
- [See YouTube videos](https://www.youtube.com/watch?v=KXq09GirynI&list=PLZ3ZVd41isDDnuCirqIhNa8vsaHmbmxqM)
- See announcenments on [GitHub](https://github.com/gdsfactory/gdsfactory/discussions/547), [google-group](https://groups.google.com/g/gdsfactory) or [LinkedIn](https://www.linkedin.com/company/gdsfactory)

## Acks

gdsfactory top contributors:

- Joaquin Matres (Google): maintainer.
- Damien Bonneau (PsiQ): cell decorator, Component routing functions, Klayout placer.
- Pete Shadbolt (PsiQ): Klayout auto-placer, Klayout GDS interface (klive).
- Troy Tamas (Rockley): get_route_from_steps, netlist driven flow (from_yaml).
- Floris Laporte (Rockley): netlist extraction and circuit simulation interface with SAX.
- Alec Hammond (Georgia Tech): Meep and MPB interface.
- Simon Bilodeau (Princeton): Meep FDTD write Sparameters.
- Thomas Dorch (Freedom Photonics): for Meep's material database access, MPB sidewall angles, and add_pin_path.
- Igal Bayn (Google): for documentation improvements and suggestions.
- Alex Sludds (MIT): for tiling fixes.
- Skandan Chandrasekar (BYU): for simphony and SiPANN plugins.
- Helge Gehring (Google): for simulation plugins, improving code quality and new components (spiral paths).
- Marc de Cea (MIT): for ge_detector, grating_coupler_dual, and mmi_90degree_hybrid

Open source heroes:

- Matthias Köfferlein (Germany): for Klayout
- Lucas Heitzmann (University of Campinas, Brazil): for gdspy
- Adam McCaughan (NIST): for phidl
- Alex Tait (Queens University): for lytest
- Thomas Ferreira de Lima (NEC): for `pip install klayout`

## Links

- [gdsfactory GitHub repo](https://github.com/gdsfactory/gdsfactory), [docs](https://gdsfactory.github.io/gdsfactory/) and [general updates](https://github.com/gdsfactory/gdsfactory/discussions/547)
- [linkedIn page](https://www.linkedin.com/company/gdsfactory/posts)
- [gdsfactory announcenments group](https://groups.google.com/g/gdsfactory)
- [awesome photonics list](https://github.com/joamatab/awesome_photonics)
