# Creating a new OpenSpace Topic
This guide walks through the full process of adding a new Topic to OpenSpace: registering it in the engine, generating the corresponding TypeScript types in [`openspace-api-js`](https://github.com/OpenSpace/openspace-api-js), and publishing those types so consuming repositories (e.g. the WebGUI) can use them.

## 1. Create the Topic
1. Write a schema for the new Topic.
1. See [Writing a JSON Schema](https://github.com/OpenSpace/OpenSpace/tree/master/support/types#writing-a-json-schema) for a detailed how-to guide.

## 2. Register the Topic in the engine
1. Register the Topic class in `server.cpp` with a unique id, e.g. `propertyTree`.
1. Add the schema to `registerCoreSchemas` in `core_registration.cpp`.

## 3. Generate the updated JSON schemas
1. Run OpenSpace's `DocsWriter`. This writes all JSON schemas into `<OpenSpace>/support/types`.

## 4. Generate the TypeScript types
1. Generate TypeScript types from the updated JSON schemas — see openspace-api-js's [Generating types from your OpenSpace build](https://github.com/OpenSpace/openspace-api-js#generating-types-from-your-openspace-build) section for the exact command and prerequisites.

## 5. Try the new types in a consuming repository
1. In the `openspace-api-js` repository, run `npm pack`. This creates a tarball, e.g. `openspace-api-js-x.x.x.tgz`.
1. In the consuming repository, run `npm install <path-to-openspace-api-js-x.x.x.tgz>` to install it as a local dependency pointing at your build.

## 6. Publish the updated `openspace-api-js` package
See the [detailed steps](./test-and-publish-openspace-api-js.md) on how to publish the updated npm package.
