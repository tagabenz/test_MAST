from apscheduler.schedulers.background import BlockingScheduler
import parser


scheduler = BlockingScheduler()
last_person = "" # Последний умерший в списке

# функция - задание
def main():
    global last_person
    
    if last_person:
        if last_person == parser.get_last_person():
            print("Нет новых покойников")
        else:
            print("Найден новый покойник")
            last_person=parser.get_last_person()
            parser.parsing(last_person)   
    else:
        last_person=parser.get_last_person()
        print("Найден новый покойник")
        parser.parsing(last_person)



if __name__ == "__main__":
    scheduler.add_job(main,'cron',second="*/10")
    scheduler.start()
    

