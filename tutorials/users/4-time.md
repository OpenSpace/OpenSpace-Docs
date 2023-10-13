# Time in OpenSpace
This section will cover the various aspects of manipulating time in OpenSpace.

## The Date/Time of the Simulation
 - Upon launch of the default profile, the simulation will be set to one day behind the current time — this is to provide full coverage of Earth. Often, temporal data will not yet be available for the current date.
 - The date of the simulation can be changed to any date.
 - Solar System positional information is only available between 1850 and 2150.

## Changing the Rate of Time Change in the Simulation
 - By default, the simulation will progress in real time.
 - The rate at which the simulation progresses can be changed.
 - You can progress forward or backward in time at any speed.
 - Time can be paused.
 - See [Using the menus: Time](5-menus-time) for details on controlling the rate of time.

## Interpolate vs Instant Time Change
 - When changing the date, the rate of time change, or pausing time, the change will be interpolated so as not to 'jump' the camera.
 - The number of seconds it will take to interpolate can be set under Settings -> Time Manager, where there are individual settings for the time change, rate of time change, and pausing.
 - Various UI elements, Lua scripts, and keyboard shortcuts will let you make these changes 'instantly' without the interpolation.

## Default Keyboard Shortcuts for Time
 - Space bar will pause time (slowing it down to a pause over 0.5 seconds)
 - Shift + Space bar will pause time instantly
 - The right arrow key will increase the rate of time (increasing over 0.5 seconds).
 - The left arrow key will decrease the rate of time (decreasing over 0.5 seconds).
 - Shift + the arrow keys will increase/decrease the rate of time immediately.
 - The number keys will set increasing specific rates of time.
 - ALT / option + number keys will set decreasing negative rates of time.

## Video
 See the next tutorial [Using the menus: Time](5-menus-time) for a video detailing using the time menu.
