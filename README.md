  
  
  
  ## Abstract  from [Poisson Image Editing ](https://www.cs.jhu.edu/~misha/Fall07/Papers/Perez03.pdf)
Using generic interpolation machinery based on solving Poisson
equations, a variety of novel tools are introduced for seamless editing
of image regions. The first set of tools permits the seamless
importation of both opaque and transparent source image regions
into a destination region. The second set is based on similar mathematical
ideas and allows the user to modify the appearance of the
image seamlessly, within a selected region. These changes can be
arranged to affect the texture, the illumination, and the color of objects
lying in the region, or to make tileable a rectangular selection. 

## Filling 

The process involves outlining a region of interest in the image and then completely removing that region from the image. In the example below the region is outlined in green, then it is removed and filled in by using the pixels surrounding the region. 
  
<img width="479" alt="image" src="https://user-images.githubusercontent.com/92171342/195895610-a40cd697-21b8-4a4b-9656-55775b8f9a78.png">

## Seamless Cloning 

Here there are 2 images needed, a source image and a destination image. The source image is the image we need to transfer to another location and in the example below the region outlined in green is to be transfered to another image. The resulting image show the region blended into the destination image seamlessly

<img width="536" alt="image" src="https://user-images.githubusercontent.com/92171342/195896265-01777592-67a7-485b-8826-76938cb60a01.png">

  
  
