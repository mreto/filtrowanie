# filtrowanie
Script written in python, using pygmsh package the wrapper on gmsh.
Script is pretty basic and it isn't flexible, it generate the polygon like the one in the example.
I'm not sure is this is excactly what we were suppose to do so I didn't put my soul in it.

To run on linux:
download Anaconda
import environment from file environmet.yml. `conda env create -f environment.yml`
activate the environment (if you added the home dir of anaconda to your PATH) `source activate inz`
`python generate_trangle.py`

The script generates the file with extension .vtu it is pretty big, I don't know if we need such accuracy.
I visualize it with ParaView.
