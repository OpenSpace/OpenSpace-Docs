# Using the Menus - Time
This section will cover using the menus to manipulate time in OpenSpace.

## Time Menu
 - Clicking on the date at the bottom of the screen will open the Time menu.
 - The Time menu can be popped out using the button in the upper right next to x
 - The Time menu is separated into sections for changing the date, the rate of time, and two helper buttons.
 - The Realtime and Now helper buttons set the rate of time to one second per second and set the date to the computer's current date respectively.
 - The other sections will be described below.

## Changing the Date/Time
 - There are different ways to change the date/time using the Time menu.
 - Clicking the arrow above or below any of the components of the date will advance or retract that part of the date.
    - For instance, to advance time one month, click the arrow above the month.
    - To retract time one day, click the arrow below the day of the month.
    - Holding shift while clicking the arrow will change the time instantly rather than interpolate the change.
 - Typing values into the components of the date is another way to change the date.
    - Type the value you want and hit enter to change the time instantly.
    - You must enter valid values for time and date, invalid values (such as 55 for day, or 75 for minutes) will result in unexpected behavior.
 - The next way to change the date is to use the calendar function of the Time menu.
    - To show the calendar, click the expand icon on the right next to the seconds component of the date.
    - Clicking on a date in the calendar will interpolate the date.
    - Hold shift while clicking to instantly set the date.
 - The most flexible way to change the date is to use the lock icon on the left, next to the year component of the date.
    - Clicking the lock icon will expand the menu with three new buttons.
    - Once activated, you can now change the components of the date without the simulation updating.
    - Once you have changed all the components to the exact date/time you want to use, then press the 'Interpolate' or 'Set' buttons to change the date in the simulation.

## Changing the Rate of Time
 - There are four components of the Time menu under "Simulation Speed."
 - The main two components are the "Display Unit" dropdown and the "Unit/second" sliders.
    - To change the rate of time, adjust the dropdown to your desired unit, and then use the slider to specify the value you want. For time to go in reverse, use the "Negative Unit/second" slider.
    - The third component is the "Quick Adjust" Slider.
 - Once you have chosen your desired rate, click and hold the "Quick Adjust" slider to make a momentary change to the rate.
    - When you release the mouse the rate will return to your chosen value.
 - The fourth components are the arrow and play/pause buttons.
    - The arrow buttons will cycle through predetermined rates of time specified by the profile.
    - The play/pause button will toggle the rate of time between zero and your specified value.
    - Just like using the spacebar, holding shift while clicking the play/pause button will make an instant change to the rate instead of an interpolated change.
  - See the previous tutorial [Time in OpenSpace](http://wiki.openspaceproject.com/docs/tutorials/users/time) for keyboard shortcuts to do some of these changes without the menu.

## Time Options in the Settings Menu
 - The TimeManager section of the Settings Menu contains four values relevant to the Time menu. Lower values will make things happen faster, higher values will make things happen slower.
  - '_Default Time Interpolation Duration_' affects how long the interpolation will take when changing the date.
  - '_Default Delta Time Interpolation Duration_' affects how long the interpolation will take when changing the rate of time.
  - '_Default Pause Interpolation Duration_' affects how long the interpolation will take when pausing, which is changing the rate of time from your chosen value to zero.
  - '_Default Unpause Interpolation Duration_' affects how long the interpolation will take when unpausing, which is changing the rate of time from zero to your chosen value.

## Video

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
