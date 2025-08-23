import open3d as o3d
import numpy as np

# ==========================
# 1️⃣ Crear nube de puntos aleatoria
# ==========================
num_points = 1000
points = np.random.rand(num_points, 3)  # puntos en rango [0,1]

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# ==========================
# 2️⃣ Crear geometrías 3D básicas
# ==========================
# Cubo
mesh_box = o3d.geometry.TriangleMesh.create_box(width=1.0, height=1.0, depth=1.0)
mesh_box.compute_vertex_normals()
mesh_box.translate((-0.5, -0.5, -0.5))  # Centrar cubo en el origen

# Esfera
mesh_sphere = o3d.geometry.TriangleMesh.create_sphere(radius=0.3)
mesh_sphere.compute_vertex_normals()
mesh_sphere.translate((1.0, 0.0, 0.0))  # Mover a la derecha

# ==========================
# 3️⃣ Aplicar transformaciones
# ==========================
# Escalar la nube de puntos para que no esté dentro del cubo
pcd.scale(2.0, center=pcd.get_center())

# Rotar cubo 45 grados alrededor del eje Z
R = mesh_box.get_rotation_matrix_from_xyz((0, 0, np.pi/4))
mesh_box.rotate(R, center=mesh_box.get_center())

# ==========================
# 4️⃣ Visualizar todo
# ==========================
o3d.visualization.draw_geometries([pcd, mesh_box, mesh_sphere])
