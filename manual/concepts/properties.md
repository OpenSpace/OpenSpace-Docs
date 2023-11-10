# Properties
Properties are a mechanism to include user-changeable values into scenegraph objects. They behave fundamentally like member-variables, but can be queried by external applications and set using Lua scripts. Each property encapsulates a single value of its specific type. For example an `IntProperty` represents a single integer value.

Properties belong to PropertyOwners, each maintaining a list of all its owned properties. A PropertyOwner can also have subowners, which have properties themselves. Each Property and PropertyOwner must have a name that is unique to the owner that it belongs to, so that it can be uniquely identified by a URI of the form `owner.subowner.property`. These URIs are then used in Lua scripts to identify a specific property and set its value.

## ViewOptions
Two properties of the same type can benefit from different input methods in the GUI, depending on what type of value the property represents. ViewOptions are used as hints to the GUI of what input method is suitable for a property. For example the `Color` ViewOption can be used to tell the GUI that a `Vec3` or `Vec4` Property actually represents a color. If set, the GUI includes a color picker as the input method for that specific property instance.
