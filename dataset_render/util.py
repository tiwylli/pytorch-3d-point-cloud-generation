import bpy
def scale_mesh(mesh, max_dim=5.0):
    """
    Scales the given object so that it's longest dimension on any axis is exactly the number of units specified by
    max_dim. This is useful for scaling objects to a consistent size.

    If an object's maximum dimension is 0, no action is performed.

    :param mesh: the object to scale to be exactly `max_dim` units at it's longest side
    :param max_dim: the limit to how big an object can be on any axis
    """
    print("Scaling mesh %s to a maximum of %s in any direction" % (mesh.name, max_dim))
    max_length = max(mesh.dimensions)
    print('=================================================',max_length)
    if max_length == 0:
        print("No scaling for %s because its dimensions are %s" % (mesh.name, repr(mesh.dimensions)))
        return  # skip scaling
    scale_factor = 1 / (max_length / max_dim)
    mesh.scale = (scale_factor, scale_factor, scale_factor)
    x, y, z = [i for i in mesh.dimensions]  # for pretty dimension formatting
    new_dimensions = "X=%s, Y=%s, Z=%s" % (x, y, z)
    print("Scale factor for mesh %s is %s. Its new dimensions are %s",
                  mesh.name, scale_factor, [i for i in new_dimensions])