---
authors:
  - name: Brian Abbott, Micah Acinapura
    affiliation: American Museum of Natural History
---


# Time Panel

![Time Panel Button](/using-openspace/toolbar/time/toolbar_button_time.png){h=50px}


## Panel Overview

:::{figure} time_panel.png
:align: right
:width: 90%
:figwidth: 40%
:alt: OpenSpace's Time Panel

The Time Panel in OpenSpace.
:::


The Time Panel is where you go to change the date and time, and alter the _Simulation Speed_, or the rate of time.

The panel has various adjustments that allow you to select the date and time by typing in values, choosing from a calendar, or using a slider to adjust the simulation speed. It has a quick adjust slider to move rate of time forward or backward interactively. And, there are buttons to automatically go to the current date and time and reset the simulation time to "realtime", or 1 second per second.


<div style="margin-left: auto; margin-right: auto; width: 640px;">
<iframe width="640" height="360" src="https://www.youtube.com/embed/z0daNU4OFFA?si=dGTIrgsDlr46b5GF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{dropdown} Visual Transcript

| Video time | Description |
|:-------------|:------------------|
| 0:00 | Open and pop-out the Time Panel. |
| 0:11 | Change the date by typing and pressing `Enter`. |
| 0:31 | Change the date with the arrows above and below the date. |
| 1:11 | Change the date by opening the calendar view and clicking on a date. |
| 1:41 | Change the rate of time with the sliders. |
| 2:20 | Using the quick adjust slider to temporarily adjust the rate of time. |
| 3:02 | Play and pause time with the panel's play and pause button. |
| 3:30 | Change the rate of time using the panel's left and right arrows. |
| 4:08 | Use the Realtime and Now buttons to set the rate of time to 1 second/second and the date to your computer's date. |
| 4:35 | Using the Time Manager settings to adjust how quickly or slowly changes happen. |
:::
</div>



:::{note}
For many profiles, when you launch OpenSpace the date will be set to the current date, minus one day. This is mainly to ensure full cloud coverage on Earth---because we receive cloud imagery from the latest satellite data, we need to show yesterday's image in order to have full-Earth coverage.
:::



## Time Transitions

There are many methods for altering the date, time, and rate of time in OpenSpace. Each of these methods results in a transition---moving the current view to the new view specified by the new date, time, or rate of time.


### Interpolated Transition

An _interpolated_ transition happens when the view smoothly changes from the initial view to the final view. As you can imagine, if you're in the Solar System and the difference in time is minutes or hours, then this transition probably will be fairly smooth, visually. However, if you have an interpolated transition on the order of many years, the transition could be visually disorienting, particularly if you're beside a planet. In this case, you may want an instantaneous transition.

### Instantaneous Transition

An _instantaneous_ transition fades the view down and fades back up at the designated date and time. It is graceful no matter the duration chosen for a new date and time, but you do not maintain a visual temporal context---it's an instantaneous switch from one view to the next.


:::::{dropdown} Transition Settings

{menuselection}`Settings --> Time Manager` contains options to control the behavior of transitions. Lower values will make things happen faster, while higher values will make a transition slower.

{menuselection}`Settings --> Time Manager --> Default Time Interpolation Duration` sets the transition duration when you change the date.

{menuselection}`Settings --> Time Manager --> Default Delta Time Interpolation Duration` sets the duration of the transition when changing the rate of time, or simulated speed.
::::::









## Set a Date and Time

There are several ways to specify the date and time in OpenSpace. You can type or add increments to the time fields at the top, you can choose from a calendar, or preset a time and choose a transition method.

### Use the Date and Time Fields

The six fields at the top of the panel---year, month, day, hours, minutes, seconds---may be used to alter the date and time. You can type directly in these fields or use the arrows above or below the fields.

:::{figure} time_panel_fields.png
:align: center
:width: 55%
:alt: OpenSpace's Time Panel

The date and time fields.
:::


**Using the Arrows:** If you use the arrows, the transition is **interpolated**, meaning the transition from your present view to the view on your new specified date is animated over some set duration.

**Typing in the Fields:** If you type your desired values directly in the fields, the transition is **instantaneous**. There is no possibility of a disorienting experience because it goes directly to the new view.




### Locking the Simulation Speed

:::{figure} time_panel_lock.png
:align: center
:width: 55%
:alt: OpenSpace's Time Panel

Pressing the Lock Button displays the Interpolate, Set, and Cancel buttons.
:::

The ![Lock Button](time_panel_lock_button.png){h=2em} button allows you to alter the date and time without altering the view. Normally, if you set a new date the view will change to the date specified, either instantaneously or by interpolating to it as we discussed above. When you use the Lock Button, you can change the date and the view won't change until you press either the Interpolate Button or the Set Button.

The {menuselection}`Interpolate` Button results in an interpolated transition, while the {menuselection}`Set` Button will bring up the view for the new date using an instantaneous transition.




## Simulation Speed

The Simulation Speed alters the **rate** of time in OpenSpace. There will be many reasons for changing the speed of the simulation: to see the planets revolve around the Sun, to spin one side of a planet into sunlight, examine a mission and its spacecraft over time, or to watch the stars move over millennia.

### Display Unit Menu

:::{figure} time_panel_simulation_units.png
:align: right
:width: 90%
:figwidth: 40%
:alt: The Time Panel display unit menu.

The Time Panel's Display Unit Menu to change the rate of time.
:::

Use the Display Unit dropdown menu to select the time units you desire, between seconds and years. Pressing on the field reveals the menu.

### Time Rate Value

Change the time increment in the input next to the display unit menu. Enter a number and then press {kbd}`Enter` to set the value. To reverse time, enter a negative number.

The unit on the rate of time is displayed above the input. By default, the rate of time is seconds per second. Of course, when the value is 1 and the unit is seconds/second, we're running in real time. If you change the unit to hours, then the input will show "hours/second", and if the value is 10, then time will move at 10 hours for every second on your watch.

### Quick Adjust

:::{figure} time_panel.png
:align: right
:width: 90%
:figwidth: 40%
:alt: OpenSpace's Time Panel
:::

Use the Quick Adjust slider to adjust the rate temporarily. For example, if you wanted to move one side of a planet into sunlight, you might set the Display Unit to Hours, then move the Quick Adjust slider a bit to the left (backward in time) or right (forward in time) at a rate that complements what you're trying to achieve. Once you let go of the slider, your rate of time will return to your original value.



### Play/Pause Button

The Play/Pause Button does just that to the Simulation Time. Pausing will, obviously, bring the passage of time in OpenSpace to a halt. Play will resume the passing of time at the presently set rate. Alternatively, you can use the {kbd}`Space` button to play and pause the simulation time. This action will include an interpolated transition to go from start to stop. If you want to forego that transition you can use {kbd}`Shift` + {kbd}`Space`, which will result in an instantaneous transition.


:::::{dropdown} Pause/Unpause Transition Options
When you press the Play/Pause button, there is a transition that occurs when time comes to a halt (Pause Button), or when time ramps up from zero to the desired simulation time (Play Button).

Inside the {menuselection}`Settings --> Time Manager` menu, you will find these two options for controlling this transition duration:
- {menuselection}`Settings --> Time Manager --> Default Pause Interpolation Duration` affects how long the transition will take when pausing, which is changing the rate of time from your chosen value to zero.
- {menuselection}`Settings --> Time Manager --> Default Unpause Interpolation Duration` affects how long the transition will take when unpausing, which is changing the rate of time from zero to your chosen value.
:::::


### Fast-forward & Rewind Buttons
The fast-forward and rewind buttons change the simulation speed according to preset increments defined in a profile. Appearing under each button is the increment it will implement and it will change as you progressively select adjacent increments.

Alternatively, you can use the keyboard shortcuts {kbd}`→` to increase and {kbd}`←` to decrease the simulation time by the increments specified in the profile. For example, in the [](/profiles/default/index.md) Profile, the second time increment is 5.0 (see the _Default Profile Time Increments_ dropdown below), and this value is shown under the fast-forward button. If you press the {kbd}`→` key, the simulated time will increase to 5 seconds per second. Press the {kbd}`←` key and it will return to 1 second per second.

You can also use the number keys {kbd}`1`, {kbd}`2`, ..., {kbd}`0` to go directly to a time increment, so {kbd}`1` sets the simulated time to the first defined increment: 1 second per second. {kbd}`2` sets it to 5 seconds per second, and so on. If you press {kbd}`Alt` + {kbd}`1`, {kbd}`Alt` + {kbd}`2`, etc., you can go directly to the negative value of the increment. So, hitting {kbd}`2` will take you to a simulated time of 5 seconds per second, and hitting {kbd}`Alt` + {kbd}`2` will take you directly to -5 seconds per second.



:::::{dropdown} Default Profile Time Increments

Each profile can have custom time increments, used with the {kbd}`→` or {kbd}`←` shortcut keys or direct shortcut keys.

These are the increments from the [](/profiles/default/index) profile file defines the increments for the Simulated Speed. You can find these in the [Profile Editor](/using-openspace/launcher/profile-editor/index.md).

:::{table} Default Profile time increments
:widths: auto
:align: center

| Shortcut Key | Increment (sec) | Increment (relatable units) |
| --- | --- | --- |
| {kbd}`1` | 1.0 | 1 second/second |
| {kbd}`2` | 5.0 | 5 seconds/second |
| {kbd}`3` | 30.0 | 30 seconds/second |
| {kbd}`4` | 60.0 | 1 minute/second |
| {kbd}`5` | 300.0 | 5 minutes/second |
| {kbd}`6` | 1800.0 | 30 minutes/second |
| {kbd}`7` | 3600.0 | 1 hour/second |
| {kbd}`8` | 43200.0 | 12 hours/second |
| {kbd}`9` | 86400.0 | 1 day/second |
| {kbd}`0` | 604800.0 | 1 week/second |
| {kbd}`Shift`+{kbd}`1` | 1209600.0 | 2 weeks/second |
| {kbd}`Shift`+{kbd}`2` | 2592000.0 | 4.3 weeks/second (~1 month) |
| {kbd}`Shift`+{kbd}`3` | 5184000.0 | 8.6 weeks/second (~2 months) |
| {kbd}`Shift`+{kbd}`4` | 7776000.0 | 12.9 weeks/second (~3 months) |
| {kbd}`Shift`+{kbd}`5` | 15552000.0 | 25.7 weeks/second (~6 months) |
| {kbd}`Shift`+{kbd}`6` | 31536000.0 | 1 year/second |
| {kbd}`Shift`+{kbd}`7` | 63072000.0 | 2 years/second |
| {kbd}`Shift`+{kbd}`8` | 157680000.0 | 5 years/second |
| {kbd}`Shift`+{kbd}`9` | 315360000.0 | 10 years/second |
| {kbd}`Shift`+{kbd}`0` | 630720000.0 | 20 years/second |
:::


:::::




## Keyboard Shortcuts

Summary of the keyboard shortcuts for the Time Panel.

:::{list-table}
:header-rows: 1
:stub-columns: 1
* - Shortcut
  - Function
* - {kbd}`Space`
  - Play or pause the simulation time.
* - {kbd}`→`
  - Increase the simulation time.
* - {kbd}`←`
  - Decrease the simulation time.
* - {kbd}`1` to {kbd}`0`
  - Change the simulation time to one of the predefined increments.
* - {kbd}`Shift` + {kbd}`1` to {kbd}`Shift` + {kbd}`0`
  - Change the simulation time to one of the predefined increments.
* - {kbd}`Shift` + {kbd}`Space`
  - Play or pause the simulation time which will result in an instantaneous transition.
* - {kbd}`Shift` + {kbd}`→`
  - Increase the simulation time with an instantaneous transition.
* - {kbd}`Shift` + {kbd}`←`
  - Decrease the simulation time with an instantaneous transition.
* - {kbd}`Alt` + {kbd}`1` to {kbd}`Alt` + {kbd}`9`
  - Change the simulation time to the negative value of the predefined increment.

:::




