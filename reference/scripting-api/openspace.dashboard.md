# `openspace.dashboard`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`addDashboardItem`](#dashboardaddDashboardItem-target)
    - [Adds a new dashboard item to the main dashboard]{#dashboardaddDashboardItem-list}


*   - [`addDashboardItemToScreenSpace`](#dashboardaddDashboardItemToScreenSpace-target)
    - [Adds a new dashboard item to an existing SceenSpaceDashboard]{#dashboardaddDashboardItemToScreenSpace-list}


*   - [`clearDashboardItems`](#dashboardclearDashboardItems-target)
    - [Removes all dashboard items from the main dashboard]{#dashboardclearDashboardItems-list}


*   - [`removeDashboardItem`](#dashboardremoveDashboardItem-target)
    - [Removes the dashboard item with the specified identifier]{#dashboardremoveDashboardItem-list}


*   - [`removeDashboardItemsFromScreenSpace`](#dashboardremoveDashboardItemsFromScreenSpace-target)
    - [Removes all dashboard items from an existing ScreenSpaceDashboard]{#dashboardremoveDashboardItemsFromScreenSpace-list}

:::

## Functions

(dashboardaddDashboardItem-target)=
### [`addDashboardItem`](#dashboardaddDashboardItem-list)
Adds a new dashboard item to the main dashboard.


:::{card} Parameters


* dashboard `Table` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.dashboard.addDashboardItem(dashboard)
:::
___

(dashboardaddDashboardItemToScreenSpace-target)=
### [`addDashboardItemToScreenSpace`](#dashboardaddDashboardItemToScreenSpace-list)
Adds a new dashboard item to an existing SceenSpaceDashboard.


:::{card} Parameters


* identifier `String` 



* dashboard `Table` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.dashboard.addDashboardItemToScreenSpace(identifier, dashboard)
:::
___

(dashboardclearDashboardItems-target)=
### [`clearDashboardItems`](#dashboardclearDashboardItems-list)
Removes all dashboard items from the main dashboard.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.dashboard.clearDashboardItems()
:::
___

(dashboardremoveDashboardItem-target)=
### [`removeDashboardItem`](#dashboardremoveDashboardItem-list)
Removes the dashboard item with the specified identifier.


:::{card} Parameters


* identifier `String | Table` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.dashboard.removeDashboardItem(identifier)
:::
___

(dashboardremoveDashboardItemsFromScreenSpace-target)=
### [`removeDashboardItemsFromScreenSpace`](#dashboardremoveDashboardItemsFromScreenSpace-list)
Removes all dashboard items from an existing ScreenSpaceDashboard.


:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.dashboard.removeDashboardItemsFromScreenSpace(identifier)
:::

