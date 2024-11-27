



(statemachine_state)=
# State




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

*   - `Identifier`
    - A string that will be used to identify the state. Cannot be the same as any other state in the machine
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Enter`
    - A string containing a Lua script that will be executed when the state is entered, i.e on a transition from another state
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Exit`
    - A string containing a Lua script that will be executed when the state is exited, i.e on a transition to another state
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::












