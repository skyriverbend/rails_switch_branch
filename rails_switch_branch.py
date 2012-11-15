#!/usr/local/bin/python
import sys
import subprocess
import re

BRANCH_NAME = sys.argv[1]

print "*** Switching from current branch to: " + BRANCH_NAME

files_changed = subprocess.check_output(("git diff " + BRANCH_NAME + " --name-status").split())
migrations = re.findall("A\\tdb/migrate/([0-9]+)", files_changed)

for migration in reversed(migrations):
  sh_command = "bundle exec rake db:migrate:down VERSION=" + migration
  print "*** Running: " + sh_command
  print
  subprocess.call(sh_command.split())

print "*** Discarding any changes to db/schema.rb"
print
subprocess.call("git checkout db/schema.rb".split())
subprocess.call(("git checkout " + BRANCH_NAME).split())

print
print "*** Running: bundle exec rake db:migrate"
print
subprocess.call("bundle exec rake db:migrate".split())

print "*** Running: bundle exec rake db:test:prepare"
print
subprocess.call("bundle exec rake db:test:prepare".split())

print
print '*** Successfully switched branches and migrated to "' + BRANCH_NAME + '"'
print
