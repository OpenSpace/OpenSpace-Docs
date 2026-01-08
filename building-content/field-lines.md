(fieldlines_id)=
# Field Lines

There are three publicly available profiles dedicated to showing space weather phenomena. They are all made by the collaborators at the [Community Coordinated Modeling Center](https://ccmc.gsfc.nasa.gov/) (CCMC) at NASA Goddard Space Flight Center. In all of these, field lines are a big part of the visualization and the story they tell. These are only examples. There are other usecases for field lines and used in other assets and profile accross OpenSpace. They are visualized using the renderable [Renderable Field Lines Sequence](fieldlinessequence_renderablefieldlinessequence)

Field lines are usually traced in simulation output volumes, but can be created in a variaty of ways. Regardless how they were created, to be visualized in OpenSpace they need to be in one of two file formats, JSON or OSFLS (OpenSpace Field Line Sequence). Each file in the sequence represent one time step. It is visualized until the next file's time step is the same as the time in OpenSpace. All files needs to be named on the format YYYY-MM-DDThh-mm-ss-nnn

## OSFLS (OpenSpace Field Lines Sequence)
The OSFLS file format is the prefered file format to use since it's binary and takes the lease amount of space. Not that some values might not be needed any longer, but still needs a value to maintain the order of bits being used for different variables.
What is needed to be stored, in order, is:

- a version number saved as a 64bit intiger. As of 2025 only 0 (zero) works as no other version excists yet.
- a double value (64 bit double precision floating point) that represent the time stamp of the data file. This number is a depricated legacy value from previous version of the renderable field lines sequence. The actually time stamps is derived from the name of the file.
- a 32 bit integer specifying which model it is. This corresponds to the list of supported models in the commons.h file found in modules/fieldlinessequence/util/. If different from any model in the list, specify it as the number in which 'Invalid' is. Ordering starts at 0.
- a uint8_t number, that works as a boolean (0 or 1 supported) called isModphable. This too is a legacy value and is no longer used.
- a uint64_t used to specify the number of lines that is in the data file.
- a uint64_t used to specify the total number of points on all lines.
- a uint64_t used to specify the number of data properties stored on the points of the lines.
- a uint64_t which specifies the number of bytes that the list of names for the data properties takes up. This will be used a little later on.

Next comes the portions of the data file which contains the vertex positions of the field lines, which uses the previous specified number of lines and total number of points.

- a list, the length of the number of lines, of int32_t, which specifies with points is the first points of each line.
- a list, the length of the number of lines, of uint32_t, which specifies the number of points included in each line.
- a list of the positions of all points. Each position consists of three 32bit float values.

 Next comes the values for the data properties. First the data, then the names.

- one list, per property, of 32 bit float values, the length of the number of points.
- a list of characters, the length of previously specified number of bytes that the list of names takes up, specifiying the names of each propery, null-seperated. Example of 24 bytes: "Bx\0By\0Bz\0rho\0temperature"

## JSON
The JSON format is more easily understandable because the file itself will be readable and not binary like the OSFLS. It also is a bit more streamlines and sizes of lists does not need to be calculated and stored seperately.

For each field line you have:
- first a time stamp named "time" on the format YYYY-MM-DDThh:mm:ss:nnn. This is a depricated legacy value, which still needs to be specified but is not used for the actual time stamp. The actually time stamps is derived from the name of the file.
- next is named "trace" and consists of two parts:
- "columns", which is a list of the name of the data properties. Importaint is that it also has the x, y and z, which will correspond to the position of the points, as the first three names in the list.
- "data" which is a list of lists. Each inner list, consists of values corresponding to the names in the "columns" list.

Example: A data file named 2025-07-14T11:00:00.000.json have only one field line with two points:
```
{
  "0": {
    "time": "2000-00-00T12:00:00.000",
    "trace": {
      "columns": [
        "x",
        "y",
        "z",
        "rho",
        "temperatur"
      ],
      "data": [
        [
          -0.2955686147,
          0.8835789298,
          -0.3630268896,
          1.8518465414775926,
          119.3012767918979,
        ],
        [
          -0.2955686184,
          0.8835789318,
          -0.3630268924,
          1.8518468546595963,
          119.30126546721327,
        ]
      ]
    }
  }
}
```
## Tracing and file format converting
Field lines can be traced in OpenSpace using the Kameleon module, developed at CCMC, which is integrated in OpenSpace. Kameleon is no longer being developed but works well for a handful of simulation models.
The tracing is done using the OpenSpace Task Manager, and using the [Kameleon Volume To Fieldlines Task.](fieldlinesequence_kameleon_volume_to_fieldlines_task)
To use this, a .task file is created that specifies the input folder with CDF files (data volumes, read more in next chapter), a folder with corresponding files that include the seed points, from where the tracing will start from, what file format to save the traced field lines in, JSON or OSFLS, where the output folder is as well as which vector field to trace the lines in. There are additional optional inputs that can be useful. Read the full documentation of the Task.

The models supported in Kameleon:
- Open GGCM / UCLA GGCM
- SWMF
- BATSRUS
- ENLIL
- MAS
- ADAPT3D
- LFM

### CDF

Only the models in the list above are supported to use the tracer in OpenSpace. The format of the data volume also needs to be CDF. At CCMC, these models can be requested to be run and output in this format. Note that there is a difference between the common file format called netCDF and this CDF.
