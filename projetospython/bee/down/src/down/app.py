import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import yt_dlp
import os
import subprocess

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

        # Add a selection for download format
        self.format_select = toga.Selection(items=['mp3', 'mp4'], style=Pack(padding=(0, 5)))
        main_box.add(self.format_select)

        # Add a button to start download
        download_button = toga.Button('Download', on_press=self.download_media, style=Pack(padding=5))
        main_box.add(download_button)

        # Add a button to play the downloaded media
        self.play_button = toga.Button('Play Media', on_press=self.play_media, style=Pack(padding=5))
        self.play_button.enabled = False
        main_box.add(self.play_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def download_media(self, widget):
        url = self.url_input.value
        download_format = self.format_select.value
        if url and download_format:
            try:
                self.download_path = os.path.join(self.get_application_directory(), 'Downloads')

                if not os.path.exists(self.download_path):
                    os.makedirs(self.download_path)

                if download_format == 'mp3':
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'm3u',
                            'preferredquality': '192',
                        }],
                        'outtmpl': os.path.join(self.download_path, '%(id)s.%(ext)s'),  # Save as id.mp3
                    }
                else:
                    ydl_opts = {
                        'format': 'bestvideo+bestaudio',
                        'outtmpl': os.path.join(self.download_path, '%(id)s.%(ext)s'),  # Save as id.mp4
                    }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                self.main_window.info_dialog('Download Complete', 'Media downloaded successfully.')
                self.play_button.enabled = True
            except Exception as e:
                self.main_window.info_dialog('Error', f'Failed to download media: {e}')
        else:
            self.main_window.info_dialog('Error', 'Please enter a valid YouTube URL and select a format.')

    def play_media(self, widget):
        media_file = os.listdir(self.download_path)[0]  # Assume there's only one file
        media_path = os.path.join(self.download_path, media_file)
        
        # Using VLC player to play the media
        try:
            subprocess.run(['vlc', media_path])
        except Exception as e:
            self.main_window.info_dialog('Error', f'Failed to play media: {e}')

    def get_application_directory(self):
        return os.path.join(os.path.expanduser('~'), 'myapp')

def main():
    return Down()
