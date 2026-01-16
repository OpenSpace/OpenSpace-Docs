# TUIO Touch Input Simulator - For Debugging Touch Navigation
OpenSpace uses the [TUIO](https://www.tuio.org/) framework for multi-touch navigation support. When developing or testing touch navigation without a touch-capable display, it is useful to have a tool that simulates TUIO inputs from mouse inputs.

An example of a simulator is the [TUIOSimulator](https://github.com/gregharding/TUIOSimulator) by Greg Harding.

:::{note}
Simulators like the TUIOSimulator only inject TUIO touch points and cannot be used to test other types of touch support, such as in the web-based interface. For UI testing, use the built-in browser touch simulation features instead.
:::
