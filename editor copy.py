from turtle import color
import moviepy
from moviepy.editor import *
import os
import sys
import time
import numpy as py
import logging as log
from moviepy.editor import *

# create a log file to store logs of the app
log.basicConfig(
    filename="logs.log",
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=log.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def videoDivider(path):
    # name of the video without the extension
    title = os.path.splitext(os.path.basename(path))[0]
    # get the first three words of the video name
    title = title.split(" ", 3)[0:3]
    # join the words with a space
    title = " ".join(title) + "..."

    videoduration = VideoFileClip(path).duration
    if videoduration <= 180:
        pass
    else:
        # create multiple videos
        # get the number of videos to be created
        numberofvideos = int(videoduration/180)
        # get the remaining time
        remainingtime = videoduration % 180
        # create the videos
        for i in range(numberofvideos):
            # create the video

            # get the start time
            start = i*180
            # get the end time
            end = (i+1)*180
            # create the video
            clip = VideoFileClip(path).subclip(start, end)
            clip.write_videofile("./videos/splited/" + title + "Part " +
                                 str(i+1)+".mp4", fp=24)

        clip = VideoFileClip(path).subclip(numberofvideos*180, videoduration)
        clip.write_videofile("./videos/splited/" + title + "Part " +
                             str(numberofvideos+1)+".mp4", fps=24)


def editor(paths):
    try:
        # clip for the video
        clip = VideoFileClip(paths)
        # flip the video
        clip = clip.fx(vfx.mirror_x)
        clip = clip.fx(vfx.colorx, 1.2)
        clip = clip.fx(afx.audio_normalize)

 #
#
#
#
        title = os.path.splitext(os.path.basename(paths))[0]
        print(title)
        width = clip.w
        height = clip.h
        difference = 0

        if width > height:
            difference = width - height
        if height > width:
            difference = height - width

        print(difference)
#
#
#
#
#
        clipwithborder = clip.margin(
            top=int(difference/2), bottom=int(difference/2), color=(255, 255, 255))

        print(clipwithborder.size)
#
#
#
#
#
        toptxtClip = TextClip(
            title, color="black", font="Elephant", fontsize=22).margin(top=int(difference/4), opacity=0).set_pos(("center", "top"))

        toptxtClip = toptxtClip.set_pos("top").set_duration(clip.duration)
#
#
#
#
#
        bottomtxtClip = TextClip(
            "CHEF FOOD", color="black", font="Elephant", fontsize=40).margin(left=int((width/5-20)), bottom=int(difference/4), opacity=0).set_pos(("center", "bottom")).set_duration(clip.duration)
#
#
#
#
#
        logo = (ImageClip('F:\\Projects\\Python\\bots\\VideoEditor\\ReactionEditor\\assets\\logo.png')
                .set_duration(clip.duration)
                .resize(height=80)
                .margin(right=int(width/3), bottom=int(difference/4 - 10), opacity=0)
                .set_pos("bottom"))
#
#
#
#
#
        rect = (ImageClip('F:\\Projects\\Python\\bots\\VideoEditor\\ReactionEditor\\assets\\rect.png').set_duration(
            clip.duration).resize(height=90).margin(right=int(width/6*3+10), top=int(height/4*3), opacity=0).set_pos("center"))
#
#
#
#
#
        like = (ImageClip('F:\\Projects\\Python\\bots\\VideoEditor\\ReactionEditor\\assets\\like.png').set_duration(
            clip.duration).resize(height=80).margin(right=int(width/6*5), top=int(height/4*3), opacity=0).set_pos("center"))
#
#
#
#
#
        likeText = TextClip(
            "Please Like and Follow", color="black", font="Arial-Bold", fontsize=15).margin(right=int(width/6*3), top=int(height/5*3 + 80), opacity=0).set_pos("center").set_duration(clip.duration)
#
#
#
#
#
        audio = AudioFileClip(
            'F:\\Projects\\Python\\bots\\VideoEditor\\ReactionEditor\\assets\\Drip.wav').set_duration(clip.duration).volumex(0.2).fx(afx.audio_fadein, 1)

        video_audio = clip.audio

        final_audio = CompositeAudioClip([video_audio, audio])

        clipwithborder = clipwithborder.set_audio(final_audio)

        final = CompositeVideoClip(
            [clipwithborder, toptxtClip, bottomtxtClip, logo, rect, like, likeText])
        final.write_videofile("./videos/edited/" +
                              title + ".mp4", fps=clip.fps)

        log.info("Video edited successfully")
    except Exception as e:
        print(e)
        log.error(e)
        sys.exit(1)

#
#
#
#
#


def main():
    # get the path of the video file
    # path = 'F:\\Projects\\Python\\bots\\VideoEditor\\ReactionEditor\\videos\\splited\\A wonderful recipe...Part 1.mp4'
    path = 'F:\\Projects\\Python\\bots\\VideoEditor\\ReactionEditor\\videos\\short.mp4'

    editor(path)
    # path = 'D:\\Videos For Uploading\\Village Tale\\Uploaded\\A wonderful recipe for fried chicken! must see.mp4'
    # videoDivider(path)


if __name__ == '__main__':
    main()
