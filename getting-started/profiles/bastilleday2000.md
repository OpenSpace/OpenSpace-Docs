# Bastille Day 2000
This is the date of July 14th, 2000 and maybe the most famous Coronal Mass Ejection (CME). This was a large CME that headed straight to earth in a ground-level event. The profile was used for two shows hosted by the AMNH in the autumn of 2020 and was mainly the result of a master's thesis project at the CCMC.

The profile is very RAM heavy because it uses a lot of data. It consists of multiple image sequences such as EUV textures on the sun and cutplanes in the heliosphere. Cutplanes are sequences of images extracted from a volume that has integrated particle flux values interpolated into the voxels of the volume. The profile also consists of magnetogram textures of the sun, a fieldline sequence of the sun, a volume rendering of the density of the CME and what we've called flux nodes. Flux nodes are points along the magnetic fields where the flux values are calculated. The data for this profile is provided by Predictive Science Inc. (PSI) and are the results of simulations. At PSI they call the flux nodes, "Stream nodes"

## Keybinds
The following keybinds are specific to this profile.

  - {kbd}`M` and {kbd}`N`: toggle a descriptive legend for the flux values
  - {kbd}`O`: toggle the flux nodes on and off
  - {kbd}`U`: toggle the fieldlines of the sun on and off
  - {kbd}`D`: toggle the volumetric rendering of the density on and off
  - {kbd}`P`: toggle the equatorial cutplane on and off
  - {kbd}`[`: toggle the meridial cutplane on and off
  - {kbd}`E`: toggle the EUV texture of the sun on and off
  - {kbd}`I`: use the next magnetogram texture in a list of magnetograms of the Sun

To better show the CME event a few different time loops have been implemented with different start and end times and differences in how fast time is sped up.

  - {kbd}`CTRL+1` for a short loop. 10:03 - 10:16, at 2 min/ second. Recommended for close-up view of the Sun
  - {kbd}`CTRL+2` for the "standard" loop. 10:03 - 11:00, at 4 min/ second. A generally good loop showing most of the event at a good pace
  - {kbd}`CTRL+3` for a fast loop. 10:03 - 11.48, at 15 min/ second. In case something particular will be showcased over and over
  - {kbd}`CTRL+4` for a long loop. 09:30 - 13:00, at 4 min/ second. Starting earlier and ends even after some of the data sets no longer have data at those time steps
  - {kbd}`R` to cancel looping and reset the time to 10.03
