# `openspace.action`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`action`](#actionaction-target)
    - [Returns information about the action as a table with the keys 'Identifier', 'Command', 'Name', 'Documentation', 'GuiPath', and 'Synchronization']{#actionaction-list}


*   - [`actions`](#actionactions-target)
    - [Returns all registered actions in the system as a table of tables each containing the keys 'Identifier', 'Command', 'Name', 'Documentation', 'GuiPath', and 'Synchronization']{#actionactions-list}


*   - [`hasAction`](#actionhasAction-target)
    - [Checks if the passed identifier corresponds to an action]{#actionhasAction-list}


*   - [`registerAction`](#actionregisterAction-target)
    - [Registers a new action]{#actionregisterAction-list}


*   - [`removeAction`](#actionremoveAction-target)
    - [Removes an existing action from the list of possible actions]{#actionremoveAction-list}


*   - [`triggerAction`](#actiontriggerAction-target)
    - [Triggers the action given by the specified identifier]{#actiontriggerAction-list}

:::

## Functions

(actionaction-target)=
### [`action`](#actionaction-list)
Returns information about the action as a table with the keys 'Identifier', 'Command', 'Name', 'Documentation', 'GuiPath', and 'Synchronization'.


:::{card} Parameters


* identifier `String` 


:::

Return type: `Table` 

:::{code-block} lua
:caption: Signature
openspace.action.action(identifier)
:::
___

(actionactions-target)=
### [`actions`](#actionactions-list)
Returns all registered actions in the system as a table of tables each containing the keys 'Identifier', 'Command', 'Name', 'Documentation', 'GuiPath', and 'Synchronization'.


Return type: `Table[]` 

:::{code-block} lua
:caption: Signature
openspace.action.actions()
:::
___

(actionhasAction-target)=
### [`hasAction`](#actionhasAction-list)
Checks if the passed identifier corresponds to an action.


:::{card} Parameters


* identifier `String` 


:::

Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.action.hasAction(identifier)
:::
___

(actionregisterAction-target)=
### [`registerAction`](#actionregisterAction-list)
Registers a new action. The first argument is the identifier which cannot have been used to register a previous action before, the second argument is the Lua command that is to be executed, and the optional third argument is the name used in a user-interface to refer to this action. The fourth is a human readable description of the command for documentation purposes. The fifth is the GUI path and the last parameter determines whether the action should be executed locally (= false) or remotely (= true, the default).


:::{card} Parameters


* action `Action` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.action.registerAction(action)
:::
___

(actionremoveAction-target)=
### [`removeAction`](#actionremoveAction-list)
Removes an existing action from the list of possible actions. The action is identifies either by the passed name, or if it is a table, the value behind the 'Identifier' key is extract and used instead.


:::{card} Parameters


* action `String | Table` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.action.removeAction(action)
:::
___

(actiontriggerAction-target)=
### [`triggerAction`](#actiontriggerAction-list)
Triggers the action given by the specified identifier.


:::{card} Parameters


* id `String` 



* arg `Table?` - Default value: `ghoul::Dictionary()` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.action.triggerAction(id, arg)
:::

