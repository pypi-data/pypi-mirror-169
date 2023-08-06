import datetime as dt
import time
from pathlib import Path
import requests
import subprocess
from urllib.parse import urljoin

# https://github.com/open-ephys/plugin-GUI/blob/main/Source/Utils/OpenEphysHttpServer.h

EXE_PATH = r"C:\Program Files\Open Ephys\open-ephys.exe"


def with_timeout(cb, timeout, mesg):
    tic = time.time()
    while not cb():
        if (time.time() - tic) > timeout:
            raise ValueError(mesg)
        time.sleep(timeout * 0.25)


class OpenEphysClient:

    def __init__(self, host='localhost', port=37497, exe_path=EXE_PATH):
        '''
        Client for communicating with OpenEphys HTTP server

        Parameters
        ----------
        host : string
            Hostname or IP address (can be localhost) of OpenEphys server.
        port : int
            Port number OpenEphys is listening on.
        exe_path : {pathlib.Path, str}
            Path to EXE for launching OpenEphys. Only works if client is
            running on the same computer as the OpenEphys server.
        '''
        self.base_uri = f'http://{host}:{port}/api/'

    def _get(self, path):
        '''
        Get a request from the server and return the response as a dictionary
        '''
        url = urljoin(self.base_uri, path)
        response = requests.get(url)
        return response.json()

    def _put(self, path, kwargs):
        '''
        Send a request to the server and return the response as a dictionary
        '''
        url = urljoin(self.base_uri, path)
        response = requests.put(url, json=kwargs)
        return response.json()

    def _get_status(self):
        return self._get('status')['mode']

    def _set_status(self, mode):
        return self._put('status', {'mode': mode})

    # Gets status of recording. Will be 'IDLE', 'ACQUIRE', 'RECORD'.
    status = property(_get_status, _set_status)

    def acquire(self, timeout=5):
        '''
        Switch to acquisition mode
        '''
        self.status = 'ACQUIRE'
        with_timeout(lambda: self.status == 'ACQUIRE', timeout,
                     'Could not start acquisition')

    def record(self, timeout=5):
        '''
        Switch to recording mode
        '''
        self.status = 'RECORD'
        with_timeout(lambda: self.status == 'RECORD', timeout,
                     'Could not start recording')

    def stop(self, timeout=5):
        '''
        Stop acquisition/recording
        '''
        self.status = 'IDLE'
        with_timeout(lambda: self.status == 'IDLE', timeout,
                     'Could not stop acquisition/recording')

    def connect(self, auto_open=False):
        '''
        Check to see if OpenEphys server is up and running

        Parameters
        ----------
        auto_open : bool
            If True and OpenEphys server is not up and running, launch an
            OpenEphys process.
        '''
        try:
            self.status
        except requests.ConnectionError:
            if auto_open:
                subprocess.Popen(EXE_PATH)
                self.status

    def close(self):
        '''
        Close the GUI window
        '''
        self._put('window', {'command': 'quit'})

    def send_message(self, message):
        '''
        Send a message to OpenEphys

        Parameters
        ----------
        message : str
            Message to send.
        '''
        self._put('message', {'text': message})

    def iter_recording_nodes(self):
        '''
        Iterate through recording nodes and yield node IDs
        '''
        for p in self._get('recording')['record_nodes']:
            yield p['node_id']

    def set_recording_filename(self, filename, mkdir=True, node='all'):
        '''
        Set recording filename

        Parameters
        ----------
        filename : {str, pathlib.Path}
            Filename to save to.
        mkdir : bool
            If True, ensure parent folder exists.
        node : {None, 'all', int}
            If None, only the general filename is set (not sure what this is,
            perhaps for OpenEphys hardware). If 'all', sets the recording
            filename on all nodes. If int, sets the recording filename only for
            the specified node.
        '''
        filename = Path(filename)
        if not filename.parent.exists() and mkdir:
            filename.parent.mkdir(parents=True)

        payload = {
            'parent_directory': str(filename.parent),
            'base_text': str(filename.name),
            'prepend_text': '',
            'append_text': '',
        }
        if node is None or node == 'all':
            self._put('recording', payload)
        if node == 'all':
            for node in self.iter_recording_nodes():
                self._put(f'recording/{node}', payload)
        elif node is not None:
            self._put(f'recording/{node}', payload)

    def get_recording_filename(self):
        '''
        Get the current recording filename
        '''
        response = self._get('recording')
        path = Path(response['parent_directory'])
        return path / response['base_text']

    def get_processors(self):
        '''
        Gets the available processors
        '''
        return self._get('processors')
