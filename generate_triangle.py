import pygmsh


def siatka(w, l_list, d_list, epsilon, lcar=1, scale=0.1):
    """
    Simple function that generate polygon as in the example.
    I am not exactly sure if this is what we were suppose to do so I didn't
    develop it much and it isn't particularity flexible.
    The arguments of the function keep the terminology from the picture we
    received

    w: value w
    l_list: list of all the values d
    d_list: -||-
    epsilon: the value of how thin should be the blue line
    lcar: I don't really know because but I think it is something with density
    of triangles
    """


    ## scale the arguments
    # w *= scale
    # dl = list(map(lambda x: x*scale, d_list))
    # d_list = dl
    # ll = list(map(lambda x: x*scale, l_list))
    # l_list = ll

    geom = pygmsh.built_in.Geometry()
    # I draw separatly the top line and the bottom line than reverse the top
    # line and merge to with bottom line to create closed polygon
    x = 0.0
    # first two points
    list_top = [[0.0, w, 0.0]]
    list_down = [[0.0, 0.0, 0.0]]
    for l, d in zip(l_list, d_list):
        x += l
        length = (w - d) / 2

        list_down.append([x, 0.0, 0.0])
        list_down.append([x, length, 0.0])
        list_down.append([x + epsilon, length, 0.0])
        list_down.append([x + epsilon, 0.0, 0.0])

        list_top.append([x, w, 0.0])
        list_top.append([x, w - length, 0.0])
        list_top.append([x + epsilon, w - length, 0.0])
        list_top.append([x + epsilon, w, 0.0])

    # there will be one more element in l_list then in d_list
    # so need to add the last one
    x += l_list[-1]
    list_down.append([x, 0.0, 0.0])
    list_top.append([x, w, 0.0])
    list_top.reverse()
    # tu na koncu lcar
    geom.add_polygon(list_down + list_top, lcar)
    points, cells, _, _, _ = pygmsh.generate_mesh(geom)
    return points, cells


if __name__ == "__main__":
    import meshio
    meshio.write_points_cells(
        "generated.vtu",
        *siatka(6.4, [6.4, 3.2, 3.2, 6.4], [2.8, 4.2, 2.8], 0.00001))
