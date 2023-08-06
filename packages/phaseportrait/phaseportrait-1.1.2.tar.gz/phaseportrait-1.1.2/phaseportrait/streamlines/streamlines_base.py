import numpy as np
from scipy import integrate
# Adapted from Raymond Speth https://web.mit.edu/speth/Public/streamlines.py with MIT license.

class Streamlines_base:
    """
    Streamlines
    --------
    Creates trajectories given a `dF` function. Using Scipy.integrate.odeint integrator.
    
    Integrated in:
        -PhasePortrait2D
        -PhasePorrtait3D
    """
    
    def _makeStreamline(self, y0, *, scypi_odeint=True):
        """
        Compute a streamline extending in both directions from the given point. Using Euler integrator.
        """
        *s, svelocity = self._makeHalfStreamline(y0, 1, scypi_odeint=scypi_odeint)  # forwards
        *r, rvelocity = self._makeHalfStreamline(y0, -1, scypi_odeint=scypi_odeint)  # backwards

        for _r in r:
            _r.reverse()
        rvelocity.reverse()

        speed = self._speed(y0)

        return *[r[i] + [y0[i]] + s[i] for i in range(len(y0))],  rvelocity + [np.sqrt(np.sum(np.square(speed)))] + svelocity
    

    def _speed(self, y0, *args, **kwargs):
        """
        Computes speed in given coordinates
        """
        if len(y0)==2:
            x, y = y0
            if not self.polar:
                speed = np.array(self.dF(x,y, **self.dF_args))

            # Polar coordinates
            else:
                R, Theta = np.sqrt(x**2 + y**2), np.arctan2(y, x)
                dR, dTheta = self.dF(R, Theta, **self.dF_args)
                speed = np.array([dR*np.cos(Theta) - R*np.sin(Theta)*dTheta, dR*np.sin(Theta)+R*np.cos(Theta)*dTheta])
        
        if len(y0)==3:
            x, y, z = y0
            if not self.polar:
                speed = np.array(self.dF(x,y,z, **self.dF_args))

            # Spherical coordinates
            else:
                R, Theta = np.sqrt(x*x + y*y + z*z), np.arctan2(y, x)
                Phi  = np.arccos(z/R) 
                dR, dTheta, dPhi = self.dF(R, Theta, Phi, **self.dF_args)
                speed = np.array([\
                    dR*np.cos(Theta)*np.sin(Phi) - R*np.sin(Theta)*np.sin(Phi)*dTheta + R*np.cos(Theta)*np.cos(Phi) * dPhi, \
                    dR*np.sin(Theta)*np.sin(Phi) + R*np.cos(Theta)*np.sin(Phi)*dTheta + R*np.sin(Theta)*np.cos(Phi) * dPhi, \
                    dR*np.cos(Phi) - R*np.sin(Phi)*dPhi
                ])
        return speed

    def _makeHalfStreamline(self, y0, sign, *, scypi_odeint=True):
        """
        Compute a streamline extending in one direction from the given point. Using Euler integrator.
        """
        # Coordinates to Numpy
        coords = y0.copy()
        # coords_mask_position = np.asarray(np.rint((coords-self.range_min)/self.delta_coords), int)
        coords_mask_position = self.get_masked_coordinates(*coords)

        # Set prev_coords_mask_position to actual position so backwards trajectory can, at least, start
        prev_coords_mask_position = coords_mask_position.copy()

        # Save arrays
        s = [[] for i in range(self.dimension)]
        svelocity = []

        i = 0
        persistency = 0

        while True:

            coords_mask_position = self.get_masked_coordinates(*coords)

            # If mask is False there is not trajectory there yet.
            if not self.used[tuple(coords_mask_position,)]:
                prev_coords_mask_position = coords_mask_position.copy()

                self.used[tuple(prev_coords_mask_position)] = True

            if i > self.maxLen / 2:
                break
            i += 1

            # Integration
            _speed = np.array(self._speed(coords))
            if np.sum(np.square(_speed)) == 0:
                break
            # deltat = np.sum(np.square(self.get_delta_coordinates(*coords))) / (4 * _speed)
            deltat = np.min(self.get_delta_coordinates(*coords)/(10*np.abs(_speed)+0.001))
            # if np.isinf(deltat):
            #     1

            if scypi_odeint:
                new_coords = integrate.odeint(self._speed, coords, [0,sign*deltat])[1]
            else: # Runge Kutta 3rd order. I'm sorry, speed is important sometimes
                k1 = self._speed(coords)
                k2 = self._speed(coords + sign*deltat*1/4*k1)
                k3 = self._speed(coords + sign*deltat*(-1*k1 + 2*k2))
                new_coords = coords + sign * deltat * ((k1+k3)/6 + 2/3*k2)

            mean_speed = np.sqrt(np.sum(np.square(new_coords-coords)))/deltat
            coords = new_coords

            # Break if out at lims
            if not ( (self.range_min < coords).all() and (coords < self.range_max).all() ):
                break
            
            # Save values
            for c, coord in enumerate(coords):
                s[c].append(coord)
            svelocity.append(mean_speed)


            # If persistency iterations in a region with previous trajectory break.
            if self.used[tuple(coords_mask_position)] and (prev_coords_mask_position!=coords_mask_position).any():
                persistency -= 1
                if persistency <= 0:
                    break

        return *s, svelocity


class Streamlines_base2D(Streamlines_base):
    """
    Streamlines2D
    --------
    Creates trajectories given a `dF` function. Using Euler integrator.
    
    Integrated in:
        -PhasePortrait2D
    """


    def __init__(
        self, dF, X, Y, maxLen=500, deltat=0.01, *, dF_args=None, polar=False, density=1, scypi_odeint=False
    ):
        """
        Compute a set of streamlines given velocity function `dF`.


        Parameters
        --------
        dF: callable
            A dF type funcion. Computes the derivatives of given coordinates.
        X and Y: 1D or 2D arrays
            Arrays of the grid points. The mesh spacing is assumed to be uniform in each dimension.
        maxLen: int, default=500
            The maximum length of an individual streamline segment.
        polar: bool, default=false
            Whether to use polar coordinates or not.
        density: int, default=1
            Density of mask grid. Used for making the stream lines not collide.
        scypi_odeint: bool, default=False
            Use scipy.odeint for integration. If `False` Runge-Kutta 3rd order is used.

        Key arguments:
        --------
        dF_args: dict|None, default=None
            dF_args of `dF` function.
        """
        super().__init__()

        self.dimension = 2
        self.dF = dF
        self.dF_args = dF_args if dF_args is not None else  {}

        self.maxLen = maxLen
        self.deltat = deltat

        self.density = int(abs(density))

        xa = np.asanyarray(X)
        ya = np.asanyarray(Y)
        self.x = xa if xa.ndim == 1 else xa[0]
        self.y = ya if ya.ndim == 1 else ya[:, 0]
        
        self.polar = polar

        # marker for which regions have contours. +1 outside the plot at the far side of every axis. 
        self.used = np.zeros((1 + X.shape[0]*self.density, 1 + X.shape[1]*self.density), dtype=bool)
        self.used[0] = True
        self.used[-1] = True
        self.used[:, 0] = True
        self.used[:, -1] = True

        self.range_min = np.array((self.x[0], self.y[0]))
        self.range_max = np.array((self.x[-1], self.y[-1]))

        self.streamlines = []

        while not self.used.all():
            nz = np.transpose(np.logical_not(self.used).nonzero())
            # Make a streamline starting at the first unrepresented grid point
            # choose = np.random.randint(nz.shape[0])
            choose = 0

            x_ind = nz[choose][0]
            x = self.x[x_ind-1] + 0.5 * (self.x[x_ind]-self.x[x_ind-1])
            y_ind = nz[choose][1]
            y = self.y[y_ind-1] + 0.5 * (self.y[y_ind]-self.y[y_ind-1])


            # x = nz[choose][0]*self.dx + self.x[0]
            # y = nz[choose][1]*self.dy + self.y[0]
            self.streamlines.append(
                self._makeStreamline(np.array([x, y]), scypi_odeint=scypi_odeint)
            )

    def get_masked_coordinates(self, x, y):
        """
        Returns index of position in masked coordinates
        """
        x_ind = np.searchsorted(self.x, x)
        y_ind = np.searchsorted(self.y, y)
        return np.array([x_ind, y_ind])

    def get_delta_coordinates(self, x, y):
        """
        Returns closest delta coordinates of grid
        """
        x_mask, y_mask = self.get_masked_coordinates(x, y)
        return np.array([
            self.x[x_mask] - self.x[x_mask-1], 
            self.y[y_mask] - self.y[y_mask-1]])

    @property
    def Range(self):
        return ((self.x[0], self.x[-1]), (self.y[0], self.y[-1])) 


class Streamlines_base3D(Streamlines_base):
    """
    Streamlines
    --------
    Creates trajectories given a `dF` function. Using Euler integrator.
    
    Integrated in:
        -PhasePortrait3D
    """


    def __init__(
        self, dF, X, Y, Z, maxLen=2500, *, dF_args=None, polar=False, density=1, scypi_odeint=False
    ):
        """
        Compute a set of streamlines given velocity function `dF`.


        Parameters
        --------
        X, Y and Z: 1D or 2D arrays
            arrays of the grid points. The mesh spacing is assumed to be uniform in each dimension.
        maxLen: int default=500
            The maximum length of an individual streamline segment.
        polar: bool default=false
            Whether to use polar coordinates or not.
        density: int, default=1
            Density of mask grid. Used for making the stream lines not collide.
        scypi_odeint: bool, default=False
            Use scipy.odeint for integration. If `False` Runge-Kutta 3rd order is used.

        Key arguments:
        --------
        dF_args: dict|None default=None
            dF_args of `dF` function.
        """
        super().__init__()
        self.dF = dF
        self.dF_args = dF_args if dF_args is not None else  {}

        self.maxLen = maxLen

        self.dimension = 3

        self.density = int(abs(density))

        xa = np.asanyarray(X)
        ya = np.asanyarray(Y)
        za = np.asanyarray(Z)
        self.x = xa if xa.ndim == 1 else xa[0,:,0]
        self.y = ya if ya.ndim == 1 else ya[:,0,0]
        self.z = za if za.ndim == 1 else za[0,0,:]

        self.polar = polar

        # marker for which regions have contours. +1 outside the plot at the far side of every axis. 
        self.used = np.zeros((1 + X.shape[0]*self.density, 1 + X.shape[1]*self.density, 1 + X.shape[2]*self.density), dtype=bool)
        self.used[0] = True
        self.used[-1] = True
        self.used[:, 0] = True
        self.used[:, -1] = True
        self.used[:,:, 0] = True
        self.used[:,:, -1] = True


        self.range_min = np.array((self.x[0], self.y[0], self.z[0]))
        self.range_max = np.array((self.x[-1], self.y[-1], self.z[-1]))

        # Make the streamlines
        self.streamlines = []

        while not self.used.all():
            nz = np.transpose(np.logical_not(self.used).nonzero())
            # Make a streamline starting at the first unrepresented grid point
            # choose = np.random.randint(nz.shape[0])
            choose = 0

            x_ind = nz[choose][0]
            x = self.x[x_ind-1] + 0.5 * (self.x[x_ind]-self.x[x_ind-1])
            y_ind = nz[choose][1]
            y = self.y[y_ind-1] + 0.5 * (self.y[y_ind]-self.y[y_ind-1])
            z_ind = nz[choose][2]
            z = self.z[z_ind-1] + 0.5 * (self.z[z_ind]-self.z[z_ind-1])
            self.streamlines.append(
                self._makeStreamline(np.array([x, y, z]), scypi_odeint=scypi_odeint)
            )

    
    def get_masked_coordinates(self, x, y, z):
        """
        Returns index of position in masked coordinates
        """
        x_ind = np.searchsorted(self.x, x)
        y_ind = np.searchsorted(self.y, y)
        z_ind = np.searchsorted(self.z, z)
        return np.array([x_ind, y_ind, z_ind])

    def get_delta_coordinates(self, x, y, z):
        """
        Returns closest delta coordinates of grid
        """
        x_mask, y_mask, z_mask = self.get_masked_coordinates(x, y, z)
        return np.array([
            self.x[x_mask] - self.x[x_mask-1], 
            self.y[y_mask] - self.y[y_mask-1], 
            self.z[z_mask] - self.z[z_mask-1]])

    @property
    def Range(self):
        return ((self.x[0], self.x[-1]), (self.y[0], self.y[-1]), (self.z[0], self.z[-1])) 