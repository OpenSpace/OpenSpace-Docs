---
authors:
  - name: Elon Olsson
    affiliation: Community Coordinated Modeling Center
---

(solarstorm2012_id)=

# Solar Storm 2012
This profile is showing several coronal mass ejection (CMEs) during July 2012, where the last one was incredible intense. Its strength was comparable to the most intense CME in recorded history, the Carrington Event of 1859, which caused damage to electric equipment world wide. Luckily this 2012 event missed Earth.

::::::::{tab-set}
:::::::{tab-item} Tour
## Tour

The event is visualized with outputs from the simulation model ENLIL which domain spands across the solar system, from the Sun to Earth. The magnetosphere of Earth in this profile is visualized using BATSRUS, which is showing the interaction of the particle flow of the solar wind and Earths magnetosphere. There is also one time step of the PFSS model showing the Suns local magnetic structure.

To best interact with these visualizations, it is recommended to use the keyboard shortcuts, especially the time loops.
:::::::

:::::::{tab-item} Keyboard Shortcuts
## Keyboard Shortcuts

::::{include} /using-openspace/keyboard-shortcuts/solarstorm2012.md
:heading-offset: 2
::::

:::::::

:::::::{tab-item} Data Sets
## Data Sets

A few simulation models have been used in this profile.
* ENLIL, for solar winds. Visualized with magnetic field lines.
* BATSRUS, for magnetosphere. Also visualized with magnetic field lines, as well as velocity field lines.
* PFSS, just one time step to highlight with field lines the comlex magnetic field in the Suns corona.

:::::::

:::::::{tab-item} Dossier
## Dossier

:::{list-table}
:header-rows: 0
:stub-columns: 1
:align: left
:width: 90%

* - Name:
  - Solar Storm 2012
* - File:
  - `data/profiles/spaceweather/solarstorm2012.profile`
* - Anchor:
  - [Sun](/content/solar-system/sun/sun/index)
* - Time:
  - 2012 07 14 at 07:00:00
* - Author:
  - CCMC
* - License:
  - [MIT](https://github.com/OpenSpace/OpenSpace/blob/master/LICENSE.md)
* - Version:
  - 1.0
:::

:::::::
::::::::