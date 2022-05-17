from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(exposure=10)
scene.set_floor(-0.05, (1.0, 1.0, 1.0))
#scene.set_background_color((1.0, 0, 0))


@ti.kernel
def initialize_voxels():
    n = 18
    for i, j in ti.ndrange(n, n):
        if i == n-1 or i == 5 or ((j == 0 or j == n-1) and (i >= 5 and i <= n-1)):
            scene.set_voxel(vec3(0, j, i), 2, vec3(0.9, 0.1, 0.1)) 

    for i, j in ti.ndrange(n, n):
        if i == n-1 or i == 5 or ((j == 0 or j == n-1) and (i >= 5 and i <= n-1)):
            scene.set_voxel(vec3(i, j, 0), 2, vec3(0.9, 0.1, 0.1)) 

    for i, j in ti.ndrange((6, 11), (1, 3)):
        scene.set_voxel(vec3(0, j, i), 2, vec3(0.0, 0.5, 0.9))

    for i in range(12, 17):
        scene.set_voxel(vec3(0, 1, i), 2, vec3(0.0, 0.5, 0.9))
    
    for i in range(14, 17):
        scene.set_voxel(vec3(0, 2, i), 2, vec3(0.0, 0.5, 0.9))

    for i in range(6, 13):
        scene.set_voxel(vec3(i, 1, 0), 2, vec3(0.0, 0.5, 0.9))
    
    for i in range(15, 17):
        scene.set_voxel(vec3(i, 1, 0), 2, vec3(0.0, 0.5, 0.9))

    for i in range(7, 11):
        scene.set_voxel(vec3(i, 2, 0), 2, vec3(0.0, 0.5, 0.9))

    scene.set_voxel(vec3(9, 3, 0), 2, vec3(0.0, 0.5, 0.9))
    scene.set_voxel(vec3(16, 2, 0), 2, vec3(0.0, 0.5, 0.9))

    scene.set_voxel(vec3(14, 16, 11), 2, vec3(0.9, 0.0, 0.0))
    scene.set_voxel(vec3(14, 15, 11), 2, vec3(0.9, 0.0, 0.0))
    scene.set_voxel(vec3(13, 15, 11), 2, vec3(0.9, 0.0, 0.0))
    scene.set_voxel(vec3(15, 16, 13), 2, vec3(0.9, 0.0, 0.0))
    scene.set_voxel(vec3(14, 16, 12), 2, vec3(0.9, 0.0, 0.0))
    scene.set_voxel(vec3(14, 16, 13), 2, vec3(0.9, 0.0, 0.0))

    for i in range(11, 14):
        scene.set_voxel(vec3(0, 16, i), 2, vec3(0.7, 0.1, 0.0))
    scene.set_voxel(vec3(0, 15, 11), 2, vec3(0.7, 0.1, 0.0))

    scene.set_voxel(vec3(13, 15, 0), 2, vec3(0.7, 0.1, 0.0))
    scene.set_voxel(vec3(14, 15, 0), 2, vec3(0.7, 0.1, 0.0))
    scene.set_voxel(vec3(14, 16, 0), 2, vec3(0.7, 0.1, 0.0))
    scene.set_voxel(vec3(15, 16, 0), 2, vec3(0.7, 0.1, 0.0))


initialize_voxels()

scene.finish()
