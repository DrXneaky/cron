from crontab import CronTab
"""
Here the object can take two parameters one for setting
the user cron jobs, it defaults to the current user
executing the script if ommited. The fake_tab parameter
sets a testing variable. So you can print what could be
written to the file onscreen instead or writting directly
into the crontab file.
"""
tab = CronTab()
cmd = 'echo +1 > cron_output'
# You can even set a comment for this command
cron_job = tab.new(cmd, comment='This is the main command')
cron_job.minute().every(1)
#writes content to crontab
tab.write()
print tab.render()

