# `openspace.event`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`disableEvent`](#eventdisableEvent-target)
    - [Disables the event with the provided identifier]{#eventdisableEvent-list}


*   - [`enableEvent`](#eventenableEvent-target)
    - [Enables the event with the provided identifier]{#eventenableEvent-list}


*   - [`registeredEvents`](#eventregisteredEvents-target)
    - [Returns the list of registered events]{#eventregisteredEvents-list}


*   - [`registerEventAction`](#eventregisterEventAction-target)
    - [Registers an action to be executed whenever an event is encountered]{#eventregisterEventAction-list}


*   - [`unregisterEventAction`](#eventunregisterEventAction-target)
    - [Unregisters a specific combination of event, action, and potentially a filter]{#eventunregisterEventAction-list}

:::

## Functions

(eventdisableEvent-target)=
### [`disableEvent`](#eventdisableEvent-list)
Disables the event with the provided identifier.


:::{card} Parameters


* identifier `Integer` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.event.disableEvent(identifier)
:::
___

(eventenableEvent-target)=
### [`enableEvent`](#eventenableEvent-list)
Enables the event with the provided identifier.


:::{card} Parameters


* identifier `Integer` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.event.enableEvent(identifier)
:::
___

(eventregisteredEvents-target)=
### [`registeredEvents`](#eventregisteredEvents-list)
Returns the list of registered events.


Return type: `Table[]` 

:::{code-block} lua
:caption: Signature
openspace.event.registeredEvents()
:::
___

(eventregisterEventAction-target)=
### [`registerEventAction`](#eventregisterEventAction-list)
Registers an action to be executed whenever an event is encountered. If the optional third parameter is provided, it describes a filter that the event is being checked against and only if it passes the filter, the action is triggered.


:::{card} Parameters


* event `String` 



* action `String` 



* filter `Table?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.event.registerEventAction(event, action, filter)
:::
___

(eventunregisterEventAction-target)=
### [`unregisterEventAction`](#eventunregisterEventAction-list)
Unregisters a specific combination of event, action, and potentially a filter.


:::{card} Parameters


* event `String` 



* action `String` 



* filter `Table?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.event.unregisterEventAction(event, action, filter)
:::

