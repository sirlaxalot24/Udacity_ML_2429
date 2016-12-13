
import tarfile
import os


os.chdir(..)
tfile = tarfile.open("enron_mail_20150507.tgz", "r:gz")
tfile.extractall("..")

print "you're ready to go!"
