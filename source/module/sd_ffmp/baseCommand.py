#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time     :  15:43
# Email    : spirit_az@foxmail.com
# File     : baseCommand.py

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from importFfmp import ffmpeg_parse_infos, get_coll
import math
import os


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class movie_message(object):
    def __init__(self, filePath):
        """
        {'video_found': True,  # 是否为视频
        'video_nframes': 40,   # 多少帧
        'video_rotation': 0,
        'audio_found': False,
        'video_fps': 24.0,
        'video_size': [2560, 1440],
        'duration': 1.63,
        'video_duration': 1.63
        }

        :param filePath:
        """
        self.movie = ffmpeg_parse_infos(filePath)

    def getFPS(self):
        return self.movie.get('video_fps')

    def getTime(self):
        dr = int(self.movie.get('video_duration') * 1000)
        t_hour_temp = (dr / 3600000) % 60
        t_hour = get_coll(t_hour_temp, 2)
        t_minu_temp = (dr / 60000) % 60
        t_minu = get_coll(t_minu_temp, 2)
        t_sec_temp = (dr / 1000) % 60
        t_sec = get_coll(t_sec_temp, 2)
        frames_temp = dr % 1000

        totalTime = '{0}:{1}:{2}:{3}'.format(t_hour, t_minu, t_sec, frames_temp)

        return totalTime, self.movie.get('video_nframes'), dr

    def get_size(self):
        return self.movie.get('video_size')

    def get_rotation(self):
        return self.movie.get('video_rotation')


if __name__ == '__main__':
    inMov = u"M:/temp/zhangyipeng/AVENGERS 3_ INFINITY WAR Trailer 1 - 3 (2018).mkv"
    mm = movie_message(inMov)

    print mm.getTime()
    print mm.get_rotation()

    # print mm._TEMP_FILES_PREFIX
    # print mm.__doc__
    # print mm.__enter__
    # print mm.__exit__
    # print mm.__init__
    # print mm.__module__
    # print mm.add_mask
    # print mm.afx
    # print mm.aspect_ratio
    # print mm.audio
    # print mm.audio_fadein
    # print mm.audio_fadeout
    # print mm.audio_normalize
    # print mm.blit_on
    # print mm.close
    # print mm.copy
    # print mm.crop
    # print mm.crossfadein
    # print mm.crossfadeout
    # print mm.cutout
    # print mm.duration
    # print mm.end
    # print mm.fadein
    # print mm.fadeout
    # print mm.filename
    # print mm.fill_array
    # print mm.fl
    # print mm.fl_image
    # print mm.fl_time
    # print mm.fps
    # print mm.fx
    # print mm.get_frame
    # print mm.h
    # print mm.has_constant_size
    # print mm.invert_colors
    # print mm.ipython_display
    # print mm.is_playing
    # print mm.ismask
    # print mm.iter_frames()
    # print mm.loop
    # print mm.make_frame
    # print mm.margin
    # print mm.mask
    # print mm.mask_and
    # print mm.mask_or
    # print mm.memoize
    # print mm.memoize_frame
    # print mm.memoized_t
    # print mm.on_color
    # print mm.pos
    # print mm.preview
    # print mm.reader
    # print mm.relative_pos
    # print mm.resize
    # print mm.rotate
    # print mm.rotation
    # print mm.save_frame
    # print mm.set_audio
    # print mm.set_duration
    # print mm.set_end
    # print mm.set_fps
    # print mm.set_ismask
    # print mm.set_make_frame
    # print mm.set_mask
    # print mm.set_memoize
    # print mm.set_opacity
    # print mm.set_pos
    # print mm.set_position
    # print mm.set_start
    # print mm.show
    # print mm.size
    # print mm.speedx
    # print mm.start
    # print mm.subclip
    # print mm.subfx
    # print mm.to_ImageClip
    # print mm.to_RGB
    # print mm.to_gif
    # print mm.to_images_sequence
    # print mm.to_mask
    # print mm.to_videofile
    # print mm.volumex
    # print mm.w
    # print mm.without_audio
    # print mm.write_gif
    # print mm.write_images_sequence
    # print mm.write_videofile
