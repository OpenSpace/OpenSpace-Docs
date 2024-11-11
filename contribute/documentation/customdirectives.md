# Custom directives

We have created custom Sphinx directives for the documentation.

:::{dossier}
:census: 1 all-sky image
:assetfile: data/assets/scene/digitaluniverse/allsky_hydrogenalpha.asset
:openspaceversion: 1
:preparedby: Doug Finkbeiner (Princeton), Brian Abbott (AMNH)
:sourceversion: 2.01
:license: cc-by
:reference: A Composite H-alpha Template for Microwave Foreground Prediction=https://doi.org/10.1086/374411;Bar=https://example.org/bar;John Doe
:::

To use this, you need a Sphinx version of at least [7.4](https://www.sphinx-doc.org/en/master/changes/7.4.html). To upgrade, run

```
pip install -r "requirements.txt"
```

The example above was created with the following code:

```md
:::{dossier}
:census: 1 all-sky image
:assetfile: data/assets/scene/digitaluniverse/allsky_hydrogenalpha.asset
:openspaceversion: 1
:preparedby: Doug Finkbeiner (Princeton), Brian Abbott (AMNH)
:sourceversion: 2.01
:license: cc-by
:reference: A Composite H-alpha Template for Microwave Foreground Prediction=https://doi.org/10.1086/374411;Bar=https://example.org/bar;John Doe
:::
```

All arguments are optional. The references are separated by `;` and can be either a name with a link or just a name. If the name has a link, place the name like so: `name=link`. The link can be an internal link to the docs page or an external link. License can be one of: `amnh`, `cc-by`, and `mit`.
