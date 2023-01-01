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
    eachVideoDuration = 180
    FullSPlittedFolder = "F:\\Projects\\Python\\bots\\VideoEditor\\Video Editor\\videos\\FullSplitted\\"

    SplittedFolder = "F:\\Projects\\Python\\bots\\VideoEditor\\Video Editor\\videos\\splited\\"

    try:
        # check if path exists
        if os.path.exists(path):
            print("Path exists")
            if os.path.isfile(path):
                print("Path is a file")
    except Exception as e:
        log.error(e)
        print("Error occured while checking the path")

    # name of the video without the extension
    title = os.path.splitext(os.path.basename(path))[0]
    # # get the first three words of the video name
    title = title.split(" ", 3)[0:3]
    # # join the words
    title = " ".join(title)

    videoduration = VideoFileClip(path).duration
    if videoduration <= eachVideoDuration:
        print("Video Duration is less than " +
              str(eachVideoDuration) + " seconds")
    else:
        # create multiple videos
        # get the number of videos to be created
        numberofvideos = int(videoduration/eachVideoDuration)
        # get the remaining time
        remainingtime = videoduration % eachVideoDuration
        # create the videos
        for i in range(numberofvideos):
            # create the video

            # get the start time
            start = i*eachVideoDuration
            # get the end time
            end = (i+1)*eachVideoDuration
            # create the video
            print("Creating " + str(i+1) + " video from " +
                  str(start) + " to " + str(end))

            clip = VideoFileClip(path).subclip(start, end)
            try:
                print("Writing video file ")
                clip.write_videofile(SplittedFolder + title + " Part " +
                                     str(i+1)+".mp4", fps=24)
            except Exception as e:
                log.error(e)
                print(e)
                print("Error occured while Writing the video")

        clip = VideoFileClip(path).subclip(
            numberofvideos*eachVideoDuration, videoduration)
        clip.write_videofile(SplittedFolder + title + " Part " +
                             str(numberofvideos+1)+".mp4", fps=24)
        # move video to the splited folder
        try:
            moveVideo(path, FullSPlittedFolder)
        except Exception as e:
            log.error(e)
            print(e)
            print("Error occured while moving the video")
        print("Video Splitted\n\n")


def editor(paths):
    FullEditedFolder = "F:\\Projects\\Python\\bots\\VideoEditor\\Video Editor\\videos\FullEdited\\"
    ChannelName = "Village Tale Food".upper()
    print("Channel: " + ChannelName)
    try:
        # clip for the video
        clip = VideoFileClip(paths)
        # flip the video
        # clip = clip.fx(vfx.mirror_x) #flip mirror video
        clip = clip.fx(vfx.colorx, 1.2)
        clip = clip.fx(afx.audio_normalize)

#
#
#
#

        title = os.path.splitext(os.path.basename(paths))[0]
        # get 5 words of the video name
        title = title.split(" ", 5)[0:5]
        title = " ".join(title).upper()

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
            top=int(difference/2), bottom=int(difference/2), color=(213, 213, 213))

        print(clipwithborder.size)
#
#
#
#
#
        toptxtClip = TextClip(
            title, color="#4F4E4E", font="Inter-Bold", stroke_width=2, stroke_color="#4F4E4E", kerning=2, fontsize=45).margin(top=int(difference/4), opacity=0).set_pos(("center", "top")).set_duration(clip.duration)

        # add wraptext, fontweight, fontcolor, fontsize, fontfamily to a new file
#
#
#
#
        bottomtxtClip = TextClip(
            ChannelName, color="#4F4E4E", font="Inter-Bold", stroke_width=2, stroke_color="#4F4E4E", kerning=2, fontsize=45).margin(bottom=int(difference/3), opacity=0).set_pos(("center", "bottom")).set_duration(clip.duration)
#
#
#
#
#
        logo = (ImageClip(r'F:\Projects\Python\bots\VideoEditor\Video Editor\assets\logo.png')
                .set_duration(clip.duration)
                .resize(height=80)
                .margin(bottom=int(difference/7), opacity=0)
                .set_pos("bottom"))
#
#
#
#
#
        # rect = (ImageClip('F:\\Projects\\Python\\bots\\VideoEditor\\ReactionEditor\\assets\\rect.png').set_duration(
        # clip.duration).resize(height=90).margin(right=int(width/6*3+10), top=int(height/4*3), opacity=0).set_pos("center"))
#
#
#
#
#
        # like = (ImageClip(r'F:\Projects\Python\bots\VideoEditor\Video Editor\assets\logo.png').set_duration(
        # clip.duration).resize(height=80).margin(right=int(width/6*5), top=int(height/4*3), opacity=0).set_pos("center"))
#
#
#
#
# #
#         likeText = TextClip(
#             "Please Like and Follow", color="black", font="Arial-Bold", fontsize=15).margin(right=int(width/6*3), top=int(height/5*3 + 80), opacity=0).set_pos("center").set_duration(clip.duration)
# #
#
#
#
#
        audio = AudioFileClip(
            r'F:\Projects\Python\bots\VideoEditor\Video Editor\assets\Drip.wav').set_duration(clip.duration).volumex(0.05).fx(afx.audio_fadein, 1)

        video_audio = clip.audio

        final_audio = CompositeAudioClip([video_audio, audio])

        clipwithborder = clipwithborder.set_audio(final_audio)

        final = CompositeVideoClip(
            [clipwithborder, toptxtClip, bottomtxtClip, logo])
        final.write_videofile("Video Editor/videos/edited/" +
                              title + ".mp4", fps=clip.fps)

        log.info("Video edited successfully")
        try:
            # move video to the edited folder
            moveVideo(paths, FullEditedFolder)
        except Exception as e:
            print(e)
            print("Error occured while moving the video")
            log.error(e)

        print("Video edited successfully \n\n\n")

    except Exception as e:
        print(e)
        log.error(e)
        sys.exit(1)

#
#
#
#
#


def moveVideo(videoPath, FolderPath):
    print("\nMoving video folder...")

    try:
        shutil.move(videoPath, FolderPath)
        print("Moved to " + str(FolderPath) + "uploaded folder")
    except Exception as e:
        print("Error in moving video to uploaded folder" + str(e))
        return


def getSplittedVideos():
    print("Getting videos")
    path = r'F:\Projects\Python\bots\VideoEditor\Video Editor\videos\splited'
    videos = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".mp4"):
                videos.append(os.path.join
                              (root, file))
    return videos


# get video files from the folder
def getUneditedVideos():
    print("Getting videos")
    try:
        path = r'F:\Projects\Python\bots\VideoEditor\Video Editor\videos\Unedited'
        videos = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".mp4"):
                    videos.append(os.path.join(root, file))
    except Exception as e:
        print("Error getting videos")
        print(e)
        log.error(e)

    return videos


def menu():
    print("1. Split videos")
    print("2. Edit videos")
    print("3. Exit")
    choice = input("Enter your choice: ")

    return choice


def main():
    # path = r'F:\Projects\Python\bots\VideoEditor\Video Editor\videos\splited\short.mp4'
    # editor(path)
    choice = menu()
    try:
        if choice == "1":
            videos = getUneditedVideos()
            print(videos)
            for video in videos:
                splitVideo(video)
        elif choice == "2":
            videos = getSplittedVideos()
            print(videos)
            for video in videos:
                editor(video)
        elif choice == "3":
            sys.exit(1)
    except Exception as e:
        print(e)
        print("Error occured")
        sys.exit(1)


if __name__ == '__main__':
    main()
