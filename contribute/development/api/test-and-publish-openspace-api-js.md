# Testing and Publishing Changes to `openspace-api-js`
This guide covers how to try out local changes to [`openspace-api-js`](https://github.com/OpenSpace/openspace-api-js), such as newly generated types, in a consuming repository (for example, the [WebGui](https://github.com/OpenSpace/OpenSpace-WebGui)), and how to publish those changes as a prerelease or stable release. It applies to any change to the package, for example, new Topics, updated Lua library functions, bug fixes, and other API changes.

## 1. Test local changes in a consuming repository
1. In the `openspace-api-js` repository, run `npm pack`. This creates a tarball, e.g., `openspace-api-js-x.x.x.tgz`.
1. In the consuming repository, run `npm install <path-to-openspace-api-js-x.x.x.tgz>` to install it as a local dependency pointing at your build.

## 2. Publish a prerelease package for testing
1. Bump to a prerelease version:
   - For a new prerelease, set an explicit version:
     ```sh
     npm version x.x.x-dev.0 --no-git-tag-version
     ```
     `--no-git-tag-version` avoids immediately committing the version bump.
   - To iterate on an existing prerelease (e.g., new Lua definitions, a new Topic), bump the prerelease number instead of jumping to a new patch/minor/major version:
     ```sh
     npm version prerelease --preid=dev --no-git-tag-version
     ```
     This bumps, for example, `1.0.3-dev.0` to `1.0.3-dev.1`.
1. Publish under the `dev` tag:
   ```sh
   npm publish --tag dev
   ```
   This ensures the prerelease is not installed by a plain `npm install openspace-api-js`.
1. Consumers can install it with `npm install openspace-api-js@dev`, or a specific version with `npm install openspace-api-js@1.0.3-dev.0`.

## 3. Upgrade from a prerelease to a stable release
When ready to promote a prerelease to a stable release, run:
```sh
npm version 1.0.3 --no-git-tag-version
npm publish
```

If you instead want to change which already-published *stable* version installs by default (without publishing again), repoint the `latest` dist-tag to that stable version, for example:
```sh
npm dist-tag add openspace-api-js@1.0.3 latest
```
Note that this only changes what `npm install openspace-api-js` resolves to. It does not turn a prerelease into a stable release.

:::{note}
**Versioning:** version numbers follow [semantic versioning](https://semver.org/), `major.minor.patch` (e.g., `1.0.3`). Use `npm version patch`, `npm version minor`, or `npm version major` for stable releases depending on the scope of the change, and the prerelease commands above for `-dev` builds. This bumps the corresponding version number by 1.

Again use `--no-git-tag-version` to avoid automatically committing the change.
:::
