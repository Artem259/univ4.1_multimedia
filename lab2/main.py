import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QStyle

from MainWindow import Ui_MainWindow


def hhmmss(ms):
    s = round(ms / 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return ("%02d:%02d:%02d" % (h, m, s)) if h else ("%02d:%02d" % (m, s))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.player = QMediaPlayer(self, QMediaPlayer.VideoSurface)

        self.player.mediaStatusChanged.connect(self.player_media_status_handler)
        self.player.stateChanged.connect(self.player_state_handler)
        self.player.positionChanged.connect(self.player_position_handler)
        self.player.durationChanged.connect(self.player_duration_handler)
        self.player.error.connect(self.player_error_handler)
        self.actionOpen.triggered.connect(self.open_file_handler)

        self.video_widget = QVideoWidget()
        self.player.setVideoOutput(self.video_widget)
        self.verticalLayout.insertWidget(0, self.video_widget)

        self.show()

    def player_media_status_handler(self, status):
        if status == QMediaPlayer.LoadedMedia:
            self.player.play()

    def player_state_handler(self, state):
        if state == QMediaPlayer.PlayingState:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def player_position_handler(self, position):
        self.playerSlider.setValue(position)
        self.positionLabel.setText(hhmmss(position))

    def player_duration_handler(self, duration):
        self.playerSlider.setRange(0, duration)
        self.durationLabel.setText(hhmmss(duration))

    def player_error_handler(self, error):
        self.statusBar.showMessage(f"Error [{error}] " + self.player.errorString(), 5000)

    def open_file_handler(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "All files (*.*);;mp3 Audio (*.mp3);;mp4 Video (*.mp4);;avi Video (*.avi)",
        )

        if path:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(path)))


if __name__ == '__main__':
    os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
