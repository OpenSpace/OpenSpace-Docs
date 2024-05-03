# Fedora
This page contains specific information necessary to compile OpenSpace on FreeBSD. This page has the [general instructions](index) as a required reading.

OpenSpace has been tested on Fedora 33. You also need a GPU that supports OpenGL 3.3. It has been tested with Nvidia cards.

## Development Tools
Install the following tools if they are not already available on your system:
  - Git 2.7+
  - GCC 11+
  - CMake 3.25+


## Dependencies
Install the following dependencies using `dnf`:

```bash
sudo dnf install glfw-devel libXi-devel libXinerama-devel libXrandr-devel libXxf86vm-devel libcurl-devel mesa-libGLU-devel qt5-qtbase-devel gdal-devel harfbuzz-devel zziplib-devel
```

## Compile OpenSpace
```bash
openSpaceHome="$HOME/source/OpenSpace"
git clone --recursive https://github.com/OpenSpace/OpenSpace "$openSpaceHome"
mkdir -p "$openSpaceHome/build"
cd "$openSpaceHome/build"

cmake \
-DCMAKE_BUILD_TYPE:STRING="Release" \
-DCMAKE_CXX_FLAGS:STRING="-DGLM_ENABLE_EXPERIMENTAL" \
-DOpenGL_GL_PREFERENCE:STRING=GLVND "$openSpaceHome"

make
```

### Building with clang
It could also be possible to build with clang. Then you have to install these packages:

```bash
sudo dnf install clang libcxx-devel
```

and use this `cmake` command

```bash
cmake -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_BUILD_TYPE:STRING="Release" -DCMAKE_CXX_FLAGS:STRING="-DGLM_ENABLE_EXPERIMENTAL" -DOpenGL_GL_PREFERENCE:STRING=GLVND "$openSpaceHome"
```

### Planet images not loading
The site `gibs.earthdata.nasa.gov` and possiby other data sources used by OpenSpace uses old TLS settings, see https://www.ssllabs.com/ssltest/analyze.html?d=gibs.earthdata.nasa.gov&s=198.118.199.5. The workaround is to run `sudo update-crypto-policies --set LEGACY` . See also https://fedoraproject.org/wiki/Changes/StrongCryptoSettings2
