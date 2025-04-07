CREATE DATABASE sqltables;
USE sqltables;

CREATE TABLE login1(
    uid INT NOT NULL AUTO_INCREMENT, 
    uname VARCHAR(30), 
    password VARCHAR(30), 
    PRIMARY KEY (uid)
);

INSERT INTO login1(uname,password) VALUES("sample1","sample1");

CREATE TABLE infologin(
    uid INT NOT NULL AUTO_INCREMENT,
    accname VARCHAR(30), 
    accnum VARCHAR(30), 
    accage INT, 
    accg VARCHAR(30),
    FOREIGN KEY (uid) REFERENCES login1(uid)
);

CREATE TABLE menu(Categories VARCHAR(50), Click VARCHAR(20));
INSERT INTO menu VALUES("Mobiles_Computers_Accessories","P");
INSERT INTO menu VALUES("Beauty_Health","Q");
INSERT INTO menu VALUES("Groceries","R");
INSERT INTO menu VALUES("Sports_Bags_Luggage","S");
INSERT INTO menu VALUES("Kids_Toys_Games","T");
INSERT INTO menu VALUES("Entertainment","U");
INSERT INTO menu VALUES("Back","X");

CREATE TABLE mobiles_computers_accessories(Sno INT, Product_Name Varchar(30), Price INT, Click INT);
INSERT INTO mobiles_computers_accessories VALUES(1,"One Plus Phone",29500,1);
INSERT INTO mobiles_computers_accessories VALUES(2,"Asus Laptop",34000,2);
INSERT INTO mobiles_computers_accessories VALUES(3,"Powertronics Power Bank",2400,3);
INSERT INTO mobiles_computers_accessories VALUES(4,"Apple Ipad",89000,4);
INSERT INTO mobiles_computers_accessories VALUES(5,"Canon D500 Camera",18000,5);
INSERT INTO mobiles_computers_accessories VALUES(6,"Vimax VR Headset",5600,6);
INSERT INTO mobiles_computers_accessories VALUES(7,"Lava Gaming Mouse",1300,7);
INSERT INTO mobiles_computers_accessories VALUES(8,"Fermi Extension Cord",1200,8);
INSERT INTO mobiles_computers_accessories VALUES(9,"Boat Headphone",3400,9);
INSERT INTO mobiles_computers_accessories VALUES(10,"Logi Webcam",2400,10);

CREATE TABLE Beauty_Health(Sno INT, Product_Name Varchar(30), Price INT, Click INT);
INSERT INTO Beauty_Health VALUES(1,"Nivea Moisturizer",120,1);
INSERT INTO Beauty_Health VALUES(2,"Lotus Sunscreen",145,2);
INSERT INTO Beauty_Health VALUES(3,"Fogg Deo",230,3);
INSERT INTO Beauty_Health VALUES(4,"Johnsons Baby Powder",95,4);
INSERT INTO Beauty_Health VALUES(5,"Clinic Plus Oil",100,5);
INSERT INTO Beauty_Health VALUES(6,"Savlon Hand Sanitizer",50,6);
INSERT INTO Beauty_Health VALUES(7,"Dettol Handwash Pouch",80,7);
INSERT INTO Beauty_Health VALUES(8,"Bodyshop Bodywash",300,8);
INSERT INTO Beauty_Health VALUES(9,"Lakme Lipstick",245,9);
INSERT INTO Beauty_Health VALUES(10,"Head And Shoulders Shampoo",185,10);

CREATE TABLE Groceries(Sno INT, Product_Name Varchar(30), Price INT, Click INT);
INSERT INTO Groceries VALUES(1,"Aashirvad Aata 1 KG",700,1);
INSERT INTO Groceries VALUES(2,"Diamond Basmati Rice 2 KG",780,2);
INSERT INTO Groceries VALUES(3,"Potato Chips Lays Mega Pack",100,3);
INSERT INTO Groceries VALUES(4,"Cadbury Dairy Milk Box",285,4);
INSERT INTO Groceries VALUES(5,"Oreo Biscuits Megasaver Pack",400,5);
INSERT INTO Groceries VALUES(6,"Cranberry Juice 2L",240,6);
INSERT INTO Groceries VALUES(7,"7UP 2L",110,7);
INSERT INTO Groceries VALUES(8,"Kissan Jam Pineapple",135,8);
INSERT INTO Groceries VALUES(9,"Silvercoin Maida 5KG",800,9);
INSERT INTO Groceries VALUES(10,"Amul Kool Cold Coffee",45,10);

CREATE TABLE sports_baggage_luggage(Sno INT, Product_Name Varchar(30), Price INT, Click INT);
INSERT INTO sports_baggage_luggage VALUES(1,"Yonex Badminton Racket",500,1);
INSERT INTO sports_baggage_luggage VALUES(2,"NB Cricket Bat",2300,2);
INSERT INTO sports_baggage_luggage VALUES(3,"Head Tennis Balls Pack of 5",300,3);
INSERT INTO sports_baggage_luggage VALUES(4,"American Tourister Suitcase",3400,4);
INSERT INTO sports_baggage_luggage VALUES(5,"Yolo Sports Bag",1000,5);
INSERT INTO sports_baggage_luggage VALUES(6,"MI Fitness band",5600,6);
INSERT INTO sports_baggage_luggage VALUES(7,"Cosco Football CR7 Edition",2900,7);
INSERT INTO sports_baggage_luggage VALUES(8,"Tenacity Roller Skates",1650,8);
INSERT INTO sports_baggage_luggage VALUES(9,"Nivea Swimming Shorts",450,9);
INSERT INTO sports_baggage_luggage VALUES(10,"Nike Sports Perfume",800,10);

CREATE TABLE Kids_Toys_Games(Sno INT, Product_Name Varchar(30), Price INT, Click INT);
INSERT INTO Kids_Toys_Games VALUES(1,"Funskool Scotland Yard",780,1);
INSERT INTO Kids_Toys_Games VALUES(2,"Monopoly Electronic Banking",2350,2);
INSERT INTO Kids_Toys_Games VALUES(3,"Hower's Kiddy Telescope",940,3);
INSERT INTO Kids_Toys_Games VALUES(4,"Gan 360 Speedcube",1200,4);
INSERT INTO Kids_Toys_Games VALUES(5,"Tumbling Monkeys",450,5);
INSERT INTO Kids_Toys_Games VALUES(6,"Cricket Attax Pack of 20",300,6);
INSERT INTO Kids_Toys_Games VALUES(7,"Jenga",370,7);
INSERT INTO Kids_Toys_Games VALUES(8,"Young Scientist Play Kit",460,8);
INSERT INTO Kids_Toys_Games VALUES(9,"Classic Ludo",120,9);
INSERT INTO Kids_Toys_Games VALUES(10,"UNO Cards",160,10);

CREATE TABLE Entertainment(Sno INT, Product_Name Varchar(30), Price INT, Click INT);
INSERT INTO Entertainment VALUES(1,"Airtel Xstream 2GB",340,1);
INSERT INTO Entertainment VALUES(2,"Netflix Prime",450,2);
INSERT INTO Entertainment VALUES(3,"Hotstar",190,3);
INSERT INTO Entertainment VALUES(4,"Valorant X",2300,4);
INSERT INTO Entertainment VALUES(5,"Minecraft",3500,5);
INSERT INTO Entertainment VALUES(6,"CSGO",800,6);
INSERT INTO Entertainment VALUES(7,"RedHams",900,7);
INSERT INTO Entertainment VALUES(8,"McAfee AntiVIrus",4000,8);
INSERT INTO Entertainment VALUES(9,"Spotify Premium",500,9);
INSERT INTO Entertainment VALUES(10,"LiveKoora",450,10);

CREATE TABLE special_gift_offers(Offers Varchar(60), Click varchar(30));
INSERT INTO special_gift_offers VALUES("Christmas gift products and boxes",1);
INSERT INTO special_gift_offers VALUES("New Year Special Wine collection",2);
INSERT INTO special_gift_offers VALUES("Makar Sankranti Fits",3);
INSERT INTO special_gift_offers VALUES("Back","X");

CREATE TABLE christmas(Sno INT, Product_Name Varchar(60), Price INT,Save INT, Click INT);
INSERT INTO christmas VALUES(1,"Luxury Lindt Silk Savouries collection",1300,400,1);
INSERT INTO christmas VALUES(2,"Danish Butter Cookies assortment Holidays Edition",340,210,2);
INSERT INTO christmas VALUES(3,"Sharp LED decoration lights",500,180,3);
INSERT INTO christmas VALUES(4,"Rise Plum Cake",270,130,4);
INSERT INTO christmas VALUES(5,"Christmas Santa Secret Gift package for kids",1300,500,5);
INSERT INTO christmas VALUES(6,"Festive Lamp Red",890,110,6);

CREATE TABLE Newyear(Sno INT, Product_Name Varchar(30), Price INT,Save INT, Click INT);
INSERT INTO Newyear VALUES(1,"McDowells Siggnature rich",8000,5400,1);
INSERT INTO Newyear VALUES(2,"Corona mischelle 2L",16000,3000,2);
INSERT INTO Newyear VALUES(3,"Kingfisher pine",10000,3900,3);
INSERT INTO Newyear VALUES(4,"Harveys holiday special",2900,1800,4);

CREATE TABLE MakarS(Sno INT, Product_Name Varchar(30), Price INT,Save INT, Click INT);
INSERT INTO MakarS VALUES(1,"Manyavar Mohey designer kurta",4500,2000,1);
INSERT INTO MakarS VALUES(2,"Nakhrali peacock shade suit",2900,1000,2);
INSERT INTO MakarS VALUES(3,"Kala Niketan Pathani kurta",3400,2000,3);
INSERT INTO MakarS VALUES(4,"Mrignayani Madhubani Saree Red",7000,2300,4);
INSERT INTO MakarS VALUES(5,"V9 oak suit",5900,1200,5);
INSERT INTO MakarS VALUES(6,"MecM Blue floral chunni",2800,1000,6);

CREATE TABLE Cart(Sno INT NOT NULL AUTO_INCREMENT, Product_Name Varchar(80), Price INT, Click INT,Quantity INT DEFAULT 1,PRIMARY KEY(Sno));
CREATE TABLE Review(id INT NOT NULL AUTO_INCREMENT,review INT, PRIMARY KEY (id));