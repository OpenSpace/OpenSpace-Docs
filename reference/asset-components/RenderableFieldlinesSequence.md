



(fieldlinessequence_renderablefieldlinessequence)=
# RenderableFieldlinesSequence

_Inherits [Renderable](#renderable)_




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

*   - `InputFileType`
    - Input file type. Should be cdf, json or osfls
    - `String`
    
    - In list { Cdf, Json, Osfls } 
    
    - {bdg-info}`No`
    
*   - `SourceFolder`
    - Path to folder containing the input files
    - `Directory`
    
    - Value of type 'Directory' 
    
    - {bdg-info}`No`
    
*   - `Color`
    - The uniform color of lines shown when 'Color Method' is set to 'Uniform'.
    - `Color4`
    
    - Value of type 'Color4' 
    
    - Yes
    
*   - `ColorMethod`
    - Color lines uniformly or using color tables based on extra quantities like, for examples, temperature or particle density.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `ColorQuantity`
    - Quantity used to color lines if the 'By Quantity' color method is selected.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `ColorTablePaths`
    - A list of paths to transferfunction .txt files containing color tables used for colorizing the fieldlines according to different parameters
    - `Table`
    
    -   [Table parameters](#RenderableFieldlinesSequenceColorTablePaths-target) 
    
    - Yes
    
*   - `ColorTableRanges`
    - List of ranges for which their corresponding parameters values will be colorized by. Should be entered as {min value, max value} per range
    - `Table`
    
    -   [Table parameters](#RenderableFieldlinesSequenceColorTableRanges-target) 
    
    - Yes
    
*   - `ExtraVariables`
    - Extra variables such as rho, p or t
    - `Table`
    
    -   [Table parameters](#RenderableFieldlinesSequenceExtraVariables-target) 
    
    - Yes
    
*   - `FlowColor`
    - Color of particles flow direction indication.
    - `Color4`
    
    - Value of type 'Color4' 
    
    - Yes
    
*   - `FlowEnabled`
    - Enables flow, showing the direction, but not accurate speed, that particles would be traveling
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FlowSpeed`
    - Speed of the flow.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `LineWidth`
    - This value specifies the line width of the fieldlines.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `LoadAtRuntime`
    - Set to true if you are streaming data during runtime
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ManualTimeOffset`
    - If data sets parameter start_time differ from start of run, elapsed_time_in_seconds might be in relation to start of run. ManuelTimeOffset will be added to trigger time.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `MaskingEnabled`
    - Enable/disable masking. Use masking to show lines where a given quantity is within a given range, for example, if you only want to see where the temperature is between 10 and 20 degrees. Also used for masking out line topologies like solar wind & closed lines.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `MaskingQuantity`
    - Quantity used for masking.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `MaskingRanges`
    - List of ranges for which their corresponding parameters values will be masked by. Should be entered as {min value, max value} per range
    - `Table`
    
    -   [Table parameters](#RenderableFieldlinesSequenceMaskingRanges-target) 
    
    - Yes
    
*   - `OutputFolder`
    - Value should be path to folder where states are saved. Specifying this makes it use file type converter (JSON/CDF input => osfls output & oslfs input => JSON output)
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `ParticleSize`
    - Size of the particles.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `ParticleSpacing`
    - Spacing inbetween particles.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `ReversedFlow`
    - Toggle to make the flow move in the opposite direction.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ScaleToMeters`
    - Convert the models distance unit, ex. AU for Enlil, to meters. Can be used during runtime to scale domain limits. 1.f is default, assuming meters as input.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `SeedPointDirectory`
    - Path to a .txt file containing seed points. Mandatory if CDF as input. Files need time stamp in file name like so: yyyymmdd_hhmmss.txt
    - `Directory`
    
    - Value of type 'Directory' 
    
    - Yes
    
*   - `SimulationModel`
    - Currently supports: batsrus, enlil & pfss
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `TracingVariable`
    - Which variable in CDF file to trace. b is default for fieldline
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



### Inherited members from [Renderable](#renderable)

:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `DimInAtmosphere`
    - Decides if the object should be dimmed (i.e. faded out) when the camera is in the sunny part of an atmosphere.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Enabled`
    - Determines whether this object will be visible or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Opacity`
    - This value determines the opacity of this renderable. A value of 0 means completely transparent
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `RenderBinMode`
    - A value that specifies if the renderable should be rendered in the Background, Opaque, Pre-/PostDeferredTransparency, Overlay, or Sticker rendering step.
    - `String`
    
    - In list { Background, Opaque, PreDeferredTransparent, PostDeferredTransparent, Overlay } 
    
    - Yes
    
*   - `Tag`
    - A single tag or a list of tags that this renderable will respond to when setting properties
    - `Table, or String`
    
    - Value of type 'Table', or Value of type 'String' 
    
    - Yes
    
*   - `Type`
    - The type of the renderable.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::
















(RenderableFieldlinesSequenceColorTablePaths-target)=
::::{dropdown} Table parameters for `ColorTablePaths`
A list of paths to transferfunction .txt files containing color tables used for colorizing the fieldlines according to different parameters


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
:::



::::




(RenderableFieldlinesSequenceColorTableRanges-target)=
::::{dropdown} Table parameters for `ColorTableRanges`
List of ranges for which their corresponding parameters values will be colorized by. Should be entered as {min value, max value} per range


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
:::



::::




(RenderableFieldlinesSequenceExtraVariables-target)=
::::{dropdown} Table parameters for `ExtraVariables`
Extra variables such as rho, p or t


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



::::




















(RenderableFieldlinesSequenceMaskingRanges-target)=
::::{dropdown} Table parameters for `MaskingRanges`
List of ranges for which their corresponding parameters values will be masked by. Should be entered as {min value, max value} per range


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
:::



::::




















## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 17
local transforms = asset.require("./transforms")



local data = asset.resource({
  Type = "HttpSynchronization",
  Name = "Ganymede Plane Simulations",
  Identifier = "juice_ganymede_fieldlines",
  Version = 1
})


local GanymedeMagnetosphere = {
  Identifier = "GanymedeMagnetosphere",
  Parent = transforms.GPHIO.Identifier,
  Renderable = {
    Type = "RenderableFieldlinesSequence",
    SourceFolder = data,
    LineWidth = 3.0,
    InputFileType = "Json",
    ColorMethod = "By Quantity",
    ColorQuantity = 0,
    ColorTableRanges = { { 62.556353386366766, 1665.5534182835445 } },
    ColorTablePaths = { asset.resource("CMR-illuminance2.txt") },
    Color = { 0.03, 0.0, 0.0, 1.0 },
    ParticleSpacing = 42.0,
    ParticleSize = 30.0,
    FlowColor = { 1.0, 1.0, 1.0, 0.1 },
    DomainEnabled = false

  },
  GUI = {
    Name = "Ganymede Magnetosphere",
    Path = "/Solar System/Missions/Juice/Fieldlines",
    Description = "Fieldlines showing a simulation of the magnetic fields around Ganymede"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(GanymedeMagnetosphere)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(GanymedeMagnetosphere)
end)



asset.meta = {
  Name = "Static fieldline representation of Ganymede's magnetic field",
  Description = [[
    Showing a single timestep of the magnetic fieldlines around Ganymede in the GPHIO
    coordinate system
  ]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


