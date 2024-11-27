



(globebrowsing_defaulttileprovider)=
# DefaultTileProvider

_Inherits [TileProvider](#TileProvider)_




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

*   - `FilePath`
    - The path to the file that is loaded by GDAL to produce tiles. Since GDAL supports it, this can also be the textual representation of the contents of a loading file
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `LayerGroupID`
    - The layer into which this tile provider is loaded
    - `Integer`
    
    - Value of type 'Integer' 
    
    - {bdg-info}`No`
    
*   - `CacheSettings`
    - Specifies the cache settings that should be applied to this layer
    - `Table`
    
    -   [Table parameters](#DefaultTileProviderCacheSettings-target) 
    
    - Yes
    
*   - `GlobeName`
    - The name of the enclosing globe
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Identifier`
    - Identifier of the enclosing layer to which tiles are provided
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Name`
    - User-facing name of this tile provider
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `PerformPreProcessing`
    - Determines if the tiles should be preprocessed before uploading to the GPU
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `TilePixelSize`
    - This value is the preferred size (in pixels) for each tile. Choosing the right value is a tradeoff between more efficiency (larger images) and better quality (smaller images). The tile pixel size has to be smaller than the size of the complete image if a single image is used.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
:::











(DefaultTileProviderCacheSettings-target)=
::::{dropdown} Table parameters for `CacheSettings`
Specifies the cache settings that should be applied to this layer


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

*   - `BlockSize`
    - The block-size of the MRF cache
    - `Integer`
    
    - Greater than: 0 
    
    - Yes
    
*   - `Compression`
    - The compression algorithm to use for cached tiles
    - `String`
    
    - In list { PNG, JPEG, LERC } 
    
    - Yes
    
*   - `Enabled`
    - Specifies whether to use caching or not
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Quality`
    - The quality setting of the compression alogrithm, only valid for JPEG
    - `Integer`
    
    - In range: ( 0,100 ) 
    
    - Yes
    
:::



::::













