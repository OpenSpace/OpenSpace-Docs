# C++ Musings
## Returning by const reference for large objects is better than hoping for copy elision
If `T` is used over `const T&`, a copy has to be generated, even if the caller is only interested in a reference. If `const T&` is used and the caller only wants a reference, no copy is needed.

[Example](https://gcc.godbolt.org/z/fvKazz)


## Defining textual constants as `const char*` or `constexpr const char*` is better than `std::string`
`std::string` does not store the text locally, but has to execute a `new` and `delete` at construction time, which `const char*` and `constexpr const char*` do not have to do.

[Example](https://gcc.godbolt.org/z/ZvbzWc)
