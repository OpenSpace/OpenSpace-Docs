# Molecules
{menuselection}`Scene --> Molecules`

Moliverse lets you show molecules inside an OpenSpace scene. You can place a molecular structure or a molecular dynamics simulation next to a planet, moon or comet.

Moliverse does not zoom continuously from planet to molecule; the scale gap is far too large for that to be useful. Instead, the molecules appear as a focused view placed in the context of the object they belong to.

## How it works
Moliverse is built on VIAMD, a molecular dynamics analysis tool developed at Linköping University. OpenSpace uses MDlib, the library at the core of VIAMD, to load molecular data, render molecules and run VIAMD's scripting language.

Each frame, OpenSpace hands its camera and simulation time to MDlib, which draws the molecules to match. In practice this means:
- Molecules move with the camera like any other object in the scene, including in dome, multi-projector and VR setups
- Trajectories are tied to OpenSpace's time. Pausing, scrubbing or changing the time rate also controls the simulation playback
- If you already work in VIAMD, the same scripting language can be used to select and style parts of a molecule in OpenSpace

## Getting started
To use Moliverse you need a molecular structure or trajectory file, and an asset that places it in the scene relative to a celestial body. Because VIAMD handles the loading, the file formats VIAMD reads are the ones Moliverse supports.
1. Load one of the example molecule assets, or copy one as a starting point for your own.
1. Point the asset at your data file and choose the object it should be attached to.
1. Adjust representation, size and playback from the molecule's properties in the user interface.

:::{figure} dome.webp
:align: center
:alt: An image of the molecular rendering in OpenSpace on a planetarium dome.

Showing the usage of the molecular rendering capabilities on a planetarium dome.
:::
