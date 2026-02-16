# OpenGL Transition Guide
Based on https://github.com/fendevel/Guide-to-Modern-OpenGL-Functions.  Many of the functions use the new _Direct State Access_ (DSA) which doesn't require so many functions to have the target bound to a specific location, but instead work directly on the object instead. The table on the OpenGL wiki describes the naming scheme for DSA-style functions: https://wikis.khronos.org/opengl/Direct_State_Access

## Textures
Old:
```cpp
glGenTextures(1, &name);
glBindTexture(GL_TEXTURE_2D, name);
```

New:
```cpp
glCreateTextures(GL_TEXTURE_2D, 1, &name);
```

Old:
```cpp
glBindTexture(GL_TEXTURE_2D, name);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
```

New:
```cpp
glTextureParameteri(name, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
glTextureParameteri(name, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
glTextureParameteri(name, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
glTextureParameteri(name, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
```


Old:
```cpp
glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGBA8, width, height);
glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, width, height, GL_RGBA, GL_UNSIGNED_BYTE, pixels);

```

New:
```cpp
glTextureStorage2D(name, 1, GL_RGBA8, width, height);
glTextureSubImage2D(name, 0, 0, 0, width, height, GL_RGBA, GL_UNSIGNED_BYTE, pixels);
```


New function [`glTextureStorage`](https://registry.khronos.org/OpenGL-Refpages/gl4/html/glTexStorage2D.xhtml) (non-DSA version: `glTexStorage` allocates memory for a texture and makes the texture _immutable_, which means only the contents of the texture can be changed, but not the data type, sizes, etc. This results in a more efficient handling and enables other OpenGL 4.6 features like [texture views](https://registry.khronos.org/OpenGL-Refpages/gl4/html/glTextureView.xhtml). It is also more robust as the driver can immediately check whether a texture is well-defined.

## Texture Units
Old:
```cpp
glActiveTexture(GL_TEXTURE0 + 3);
glBindTexture(GL_TEXTURE_2D, name);
```

New:
```cpp
glBindTextureUnit(3, name);
```

## Bindless textures
In addition to being able to bind textures to shaders, it is also possible to use bindless textures, which circumvent some of the restrictions of texture bindings (namely the limitation on the number of textures being bound). This part of the code is still evolving in the PR, so the recommendations are not finished.

## Framebuffer
Old:
```cpp
glGenFramebuffers(1, &fbo);
```

New:
```cpp
glCreateFramebuffers(1, &fbo);
```


Old:
```cpp
glBindFramebuffer(GL_FRAMEBUFFER, fbo);
glFramebufferTexture(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, tex, 0);
glFramebufferTexture(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, depthTex, 0);
```

New:
```cpp
glNamedFramebufferTexture(fbo, GL_COLOR_ATTACHMENT0, tex, 0);
glNamedFramebufferTexture(fbo, GL_DEPTH_ATTACHMENT, depthTex, 0);
```


Old:
```cpp
glBindFramebuffer(GL_READ_FRAMEBUFFER, src);
glBindFramebuffer(GL_DRAW_FRAMEBUFFER, dst);

glBlitFramebuffer(srcX, srcY, srcW, srcH, dstX, dstY, dstW, dstH, GL_COLOR_BUFFER_BIT, GL_LINEAR);
```

New:
```cpp
glBlitNamedFramebuffer(src, dst, srcX, srcY, srcW, srcH, dstX, dstY, dstW, dstH, GL_COLOR_BUFFER_BIT, GL_LINEAR);
```


Old:
```cpp
glBindFramebuffer(GL_FRAMEBUFFER, fbo);
glClearColor(r, g, b, a);
glClearDepth(d);
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
```

New:
```cpp
glClearNamedFramebufferfv(fbo, GL_COLOR, 0, &rgba);
glClearNamedFramebufferfv(fbo, GL_DEPTH, 0, &d);
```

The `0` in the new function call are the attachment points to the framebuffer. So `0` will clear the first color attachment, `1` will clear the second, etc. The index for the depth buffer is always 0 since there can only be a single depth buffer attachment.

## Buffers and Vertex Array Objects
Old:
```cpp
struct Vertex {
  glm::vec3 pos;
  glm::vec3 nrm;
  glm::vec2 tex;
};

glGenVertexArrays(1, &vao);
glGenBuffers(1, &vbo);
glGenBuffers(1, &ibo);

glBindVertexArray(vao);

GLuint posAttribLocation = 0;
glEnableVertexAttribArray(posAttribLocation);
glVertexAttribPointer(posAttribLocation, 3, GL_FLOAT, GL_FALSE, sizeof(Vertex), nullptr);

GLuint normalAttribLocation = 1;
glEnableVertexAttribArray(normalAttribLocation);
glVertexAttribPointer(normalAttribLocation, 3, GL_FLOAT, GL_FALSE, sizeof(Vertex), reinterpret_cast<void*>(offsetof(Vertex, nrm));

GLuint texAttribLocation = 2;
glEnableVertexAttribArray(texAttribLocation);
glVertexAttribPointer(texAttribLocation, 2, GL_FLOAT, GL_FALSE, sizeof(Vertex), reinterpret_cast<void*>(offsetof(Vertex, nrm));
glBindVertexArray(0);

glBindBuffer(GL_ARRAY_BUFFER, vbo);
glBufferData(
  GL_ARRAY_BUFFER,
  vertexArray.size() * sizeof(Vertex),
  vertexArray.data(),
  GL_STREAM_DRAW
);

glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibo);
glBufferData(
  GL_ELEMENT_ARRAY_BUFFER,
  indexArray.size() * sizeof(uint8_t),
  indexArray.data(),
  GL_STREAM_DRAW
);

glBindVertexArray(0);
```

New:
```cpp
struct Vertex {
  glm::vec3 pos;
  glm::vec3 nrm;
  glm::vec2 tex;
};

glCreateBuffers(1, &vbo);
glCreateBuffers(1, &ibo);
glCreateVertexArrays(1, &vao);
glVertexArrayVertexBuffer(vao, 0, vbo, 0, sizeof(Vertex));
glVertexArrayElementBuffer(vao, ibo);

GLuint posAttribLocation = 0;
glEnableVertexArrayAttrib(vao, posAttribLocation);
glVertexArrayAttribFormat(vao, posAttribLocation, 3, GL_FLOAT, GL_FALSE, 0);
glVertexArrayAttribBinding(vao, posAttribLocation, 0);

GLuint normalAttribLocation = 0;
glEnableVertexArrayAttrib(vao, normalAttribLocation);
glVertexArrayAttribFormat(vao, normalAttribLocation, 3, GL_FLOAT, GL_FALSE, offsetof(Vertex, nrm));
glVertexArrayAttribBinding(vao, normalAttribLocation, 0);

GLuint texAttribLocation = 0;
glEnableVertexArrayAttrib(vao, texAttribLocation);
glVertexArrayAttribFormat(vao, texAttribLocation, 2, GL_FLOAT, GL_FALSE, offsetof(Vertex, tex));
glVertexArrayAttribBinding(vao, texAttribLocation, 0);

glNamedBufferData(
  vbo,
  vertexArray.size() * sizeof(float),
  vertexArray.data(),
  GL_STREAM_DRAW
);

glNamedBufferData(
  ibo,
  indexArray.size() * sizeof(uint8_t),
  indexArray.data(),
  GL_STREAM_DRAW
);
```

_Important_: Forgetting to call the new function `glVertexArrayAttribBinding` to match up the attribute with the buffer object that has the data will cause a null pointer access deep in the Nvidia driver without a callstack.  So if that happens, it's most likely the cause.
