



(statemachine_statemachine)=
# StateMachine




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

*   - `States`
    - A list of states
    - `Table`
    
    -   [Table parameters](#StateMachineStates-target) 
    
    - {bdg-info}`No`
    
*   - `Transitions`
    - A list of transitions between the different states
    - `Table`
    
    -   [Table parameters](#StateMachineTransitions-target) 
    
    - {bdg-info}`No`
    
*   - `StartState`
    - The initial state of the state machine. Defaults to the first in the list
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::







(StateMachineStates-target)=
::::{dropdown} Table parameters for `States`
A list of states


* Optional: {bdg-info}`No`


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
    
    - [State](#statemachine_state)
    
    - Yes
    
:::



::::




(StateMachineTransitions-target)=
::::{dropdown} Table parameters for `Transitions`
A list of transitions between the different states


* Optional: {bdg-info}`No`


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
    
    - [Transition](#statemachine_transition)
    
    - Yes
    
:::



::::





