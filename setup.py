from distutils.core import setup, Extension

# if osx
import os
os.environ['LDFLAGS'] = '-framework Carbon -framework AudioUnit -framework AudioToolbox -framework CoreAudio'

module = Extension('cquiet',
                   sources=['quietmodule.c'],
                   extra_compile_args=['-std=c99', '-Iinclude'],
                   extra_link_args=['-Llib', 'libquiet.a', 'libportaudio.a', 'libjansson.a', 'libliquid.a', 'libfec.a'],
                   )

setup(name='quiet',
      version='0.1',
      description='Quiet Modem',
      author='Brian Armstrong',
      author_email='brian.armstrong.ece+pypi@gmail.com',
      url='https://github.com/quiet',
      ext_modules=[module],
      packages=['quiet'],
)
