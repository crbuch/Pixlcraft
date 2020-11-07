The way the algorithm works is it takes a pixel of the image and gets the distance of the RGBA value from the image pixel to the average RGBA values of a block. 
It does this for every block I have added (30 blocks so far) and determines the lowest distance out of all the blocks. Then it returns the namespace id of the 
block it looks closest to. It combines the block and the relative coordinates of the image pixel (from the orgin) into a single line setblock command. it does this for 
every pixel of the image. (scanning all the pixels in the y axis' from left to right). It packs those single line commands into an .mcfunction file/files (depending on the length) 
and it compresses them into an archive consisting of a manifest.json file, the pack icon, and all the functions. Then the archive gets renamed from .zip to .mcfunction which is 
read by minecraft as a behavior pack. This is a similar tool to Spritecraft made by Autosaved, except this works on bedrock (Pocket edition and windows edition) rather than java. It also does not require mcedit.
