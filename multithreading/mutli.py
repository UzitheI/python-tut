import threading
import time

def eating_food(food_name):
    time.sleep(3)
    print(f" I'm eating {food_name}")

def walking_the_dog(dog_name):
    time.sleep(6)
    print(f"I'll be walking {dog_name}")
    
def attending_marriage(husband,wife):
    time.sleep(10)
    print(f"I'll be attending {husband}'s & {wife}'s marriage.")


thread1=threading.Thread(target=eating_food,args=('Momo',))

thread2=threading.Thread(target=walking_the_dog, args=('dogesh',))

thread3=threading.Thread(target=attending_marriage,args=('Ram','Sita'))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()


