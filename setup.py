from distutils.core import setup

setup(name="beacon", version="0.1",
      description="BEAmline CONfiguration library",
      author="S. Petitdemange, M. Guijarro (ESRF)",
      package_dir={"beacon": "beacon"},
      packages=["beacon", "beacon.conductor"]) 