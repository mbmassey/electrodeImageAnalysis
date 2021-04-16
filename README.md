# electrodeImageAnalysis

For the nEXO project, we have a pair of electrodes that induce a strong electric field in a liquid xenon time projection chamber. The main challenge we face are electric glitches, which cause charge breakdowns in the liquid xenon and overwhelm the SIPM and charge sensors. These glitches seem to melt the surface of the electrodes, removing the gold surface and warping the steel underneath.<br>   
I analyze the electrode images in two steps: 
1. First, find the area of the circle (the scope) with Hough Circles. A binary
   threshold and Gaussian Blur are used to isolate the fieldview.
2. Next, find the area of the gold surface left unscathed by glitches with inRange and findContour.<br>   
*ElectrodeDemo* shows an example of this analysis on a single image.<br>
*ElectrodeAnalysis* is the data pipeline from an image folder to a dataframe containing all coordinates and areas.<br>
This uses pandas and regex. The number of photos and the variety of coordinates
are unknown, but the image filenames follow 'yX\_xX.JPG' (e.g. 'y18\_x48.JPG')
