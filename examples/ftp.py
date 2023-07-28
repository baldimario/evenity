"""FTP Example"""
import os
import dotenv
from hooked.observer import Observer # pylint: disable=import
from hooked.event.plugins.ftp import FTPObservableConsumer

ABSPATH = os.path.abspath(os.path.dirname(__file__))

class FTPListener(Observer):
    """FTPListener class"""

    def __init__(self, observable):
        super().__init__(observable)
        self.listen("ftp", self.on_ftp)

    def on_ftp(self, file):
        """On ftp event"""
        print(f'Got file, path: {file}')
        os.unlink(file)

def main():
    """Main function"""
    ftp_consumer = FTPObservableConsumer(
        user=os.environ.get('FTP_USER'),
        password=os.environ.get('FTP_PASSWORD'),
        port=os.environ.get('FTP_PORT'),
        path=os.path.join(ABSPATH, os.environ.get('FTP_PATH'))
    )

    FTPListener(ftp_consumer)

    ftp_consumer.consume()

if __name__ == '__main__':
    main()