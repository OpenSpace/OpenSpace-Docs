



(core_light_source)=
# LightSource




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
    - The identifier of the light source
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - {bdg-info}`No`
    
*   - `Type`
    - The type of the light source that is described in this element. The available types of light sources depend on the configuration of the application and can be written to disk on application startup into the FactoryDocumentation
    - `String`
    
    - Must name a valid LightSource type 
    
    - {bdg-info}`No`
    
*   - `Enabled`
    - Whether the light source is enabled or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::












