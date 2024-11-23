



(core_mission_mission)=
# MissionPhase




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

*   - `Name`
    - The human readable name of this mission or mission phase that is displayed to the user
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Actions`
    - Actions associated with this phase
    - `Table`
    
    -   [Table parameters](#MissionPhaseActions-target) 
    
    - Yes
    
*   - `Description`
    - A description of this mission or mission phase
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Image`
    - An image that can be presented to the user during this phase of a mission
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Link`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Milestones`
    - 
    - `Table`
    
    -   [Table parameters](#MissionPhaseMilestones-target) 
    
    - Yes
    
*   - `Phases`
    - The phases into which this mission or mission phase is separated
    - `Table`
    
    -   [Table parameters](#MissionPhasePhases-target) 
    
    - Yes
    
*   - `TimeRange`
    - The time range for which this mission or mission phase is valid. If no time range is specified, the ranges of sub mission phases are used instead
    - `Table`
    
    -   [Table parameters](#MissionPhaseTimeRange-target) 
    
    - Yes
    
:::









(MissionPhaseActions-target)=
::::{dropdown} Table parameters for `Actions`
Actions associated with this phase


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



::::










(MissionPhaseMilestones-target)=
::::{dropdown} Table parameters for `Milestones`



* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - Important dates
    - `Table`
    
    -   [Table parameters](#MissionPhaseMilestones*-target) 
    
    - Yes
    
:::



(MissionPhaseMilestones*-target)=
#### Table parameters for `*`
Important dates


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Actions`
    - 
    - `Table`
    
    -   [Table parameters](#MissionPhase*Actions-target) 
    
    - Yes
    
*   - `Date`
    - An image that can be presented to the user during this phase of a mission
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Description`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Image`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Link`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Name`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
:::



(MissionPhase*Actions-target)=
#### Table parameters for `Actions`



* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::





::::




(MissionPhasePhases-target)=
::::{dropdown} Table parameters for `Phases`
The phases into which this mission or mission phase is separated


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `Table`
    
    - [MissionPhase](#core_mission_mission)
    
    - Yes
    
:::



::::




(MissionPhaseTimeRange-target)=
::::{dropdown} Table parameters for `TimeRange`
The time range for which this mission or mission phase is valid. If no time range is specified, the ranges of sub mission phases are used instead


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `End`
    - 
    - `String`
    
    - A string representing a valid date 
    
    - Yes
    
*   - `Start`
    - 
    - `String`
    
    - A string representing a valid date 
    
    - {bdg-info}`No`
    
:::



::::



