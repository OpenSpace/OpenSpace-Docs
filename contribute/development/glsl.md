# GLSL Shader Coding Style
- Indentation is 2 spaces
- When functions are multiple lines, each argument does _not_ have to be on its own line

- [Interface Blocks](https://wikis.khronos.org/opengl/Interface_Block_(GLSL)) should be used to pass data between shader stages. The interface blocks are matched based on the struct name instead of the variable name, which makes logical naming a lot easier. By using the name `Data` for all Interface blocks, we make sure that they always work and make it easy to remember.

Old:
```glsl
// vertex
in vec3 in_position;
in vec3 in_bvLumAbsMag;
in vec3 in_velocity;
in float in_speed;

out vec3 vs_bvLumAbsMag;
out vec3 vs_velocity;
out float vs_speed;

// geometry
layout(points) in;
in vec3 vs_bvLumAbsMag[];
in vec3 vs_velocity[];
in float vs_speed[];

layout(triangle_strip, max_vertices = 4) out;
out vec3 vs_position;
out vec2 texCoords;
flat out float ge_bv;
flat out vec3 ge_velocity;
flat out float ge_speed;
flat out float gs_screenSpaceDepth;

// fragment
in vec3 vs_position;
in vec2 texCoords;
flat in float ge_bv;
flat in vec3 ge_velocity;
flat in float ge_speed;
flat in float gs_screenSpaceDepth;
```

New:
```glsl
// vertex
layout(location = 0) in vec3 in_position;
layout(location = 1) in vec3 in_bvLumAbsMag;
layout(location = 2) in vec3 in_velocity;
layout(location = 3) in float in_speed;
layout(location = 4) in float in_otherData;

out Data {
  vec3 bvLumAbsMag;
  vec3 velocity;
  float speed;
  float otherData;
} out_data;

// geometry
layout(points) in;
in Data {
  vec3 bvLumAbsMag;
  vec3 velocity;
  float speed;
  float otherData;
} in_data[];

layout(triangle_strip, max_vertices = 4) out;
out Data {
  vec3 position;
  flat vec3 velocity;
  vec2 texCoords;
  flat float bv;
  flat float speed;
  flat float otherData;
  flat float screenSpaceDepth;
} out_data;

// fragment
in Data {
  vec3 position;
  flat vec3 velocity;
  vec2 texCoords;
  flat float bv;
  flat float speed;
  flat float otherData;
  flat float screenSpaceDepth;
} in_data;
```

Interface blocks can't be used to transfer data into a vertex shader or out of a fragment shader.  The naming convention is that data flowing into a shader is prefixed with `in_` and data flowing out of a shader is prefixed with `out_`

- No underscores are allowed in variable names apart from the `in_` and `out_` prefixes to make it immediately obvious when we are manipulating such data.
- The order in the top of a shader file is:
  1. Includes
  2. `in` variables
  3. `out` variable
  4. `uniform`s
  5. `const`ants
  6. Two empty lines
  7. Other functions
  8. Two empty lines (if there are no other functions, this step is skipped)
  9. `main` or `getFragment` function
