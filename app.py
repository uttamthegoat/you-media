from flask import Flask, render_template, jsonify, request
from pytube import YouTube
import os
import instaloader
from utils import delete_txt_files


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/youtube-media')
def youtube_media():
    return render_template("youtube.html")


@app.route('/downloadmedia', methods=["POST"])
def download():
    if request.method == "POST":
        result = request.form
        video_url = request.form['URL_Link']

        download_folder = "youtube"
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        try:
            video = YouTube(video_url)
            stream = video.streams.get_highest_resolution()
            video_path = os.path.join(download_folder, f"{video.title}.mp4")
            stream.download(output_path=download_folder)

            return render_template("result.html", result=result, success=True, video_path=video_path)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template("result.html", result=result, success=False, error_message=error_message)


@app.route('/instagram-post')
def instagram_post():
    return render_template("instagram.html")


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

        try:
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
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template("result.html", result=result, success=False, error_message=error_message)


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)

