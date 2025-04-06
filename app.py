from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from camera import VideoCamera

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Enables WebSocket support

# Initialize the camera with socketio for alert emission
camera = VideoCamera(socketio)

@app.route('/')
def index():
    return render_template('index.html')  # Main page

def generate_frames():
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    socketio.run(app, debug=True)
