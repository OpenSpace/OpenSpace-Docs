# Welcome to OpenSpace's documentation!
Welcome to the official documentation for [OpenSpace](https://openspaceproject.com), which is an open-source interactive data visualization software designed to visualize the entire known universe and portray our ongoing efforts to investigate the cosmos covering all possible scales.

In addition to the documentation provided here, you are very welcome on our [Slack channel](https://openspacesupport.slack.com) to which you can freely [sign-up](https://join.slack.com/t/openspacesupport/shared_invite/enQtMjUxNzUyMTQ1ODQxLTRmNDI1YTA4ODkzODUyODE0YjIzODU0NWU1NGY1NWIzZDUzMDgwM2VkYmE1ZGY3MmU2OWI5NzhlN2U3NWU2NTQ).

On the left you can find a table of contents that allows you to access the individual topics of interest. The table also contains a search function to search through the available pages. If you are new to _OpenSpace_, we'd recommend you to start in the [Getting Started](users/getting-started/index) section.

The overall structure of the documentation is as follows:

  - General

    Information about the different versions of OpenSpace, such as changelogs between versions or academic publications that came out of the project. If you find a publication missing, feel free to add it in a Pull Request on [GitHub](https://github.com/OpenSpace/OpenSpace-Docs) or let us know in the [Slack channel](https://openspacesupport.slack.com).

  - Users

    A collection of pages that are applicable to general users of OpenSpace, including information about how to use the software or how to get started.

  - Manual

    Pages that describe individual subsystems or components of OpenSpace in greater detail. If you want to learn more about concrete elements of OpenSpace, this is the place to be.

  - Tutorials

    Informational tutorials that run the users through the initial steps of setting up OpenSpace. The tutorials are provided with both text and video.

  - How-To

    Practical hands-on guides that show a variety of things that can be achieved with OpenSpace. These are meant to give you the tools to create your own content and also get inspiration about what is possible with the software through examples.

  - Development

    Information that is predominantly aimed at developers that want to contribute to the C++ source code of OpenSpace and/or compile the software from source found on [GitHub](https://github.com/OpenSpace/OpenSpace).

  - Support

    A collection of pages that do not contain any information about OpenSpace itself, but that are helpful for writing the documentation itself.


## Get involved
OpenSpace is an open-source project and relies on the contribution by a community of volunteers. In particular, the documentation always needs feedback and help. If you come across errors in the documentation, find something that is unclear, or lack essential information, help us to make the documentation better by either letting us know in the `#documentation` channel of the [Slack channel](https://openspacesupport.slack.com) or by suggesting a change on the [GitHub](https://github.com/OpenSpace/OpenSpace-Docs) of the documentation.


<!--
  General
-->
:::{toctree}
:caption: General
:maxdepth: 2
:hidden:
:titlesonly:

general/releases/index
general/links
general/academics
:::


<!--
  Users
-->
:::{toctree}
:caption: Users
:maxdepth: 2
:hidden:
:titlesonly:

users/getting-started/index
users/profiles/index
users/console/index
users/handling-errors
users/hardware-requirements
users/faq/index
:::


<!--
  Manual
-->
:::{toctree}
:caption: Manual
:maxdepth: 2
:hidden:
:titlesonly:

manual/navigation/index
manual/assets/index
manual/content/index
manual/properties/index
manual/scenegraph/index
manual/events/index
manual/data-distribution/index
:::


<!--
  Tutorials
-->
:::{toctree}
:caption: Tutorials
:maxdepth: 1
:hidden:

tutorials/users/index
tutorials/installers/index
tutorials/builders/index
:::


<!--
  How-To
-->
:::{toctree}
:caption: How-Tos
:maxdepth: 1
:hidden:

how-to/index
:::


<!--
  Development
-->
:::{toctree}
:caption: Development
:maxdepth: 2
:hidden:
:titlesonly:

dev/compiling/index
dev/tools/index
dev/dependencies/index
dev/coding-style
dev/deploying-windows
dev/folder-layout
dev/pull-requests
dev/branches
dev/cpp-musings
dev/skybrowser
dev/webrtc/index
dev/faq
:::


<!--
  Support
-->
:::{toctree}
:caption: Support
:hidden:

support/kitchensink
support/field-list-example
:::
