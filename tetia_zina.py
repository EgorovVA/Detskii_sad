import random
import shelve

class color_RGB:
    def genereit_color(self): 
        return " R: "+str(random.randrange(0, 255, 1))+ " G: " +str(random.randrange(0, 255, 1))+ " B: " +str(random.randrange(0, 255, 1))

class bascet(color_RGB):
    def down(self):
        self.bols = random.randrange(1, 10, 1)
        self.cube = random.randrange(1, 10, 1)

        return self.bols,self.cube,self.genereit_color()
    
class mom:
    def inslall_child(self):
        return self.name, self.age , self.gender
    def unslall_child(self):
        return [self.name, self.age , self.gender]
    
class child(mom):
    def __init__(self, name, age, gender):
        self.name=name
        self.age = age
        self.gender = gender

class analitic:
    def init_analitic(self, data_inf , age, m , w):
        self.data_inf = data_inf 
        self.data_inf['возвраст'] =age
        self.data_inf['мальчики'] = m
        self.data_inf['девочки'] = w

    def app_del_gender_age(self, load, app_del=1):
        age = self.data_inf['возвраст']
        age[load[1]] += app_del
        self.data_inf['возвраст'] =age
    
        if(load[2]=='м'or load[2]=='М'):
            gender = self.data_inf['мальчики']
            gender += app_del
            self.data_inf['мальчики'] = gender
        else:
            gender =self.data_inf['девочки']
            gender += app_del
            self.data_inf['девочки'] = gender

    def analitic_gender(self):
        return self.data_inf['девочки'], self.data_inf['мальчики']
    
    def analitic_age(self):
        return self.data_inf['возвраст']


class vospitatel(bascet,mom,analitic):
    def __init__(self, data,data_inf , age, m ,w):
        self.init_analitic(data_inf , age, m ,w)
        self.data = data

    def app_child(self,load):

        vedro =  bascet()
        self.app_del_gender_age(load)
        

        if('а'<=load[0][0] and 'я'>=load[0][0]):
            char = chr(ord(load[0][0])-32)
        else:
            char = load[0][0]
        self.data[char]+=[load+vedro.down()]

    def finde_el(self, arr,load):
        for i in range(len(arr)):
            print(len(arr))
            if(arr[i][0].lower()==load[0].lower() and arr[i][1]==load[1] and arr[i][2]==load[2]):
                
                return i
        return -1
    
    def del_child(self,load):


        self.app_del_gender_age(load, -1)

        if('а'<=load[0][0] and 'я'>=load[0][0]):
            char = chr(ord(load[0][0])-32)
        else:
            char = load[0][0]

        arr = self.data[char]
        print("!!!!!!!",len(arr))
        index = self.finde_el(arr,load)
        if index !=0:
            print("Забираем игрушки: "+str(arr[index][3])+ " " +str(arr[index][4])+str(arr[index][5]) )
            arr.pop(index)
        else:
            print("Такого ребенка нет")
        self.data[char] = arr

    def write_all_data(self, db):
        for x in self.data.keys():
            print ( x ,"   ", self.data[ x ])


if __name__ == '__main__':
    db= shelve.open("Дети")
    db_info= shelve.open("Доп_информ")
    


    m = db_info['мальчики']
    w = db_info['девочки']
    age = db_info['возвраст']



    a = vospitatel(db, db_info, age, m, w)
    cout_arr_age = []
    for i in range(8):
        cout_arr_age.append(i)
    
    start =  int(input("Создать новый файл или работать с ныненшним(0/1): "))
    if(start == 0):
        m = 0
        w = 0
        age = []
        for i in range(32):
            db[chr(ord('А')+i)]=[]
        for i in range(8):
            age.append(0)
        db_info['мальчики'] =0
        db_info['девочки'] = 0
        db_info['возвраст'] =age

    while(1):

        menu = int(input("Здраствуйте, что вы хотите сделать (напишите число из пунктов):\n 1)Привести детей\n 2)Время уже 12:00, надо узнать сколько мальчиков и девочек в садике\n 3)Время уже 12:00, надо узнать колличсетыо детей разного возвраста\n 4)Забрать детей\n 5)Вывести все данные о детях в садике\n 6)Сохранить и выйти \n"))
        if(menu==1):
            count_child = input("Сколько детей вы привели в садик: ")
            for i in range (int(count_child)):
                name = input("Введите ФИО вашего ребёночка: ")
                age = input("Введите сколько ему годиков(0-7): ")
                gender = input("Введите какого он пола (м/ж): ")
                reg_gata = child(name,int(age),gender)
                load = reg_gata.inslall_child()
                a.app_child(load)

        if(menu==2):
            info = a.analitic_gender()
            print("Девочек: "+str(info[0]) + " Мальчиков: "+str(info[1]))

        if(menu==3):
            info_age = a.analitic_age()
            print(cout_arr_age)
            string =' '
            for i in range(8):
                string += str(info_age[i])+', '
            print(string)
        
        if(menu==4):
            name = input("Введите ФИО вашего ребёночка: ")
            age = input("Введите сколько ему годиков(0-7): ")
            gender = input("Введите какого он пола (м/ж): ")
            reg_gata = child(name,int(age),gender)
            load = reg_gata.unslall_child()
            a.del_child(load)
            db.close()
            db= shelve.open("Дети")
        if(menu==5):
            a.write_all_data(db)
            
        if(menu==6):
            db.close()
            raise SystemExit
           
        


    


