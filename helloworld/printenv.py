from google.appengine.ext import webapp
import os

class PrintEnvironmentHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write("hello")
        for name in os.environ.keys():
            self.response.out.write("%s = %s<br />\n" % (name, os.environ[name]))



application = webapp.WSGIApplication(
    [
        ('/', PrintEnvironmentHandler),
       
    ], debug=True)

def main():
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
