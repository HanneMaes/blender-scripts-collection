import bpy, random

materials = ['white', 'black', 'metallic']
bgColors = [(1, 1, 1, 1), (0, 0, 0, 1)]

heads = ['head Sphere', 'head Cube', 'head Icosphere']
torsos = ['torso Cube', 'torso Icosphere', 'torso Sphere', 'torso Cone']

################################################################

def randomMeshAndMaterial(_meshes, _material):

    # hide all meshes in array
    for _mesh in _meshes:
        bpy.data.objects[_mesh].hide_viewport = True
        bpy.data.objects[_mesh].hide_render = True
        
    # unhide random mesh
    randomMeshName = random.choice(_meshes)
    randomMesh = bpy.data.objects[randomMeshName]
    randomMesh.hide_viewport = False 
    randomMesh.hide_render = False 
    print(randomMeshName)
    
    # assign material
    bpy.ops.object.select_all(action='DESELECT')            # deselect all
    bpy.ops.object.select_pattern(pattern=randomMeshName)   # select mesh
    selectedObject = bpy.context.active_object
    if selectedObject.data.materials:
        selectedObject.data.materials[0] = material         # assign to 1st material slot
    else:
        selectedObject.data.materials.append(material)      # assign if there are no slots

################################################################

print()
print('---')
print()

# choose random material
randomMaterial = random.choice(materials)
material = bpy.data.materials.get(randomMaterial)
print('material: ' + randomMaterial)

# choose random elements
randomMeshAndMaterial(heads, material)
randomMeshAndMaterial(torsos, material)

# bg color
randomBgColor = random.choice(bgColors)
bpy.data.scenes["Scene"].node_tree.nodes["Alpha Over"].inputs[1].default_value = randomBgColor
print('background: ' + str(randomBgColor))

# deselect all & update the 3D viewport
print()
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
