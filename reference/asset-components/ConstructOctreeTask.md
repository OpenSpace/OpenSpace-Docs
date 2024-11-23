



(gaiamission_constructoctreefrombin)=
# ConstructOctreeTask

_Inherits [Task](#core_task)_




## Members


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `InFileOrFolderPath`
    - If SingleFileInput is set to true then this specifies the path to a single BIN file containing a full dataset. Otherwise this specifies the path to a folder with multiple BIN files containing subsets of sorted star data
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `OutFileOrFolderPath`
    - If SingleFileInput is set to true then this specifies the output file name (including full path). Otherwise this specifies the path to the folder which to save all files
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `FilterBpG`
    - If defined then only stars with Bp-G color values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterBpMag`
    - If defined then only stars with Bp mean magnitude values between [min, max] will be inserted into Octree (if min is set to 20.0 it is read as -Inf, if max is set to 20.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away. Default BpMag = 20.0 if no value existed
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterBpRp`
    - If defined then only stars with Bp-Rp color values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterDec`
    - If defined then only stars with DEC values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterDecError`
    - If defined then only stars with DEC Error values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterGMag`
    - If defined then only stars with G mean magnitude values between [min, max] will be inserted into Octree (if min is set to 20.0 it is read as -Inf, if max is set to 20.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away. Default GMag = 20.0 if no value existed
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterGRp`
    - If defined then only stars with G-Rp color values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterParallax`
    - If defined then only stars with Parallax values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterParallaxError`
    - If defined then only stars with Parallax Error values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterPmdec`
    - If defined then only stars with Proper Motion DEC values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterPmdecError`
    - If defined then only stars with Proper Motion DEC Error values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterPmra`
    - If defined then only stars with Proper Motion RA values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterPmraError`
    - If defined then only stars with Proper Motion RA Error values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterPosX`
    - If defined then only stars with Position X values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterPosY`
    - If defined then only stars with Position Y values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterPosZ`
    - If defined then only stars with Position Z values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterRa`
    - If defined then only stars with RA values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterRaError`
    - If defined then only stars with RA Error values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterRpMag`
    - If defined then only stars with Rp mean magnitude values between [min, max] will be inserted into Octree (if min is set to 20.0 it is read as -Inf, if max is set to 20.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away. Default RpMag = 20.0 if no value existed
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterRv`
    - If defined then only stars with Radial Velocity values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterRvError`
    - If defined then only stars with Radial Velocity Error values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterVelX`
    - If defined then only stars with Velocity X values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterVelY`
    - If defined then only stars with Velocity Y values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterVelZ`
    - If defined then only stars with Velocity Z values between [min, max] will be inserted into Octree (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `MaxDist`
    - If set it determines what MAX_DIST to use when creating Octree
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `MaxStarsPerNode`
    - If set it determines what MAX_STAR_PER_NODE to use when creating Octree
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `SingleFileInput`
    - If true then task will read from a single file and output a single binary file with the full Octree. If false then task will read all files in specified folder and output multiple files for the Octree
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::



### Inherited members from [Task](#core_task)

:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Type`
    - This key specifies the type of Task that gets created. It has to be one of the valid Tasks that are available for creation (see the FactoryDocumentation for a list of possible Tasks), which depends on the configration of the application
    - `String`
    
    - A valid Task created by a factory 
    
    - {bdg-info}`No`
    
:::































































