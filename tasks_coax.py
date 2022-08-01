from moviepy.editor import *
import os
from noteukrfilms.main import *


def task1() -> int:
    """
    There is string s = "Python Bootcamp". Write the code that hashes string.
    """
    s = "Python Bootcamp"
    return hash(s)


def task2(url: str) -> str:
    """
    You are working on a project for TikTok. 
    The future project will be a web-site of all public GIF images. 
    You need to write a function that converts TikTok video to GIF. 
    The input parameter is url address of TikTok video.
    The output parameter is path to GIF image, i.e. "/home/user/TikTok-example-1.gif".
    """
    clip = (VideoFileClip(url))
    clip.write_gif("output.gif")
    return os.path.abspath(os.getcwd() + "/output.gif")


def task_optional():
    test = NoteFilm("file.csv")
    data2 = test.read_notes()
    print(data2)
    test.print_notes()
    print(test.get_avg_rating())
    test.add_note(film_name="Iron Man", note="Just good film!", rating=4)
    test.remove_note(num=1)


print("Task 1: ", task1())
print("Task 2: ", task2("https://v16-webapp.tiktok.com/2b369a9bec37bcb3da356f6ace782194/62e7f5ef/video/tos/alisg/tos-alisg-pve-0037c001/4e1c35c0714d4affa4f9409d1343d0a1/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=1774&bt=887&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8Zdwr1we2NRMTyl7Gb&mime_type=video_mp4&qs=0&rc=Ozs3PDtmZDkzaDg1OmY4PEBpM283OTQ6ZmllPDMzODczNEBhNjNhMWMvNi8xLTQwLWNhYSNraTQ0cjRnbmNgLS1kMS1zcw%3D%3D&l=2022080109485201019017602108166609"))
print("Task optional: \n")
task_optional()
