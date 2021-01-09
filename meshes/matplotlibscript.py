
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import open3d as o3d
import numpy as np
import signal

keep_running = True

def get_pts(infile):
    # Read .ply file
    pcd = o3d.io.read_point_cloud(infile) # Read the point cloud
    o3d.visualization.draw_geometries([pcd])
    points = np.asarray(pcd.points) 
    colors = np.asarray(pcd.colors) 
    return points, colors #returns X,Y,Z points skipping the first 12 lines

def handler(signum, frame):
    """Sets up the kill handler, catches SIGINT"""
    global keep_running
    keep_running = False

def main(infile):
    plt.ion()
    fig = plt.figure(111,figsize=(20.0,20.0),dpi=150)
    ax = fig.add_subplot(111, projection='3d')
    altitude = -0
    azimuth = -45
    ax.view_init(altitude, azimuth)

    print('Press Ctrl-C in terminal to stop')
    signal.signal(signal.SIGINT, handler)

    pc,colors = get_pts(infile)
    mask = np.random.choice(pc.shape[0], int(pc.shape[0]/4), replace=False)
    pc = pc[mask]
    colors = colors[mask]

    matplotlib_ax_logic(ax,pc,colors)

    while keep_running:
        mask = np.random.choice(pc.shape[0], int(pc.shape[0]/4), replace=False)
        mod_pc = pc[mask]
        mod_colors = colors[mask]

        matplotlib_ax_logic(ax,mod_pc,mod_colors)

        plt.draw()
        plt.waitforbuttonpress(0.01)

def matplotlib_ax_logic(ax,pc,colors):
    ax.clear()
    mask = np.random.choice(pc.shape[0], int(pc.shape[0]/4), replace=False)
    pc = pc[mask]
    colors = colors[mask]
    x,y,z = pc[:,0],pc[:,1],pc[:,2]
    ax.scatter(x, y, z, c=colors, marker='.')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.set_xlim(-6,6)
    ax.set_ylim(-6,6)
    ax.set_zlim(-6,6)

    plt.show()	
	
if __name__ == '__main__':
    infile = 'hallway_coordinates.ply'
    main(infile)
