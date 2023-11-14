# Pull Requests
This article is mostly aimed at the internal OpenSpace developers, but would be recommended practice for outside contributors as well.

Due to our branching model, which is adapted from [here](http://nvie.com/posts/a-successful-git-branching-model), all features for which Pull Requests are relevant will have been developed in a specific feature branch of the form `feature/<feature-name>`. Especially for independent features, we want to keep the number of commits in the Git history reasonably low but still allow for continuous commits during the development. To square this circle there are two methods:

  1. If the individual commits have not been pushed to the server, it is possible to squash the commits interactively (see [here](https://ariejan.net/2011/07/05/git-squash-your-latests-commits-into-one), then push one commit to the server and use that as the version for the Pull Request.
  1. If the individual commits have already been pushed to the server (the preferred way), it is better to merge all commits into a single new one in a separate branch and use that as the version for the Pull Request.

Alternatively, if there is a fix for a specific issue, the branch should be `issue/<issue-number>` with the issue number being the number of the GitHub issue.

In either way, the commits that happen directly to the `master` branch should be kept to an absolute minimum to ensure that the branch can always be compiled.
