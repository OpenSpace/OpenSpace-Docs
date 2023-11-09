# Welcome to OpenSpace's documentation!

Welcome to the official documentation for [OpenSpace](https://openspaceproject.com), which is an open-source interactive data visualization software designed to visualize the entire known universe and portray our ongoing efforts to investigate the cosmos covering all possible scales.

In addition to the documentation provided here, you are very welcome on our [Slack channel](https://openspacesupport.slack.com) to which you can freely [sign-up](https://join.slack.com/t/openspacesupport/shared_invite/enQtMjUxNzUyMTQ1ODQxLTRmNDI1YTA4ODkzODUyODE0YjIzODU0NWU1NGY1NWIzZDUzMDgwM2VkYmE1ZGY3MmU2OWI5NzhlN2U3NWU2NTQ).

On the left you can find a table of contents that allows you to access the individual topics of interest. The table also contains a search function to search through the available pages. If you are new to _OpenSpace_, we'd recommend you to start in the [Getting Started](getting-started/introduction/index) section.

The overall structure of the documentation is as follows:

 - General

   Information about the different versions of OpenSpace, such as changelogs between versions or academic publications that came out of the project

 - Users

   A collection of pages that are applicable to general users of OpenSpace, including information abuot how to use the software or how to get started

 - Development

   Information that is predominantly aimed at developers that want to contribute to the C++ source code of OpenSpace and/or compile the software from [GitHub](https://github.com/OpenSpace/OpenSpace)

 - Tutorials

   Informational tutorials that run the users through the initial steps of setting up OpenSpace. The tutorials are provided with both text and video

 - Support

   A collection of pages that do not contain any information about OpenSpace, but that are helpful to write the documentation itself.

## Get involved
OpenSpace is an open-source project and relies on the contribution by a community of volunteers. In particular, the documentation always needs feedback and help. If you come across errors in the documentation, find something that is unclear, or lack essential information, help us to make the documentation better by either letting us know in the `#documentation` channel of the [Slack channel](https://openspacesupport.slack.com) or by suggesting a change on the [GitHub](https://github.com/OpenSpace/OpenSpace-Docs) of the documentation.

:::{toctree}
:caption: General
:name: sec-general
:maxdepth: 2
:hidden:
:titlesonly:

releases/index
general/academics
:::

:::{toctree}
:caption: Getting Started
:name: sec-gettingstarted
:maxdepth: 2
:hidden:
:titlesonly:

getting-started/introduction/index
getting-started/profiles/index
:::

:::{toctree}
:caption: Users
:name: sec-users
:maxdepth: 2
:hidden:
:titlesonly:

users/commandline
users/kiosk
users/handling-errors
users/hardware-requirements
users/faq
:::

:::{toctree}
:caption: Manual
:name: sec-manual
:maxdepth: 2
:hidden:
:titlesonly:

manual/navigation/index
manual/assets/index
manual/content/index
manual/data-distribution
:::

:::{toctree}
:caption: Development
:name: sec-dev
:maxdepth: 2
:hidden:
:titlesonly:

dev/index
dev/coding-style
dev/concepts
dev/git
dev/folder-layout
dev/pull-requests
dev/cpp-musings
dev/deploying-windows
dev/faq
:::

:::{toctree}
:caption: Tutorials
:name: sec-tutorials
:maxdepth: 1
:hidden:

tutorials/users/index
tutorials/installers/index
tutorials/builders/index
:::


:::{toctree}
:caption: Support
:name: sec-support
:maxdepth: 1
:hidden:
:glob:

support/*
:::
