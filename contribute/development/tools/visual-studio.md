# Visual Studio Tips and Tricks

## Detecting Exceptions
A common problem is that an exception is thrown somewhere in the code and we can only put a breakpoint in the `catch` part at which point we have lost the stack information of where the exception originated from and finding that out can be cumbersome.

{menuselection}`Debug --> Exception Settings --> C++ Exceptions --> <All C++ Exceptions not in this list>` should be checked

If that checkbox is selected, Visual Studio will break every time a C++ exception is thrown. In most of our code, exceptions are only raised when something bad happened, which shouldn't be too often (famous last words), so it is a good way to detect the source location of the exception.


## Breaking on floating point exceptions
Sometimes numbers break, for example `float x = std::sqrt(-1.0)` would store as a NaN, which would then propagate further into other calculations. Finding the source error of this can be very tedious and cumbersome as it involves a lot of (`assert(x == x)`).

Doing this somewhere early in the program:
```cpp
#include <float.h>
_clearfp();
_controlfp(
    _controlfp(0, 0) & ~(_EM_ZERODIVIDE | _EM_OVERFLOW),
    _MCW_EM
);
```

Will cause exceptions to be thrown everytime an overflow or a division by 0 occurs anywhere in the code.


## Disabling optimizations for a particlar part of code
When running OpenSpace in `RelWithDebInfo` the compiler applies optimizations throughout the code, which makes it difficult to look at individual variables as they might have been optimized away.

Adding `pragma optimize ("", off)` to the top of a file will disable all optimizations *only for that file* and will preserve all variables, etc.


## Command Palette
Visual Studio also has a command palette, which is accessible through {kbd}`CTRL+T`. Different prefixes in the search bar allow you to filter for files (`f:`), types (`t:`), or members (`m:`).
