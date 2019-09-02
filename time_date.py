from PyQt5.QtCore import QDate, Qt, QTime, QDateTime

now = QDate.currentDate()
print(now.toString(Qt.ISODate))

time = QTime.currentTime()
print(time.toString())

datetime = QDateTime.currentDateTime()
print(datetime.toString('yyyy-MM-dd\nhh:mm:ss'))
print(datetime.toString(Qt.DefaultLocaleShortDate))
