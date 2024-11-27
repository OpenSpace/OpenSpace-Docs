---
authors:
  - name: Brian Abbott, Micah Acinapura
    affiliation: American Museum of Natural History
---


# Time Menu: 

:::{warning}
This section is in progress. Text will appear on this page in the future.
:::


## Time
This section will cover the various aspects of manipulating time in OpenSpace. We often refer to this as the _In-Game time_ as it oftentimes will be different from the time shown on a _wall clock_.


## Keyboard Shortcuts
Upon launch of the default profile, the simulation will be set to one day behind the current time -- this is to provide full coverage of Earth as often, temporal data will not yet be available for the current date. However, the date of the simulation can be changed to any date. By default the simulation will progress in real time, also expressed as _1 second per second_. The rate at which the simulation progresses (also called the _Delta Time_) can be changed. Press the {kbd}`RightArrow` key once to change it to _5 seconds per second_. Now time inside _OpenSpace_ progresses five times as fast as in real life. Press the {kbd}`LeftArrow` to change it back to real-time. You can also pause the progress of time entirely by pressing the {kbd}`Space` key. Lastly, the number keys {kbd}`1-0` are set to different _Delta Times_ that can be accessed directly through those keys.

As you can tell, all of the keys we have used so far have changed the time smoothly. To see this in action use the {kbd}`RightArrow` key to increase the _Delta Time_ to _12h per second_ and you should see Earth rotate every two seconds. If you now press the {kbd}`Space` key, it will take a short while for the Earth to stop spinning. If you press {kbd}`Shift+Space` instead, the Earth will start spinning immediately instead. Similarly, {kbd}`Shift+1-0` and {kbd}`Shift+LeftArrow` and {kbd}`Shift+RightArrow` will instantaneously change the _Delta Time_ to the new value.

Lastly, {kbd}`Alt+1-0` will change the _Delta Time_ to the corresponding negative value. So {kbd}`2` will change it to _5 seconds per second_ and {kbd}`Alt+2` will change it to _-5 seconds per second_, meaning that we slowly move into the past.


## Time Menu
Keyboard shortcuts are useful to quickly change the time, but it can be difficult to set an accurate time using these buttons. In order to jump to a specific time, click on the date at the bottom of the screen will open the Time menu. The Time menu can be popped out using the button in the upper right next to `x`. The Time menu is separated into sections for changing the date, the rate of time, and two buttons. The {menuselection}`Realtime` and {menuselection}`Now` buttons set the rate of time to one second per second and set the date to the current date respectively.

There are different ways to change the date/time using the Time menu. Clicking the arrow above or below any of the date components will advance or retract that part of the date. For example, clicking the arrow above the current month will advance time by one month, clicking on the arrow below the current day will change the time inside _OpenSpace_ back by one day. Similar to the keyboard shortcuts above, holding the {kbd}`Shift` key while clicking on the arros will change the time instantly.

You can also type values directly into the date components. After entering the value you must press the {kbd}`Enter` key to confirm the change. Make sure to enter valid values for time and date, invalid values (such as 55 for day, or 75 for minutes) will result in unexpected behavior. An alternatie way to change the date is to use the calendar function of the Time menu. To show the calendar, click the expand icon on the right next to the seconds component of the date. Clicking on a date in the calendar will smoothly transition the date, holding {kbd}`Shift` while clicking instantly sets the date.

The most flexible way to change the date is to use the lock icon on the left, next to the year component of the date. Clicking the lock icon will expand the menu with three new buttons. Once activated, you can now change the components of the date without the simulation updating. Once you have changed all the components to the exact date/time you want to use, then press the 'Interpolate' or 'Set' buttons to change the date in the simulation.

### Changing the Rate of Time
There are four components of the Time menu under {menuselection}`Simulation Speed`. The main two components are the {menuselection}`Display Unit` dropdown and the {menuselection}`Unit/second` sliders. To change the rate of time, adjust the dropdown to your desired unit, and then use the slider to specify the value you want. For time to go in reverse, use the {menuselection}`Negative Unit/second` slider. The third component is the {menuselection}`Quick Adjust` Slider.

Once you have chosen your desired rate, click and hold the {menuselection}`Quick Adjust` slider to make a momentary change to the rate. When you release the mouse the rate will return to your chosen value. The fourth components are the arrow and Play/Pause buttons. The arrow buttons will cycle through predetermined rates of time specified by the profile the same way as the {kbd}`LeftArrow` and {kbd}`RightArrow` keys will. The Play/Pause button will toggle the rate of time between zero and your specified value just like using the {kbd}`Space` key, holding {kbd}`Shift` while clicking the Play/Pause button will make an instant change to the rate instead of a smooth change.


## Time Options in the Settings Menu
The {menuselection}`Settings --> Time Manager` section contains four values relevant to the Time menu. Lower values will make things happen faster, higher values will make things happen slower. {menuselection}`Default Time Interpolation Duration` affects how long the interpolation will take when changing the date. {menuselection}`Default Delta Time Interpolation Duration` affects how long the interpolation will take when changing the rate of time. `Default Pause Interpolation Duration` affects how long the interpolation will take when pausing, which is changing the rate of time from your chosen value to zero. {menuselection}`Default Unpause Interpolation Duration` affects how long the interpolation will take when unpausing, which is changing the rate of time from zero to your chosen value.


## Video
This video illustrates all of the concepts that are presented in this part of the getting started guide:

<iframe width="740" height="530" src="https://www.youtube.com/embed/z0daNU4OFFA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

| Video time | Description |
|:-------------|:------------------|
| 0:00 | Open and pop-out the Time menu. |
| 0:11 | Change the date by typing and pressing Enter. |
| 0:31 | Change the date with the arrows above and below the date. |
| 1:11 | Change the date by opening the calendar view and clicking on a date. |
| 1:41 | Change the rate of time with the sliders. |
| 2:20 | Using the quick adjust slider to temporarily adjust the rate of time. |
| 3:02 | Play and pause time with the menu's play and pause button. |
| 3:30 | Change the rate of time using the menu's left and right arrows. |
| 4:08 | Use the Realtime and Now buttons to set the rate of time to 1 second/second and the date to your computer's date. |
| 4:35 | Using the Time Manager settings to adjust how quickly or slowly changes happen. |

