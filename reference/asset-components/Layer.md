



(globebrowsing_layer)=
# Layer




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

*   - `Identifier`
    - The unique identifier for this layer.
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - {bdg-info}`No`
    
*   - `Adjustment`
    - Parameters that set individual adjustment parameters for this layer
    - `Table`
    
    -   [Table parameters](#LayerAdjustment-target) 
    
    - Yes
    
*   - `BlendMode`
    - Sets the blend mode of this layer to determine how it interacts with other layers on top of this
    - `String`
    
    - In list { Normal, Multiply, Add, Subtract, Color } 
    
    - Yes
    
*   - `Color`
    - If the 'Type' of this layer is a solid color, this value determines what this solid color is.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `Description`
    - A human-readable description of the layer to be used in informational texts presented to the user
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Enabled`
    - Determine whether the layer is enabled or not. If this value is not specified, the layer is disabled
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Name`
    - A human-readable name for the user interface. If this is omitted, the identifier is used instead
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Opacity`
    - The opacity value of the layer
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `Settings`
    - Specifies the render settings that should be applied to this layer
    - `Table`
    
    -   [Table parameters](#LayerSettings-target) 
    
    - Yes
    
*   - `Type`
    - Specifies the type of layer that is to be added. If this value is not specified, the layer is a DefaultTileProvider
    - `String`
    
    - In list { DefaultTileProvider, SingleImageProvider, ImageSequenceTileProvider, SizeReferenceTileProvider, TemporalTileProvider, TileIndexTileProvider, TileProviderByIndex, TileProviderByLevel, SolidColor, SpoutImageProvider, VideoTileProvider } 
    
    - Yes
    
*   - `ZIndex`
    - Determines where the layer is placed in the list of available layers. Layers are applied in the order of their Z indices, with higher indices obscuring layers with lower values.
    - `Integer`
    
    - Greater than: 0 
    
    - Yes
    
:::









(LayerAdjustment-target)=
::::{dropdown} Table parameters for `Adjustment`
Parameters that set individual adjustment parameters for this layer


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

*   - `ChromaKeyColor`
    - Specifies the chroma key used when selecting 'ChromaKey' for the 'Type'
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `ChromaKeyTolerance`
    - Specifies the tolerance to match the color to the chroma key when the 'ChromaKey' type is selected for the 'Type'
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Type`
    - Specifies the type of the adjustment that is applied
    - `String`
    
    - In list { None, ChromaKey, TransferFunction } 
    
    - Yes
    
:::



::::
















(LayerSettings-target)=
::::{dropdown} Table parameters for `Settings`
Specifies the render settings that should be applied to this layer


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

*   - `Gamma`
    - The gamma value that is applied to each pixel of the layer
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Multiplier`
    - The multiplicative factor that is applied to each pixel of the layer
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Offset`
    - An additive offset that is applied to each pixel of the layer
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
:::



::::







