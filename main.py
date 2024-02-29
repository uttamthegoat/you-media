from flask import Flask,render_template,jsonify,request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")  # Corrected line


@app.route('/downloadmedia', methods=["POST"])
def download():
    if request.method == "POST":
        result= request.form
        video_url= request.form['URL_Link']
        def video_dowload(url):
            video=YouTube(url)
            stream=video.streams.get_highest_resolution()
            stream.download() 
        video_dowload(video_url)
        return render_template("result.html",result = result) 

if __name__ == '__main__':
    app.run(debug=True)
