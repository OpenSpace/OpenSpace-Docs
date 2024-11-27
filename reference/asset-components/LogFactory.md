



(core_logfactory)=
# LogFactory




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

*   - `File`
    - The filename to which the log will be written
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Type`
    - The type of the new log to be generated
    - `String`
    
    - In list { html, Text } 
    
    - {bdg-info}`No`
    
*   - `Append`
    - Determines whether the file will be cleared at startup or if the contents will be appended to previous runs
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `CategoryStamping`
    - Determines whether the log entries should be stamped with the category that creates the log message
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `DateStamping`
    - Determines whether the log entries should be stamped with the date at which the message was logged
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `LogLevel`
    - The log level for this specific text-based log
    - `String`
    
    - In list { AllLogging, Trace, Debug, Info, Warning, Error, Fatal, NoLogging } 
    
    - Yes
    
*   - `LogLevelStamping`
    - Determines whether the log entries should be stamped with the log level that was used to create the log message
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `LogRotation`
    - The number of files that should be kept around for this Log
    - `Integer`
    
    - Greater than: 0 
    
    - Yes
    
*   - `TimeStamping`
    - Determines whether the log entires should be stamped with the time at which the message was logged
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::
























