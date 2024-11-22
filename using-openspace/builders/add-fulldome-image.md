# Use a fulldome image in OpenSpace
Here, we walk through the steps needed to display a [fulldome](https://en.wikipedia.org/wiki/Fulldome) frame in OpenSpace. 

1. Convert the fulldome frame to a 360 image with [equirectangular projection](https://en.wikipedia.org/wiki/Equirectangular_projection)
2. Use the 360 image as the texture for a [RenderableSphereImageLocal](/generated/asset-components/RenderableSphereImageLocal)
3. Move the camera inside the rendered sphere, to the center of the sphere, and look towards the hemisphere which has the desired view.

## 1. Convert the fulldome frame to a 360 image
This can be done with [Blender](https://www.blender.org/) with the use of this [blend file](https://informal.jpl.nasa.gov/museum/sites/default/files/ResourceLibrary/fulldome-to-equirectangular-converter_version3.zip) 
or using other tools like [OCVWarp](https://github.com/hn-88/OCVWarp/wiki/Transform-types)

## 2. Create a renderable sphere
An example of a renderable sphere created in this manner using a local texture is described in another howto article.

## 3. Move the camera
If the renderable sphere is scaled to be very large, the camera would already be inside the sphere with the default view, and only [yaw/pitch adjustments](/getting-started/navigation) may 
need to be made.
