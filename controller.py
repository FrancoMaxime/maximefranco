import web
import traceback
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from web.wsgiserver import CherryPyWSGIServer

GMAIL_USER = 'archein.lol@gmail.com'
GMAIL_Recipient='franco.maxime@gmail.com'
GMAIL_PASS = ''
SMTP_SERVER = 'smtp.google.com'
SMTP_PORT = 587

class Index:
    def GET(self):
        return render_partial.index()
        
    def POST(self):
		data = web.input()
		if not'full-name' in data or data['full-name'] == '':
			return render_partial.index()
		if not 'content' in data or data['content'] == '':
			return render_partial.index()
		if not 'email' in data or data['email'] == '':
			return render_partial.index()
		if not 'subject' in data or data['subject'] == '':
			return render_partial.index()
		text = 'Message from : \n' +  data['full-name']
		text += '\nEmail : \n' +  data['email']
		text += '\nContent : \n' +  data['content']
		send_mail(GMAIL_Recipient, data['subject'], text)
		return render_partial.index()
		
        
def notfound():
    return web.notfound(render_partial.notfound())

def send_mail(recipient, subject, text):
  try:
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = u'To:' + recipient + u'\n' + u'From: ' + GMAIL_USER
    header = header + '\n' + u'Subject:' + subject + u'\n'

    msg = MIMEMultipart('alternative')
    msg.set_charset('utf8')
    msg['From'] = GMAIL_USER
    msg['To'] = recipient
    msg['Subject'] = Header(
        subject.encode('utf-8'),
        'UTF-8'
    ).encode()

    _attach = MIMEText(text.encode('utf-8'), 'plain', 'UTF-8')
    msg.attach(_attach)
    print msg.as_string()

    smtpserver.sendmail(GMAIL_USER, recipient, msg.as_string())
    smtpserver.close()
    print "DONE"
    return True
  except:
    traceback.print_exc()
    return False
    
if __name__ == "__main__":
    try:
        web.config.debug = True
        render = web.template.render('templates/', base='layout')
        render_partial = web.template.render('templates/')
        urls = (
			'/', 'Index',
			'/index','Index',
			'/home','Index',
        )
        
	    ssl_cert = '/etc/letsencrypt/live/maximefranco.be/cert.pem'
        ssl_key = '/etc/letsencrypt/live/maximefranco.be/privkey.pem'
        CherryPyWSGIServer.ssl_certificate = ssl_cert
        CherryPyWSGIServer.ssl_private_key = ssl_key
        
        app = web.application(urls, globals())
        app.notfound = notfound
        app.run()
    except:
        traceback.print_exc(file=sys.stdout)
    finally:
        print 'fin des threads'
