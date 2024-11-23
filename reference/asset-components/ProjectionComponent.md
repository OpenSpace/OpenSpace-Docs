



(spacecraftinstruments_projectioncomponent)=
# ProjectionComponent




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

*   - `Aberration`
    - The aberration correction that is supposed to be used for the projection. The values for the correction correspond to the SPICE definition as described in ftp://naif.jpl.nasa.gov/pub/naif/toolkit_docs/IDL/cspice/spkezr_c.html
    - `String`
    
    - In list { NONE, LT, LT+S, CN, CN+S, XLT, XLT+S, XCN, XCN+S } 
    
    - {bdg-info}`No`
    
*   - `Instrument`
    - 
    - `Table`
    
    -   [Table parameters](#ProjectionComponentInstrument-target) 
    
    - {bdg-info}`No`
    
*   - `Observer`
    - The observer that is doing the projection. This has to be a valid SPICE name or SPICE integer
    - `String`
    
    - A SPICE name of the observing object 
    
    - {bdg-info}`No`
    
*   - `Target`
    - The observed object that is projected on. This has to be a valid SPICE name or SPICE integer
    - `String`
    
    - A SPICE name of the observed object 
    
    - {bdg-info}`No`
    
*   - `AspectRatio`
    - Sets the desired aspect ratio of the projected texture. This might be necessary as planets usually have 2x1 aspect ratios, whereas this does not hold for non-planet objects (comets, asteroids, etc). The default value is '1.0'
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `DataInputTranslation`
    - 
    - `Table`
    
    -  
    
    - Yes
    
*   - `EventFile`
    - 
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `PotentialTargets`
    - The list of potential targets that are involved with the image projection
    - `Table`
    
    -   [Table parameters](#ProjectionComponentPotentialTargets-target) 
    
    - Yes
    
*   - `Sequence`
    - This value specifies one or more directories from which images are being used for image projections. If the sequence type is set to 'playbook', this value is ignored
    - `Directory, or Table`
    
    - Value of type 'Directory', or Value of type 'Table' 
    
    - Yes
    
*   - `SequenceType`
    - This value determines which type of sequencer is used for generating image schedules. The 'playbook' is using a custom format designed by the New Horizons team, the 'image-sequence' uses lbl files from a directory, and the 'hybrid' uses both methods
    - `String`
    
    - In list { image-sequence, playbook, hybrid, instrument-times, image-and-instrument-times } 
    
    - Yes
    
*   - `ShadowMap`
    - Determines whether the object requires a self-shadowing algorithm. This is necessary if the object is concave and might cast a shadow on itself during presentation. The default value is 'false'
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `TextureMap`
    - Determines whether the object requires a self-shadowing algorithm. This is necessary if the object is concave and might cast a shadow on itself during presentation. The default value is 'false'
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `TimesDataInputTranslation`
    - 
    - `Table`
    
    -  
    
    - Yes
    
*   - `TimesSequence`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::









(ProjectionComponentInstrument-target)=
::::{dropdown} Table parameters for `Instrument`



* Optional: {bdg-info}`No`


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Aspect`
    - The aspect ratio of the instrument in relation between x and y axis
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `Fovy`
    - The field of view in degrees along the y axis
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `Name`
    - The instrument that is used to perform the projections
    - `String`
    
    - A SPICE name of an instrument 
    
    - {bdg-info}`No`
    
:::



::::














(ProjectionComponentPotentialTargets-target)=
::::{dropdown} Table parameters for `PotentialTargets`
The list of potential targets that are involved with the image projection


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















