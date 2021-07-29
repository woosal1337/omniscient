import speedtest
import rich
from rich import pretty
from rich.console import Console

console = Console()

class speedtesting():

    def __init__(self):

        self.st = speedtest.Speedtest()

    def get_download_speed(self):

        """
        Return Download Speed
        :return:
        """

        download = self.st.download()
        download = download / 1048076

        console.print(f"Download Speed: {round(download, 3)} Mbps", style="green")
        return f"Download Speed: {round(download, 3)} Mbps"

    def get_upload_speed(self):

        """
        Return Upload Speed
        :return:
        """

        upload = self.st.upload()
        upload = upload / 1048076

        console.print(f"Upload Speed: {round(upload, 3)} Mbps", style="green")
        return f"Upload Speed: {round(upload, 3)} Mbps"

    def get_ping(self):

        """

        :return:
        """

        self.st.get_servers([])
        ping = self.st.results.ping

        console.print(f"Ping: {ping}", style="green")
        return f"Ping: {ping}"

    def get_all_speed(self):

        """
        Return Download/Upload/Ping Speed and Values
        :return:
        """

        download = self.st.download()
        upload = self.st.upload()

        download = download / 1048076
        upload = upload / 1048076
        self.st.get_servers([])
        ping = self.st.results.ping

        console.print(f"Download Speed: {round(download, 3)} Mbps\nUpload Speed: {round(upload, 3)} Mbps\nPing: {ping}",
                      style="green")
        return f"Download Speed: {round(download, 3)} Mbps\nUpload Speed: {round(upload, 3)} Mbps\nPing: {ping}"