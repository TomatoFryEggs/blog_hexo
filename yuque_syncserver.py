
import web
import subprocess

urls = ("/sync-yuque", "callSync")
app = web.application(urls, globals())

class callSync:
    def POST(self):
        p = subprocess.Popen(["npm", "run","g"], stdout=subprocess.PIPE)
        print(p.communicate()[0])
        return 'sync done'

if __name__ == "__main__":
    app.run()
