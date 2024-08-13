import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import yt_dlp
import os

class Down(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Add a label
        label = toga.Label('My first application', style=Pack(padding=(0, 5)))
        main_box.add(label)

        # Add a text input for YouTube URL
        self.url_input = toga.TextInput(style=Pack(padding=(0, 5)))
        self.url_input.placeholder = 'Enter YouTube URL'
        main_box.add(self.url_input)

        # Add a button to start download
        download_button = toga.Button('Download Video', on_press=self.download_video, style=Pack(padding=5))
        main_box.add(download_button)

        # Add a button to open the video
        self.open_button = toga.Button('Open Video', on_press=self.open_video, style=Pack(padding=5))
        self.open_button.enabled = False
        main_box.add(self.open_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def download_video(self, widget):
        url = self.url_input.value
        if url:
            try:
                self.download_path = os.path.join(self.get_application_directory(), 'Downloads')

                if not os.path.exists(self.download_path):
                    os.makedirs(self.download_path)

                ydl_opts = {
                    'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                self.main_window.info_dialog('Download Complete', 'Video downloaded successfully.')
                self.open_button.enabled = True
            except Exception as e:
                self.main_window.info_dialog('Error', f'Failed to download video: {e}')
        else:
            self.main_window.info_dialog('Error', 'Please enter a valid YouTube URL.')

    def open_video(self, widget):
        video_file = os.listdir(self.download_path)[0]  # Assume there's only one file
        video_path = os.path.join(self.download_path, video_file)

        # Call the native Android activity to play the video
        intent = self.get_main_activity().getIntent()
        intent.setClassName("com.example.down", "com.example.down.VideoPlayerActivity")
        intent.putExtra("videoPath", f'file://{video_path}')
        self.get_main_activity().startActivity(intent)

    def get_application_directory(self):
        return os.path.join(os.path.expanduser('~'), 'myapp')

def main():
    return Down()
