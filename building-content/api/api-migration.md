# Migrating to the OpenSpace JavaScript API 1.0.0
This guide outlines the required changes when upgrading from the old (unversioned) OpenSpace JavaScript API to the latest version (1.0.0), introduced in OpenSpace version 0.22.0. These include breaking changes, so existing integrations of the API will need to be updated.

## Migration Summary
  - Replace `singleReturnLibrary()` and `multiReturnLibrary()` with `library()` [details](#singlereturnlibrary-and-multireturnlibrary---removed)
  - Remove any usage of `library(boolean)` [details](#libraryboolean---simplified)
  - Replace `topic.iterator()` with direct iteration over `topic` [details](#topic-iteration---simplified)
  - Replace `topic.iterator().next()` with `topic.next()` [details](#topic-iteration---simplified)
  - Remove `[1]` when accessing Lua return values [details](#lua-return-values---simplified)


## Installation
### npm
If you are using npm, update to the latest version:
```sh
npm install openspace-api-js@0.9.11
```

### Script tag
If you are including the API via a script tag, the preferred approach is to load it directly from the OpenSpace CDN:
```html
<script type="text/javascript" src="https://liu-se.cdn.openspaceproject.com/api/1.0.0/openspace-api.js"></script>
```

If you require an offline-capable version, download the [latest release](https://github.com/OpenSpace/openspace-api-js/blob/master/dist/openspace-api.js) and serve it locally:
```html
<script type="text/javascript" src="openspace-api.js"></script>
```

## API Changes
### `singleReturnLibrary` and `multiReturnLibrary` - removed
The separate library constructors have been unified into a single method.

```js
// Before - single return
const openspace = api.singleReturnLibrary();
openspace.setPropertyValueSingle("someprop", true);
```
```js
// Before - multi return
const openspace = api.multiReturnLibrary();
openspace.setPropertyValueSingle("someprop", true);
```

```js
// After
const openspace = api.library();
openspace.setPropertyValueSingle("someprop", true);
```

### `library(boolean)` - simplified
The boolean parameter is no longer supported.

```js
// Before
const openspace = api.library(true);
const openspace = api.library(false);
```

```js
// After
const openspace = api.library();
```

### Topic iteration - simplified
The `.iterator()` function is removed and instead `Topics` are now directly async iterable.

```js
// Before
const topic = api.subscribeToProperty("Scene.Earth.Scale.Scale");

for await (const data of topic.iterator()) {
  console.log(data.value);
}
```

```js
// After
const topic = api.subscribeToProperty("Scene.Earth.Scale.Scale");

for await (const data of topic) {
  console.log(data.value);
}
```

As a result, `iterator.next()` is no longer valid. A new function `topic.next()` can be used to await and access the next data value.

```js
// Before
const topic = api.subscribeToProperty("Scene.Earth.Scale.Scale");

const data = await topic.iterator().next();
console.log(data.value.value);
```

```js
// After
const topic = api.subscribeToProperty("Scene.Earth.Scale.Scale");

const data = await topic.next();
console.log(data.value);
```

### Lua return values - simplified
Lua return values are no longer wrapped under key `[1]`. Values are now returned directly.
> If you previously used `singleReturnLibrary()` no changes are necessary - this behavior is now the default.

```js
// Before
const openspace = api.library();
const value = await openspace.time.currentTime();
const time = value[1];

// Or accessed directly
const openspace = api.library();
const time = await openspace.time.currentTime()[1];
```

```js
// After
const openspace = api.library();
const time = await openspace.time.currentTime();
```
