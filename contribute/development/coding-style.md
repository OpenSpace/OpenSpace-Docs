# Coding Style

This document provides the general coding guidelines for C++ code in the OpenSpace project. The guidelines are based on [these](http://geosoft.no/development/cppstyle.html) guides, but were adapted and modified. Following this document ensures a common coding style for the project. Each developer using their own guidelines will quickly lead to fragmented code and decrease readability and maintainability. Please note rule #1; if, in a specific situation, the application of a rule would make the source code less readable it is advised to not follow the rule.

Sections [General](#general), [Naming](#naming), and [Structure](#structure) contain the coding style rules. Section [Best Practices](#best-practices) contains broader best practices for coding in general, and Section [File Formatting](#file-formatting) contains rules and examples on how to format the files in order to be consistent with the rest of the code base.



## General
### 0. "Boy Scouts" rule
While editing a piece of code and you find some other code that violates some of rules, fix it and leave it in a better state than you found it.

### 1. Violations to the guidelines are allowed if it enhances readability of the code
The main goal of these guidelines is to improve readability and thereby the understanding, the maintainability, and general quality of the code. It is impossible to cover all the specific cases in a general guide and the programmer should be flexible. However, the guidelines should be followed as closely as possible without sacrificing readability.

### 2. Class and method headers must include Doxygen-style comments
It is important to document the header so that other people do not need to dive into the code to understand the API.

### 3. File content must be kept within 90 columns
90 columns on a moderate font size allows two files to be opened side-by-side. Sticking to a fixed, manually enforced linebreak improves readability where unintentional line breaks are avoided when passing files between programmers. See examples [below](#file-formatting) on how to handle lines that are longer than 90 characters.

### 4. All TABs must be 4 spaces
TABs can be handled differently on different operating systems and make it hard to correctly format code. Most editors have settings that will automatically convert TABs to spaces.

### 5. Use the `auto` keyword sparingly
The overuse of `auto` in the code can make the code much harder to understand. If the return type of a function is known, the `auto` keyword must not be used unless the type is very verbose. In general the use of `auto` to deduce the type must be avoided with the only exceptions being the shortening of iterator types (example 1), shortening of time-measuring types from the `std::chrono` library (example 2), storing lambda functions (example 3), structured bindings (example 4), and if the type is explicitly mentioned on the same line (or line continuation if the column width was exceeded) (example 5).

```cpp
// Example 1
auto it = std::find(vector.begin(), vector.end(), value);

// Example 2
auto start = std::chrono::high_resolution_clock::now();

// Example 3
auto fn = [](int value) { return value * 2; };

// Example 4
auto& [val, ue] = std::tuple<std::string, int>("abc", 2);

// Example 5
auto type = std::make_unique<Struct>(val1, val2);
```

### 6. Use `//` for all comments, including multi-line comments
Using `//` comments ensure that it is always possible to comment out entire sections of a file using /\* \*/ for debugging purposes etc. Please note that his rule does not apply to the Doxygen comments in the header, as we use the variant that starts with `/**`.



## Naming
### 7. Negated boolean variable names should be avoided
```cpp
bool hasError = ...; // NOT: hasNoError
bool isFound = ...; // NOT: isNotFound
```
The problem arises when such a name is used in conjunction with the logical negation operator as this results in a double negative. It is not immediately apparent what `isNotFound` means. Leaving the code as simple as possible enhances readability.

### 8. Enumerations must not be in upper case and should be strongly typed
If there is no inherent mapping to integer types, the first value should be manually set to be equal to 0. If possible, prefer strongly typed enumerations for type safety. Strongly typed enumerations will prevent easy misuse in client code. If a strongly typed enumeration is not possible (due to mixing with outside code, each enumerated type should contain the enum name as a prefix.
```cpp
enum Color {
    ColorRed = 0,
    ColorGreen,
    ...
}

// Prefer
enum class Color {
    Red = 0,
    Green,
    ...
}
```

This makes it easy to find values for that type as the code completion of any IDE will suggest when typing the initial name. Strongly typed `enum`s are preferred as they are placed into their own namespace and do not collide with other definitions.

### 9. Names for methods or functions must be verbs and written in CamelCase starting with lower case
Methods should be named in such a way that, if applied to a properly named variable, it makes as much grammatical sense as possible. If two methods only differ in the fact that one will return a modified copy while the other changes and object in-place, the passive and active form of the verb should be used respectively `Vector::normalize(vector)`vs. `normalizedVector = vector.normalized()`
Following this standard, it becomes easy to spot bugs where a return value is omitted.

### 10. Names representing namespaces must be all lowercase and should not be nested deeper than two levels
A third level is admissible if the last level is an `internal` namespace that is an implementation detail. Limiting the `namespace`s to two prevents awkwardly long prefixes in the code which would otherwise require `using` statements.

### 11. Abbreviations in names must be avoided
```cpp
computeAverage();   // NOT: compAvg();
```
There are two types of words to consider. First are the common words listed in the dictionary. These must never be abbreviated. Never write: `cmd` instead of `command`, `cp` instead of `copy`, `init` instead of `initialize` etc. Then, there are domain specific phrases that are more naturally known through their abbreviations/acronym. These phrases should be kept abbreviated. Never write: `HypertextMarkupLanguage` instead of `html`, `CentralProcessingUnit` instead of `cpu`, etc.

### 12. Private class variables must have underscore prefix if part of a larger class
```cpp
class SomeClass {
// ...
private:
  int _depth = 0;
};
```
Besides its name and type, the scope of a variable is its most important feature. Indicating class scope by using underscores makes it easy to distinguish class variables from local variables. There are two side effects of the underscore naming convention; first, it simplifies searching for member variables as code completion will list all member variables if `_` is entered. Second, it nicely resolves the problem of finding reasonable variable names for setter methods and constructors:
```cpp
void setDepth(int depth) {
  _depth = depth;
}
```
An exception to this is simple `struct`s whose main purpose is to hold multiple values without much additional logic in which case the variable's prefix `_` can be omitted.

### 13. The length of a variable name should correspond to the length of its scope
Variables with a large scope should have long names, variables with a small scope can have short names. Obviously this is just a rule of thumb. Scratch variables used for temporary storage or indices are best kept short. A programmer reading such variables should be able to assume that its value is not used outside of a few lines of code.

### 14. The terms get/set must be used where an attribute is accessed. The prefix 'get' must be omitted in case the value is returned. 'get' is only to be used when the value is returned in a referenced parameter
```cpp
name = employee.name(); // Value is returned directly -> no get...
employee.setName(name);
string name;
employee.getName(name); // Value is returned in reference parameter -> get...
value = matrix.element(2, 4);
matrix.setElement(2, 4, value);
float value;
matrix.getElement(2, 4, value); // Value is returned in reference parameter -> get...
```
The preferred way is returning the value directly, returning by reference should only be a last resort. Omitting the word `get` in the accessor turns it from a verb construct into a noun construct and it therefore makes more grammatical sense when it is used in code, c.f.: `if (employee.name().empty())` vs. `if (employee.getName().empty())`


### 15. The prefix `n` should be used for variables representing a number of objects
```cpp
nPoints, nLines, ...
```

### 16. The prefix `i` should be used for variables representing an entity number
```cpp
iTable, iEmployee
```
This effectively makes these variables named iterators. In a short loop, using just the variable `i` is well understood and fine.

### 17. The prefixes `is`, `has`, `should`, or `can` should be used for boolean variables and methods
`isSet`, `isVisible`, `isFinished`, `isFound`, `isOpen`
Using the `is` prefix solves a common problem of choosing bad boolean names like `status` or `flag`. `isStatus` or `isFlag` simply doesn't fit, and the programmer is forced to choose more meaningful names. There are a few alternatives to the is prefix that fit better in some situations. These are the `has`, `can`, and `should` prefixes:
```cpp
bool hasLicense();
bool canEvaluate();
bool shouldSort();
```

### 18. Abbreviations and acronyms must not be uppercase when used as name
```cpp
exportHtmlSource(); // NOT: exportHTMLSource();
openDvdPlayer();    // NOT: openDVDPlayer();
```
Using all uppercase for the base name will give conflicts with the naming conventions given above. A variable of this type would have to be named dVD, hTML etc. which obviously is not very readable. Another problem is illustrated in the examples above; When the name is connected to another, the readability is seriously reduced; the word following the abbreviation does not stand out as it should.



## Structure
### 19. `#include` statements should be at the top of the file, sorted and grouped
Include-files should be grouped based on their first directory entry (´modules´, ´openspace´, ´ghoul´) in this ordered, followed by headers for external libraries, followed by standard libraries. Each group must be sorted alphabetrically individually. The first entry in a `.cpp` file is the corresponding `.h` file separated from the remaining headerfiles by an empty line. For header files, the first entry/entries are the header files of the parent classes separated by an empty line.
```cpp
#include "com/company/ui/PropertiesDialog.h"

#include "com/company/ui/MainWindow.h"
#include <qt/qbutton.h>
#include <qt/qtextfield.h>
#include <fstream>
#include <iomanip>
```
In addition to showing the individual include files, it also gives a clue about the modules that are involved in the source file. Include file paths must never be absolute. A `cpp` file should always include it's accompanying header file first and separate the other includes by an empty line.

### 20. The parts of a class must be sorted `public`, `protected` and `private`
Not applicable sections should be left out. The ordering is "most public first" so people who only wish to use the class can stop reading when they reach the protected/private sections.

### 21. Type conversions must always be done explicitly
Don't rely on implicit type conversion.
```cpp
floatValue = static_cast<float>(intValue); // NOT: floatValue = intValue;
```
Implementing this removes a lot of bugs that come from unexpected conversion. By making it very visible that a casting is intended, it becomes easier to spot buggy casts

### 22. All definitions must reside in source or inline files
```cpp
class MyClass {
public:
  int getValue () { return _value; }  // No
  ...
private:
  int _value;
}
```
The header files should declare an interface and the source file should implement it. Exceptions to this are template classes and template functions among others. The implementations of those methods must go in a `*.inl` file that is included at the bottom of the header file. The `inl` file does not require an include guard as it should never be included directly except in the header file it belongs to. While this restriction increases the number of files that we have to take care of, it also drastically enhances the readability of the code when looking at the header as one doesn't have to mentally remove any code but can focus on the function definitions instead.

### 23. Implicit test for `0` should only be used for boolean variables and pointer-types
```cpp
bool isTrue = ...;
if (isTrue) // NOT: if (isTrue == true)
int nLines;
if (nLines != 0) // NOT: if (nLines)
double value;
if (value != 0.0) // NOT: if (value)
std::unique_ptr<int> ptr;
if (ptr)        // OR: if (ptr != nullptr)
```
Using an explicit test, the statement gives an immediate clue of the type being tested. Testing pointers for `nullptr` is so common that it can be used.

### 24. Complex conditional expressions should be avoided. Introduce constant temporary boolean variables instead
```cpp
bool isFinished = (elementNo < 0) || (elementNo > maxElement);
bool isRepeatedEntry = elementNo == lastElement;
if (isFinished || isRepeatedEntry) {
    ...
}
// NOT:
if ((elementNo < 0) || (elementNo > maxElement) ||
     elementNo == lastElement)
{
  ...
}
```
By assigning boolean variables to expressions, the program gets automatic documentation. The construction will be easier to read, debug, and maintain. In optimized code, the intermediate variables will be removed either way, so they don't incur any performance drawbacks.

### 25. Executable statements in conditionals should be avoided
```cpp
File* fileHandle = open(fileName, "w");
if (!fileHandle) {
... }
// NOT:
if (!(fileHandle = open(fileName, "w"))) {
... }
```
This is an extension of the "one statement per line" rule that makes things easier to debug. Storing values in local variables is not a performance drawback as they will get optimized away. This rule also discourages assignments in `if` statements as allowed in newer C++:  `if (int i = value()) { ... }`

This rule is somewhat relaxed with C++ feature of having an instruction and evaluating the result in the same if statement. As long as this lowers the scope of the variable the following is allowed:  `if (int count = countThings();  count > 0) {`

### 26. The use of magic values in the code should be avoided
Numbers other than `0`, `1`, or `-1` should be declared as named constants instead. The same holds true for string constants, refactoring is made easier if they are defined as a constant.

This rule also enforces the "code as documentation" guide as it avoids magic constants, but makes things more readable

### 27. `nullptr` must be used instead of `0` or `NULL` for declaring null pointer
`NULL` is part of the standard C library, but is made obsolete in C++ and `0` has a double meaning as an integer and the null pointer. Use the C++ `nullptr` instead.


## Doxygen Comments
We use Doxygen to document classes, enums, functions, etc. in the source code. A list of available commands for Doxygen can be found [here](https://www.doxygen.nl/manual/commands.html). Like the coding style, a common documentation structuring helps to read the documentation at a quick glance. Particularly useful are the [`\p`](https://www.doxygen.nl/manual/commands.html#cmdp), [`\param`](https://www.doxygen.nl/manual/commands.html#cmdparam), [`\throw`](https://www.doxygen.nl/manual/commands.html#cmdthrow), [`\return`](https://www.doxygen.nl/manual/commands.html#cmdreturn), [`\pre`](https://www.doxygen.nl/manual/commands.html#cmdpre), [`\post`](https://www.doxygen.nl/manual/commands.html#cmdpost), and [`\see`](https://www.doxygen.nl/manual/commands.html#cmdsee) commands.

Syntax highlighting in Doxygen can be done using Markdown-style annotations.

### 1. Overall structure for Doxygen comments
Nonapplicable things of course can be left out, and if that happens, we leave out the empty line at the end.

  1. Description text
  1. Empty line
  1. Template parameter, parameter, and return value description. If a description has multiple lines, the next line is aligned with the *parameter name* (for parameters) or the first word (for return values)
  1. Empty line
  1. Exception, precondition, and postcondition statements. If an explanation has multiple lines, the next line is aligned with the *exception type* (for exceptions) or the first word (for pre- and postconditions)
  1. Empty line
  1. Additional reading in the form for `\see` statements


### 2. Use `\` for commands instead of `@`
For Doxygen, both `\param` as well as `@param` are allowed (the same for all other commands), but we use the version of commands that start with `\`

### 3. Use singular version of commands
Use `\return` instead of `\returns`, `\throw` instead of `\throws`, etc.

### 4. Member variables and enum members are documented with `///`, everything else with `/**  */`
This makes it very easy to quickly identify where the break between functions and members is in a header file. The only exception is for functions that do a simple overload declaration to save on space:
```cpp
/**
 * Converts the \p timeString representing a date to a double precision
 * value representing the ephemeris time; that is the number of TDB
 * seconds past the J2000 epoch.
 *
 * \param time A string representing the time to be converted
 * \return The converted time; the number of TDB seconds past the J2000 epoch,
 * representing the passed \p timeString
 *
 * \pre \p timeString must not be empty
 */
static double convertTime(const std::string& time);

/// \overload static double convertTime(const std::string& time)
static double convertTime(const char* time);
```

Member variables should also be documented on the previous line, not the same one. So prefer:
```cpp
/// This is a member variable
int memberVariable = 0;
```
over
```cpp
int memberVariable = 0; ///< This is a member variable
```

### 5. The description text ends with a `.`, everything else does not have a period at end
Parameter and return value descriptions inparticular are shown more *list-like* and thus don't need a `.` at the end

### 6. No separate `\brief` section
The first sentence of the description is automatically turned into a brief description. This means that the first sentence should be a good short explanation of the documented entity, but also it means that it doesn't have to be specified in a special way, meaning it can be a flowing text

### 7. Capitalization
The first word of a parameter, return value, exception, precondition, or postcondition description should either start with a capital letter or with a parameter name or a code literal.

Example:
```cpp
/**
 * \param action The action which is checked for each button
 * \return `true` if there is at least one joystick whose \p button is in the
 *         \p action state
 *
 * \pre \p button must be 0 or positive
 */
```

### 8. No documentation for namespaces
`namespace`s don't need to be documented in the code

### Example
```cpp
/**
 * Returns the \p position of a \p target body relative to an \p observer in a
 * specific \p referenceFrame, optionally corrected for \p lightTime (planetary
 * aberration) and stellar aberration (\p aberrationCorrection).
 *
 * \param target The target body name or the target body's NAIF ID
 * \param observer The observing body name or the observing body's NAIF ID
 * \param referenceFrame The reference frame of the output position vector
 * \param aberrationCorrection The aberration correction used for the position
 *        calculation
 * \param ephemerisTime The time at which the position is to be queried
 * \param lightTime If the \p aberrationCorrection is different from
 *        AbberationCorrection::Type::None, this variable will contain the light time
 *        between the observer and the target.
 * \return The position of the \p target relative to the \p observer in the specified
 *         \p referenceFrame
 *
 * \throw SpiceException If the \p target or \p observer do not name a valid
 *        NAIF object, \p referenceFrame does not name a valid reference frame or if
 *        there is not sufficient data available to compute the position or neither
 *        the target nor the observer have coverage.
 * \pre \p target must not be empty.
 * \pre \p observer must not be empty.
 * \pre \p referenceFrame must not be empty.
 * \post If an exception is thrown, \p lightTime will not be modified.
 *
 * \sa http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/spkpos_c.html
 * \sa http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/naif_ids.html
 */
```


## Best Practices
### Standard library is your friend
The C++ standard libraries `<algorithm>` header contains many useful functions that can make programming life very easy. Good examples are [`std::for_each`](https://en.cppreference.com/w/cpp/algorithm/for_each), [`std::accumulate`](https://en.cppreference.com/w/cpp/algorithm/accumulate), [`std::lower_bound`](https://en.cppreference.com/w/cpp/algorithm/lower_bound), [`std::all_of`](https://en.cppreference.com/w/cpp/algorithm/all_any_none_of). See [Cppreference](https://en.cppreference.com/w/cpp/algorithm).

### Keep it simple, sailor
Looking at the time spend for each line of code, the amount of time that future developers (including the future-self of the author of a line) will spend much much more wall-clock time on any code snippet than the CPU spends executing it. **Unless it is a performance-critical part of the run-loop**, prefer easy to understand code over obscure and optimized code. If you come back to a code you wrote 6 months later, it is effectively the same as someone else going back to that code.



## File formatting
### Handling line breaks
```cpp

// In order to keep the code on this page
// compact, a smaller line length is
// simulated
//                                        line
//                                       break
// ........................................|
//
// In a **header** file
//

// Functions:
// Return value + function + parameter fits
ReturnType function(int parameter) const;

// Second argument does not fit in the same
// line.
// Solution: Keep as compact as possible
// with following lines indented by 4
// spaces
ReturnType function(int parameter1,
    int parameter2, int param3) const;

// Only a final const or override does not
// fit in the same line.
// Solution: The last parameter or function
// name moves together with the last
// qualified
ReturnType function(int parameter1,
    int parameter2, int parameter3,
    int p) const;

// Due to a very long function name, even
// the first parameter does not fit on the
// first line.
// Solution: Same as above, but even the
// first parameter is on the next line
// indented by 4 spaces.
ReturnType veryLongFunctionFame(
    int parameter1, int parameter2);

// A long return type and long function
// name cause the function name not to fit
// on the same line
// Solution: Return type gets its own line
VeryLongAndComplexReturnType
veryLongFunctionFame(int parameter1);



//
// In a **source** file
//
// ........................................|

// Same rules as for the header with two
// exceptions:
// 1. If the declaration, for any reason,
//    turns into multiple lines, the
//    opening { gets its own line
VeryLongAndComplexReturnType
veryLongFunctionFame(int parameter1)
{

// 2. When parameters are split up, the
// following parameters are all aligned
// with the opening ( of the parameter list
// or right-aligned, if they don't fit
ReturnType function(int param1, int p2,
                    int p3, int p4,
                    int parameter2,
               int reallyLongParameterName)
{

// 3. Once a "too long" parameter is
// encountered, all the remaining
// parameters are also right-aligned
Return Type function(int param1, int p2,
                     int p2, int p3,
               int reallyLongParameterName,
                                    int p4)
{

// 4. Once a "too long" parameter is
// encountered, all the remaining
// parameters are also right-aligned
Return Type function(int param1, int p2,
                     int p2, int p3,
               int reallyLongParameterName,
                            int p4, int p5)
{

//
// Function calls
//
// ........................................|

// Functions that don't fit in a single
// line have their parameters split into
// separate lines each. The closing );
// gets its own line

// Things that fit
int r = function(p1, p2);

// Things that don't fit all go on separate
// lines and do **not** compact and the
// lines should be broken as early as
// possible
int result = function(
    secondFunction(parameter1),
    p3,
    parameter1 * parameter2 * abs(p3)
);

// An exception to this is the handling of
// parameters to the std::format function
// since this function is not supposed to
// take any complex, derived parameters.
// In this case, it is better to provide
// the arguments in a compact manner:
LINFO(std::format(
    "Foobar {} and barfoo {}", nBars, nFoos
));

// The exception continues even if the
// arguments don't fit on the same line.
// In the case were the arguments are going
// into the std::format function, they can
// all be on the same line. But avoid any
// complex function expressions in here
LINFO(std::format(
    "Foobarbazbarbazbar {} and barfoo {}",
    nBars, nFoos
));

// Another exception is when calling the
// `connect` function in Qt code. In that
// case it is more useful to group the
// object together with the signal/slot.
connect(
  obj, &TypeA::foo,
  this, &TypeB::bar
);

//
// Operators
//
// ........................................|

// Chains of operators that don't fit into
// one line are split up on logical
// barriers and align with the first
// argument

int i = parameter1 * parameter2 * j +
        parameter2 * k;

```

### Constructor layout
The initialization of member variables should happen in the header file, if possible. Remaining member variable initialization in the constructor should be organized as follows:
```cpp
// All initialization is on a separate line with the : or , starting the line
Classname::ClassName(int parameter, int parameter2)
    : _memberVar(parameter)
    , _memberVar2(parameter + parameter2)
```
If a member variable initialization takes more than one line, it follows the rules for functions:
```cpp
// ........................................|
Classname::ClassName(int parameter1,
                     int parameter2)
    : _memberVariableTakingParameters(
        parameter1,
        Enum::Yes
    )
    , _memberParam2(parameter2)
{
```
