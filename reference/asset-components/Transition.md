



(statemachine_transition)=
# Transition




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

*   - `From`
    - The identifier of the state that can trigger the transition
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `To`
    - The identifier of the state that the state machine will move to after the transition
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Action`
    - A string containing a Lua script that will be executed when the transition is triggered
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::












