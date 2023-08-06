import pathlib

from setuptools import setup


def parse_requirements_file(fname):
    requirements = list()
    with open(fname, 'r') as fid:
        for line in fid:
            req = line.strip()
            if req.startswith('#'):
                continue
            # strip end-of-line comments
            req = req.split('#', maxsplit=1)[0].strip()
            requirements.append(req)
    return requirements


readme = (pathlib.Path(__file__).parent / "README.md").read_text()

version = None
with open(pathlib.Path('mne_qt_browser') / '_version.py', 'r') as fid:
    for line in (line.strip() for line in fid):
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip('\'')
            break
if version is None:
    raise RuntimeError('Could not determine version')

setup(name='mne-qt-browser',
      version=version,
      maintainer='Martin Schulz',
      maintainer_email='dev@earthman-music.de',
      description='A new backend based on pyqtgraph for the 2D-Data-Browser '
                  'in MNE-Python.',
      long_description=readme,
      long_description_content_type='text/markdown',
      license='License :: OSI Approved :: BSD License',
      url='https://github.com/mne-tools/mne-qt-browser',
      download_url='https://github.com/mne-tools/mne-qt-browser/archive/refs'
                   f'/tags/v{version}.tar.gz',
      project_urls={'Bug Tracker':
                    'https://github.com/mne-tools/mne-qt-browser/issues'},
      classifiers=['Programming Language :: Python :: 3',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent'],
      packages=['mne_qt_browser'],
      include_package_data=True,
      install_requires=parse_requirements_file('requirements.txt'),
      extras_require={
          'opengl': ['pyopengl'],
      },
      )
