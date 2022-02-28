Описание задачи
Предположим есть данные о разных автомобилях и спецтехнике. Данные представлены в виде таблицы с характеристиками. 
Вся техника разделена на три вида: спецтехника, легковые и грузовые автомобили. 

| car_type | brand | passenger_seats_count | photo_file_name | body_whl | carrying | extra |
|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
| car | Nissan xTtrail | 4 | f1.jpeg |   |  2.5 |   | 
| truck | Man |   | f2.jpeg |  8x3x2.5 |  20 |   | 
| car | Mazda 6 | 4 | f3.jpeg |   |  2.5 |   | 
| spec_machine | 	Hitachi |  | f4.jpeg |   |  1.2 | Легкая техника для уборки снега | 

Необходимо создать свою иерархию классов для данных, которые описаны в таблице. Классы должны называться CarBase (базовый класс для всех типов машин), 
Car (легковые автомобили), Truck (грузовые автомобили) и SpecMachine (спецтехника). 

Все объекты имеют обязательные атрибуты:
- car_type, значение типа объекта и может принимать одно из значений: «car», «truck», «spec_machine».
- photo_file_name, имя файла с изображением машины, допустимы названия файлов изображений с расширением из списка: «.jpg», «.jpeg», «.png», «.gif»
- brand, марка производителя машины
- carrying, грузоподъемность

В базовом классе CarBase нужно реализовать метод get_photo_file_ext для получения расширения файла изображения. 
Для грузового автомобиля необходимо в конструкторе класса определить атрибуты: body_length, body_width, body_height, отвечающие соответственно за габариты кузова — длину, ширину и высоту. 
Габариты передаются в параметре body_whl (строка, в которой размеры разделены латинской буквой «x»). 
Также для класса грузового автомобиля необходимо реализовать метод get_body_volume, возвращающий объем кузова.
В классе Car должен быть определен атрибут passenger_seats_count (количество пассажирских мест), а в классе SpecMachine — extra (дополнительное описание машины).

Полная информация о атрибутах классов приведена в таблице ниже, где 1 - означает, что атрибут обязателен для объекта, 0 - атрибут должен отсутствовать.
| car_type | brand | passenger_seats_count | photo_file_name |
|:---------:|:---------:|:---------:|:---------:|
| car_type | 1 | 1 | 1 |
| photo_file_name | 1 | 1 | 1 |
| brand | 1 | 1 | 1 |
| carrying | 1 | 1 | 1 |
| passenger_seats_count | 1 | 0 | 0 |
| body_width | 0 | 1 | 0 |
| body_height | 0 | 1 | 0 |
| body_length | 0 | 1 | 0 |
| extra | 0 | 0 | 1 |

Обратите внимание, что у каждого объекта из иерархии должен быть свой набор атрибутов и методов. 
Например, у класса легковой автомобиль не должно быть метода get_body_volume в отличие от класса грузового автомобиля. 
Имена атрибутов и методов должны совпадать с теми, что описаны выше.

Далее вам необходимо реализовать функцию get_car_list, на вход которой подается имя файла в формате csv. 
Файл содержит данные, аналогичные строкам из таблицы. 
Вам необходимо прочитать этот файл построчно при помощи модуля стандартной библиотеки csv.
Затем проанализировать строки на валидность и создать список объектов с автомобилями и специальной техникой. 
Функция должна возвращать список объектов.

Несколько примеров работы:
```
>>> from solution import *
>>> car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
>>> print(car.car_type, car.brand, car.photo_file_name, car.carrying,
... car.passenger_seats_count, sep='\n')
car
Bugatti Veyron
bugatti.png
0.312
2
>>> truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
>>> print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length,
... truck.body_width, truck.body_height, sep='\n')
truck
Nissan
nissan.jpeg
3.92
2.09
1.87
>>> spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
>>> print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying,
... spec_machine.photo_file_name, spec_machine.extra, sep='\n')
spec_machine
Komatsu-D355
93.0
d355.jpg
pipelayer specs
>>> spec_machine.get_photo_file_ext()
'.jpg'
>>> cars = get_car_list('cars_week3.csv')
>>> len(cars)
4
>>> for car in cars:
...     print(type(car))
... 
<class 'solution.Car'>
<class 'solution.Truck'>
<class 'solution.Truck'>
<class 'solution.Car'>
>>> cars[0].passenger_seats_count
4
>>> cars[1].get_body_volume()
60.0
>>>
```
