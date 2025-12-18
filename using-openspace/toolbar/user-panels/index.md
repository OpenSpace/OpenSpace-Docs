# User Panels

![User Panels Button](/using-openspace/toolbar/user-panels/toolbar_button_user_panels.png)

User Panels in OpenSpace are custom panels that are developed by users outside of the OpenSpace development team. They allow custom functionality within OpenSpace. By default, OpenSpace does not ship with any such panels, but panels may be available on the [OpenSpace Hub](https://hub.openspaceproject.com/).

:::{figure} user-panels.png
:align: center
:width: 60%
:figwidth: 80%
:alt: OpenSpace's User Panels Panel

The User Panels Panel in OpenSpace.
:::


:::{note}
We will cover some basics of building a user panel in a future article.
:::



## Location
Whether you develop one yourself or download one from the Hub, they appear in the `OpenSpace/user/webpanels` folder. 


## Open a User Panel
If you have a user panel in that folder, you can access it within OpenSpace's User Panels Panel via the dropdown under Open Local Panel. With a panel selected, open is via the {octicon}`link-external;1em` button.

## Open From a URL

You can also open a panel from a URL. A user panel is merely an HTML page, so it is possible to host these on the web and access them via a URL. Adding the URL and a title, then hitting the open button {octicon}`link-external;1em` will also open the panel alongside the User Panels.

## Links
We include two links in this panel: one for the [OpenSpace Hub](https://hub.openspaceproject.com/) and one for the [Show Composer](http://localhost:4680/showcomposer/). These will open in a new panel and will benefit from expanding the width of the panel.

:::{admonition} Show Composer
We will cover the Show Composer in a future article.
:::