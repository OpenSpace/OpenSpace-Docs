



(base_dashboarditem_text)=
# DashboardItemText

_Inherits [DashboardItem](#DashboardItem)_




## Members


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `FontName`
    - This value is the name of the font that is used. It can either refer to an internal name registered previously, or it can refer to a path that is used.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `FontSize`
    - This value determines the size of the font that is used to render the distance.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Text`
    - The text to be displayed.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::













## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 511
asset.require("spice/core") -- openspace.time.advancedTime depends on SPICE
asset.require("scene/solarsystem/planets/earth/atmosphere")



-- Function to advance a time stamp in the given number of days, hours, minutes and
-- seconds. returns the new time stamp
local function advance(time, days, hours, minutes, seconds)
  local result = openspace.time.advancedTime(time, tostring(days) .. "d")
  result = openspace.time.advancedTime(result, tostring(hours) .. "h")
  result = openspace.time.advancedTime(result, tostring(minutes) .. "m")
  result = openspace.time.advancedTime(result, tostring(seconds) .. "s")

  return result
end

local LaunchTime = "2021-12-25T12:20:00.000"
local DetachTime = "2021-12-25T12:50:00.000"

-- JWST timelapse timeline, forwards
local function createForwardTimelapse()
  local timelapse = [[
    -- Mission start, setup 2 sec after, reset night layer
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 0, 0, 0, 2) .. [[",
      "openspace.setPropertyValueSingle(\"Scene.Earth.Renderable.Layers.NightLayers.Earth_at_Night_2012.Settings.Gamma\", 1.0)" ..
      "openspace.setPropertyValueSingle(\"Scene.EarthAtmosphere.Renderable.Enabled\", true)"
    )

    -- Mission start, GO 3 sec after
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 0, 0, 0, 3) .. [[",
      "openspace.time.interpolateDeltaTime(5)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 5 seconds/second\")"
    )

    -- Speed up when reaching higher altitude
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 0, 0, 2, 0) .. [[",
      "openspace.time.interpolateDeltaTime(300)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 5 minutes/second\")"
    )

    -- array deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 0, 0, 30 - 2, 20 - 40) .. [[", -- 2 min 40 sec pre delay
      "openspace.time.interpolateDeltaTime(1)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 1 second/second\")"
    )

    -- array complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 0, 0, 30, 42) .. [[",
      "openspace.time.interpolateDeltaTime(2400)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 40 minutes/second\")"
    )

    -- Make night layer more visible, at around 14:00
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(DetachTime, 0, 1, 10, 0) .. [[",
      "openspace.time.interpolateDeltaTime(7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 2 hours/second\")" ..
      "openspace.setPropertyValueSingle(\"Scene.Earth.Renderable.Layers.NightLayers.Earth_at_Night_2012.Settings.Gamma\", 0.7)" ..
      "openspace.setPropertyValueSingle(\"Scene.EarthAtmosphere.Renderable.Enabled\", false)"
    )

    -- antenna deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
    advance(LaunchTime, 0, 18, 0, 0) .. [[",
      "openspace.time.interpolateDeltaTime(1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 30 minutes/second\")"
    )

    -- antenna complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 0, 23, 39, 0) .. [[",
      "openspace.time.interpolateDeltaTime(18000)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 5 hours/second\")"
    )

    -- fw palette deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 2, 18 - 2, 20, 35) .. [[", -- 2h pre delay so time to interpolate
      "openspace.time.interpolateDeltaTime(3600)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 1 hour/second\")"
    )

    -- fw palette complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 3, 6, 0, 0) .. [[",
      "openspace.time.interpolateDeltaTime(1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 30 minutes/second\")"
    )

    -- r palette deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 3, 8, 51, 0) .. [[",
      "openspace.time.interpolateDeltaTime(1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 30 minutes/second\")"
    )

    -- r palette complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 3, 12, 0, 0) .. [[",
      "openspace.time.interpolateDeltaTime(120)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 2 minutes/second\")"
    )

    -- base rise deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 3, 12, 22, 0) .. [[",
      "openspace.time.interpolateDeltaTime(7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 2 hours/second\")"
    )

    -- base rise complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 4, 17, 35, 0) .. [[",
      "openspace.time.interpolateDeltaTime(1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 30 minutes/second\")"
    )

    -- aft flap deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 4, 21, 0, 0) .. [[",
      "openspace.time.interpolateDeltaTime(600)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 10 minutes/second\")"
    )

    -- aft flap complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 1, 37, 0) .. [[",
      "openspace.time.interpolateDeltaTime(3600)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 1 hour/second\")"
    )

    -- mid booms extend
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 11, 29, 43) .. [[",
      "openspace.time.interpolateDeltaTime(1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 30 minutes/second\")"
    )

    -- first boom stop
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 12, 16, 16) .. [[",
      "openspace.time.interpolateDeltaTime(1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 30 minutes/second\")"
    )

    -- right boom complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 17, 42, 5) .. [[",
      "openspace.time.interpolateDeltaTime(1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 30 minutes/second\")"
    )

    -- left booms complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 22, 6, 0) .. [[",
      "openspace.time.interpolateDeltaTime(30)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 30 seconds/second\")"
    )

    -- tension sun shield membranes
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 22, 9, 14) .. [[",
      "openspace.time.interpolateDeltaTime(60)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 1 minute/second\")"
    )

    -- membrane tension complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 22, 20, 0) .. [[",
      "openspace.time.interpolateDeltaTime(7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 2 hours/second\")"
    )

    -- membranes separate
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 6, 12, 36, 49) .. [[",
      "openspace.time.interpolateDeltaTime(3600)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 1 hour/second\")"
    )

    -- secondary mirror deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 7, 0, 0, 0) .. [[",
      "openspace.time.interpolateDeltaTime(18000)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 5 hours/second\")"
    )

    -- secondary mirror complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 11, 10, 33, 0) .. [[",
      "openspace.time.interpolateDeltaTime(1200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 20 minutes/second\")"
    )

    -- aft radiator deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 11, 12, 20, 48) .. [[",
      "openspace.time.interpolateDeltaTime(1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 30 minutes/second\")"
    )

    -- aft radiator complete, forward
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 11, 16, 5, 0) .. [[",
      "openspace.time.interpolateDeltaTime(7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 2 hours/second\")"
    )

    -- rt cord fold wings deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 12, 9, 30, 0) .. [[",
      "openspace.time.interpolateDeltaTime(7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 2 hours/second\")"
    )

    -- rt cord fold wings complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 13, 12, 40, 48) .. [[",
      "openspace.time.interpolateDeltaTime(7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 2 hours/second\")"
    )

    -- lft cord fold wings deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 13, 23, 0, 0) .. [[",
      "openspace.time.interpolateDeltaTime(7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: 2 hours/second\")"
    )

    -- lft cord fold wings complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 14, 19, 0, 0) .. [[",
      "openspace.time.interpolateDeltaTime(1)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"\")" ..
      "openspace.setPropertyValueSingle(\"Scene.Earth.Renderable.Layers.NightLayers.Earth_at_Night_2012.Settings.Gamma\", 1.0)" ..
      "openspace.setPropertyValueSingle(\"Scene.EarthAtmosphere.Renderable.Enabled\", true)"
    )

    -- Finished, slow down, 1 sec after end
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 14, 19, 0, 2) .. [[",
      "openspace.scriptScheduler.clear(0)"
    )
  ]]

  return timelapse
end





-- JWST timelapse timeline, backwards
local function createBackwardTimelapse()
  local timelapse = [[
    -- Finished
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 0, 0, 30, 20) .. [[",
      "",
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"\")" ..
      "openspace.scriptScheduler.clear(0)"
    )

    -- array complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 0, 0, 30 + 1, 42 + 10) .. [[", -- 1 min 10 sec pre delay so time to interpolate
      "",
      "openspace.time.interpolateDeltaTime(-1)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -1 second/second\")"
    )
    -- array complete, prepare
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 0, 0 + 1, 30 + 10, 42) .. [[", -- 1h 10 min delay for interpolation
      "",
      "openspace.time.interpolateDeltaTime(-120)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -2 minutes/second\")"
    )

    -- Reset night layer, at around 14:00
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(DetachTime, 0, 1 + 1, 10, 0) .. [[", -- 1h pre delay so time to interpolate
      "",
      "openspace.time.interpolateDeltaTime(-2400)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -40 minutes/second\")" ..
      "openspace.setPropertyValueSingle(\"Scene.Earth.Renderable.Layers.NightLayers.Earth_at_Night_2012.Settings.Gamma\", 1.0)" ..
      "openspace.setPropertyValueSingle(\"Scene.EarthAtmosphere.Renderable.Enabled\", true)"
    )

    -- antenna deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
    advance(LaunchTime, 0, 18, 0, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -2 hours/second\")"
    )

    -- antenna complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 0, 23 + 1, 39, 0) .. [[", -- 1h pre delay so time to interpolate
      "",
      "openspace.time.interpolateDeltaTime(-1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -30 minutes/second\")"
    )

    -- fw palette deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 2, 18, 20, 35) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-18000)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -5 hours/second\")"
    )

    -- fw palette complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 3, 6, 0, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-3600)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -1 hour/second\")"
    )

    -- r palette deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 3, 8, 51, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -30 minutes/second\")"
    )

    -- r palette complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 3, 12, 0, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -30 minutes/second\")"
    )

    -- base rise deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 3, 12, 22, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-120)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -2 minutes/second\")"
    )

    -- base rise complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 4, 17, 35, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -2 hours/second\")"
    )

    -- aft flap deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 4, 21, 0, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -30 minutes/second\")"
    )

    -- aft flap complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 1, 37 + 30, 0) .. [[", -- 30 min pre delay so time to interpolate
      "",
      "openspace.time.interpolateDeltaTime(-600)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -10 minutes/second\")"
    )

    -- mid booms extend
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 11, 29, 43) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-3600)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -1 hour/second\")"
    )

    -- first boom stop
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 12, 16, 16) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -30 minutes/second\")"
    )

    -- right boom complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 17, 42, 5) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -30 minutes/second\")"
    )

    -- left booms complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 22, 6, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -30 minutes/second\")"
    )

    -- tension sun shield membranes
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 22, 9, 14) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-30)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -30 seconds/second\")"
    )

    -- membrane tension complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 5, 22, 20, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-60)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -1 minute/second\")"
    )

    -- membranes separate
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 6, 12, 36, 49) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -2 hours/second\")"
    )

    -- secondary mirror deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 7, 0, 0, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-3600)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -1 hour/second\")"
    )

    -- secondary mirror complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 11, 10, 33, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-18000)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -5 hours/second\")"
    )

    -- aft radiator deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 11, 12, 20, 48) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-1200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -20 minutes/second\")"
    )

    -- aft radiator complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 11, 16 + 1, 5, 0) .. [[", -- 1h pre delay so time to interpolate
      "",
      "openspace.time.interpolateDeltaTime(-1800)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -30 minutes/second\")"
    )

    -- rt cord fold wings deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 12, 9, 30, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -2 hours/second\")"
    )

    -- rt cord fold wings complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 13, 12, 40, 48) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -2 hours/second\")"
    )

    -- lft cord fold wings deploy
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 13, 23, 0, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -2 hours/second\")"
    )

    -- lft cord fold wings complete
    openspace.scriptScheduler.loadScheduledScript("]] ..
      advance(LaunchTime, 14, 19, 0, 0) .. [[",
      "",
      "openspace.time.interpolateDeltaTime(-7200)" ..
      "openspace.setPropertyValueSingle(\"Dashboard.JWSTStateText.Text\", \"Time speed: -2 hours/second\")" ..
      "openspace.setPropertyValueSingle(\"Scene.Earth.Renderable.Layers.NightLayers.Earth_at_Night_2012.Settings.Gamma\", 0.7)" ..
      "openspace.setPropertyValueSingle(\"Scene.EarthAtmosphere.Renderable.Enabled\", false)"
    )
  ]]

  return timelapse
end


-- We have define the actual content of these actions in the onInitialize function since
-- the `advanceTime` function is not available at Asset load time and we have to wait
-- until the initialize function for it
local PlayForwards
local PlayDetach
local PlayBackwards
local ClearTimelapse
local ToggleDirection

local Text = {
  Type = "DashboardItemText",
  Identifier = "JWSTStateText",
  GuiName = "JWST State Dashboard Text",
  Text = ""
}


asset.onInitialize(function()
  PlayForwards = {
    Identifier = "os.jwst.PlayForwards",
    Name = "Play JWST from start",
    Command = [[
      openspace.scriptScheduler.clear(0)
      openspace.time.setDeltaTime(1)
      openspace.setPropertyValueSingle("Dashboard.JWSTStateText.Text", "")
      openspace.time.setTime("]] .. advance(LaunchTime, 0, 0, 0, 1) .. [[")
      ]] .. createForwardTimelapse() .. [[
      openspace.time.setDeltaTime(1)
    ]],
    Documentation = "Jump to the JWST launch time and play the timelapse of deployment forward",
    GuiPath = "/JWST",
    IsLocal = false
  }

  PlayDetach = {
    Identifier = "os.jwst.PlayDetach",
    Name = "Play JWST from detach",
    Command = [[
      openspace.scriptScheduler.clear(0)
      openspace.time.setDeltaTime(1)
      openspace.setPropertyValueSingle("Dashboard.JWSTStateText.Text", "")
      openspace.setPropertyValueSingle("Scene.Earth.Renderable.Layers.NightLayers.Earth_at_Night_2012.Settings.Gamma", 1.0)
      openspace.setPropertyValueSingle("Scene.EarthAtmosphere.Renderable.Enabled", true)
      openspace.time.setTime("]] .. DetachTime .. [[")
      ]] .. createForwardTimelapse() .. [[
      openspace.time.setDeltaTime(1)
    ]],
    Documentation = "Jump to the JWST detach time and play the timelapse of deployment forward",
    GuiPath = "/JWST",
    IsLocal = false
  }

  PlayBackwards = {
    Identifier = "os.jwst.PlayBackwards",
    Name = "Play JWST from end",
    Command = [[
      openspace.scriptScheduler.clear(0)
      openspace.time.setDeltaTime(-1)
      openspace.setPropertyValueSingle("Dashboard.JWSTStateText.Text", "")
      openspace.time.setTime("2022 JAN 09 07:20:01")
      ]] .. createBackwardTimelapse() .. [[
      openspace.time.setDeltaTime(-1)
    ]],
    Documentation = "Jump to the end of JWST deployment time and play the timelapse of deployment in reverse",
    GuiPath = "/JWST",
    IsLocal = false
  }

  ClearTimelapse = {
    Identifier = "os.jwst.ClearTimelapse",
    Name = "Clear JWST timelapse",
    Command = [[
      openspace.scriptScheduler.clear(0)
      openspace.setPropertyValueSingle("Dashboard.JWSTStateText.Text", "")
      openspace.setPropertyValueSingle("Scene.Earth.Renderable.Layers.NightLayers.Earth_at_Night_2012.Settings.Gamma", 1.0)
      openspace.setPropertyValueSingle("Scene.EarthAtmosphere.Renderable.Enabled", true)
      local deltaTime = openspace.time.deltaTime()
      if deltaTime >= 0 then
        openspace.time.setDeltaTime(1)
      else
        openspace.time.setDeltaTime(-1)
      end
    ]],
    Documentation = "Set delta time back to realtime and clear the JWST deployment timelapse",
    GuiPath = "/JWST",
    IsLocal = false
  }

  ToggleDirection = {
    Identifier = "os.jwst.ToggleDirection",
    Name = "Toggle forwards / backwards",
    Command = [[
      -- Flip deltatime
      local deltaTime = openspace.time.deltaTime()
      openspace.time.setDeltaTime(-deltaTime)

      -- Switch timelapse script
      if deltaTime < 0 then
        -- Going backwards and switching to forwards
        openspace.scriptScheduler.clear(0)
        ]] .. createForwardTimelapse() .. [[
      else
        -- Going forwards and switching to backwards
        openspace.scriptScheduler.clear(0)
        ]] .. createBackwardTimelapse() .. [[
      end

      -- Update the dashboard text
      local text = openspace.propertyValue("Dashboard.JWSTStateText.Text")
      if string.len(text) > 14 then
        local newText = ""
        if text:sub(13, 13) == "-" then
          newText = text:sub(1,12) .. text:sub(14)
        else
          newText = text:sub(1,12) .. "-" .. text:sub(13)
        end
        openspace.setPropertyValueSingle("Dashboard.JWSTStateText.Text", newText)
      else
        openspace.setPropertyValueSingle("Dashboard.JWSTStateText.Text", "")
      end
    ]],
    Documentation = "Toggle deployment timelapse direction between forwards and backwards",
    GuiPath = "/JWST",
    IsLocal = false
  }

  openspace.action.registerAction(PlayForwards)
  openspace.action.registerAction(PlayDetach)
  openspace.action.registerAction(PlayBackwards)
  openspace.action.registerAction(ClearTimelapse)
  openspace.action.registerAction(ToggleDirection)

  openspace.dashboard.addDashboardItem(Text)
end)

asset.onDeinitialize(function()
  openspace.scriptScheduler.clear()
  openspace.dashboard.removeDashboardItem(Text)

  openspace.action.removeAction(PlayForwards)
  openspace.action.removeAction(PlayDetach)
  openspace.action.removeAction(PlayBackwards)
  openspace.action.removeAction(ClearTimelapse)
  openspace.action.removeAction(ToggleDirection)
end)



asset.meta = {
  Name = "James Webb Space Telescope Timelapse",
  Description = [[
    Scripts that are scheduled to alter the speed of the simulation time so the deployment
    of the James Webb Space Telescope looks smoother.
  ]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


