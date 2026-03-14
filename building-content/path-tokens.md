# Path Tokens
Path Tokens are a string-substitution system in OpenSpace that maps short, symbolic names to actual file-system locations. Instead of writing absolute paths that are tied to a specific machine or folder layout, you write a token such as `${SYNC}` or `${USER_ASSETS}`, and OpenSpace resolves it to the correct directory at runtime. This makes every path in your assets, profiles, and scripts portable across different machines, operating systems, and installation layouts.

### Why Path Tokens Exist
OpenSpace installations can vary significantly: the application might live in different directories on different computers, large data sets might be stored on a separate drive, and user-created content should survive application upgrades. Hard-coding absolute paths would break as soon as any of these conditions change. Path tokens solve this by introducing a layer of indirection — a token always points to the right place for the current installation, regardless of where that happens to be on disk.

### Common Use Cases
- **Keeping user content separate from the installation.** The `${USER}` tree (`${USER_ASSETS}`, `${USER_PROFILES}`, `${USER_CONFIG}`, …) is deliberately outside the core application folders. This means you can update or reinstall OpenSpace without losing your personal assets, profiles, recordings, or screenshots.
- **Storing large data on a different drive.** The sync folder can grow very large. By setting the `OPENSPACE_SYNC` environment variable you can redirect `${SYNC}` to a spacious secondary disk while keeping the rest of the installation on a faster primary drive.
- **Planetarium and multi-machine deployments.** In a dome or cluster environment, administrators often point `${SYNC}` or `${USER}` to a shared network location so that every rendering node resolves the same data without duplicating it locally.

### Where Tokens Are Defined
The default set of path tokens is defined in the `openspace.cfg` configuration file in the `Paths` table. This is the only place where tokens are declared as part of the static configuration. Tokens can also be added or overridden at runtime using the Lua function `openspace.setPathToken` (see [Registering Tokens at Runtime](#registering-tokens-at-runtime) below).

### Path Separator Convention
Regardless of the operating system, path tokens and the paths they resolve to always use forward slashes (`/`). This keeps asset and script code consistent across Windows and Linux.

### The `${BASE}` Token
`${BASE}` is the root anchor of the token system. It always points to the root directory of the OpenSpace installation folder. Most other tokens are defined relative to `${BASE}`, either directly or through intermediate tokens like `${DATA}` or `${USER}`.

## How to Use Path Tokens
The most common way to resolve a tokenized path is with the Lua function `openspace.absPath`.

```lua
local p = openspace.absPath("${USER_ASSETS}/folder/file.asset")
-- Example result (assuming OpenSpace is installed in your user folder):
-- C:/Users/you/OpenSpace/user/data/assets/folder/file.asset
```

Use braces with a leading `$` when referencing a token in paths:
- `${ASSETS}/...`
- `${USER}/...`
- `${SYNC}/...`


## Token Expansion and Nested Definitions
Internally, tokens can be defined in terms of other tokens. For example:

- `ASSETS = "${DATA}/assets"`
- `DATA = "${BASE}/data"`

This means `${ASSETS}` ultimately resolves through `${DATA}` and then `${BASE}`. `${BASE}` is the OpenSpace installation root and is used as the anchor for many default paths.


## Customization via Environment Variables
Most users are not expected to add new path tokens. However, several of the defaults can be redirected by setting an environment variable on the operating system *before* launching OpenSpace.

The supported environment variables are:

| Environment Variable      | Overrides Token    | Typical Reason                                  |
| ------------------------- | ------------------ | ----------------------------------------------- |
| `OPENSPACE_USER`          | `${USER}`          | Move user content to a different location       |
| `OPENSPACE_SYNC`          | `${SYNC}`          | Store synced data on a larger or shared drive   |
| `OPENSPACE_GLOBEBROWSING` | `${GLOBEBROWSING}` | Redirect GlobeBrowsing data to a dedicated disk |

If an environment variable is not set, OpenSpace falls back to the default location shown in the [Default Path Tokens](#default-path-tokens) table.

You can also override any token directly in `openspace.cfg` by editing the `Paths` table.


## Registering Tokens at Runtime
For advanced use cases you can create or override a path token while OpenSpace is running:

```lua
openspace.setPathToken("MY_DATASET", "D:/datasets/my-project")
```

After this call, `${MY_DATASET}` can be used anywhere a tokenized path is accepted. This is useful for automation scripts or temporary overrides during a session. Keep in mind that tokens set this way do not persist across restarts — add them to `openspace.cfg` if they should be permanent.


## Default Path Tokens

The following tokens are available by default:

| Token | Default Mapping | Notes |
|---|---|---|
| `DATA`                       | `${BASE}/data`                                       | Core data directory                   |
| `ASSETS`                     | `${DATA}/assets`                                     | Built-in assets                       |
| `PROFILES`                   | `${DATA}/profiles`                                   | Built-in profiles                     |
| `USER`                       | `OPENSPACE_USER` or `${BASE}/user`                   | User root folder                      |
| `USER_ASSETS`                | `${USER}/data/assets`                                | User assets                           |
| `USER_PROFILES`              | `${USER}/data/profiles`                              | User profiles                         |
| `USER_CONFIG`                | `${USER}/config`                                     | User configuration                    |
| `USER_WEBPANELS`             | `${USER}/webpanels`                                  | User webpanels                        |
| `USER_SHOWCOMPOSER`          | `${USER}/showcomposer`                               | ShowComposer root                     |
| `USER_SHOWCOMPOSER_UPLOADS`  | `${USER}/showcomposer/uploads`                       | ShowComposer uploads                  |
| `USER_SHOWCOMPOSER_PROJECTS` | `${USER}/showcomposer/projects`                      | ShowComposer projects                 |
| `FONTS`                      | `${DATA}/fonts`                                      | Fonts                                 |
| `TASKS`                      | `${DATA}/tasks`                                      | Tasks                                 |
| `SYNC`                       | `OPENSPACE_SYNC` or `${BASE}/sync`                   | Sync folder                           |
| `SYNC_DYNAMIC`               | `${SYNC}/dynamically_downloaded`                     | Files downloaded as needed at runtime |
| `SCREENSHOTS`                | `${USER}/screenshots`                                | Screenshot output                     |
| `WEB`                        | `${DATA}/web`                                        | Web resources                         |
| `RECORDINGS`                 | `${USER}/recordings`                                 | Recording output                      |
| `CACHE`                      | `${BASE}/cache`                                      | Cache                                 |
| `CONFIG`                     | `${BASE}/config`                                     | Application config                    |
| `DOCUMENTATION`              | `${BASE}/documentation`                              | Local docs                            |
| `LOGS`                       | `${BASE}/logs`                                       | Log files                             |
| `MODULES`                    | `${BASE}/modules`                                    | Modules                               |
| `SCRIPTS`                    | `${BASE}/scripts`                                    | Scripts                               |
| `SHADERS`                    | `${BASE}/shaders`                                    | Shader files                          |
| `TEMPORARY`                  | `${BASE}/temp`                                       | Temporary files                       |
| `GLOBEBROWSING`              | `OPENSPACE_GLOBEBROWSING` or `${USER}/globebrowsing` | GlobeBrowsing data                    |


## Best Practices
  - Always use tokenized paths (`${...}`) in assets, profiles, and scripts instead of absolute OS-specific paths. This keeps your content portable.
  - Use `openspace.absPath` when a Lua script needs the fully resolved path at runtime.
  - Place personal or project-specific content under `${USER_ASSETS}` rather than inside the installation's `${ASSETS}` folder. This protects your work from being overwritten during an upgrade.
  - When collaborating or distributing content, never assume a particular install location — rely on tokens instead.
  - Use environment variables (`OPENSPACE_SYNC`, `OPENSPACE_GLOBEBROWSING`) to redirect large or shared data to an appropriate drive; reserve `openspace.setPathToken` for temporary or scripted overrides.
