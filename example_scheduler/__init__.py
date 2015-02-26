"""
Example Scheduler
"""

from tornado.ioloop import IOLoop
from apscheduler.schedulers.tornado import TornadoScheduler
from time import sleep

count = 0
def tick():
    global count
    count += 1
    sleep(3)
    print('Counter: %s' % count)

def getJobs():
    for job in scheduler.get_jobs():
        print job

scheduler = TornadoScheduler()
def main():
    # Let's use the TornadoScheduler class we instantiated above 
    global scheduler

    #Example date job
    scheduler.add_job(tick, 'date', name='tick-date-2015-02-25 20:32:00', run_date='2015-02-25 22:26:00', timezone='America/Chicago')

    # Example interval jobs
    scheduler.add_job(tick, 'interval', name='tick-interval-3-seconds', seconds=4, timezone='America/Chicago')
    scheduler.add_job(getJobs, 'interval', name='getJobs-interval-3-seconds', seconds=3, timezone='America/Chicago')

    scheduler.start()
    print('Press Ctrl+C to exit')

    # Execution will block here until Ctrl+C is pressed.
    try:
        IOLoop.instance().start()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == '__main__':
    main()
