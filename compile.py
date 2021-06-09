from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("source.client.config", ["source/client/config.py"]),
    Extension("source.client.design", ["source/client/design.py"]),
    Extension("source.client.multithreading", ["source/client/multithreading.py"]),
    Extension("source.client.resources_rc", ["source/client/resources_rc.py"]),
    Extension("source.client.ui", ["source/client/ui.py"]),
    Extension("source.client.custom_widgets", ["source/client/custom_widgets.py"]),
    ]

for e in ext_modules:
    e.cython_directives = {'language_level': "3"}

setup(
    name='TimeSeriesForecaster',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)