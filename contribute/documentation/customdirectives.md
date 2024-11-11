# Custom directives

We have created custom Sphinx directives for the documentation.

:::{dossier}
:census: 1 all-sky image
:assetfile: data/assets/scene/digitaluniverse/allsky_hydrogenalpha.asset
:openspaceversion: 1
:preparedby: Doug Finkbeiner (Princeton), Brian Abbott (AMNH)
:sourceversion: 2.02
:license: mit

[A Composite H-alpha Template for Microwave Foreground Prediction](https://doi.org/10.1086/374411)
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
:sourceversion: 2.02
:license: amnh

[A Composite H-alpha Template for Microwave Foreground Prediction](https://doi.org/10.1086/374411)
:::
```

All arguments are optional. The references are placed in the content of the directive.
This is so we can include links in the references. License can be one of: `amnh`, `cc-by`, and `mit`.
