# Update API
This guide outlines the required changes when upgrading from the old (unversioned) OpenSpace JavaScript API to the latest version (1.0.0). These include breaking changes, so existing integrations will need to be updated.

## Migration Summary
  - Replace `singleReturnLibrary()` and `multiReturnLibrary()` with `library()`
  - Remove any usage of `library(boolean)`
  - Replace `topic.iterator()` with direct iteration over `topic`
  - Replace `topic.iterator().next()` with `topic.next()`
  - Remove `[1]` when accessing Lua return values


## Installation
### npm
If you are using npm, update to the latest version:
```sh
npm install openspace-api-js@0.9.11
```
### Script tag
If you are including the API via a script tag, replace your existing file with the [latest version](https://github.com/OpenSpace/openspace-api-js/blob/master/dist/openspace-api.js):
```html
<script type="text/javascript" src="openspace-api.js"></script>
```

## API Changes
### `singleReturnLibrary` and `multiReturnLibrary` - removed
The separate library constructors have been unified into a single method.

Before
```js
const openspace = api.singleReturnLibrary();
openspace.setPropertyValueSingle("someprop", true);
```
```js
const openspace = api.multiReturnLibrary();
openspace.setPropertyValueSingle("someprop", true);
```

After
```js
const openspace = api.library();
openspace.setPropertyValueSingle("someprop", true);
```

### `library(boolean)` - simplified
The boolean parameter is no longer supported.

Before
```js
const openspace = api.library(true);
const openspace = api.library(false);
```

After
```js
const openspace = api.library();
```
### Topic iteration - simplified
The `.iterator()` function is removed and instead `Topics` are now directly async iterable.

Before
```js
const topic = api.subscribeToProperty("Scene.Earth.Scale.Scale");

for await (const data of topic.iterator()) {
  console.log(data.value);
}
```

After
```js
const topic = api.subscribeToProperty("Scene.Earth.Scale.Scale");

for await (const data of topic) {
  console.log(data.value);
}
```

As a result, `iterator.next()` is no longer valid. A new function `topic.next()` can be used to await and access the next data value.

Before
```js
const topic = api.subscribeToProperty("Scene.Earth.Scale.Scale");

const data = await topic.iterator().next();
console.log(data.value.value);
```

After
```js
const topic = api.subscribeToProperty("Scene.Earth.Scale.Scale");

const data = await topic.next();
console.log(data.value);
```
### Lua return values - simplified
Lua return values are no longer wrapped under key `[1]`. Values are now returned directly.
> If you previously used `singleReturnLibrary()` no changes are necessary - this behavior is now the default.

Before
```js
const openspace = api.library();
const value = await openspace.time.currentTime();
const time = value[1];

// Or accessed directly
const openspace = api.library();
const time = await openspace.time.currentTime()[1];
```

After
```js
const openspace = api.library();
const time = await openspace.time.currentTime();
```
