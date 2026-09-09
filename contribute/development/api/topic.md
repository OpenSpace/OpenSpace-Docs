# Creating a new OpenSpace Topic
This guide explains what a Topic is and how to create one: writing a schema and registering it in the engine. Once a Topic is created, see [Update TypeScript types from OpenSpace build](./update-typescript-types.md) for how to generate and publish the corresponding TypeScript types in [`openspace-api-js`](https://github.com/OpenSpace/openspace-api-js) so consuming repositories (for example, the [WebGui](https://github.com/OpenSpace/OpenSpace-WebGui)) can use them.

## What is a Topic?
TODO: Add a short explanation of what a Topic is, how it fits the OpenSpace API, our philosophy of using Lua functions, vs Topics, vs Events. Do we also want to include a link or something to our existing Topics?

## 1. Create the Topic
Write a schema for the new Topic (see [Writing a JSON Schema](https://github.com/OpenSpace/OpenSpace/tree/master/support/types#writing-a-json-schema) for a detailed how-to guide).

## 2. Register the Topic in the engine
1. Register the Topic class in `src/topic/server.cpp` with a unique ID, e.g., `propertyTree`.
1. Add the schema to `registerCoreSchemas` in `core_registration.cpp`.

## Using the Topic
The Topic is used via the [JavaScript](https://github.com/OpenSpace/openspace-api-js) or [Python](https://github.com/OpenSpace/openspace-api-python) APIs. Use the same ID registered in step #2 to start the Topic.
