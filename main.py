from flask import Flask, render_template, jsonify, request
from pytube import YouTube, Playlist
import os
import instaloader
from utils import delete_txt_files, try_except_wrapper


app = Flask(__name__)

@try_except_wrapper
@app.route('/')
def hello_world():
    return render_template("index.html")


@try_except_wrapper
@app.route('/youtube-media')
def youtube_media():
    return render_template("youtube.html")


@try_except_wrapper
@app.route('/downloadmedia', methods=["POST"])
def download_media():
    if request.method == "POST":
        result = request.form
        video_url = request.form['URL_Link']

        download_folder = "youtube\\videos"
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        print(video_url)
        
        video = YouTube(video_url)
        stream = video.streams.get_highest_resolution()
        video_path = os.path.join(download_folder, f"{video.title}.mp4")
        stream.download(output_path=download_folder)

        return render_template("result.html", result=result, success=True, video_path=video_path)
        
@try_except_wrapper
@app.route('/download-playlist', methods=["POST"])
def download_playlist():
    if request.method == "POST":
        result = request.form
        links = request.form['playlist_Link']
        folder_name = request.form['folder_Name']

        SAVE_PATH = "youtube\\"+folder_name
        if  not os.path.exists(SAVE_PATH):
            os.makedirs(SAVE_PATH)

        playlist = Playlist(links)
        PlayListLinks = playlist.video_urls
        N = len(PlayListLinks)
        
        print(f"This link found to be a Playlist Link with number of videos equal to {N} ")
        print(f"\n Lets Download all {N} videos")

        for i,link in enumerate(PlayListLinks):

            yt = YouTube(link)
            d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            d_video.download(SAVE_PATH)
            print(i+1, ' Video is Downloaded.')
        return render_template("result.html", result=result, success=True, video_path=SAVE_PATH)




@try_except_wrapper
@app.route('/instagram-post')
def instagram_post():
    return render_template("instagram.html")


@try_except_wrapper
@app.route('/download-insta-posts', methods=["POST"])
def download_all_posts():
    if request.method == "POST":
        result = request.form
        username = request.form['username']

        loader = instaloader.Instaloader(download_comments=False, save_metadata=False, download_geotags=False, download_video_thumbnails=False)
        loader.download_comments = loader.save_metadata = False

        download_folder = "instagram-"+username
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        
        profile = instaloader.Profile.from_username(
            loader.context, username)

        cnt=0
        for post in profile.get_posts():
            # if(cnt==5):
            #     break
            if(post.is_video is not True):
                loader.download_post(post, target=download_folder)
                cnt+=1
        
        delete_txt_files(download_folder)

        print(f"All posts from {username} downloaded successfully.")
        return render_template("result.html", result=result, success=True)


@try_except_wrapper
@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)

