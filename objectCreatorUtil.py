from maya import cmds

def createObject(obj_type, name=""):
    if obj_type == "cube":
        return cmds.polyCube(name=name or "pCube#")[0]
    elif obj_type == "cone":
        return cmds.polyCone(name=name or "pCone#")[0]
    elif obj_type == "sphere":
        return cmds.polySphere(name=name or "pSphere#")[0]
    elif obj_type == "torus":
        return cmds.polyTorus(name=name or "pTorus#")[0]
    else:
        return None