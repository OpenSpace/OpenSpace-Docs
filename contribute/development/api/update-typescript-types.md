# Update TypeScript types from OpenSpace build
The [JavaScript API](https://github.com/OpenSpace/openspace-api-js) supports TypeScript types which are generated from JSON schemas. The npm package [`openspace-api-js`](https://github.com/OpenSpace/openspace-api-js) ships with pre-generated types targeting a specific OpenSpace version. These types need to be updated regularly, for example, whenever a Topic's schema is changed, adding a new Topic, or updating the Lua API.

This guide walks through generating the corresponding TypeScript types in `openspace-api-js` from an OpenSpace build, and trying them out in a consuming repository (for example, the [WebGui](https://github.com/OpenSpace/OpenSpace-WebGui)).

## 1. Generate the updated JSON schemas
If a Topic's schema has changed, it needs to be regenerated. Run OpenSpace's `DocsWriter`. This writes all JSON schemas into `<OpenSpace>/support/types`
:::(Note)
Skip this step unless you've changed a Topic's schema.
:::

## 2. Generate the TypeScript types
There are two types that can be generated for the API: [Topic types](https://github.com/OpenSpace/openspace-api-js#topic-types-generate-topic-types) from updated JSON schemas and [Lua API types](https://github.com/OpenSpace/openspace-api-js#lua-library-types-generate-lua-library) from new or updated Lua functions. See `openspace-api-js`'s [Generating types from your OpenSpace build](https://github.com/OpenSpace/openspace-api-js#generating-types-from-your-openspace-build) section for the exact command and prerequisites.

## 3. Test local changes in a consuming repository
1. In the `openspace-api-js` repository, run `npm pack`. This creates a tarball, e.g. `openspace-api-js-x.x.x.tgz`.
1. In the consuming repository, run `npm install <path-to-openspace-api-js-x.x.x.tgz>` to install it as a local dependency pointing at your build.

## 4. Publish the updated package
See the [detailed steps](./test-and-publish-openspace-api-js.md) on how to publish the updated `openspace-api-js` package.
