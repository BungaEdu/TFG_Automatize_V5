import os

def rutaRepositorio():
    dirName = os.path.abspath(os.path.join(__file__, "../../../"))
    return dirName
