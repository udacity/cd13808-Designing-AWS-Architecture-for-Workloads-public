from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

def backup_database():
    print(f"Backing up database at {datetime.datetime.now()}")
    # Simulating database backup
    # In a real scenario, you would add code to perform the actual backup

scheduler = BlockingScheduler()
scheduler.add_job(backup_database, 'interval', hours=24)

if __name__ == '__main__':
    scheduler.start()