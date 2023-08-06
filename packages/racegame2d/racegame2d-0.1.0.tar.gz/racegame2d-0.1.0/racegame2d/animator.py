import numpy as np
import pandas as pd
import os
import subprocess
from collocation_opt.storage.saved_solution import SavedSolution
from tqdm import tqdm
import tempfile
from dynmodels.bicycle_model import BicycleModel
from .racegame_display import RacecarDisplay
from track_model.track import Track
from track_model import utils as tutils


class Animator():

    def __init__(self, track: Track):
        self.model = BicycleModel()
        self.gui = RacecarDisplay(track, res=1080)
        self.track: Track = track
        self.fps: float = 30
        self.figdir = tempfile.TemporaryDirectory()
        # Initialize temporary figures directory

    def clear_figures(self, figures_dir: str):
        self.figdir.cleanup()

    def animate(self, sol: SavedSolution):
        figures_dir = self.figdir.name
        time_main = sol.get_values('time')
        duration = time_main[-1] - time_main[0]
        n_frames = int(duration * self.fps)
        time_arr = np.linspace(time_main[0], time_main[-1], n_frames)
        sol_interp = sol.interpolate('time', time_arr)
        car_x = sol_interp.get_values(self.model.x.get_name())
        car_y = sol_interp.get_values(self.model.y.get_name())
        car_angle = sol_interp.get_values(self.model.yaw.get_name())
        sdist = sol_interp.get_values(self.model.s_dist.get_name())
        # Make plot for each frame
        for fidx, time in enumerate(time_arr):
            fidx_str = str(fidx).zfill(4)
            px, py, angle = car_x[fidx], car_y[fidx], car_angle[fidx]
            tangle = self.track.get_point(sdist[fidx]).get_orientation()
            fname = '{}.png'.format(fidx_str)
            fname = os.path.join(figures_dir, fname)
            self.gui.update_display(px, py, angle, tangle)
            self.gui.save_frame(fname)

    def make_movie(self, fname: str='movie.mp4'):
        '''
        Calls ffmpeg to make a movie from the figs directory.
        '''
        figures_dir = self.figdir.name
        cmd = 'ffmpeg'
        params = [cmd]
        params.append('-y')
        params.append('-framerate')
        params.append(str(self.fps))
        params.append('-i')
        params.append('{}/%04d.png'.format(figures_dir))
        params.append('{}'.format(fname))
        #cmd = cmd.format(fps)
        p = subprocess.run(params)
        print('\n')
        print('Created movie')

    def clean(self):
        '''
        Cleanup temp directory
        '''
        self.clear_figures(self.figdir)
        print('removed temporary directory: {}'.format(self.figdir.name))
