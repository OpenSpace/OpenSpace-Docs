# `openspace.statemachine`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`canGoToState`](#statemachinecanGoToState-target)
    - [Returns true if there is a defined transition between the current state and the given string name of a state, otherwise false]{#statemachinecanGoToState-list}


*   - [`createStateMachine`](#statemachinecreateStateMachine-target)
    - [Creates a state machine from a list of states and transitions]{#statemachinecreateStateMachine-list}


*   - [`currentState`](#statemachinecurrentState-target)
    - [Returns the string name of the current state that the statemachine is in]{#statemachinecurrentState-list}


*   - [`destroyStateMachine`](#statemachinedestroyStateMachine-target)
    - [Destroys the current state machine and deletes all the memory]{#statemachinedestroyStateMachine-list}


*   - [`goToState`](#statemachinegoToState-target)
    - [Triggers a transition from the current state to the state with the given identifier]{#statemachinegoToState-list}


*   - [`possibleTransitions`](#statemachinepossibleTransitions-target)
    - [Returns a list with the identifiers of all the states that can be transitioned to from the current state]{#statemachinepossibleTransitions-list}


*   - [`printCurrentStateInfo`](#statemachineprintCurrentStateInfo-target)
    - [Prints information about the current state and possible transitions to the log]{#statemachineprintCurrentStateInfo-list}


*   - [`saveToDotFile`](#statemachinesaveToDotFile-target)
    - [Saves the current state machine to a ]{#statemachinesaveToDotFile-list}


*   - [`setInitialState`](#statemachinesetInitialState-target)
    - [Immediately sets the current state to the state with the given name, if it exists]{#statemachinesetInitialState-list}

:::

## Functions

(statemachinecanGoToState-target)=
### [`canGoToState`](#statemachinecanGoToState-list)
Returns true if there is a defined transition between the current state and the given string name of a state, otherwise false.


:::{card} Parameters


* state `String` 


:::

Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.statemachine.canGoToState(state)
:::
___

(statemachinecreateStateMachine-target)=
### [`createStateMachine`](#statemachinecreateStateMachine-list)
Creates a state machine from a list of states and transitions. See State and Transition documentation for details. The optional thrid argument is the identifier of the desired initial state. If left out, the first state in the list will be used.


:::{card} Parameters


* states `Table` 



* transitions `Table` 



* startState `String?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.statemachine.createStateMachine(states, transitions, startState)
:::
___

(statemachinecurrentState-target)=
### [`currentState`](#statemachinecurrentState-list)
Returns the string name of the current state that the statemachine is in.


Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.statemachine.currentState()
:::
___

(statemachinedestroyStateMachine-target)=
### [`destroyStateMachine`](#statemachinedestroyStateMachine-list)
Destroys the current state machine and deletes all the memory.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.statemachine.destroyStateMachine()
:::
___

(statemachinegoToState-target)=
### [`goToState`](#statemachinegoToState-list)
Triggers a transition from the current state to the state with the given identifier. Requires that the specified string corresponds to an existing state, and that a transition between the two states exists.


:::{card} Parameters


* newState `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.statemachine.goToState(newState)
:::
___

(statemachinepossibleTransitions-target)=
### [`possibleTransitions`](#statemachinepossibleTransitions-list)
Returns a list with the identifiers of all the states that can be transitioned to from the current state.


Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.statemachine.possibleTransitions()
:::
___

(statemachineprintCurrentStateInfo-target)=
### [`printCurrentStateInfo`](#statemachineprintCurrentStateInfo-list)
Prints information about the current state and possible transitions to the log.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.statemachine.printCurrentStateInfo()
:::
___

(statemachinesaveToDotFile-target)=
### [`saveToDotFile`](#statemachinesaveToDotFile-list)
Saves the current state machine to a .dot file as a directed graph. The resulting graph can be rendered using external tools such as Graphviz. The first parameter is the name of the file, and the second is an optional directory. If no directory is given, the file is saved to the temp folder.


:::{card} Parameters


* filename `String` 



* directory `String?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.statemachine.saveToDotFile(filename, directory)
:::
___

(statemachinesetInitialState-target)=
### [`setInitialState`](#statemachinesetInitialState-list)
Immediately sets the current state to the state with the given name, if it exists. This is done without doing a transition and completely ignores the previous state.


:::{card} Parameters


* startState `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.statemachine.setInitialState(startState)
:::

