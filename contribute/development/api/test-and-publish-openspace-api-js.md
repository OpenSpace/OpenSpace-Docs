# Testing and Publishing `openspace-api-js` Changes
This guide covers how to try out local changes to [`openspace-api-js`](https://github.com/OpenSpace/openspace-api-js), such as newly generated types, in a consuming repository, and how to publish those changes as a prerelease or stable release. It applies to any change to the package (new Topics, updated Lua library functions, bug fixes, etc.), not just Topic creation.

## 1. Try the new types in a consuming repository
1. In the `openspace-api-js` repository, run `npm pack`. This creates a tarball, e.g. `openspace-api-js-x.x.x.tgz`.
1. In the consuming repository, run `npm install <path-to-openspace-api-js-x.x.x.tgz>` to install it as a local dependency pointing at your build.

## 2. Publish the updated package
1. Bump to a prerelease version:
   - For a new prerelease, set an explicit version:
     ```sh
     npm version x.x.x-dev.0 --no-git-tag-version
     ```
     `--no-git-tag-version` avoids immediately committing the version bump.
   - To iterate on an existing prerelease (e.g. new Lua definitions, a new Topic), bump the prerelease number instead of jumping to a new patch/minor/major version:
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
1. When ready to promote a prerelease to a stable release:
   ```sh
   npm version 1.0.3 --no-git-tag-version
   npm publish
   ```
   If the already-published prerelease build is good as-is, you can skip republishing and just repoint the tag:
   ```sh
   npm dist-tag add openspace-api-js@1.0.3-dev.0 latest
   ```
