# Turntable

Ovaj add-on omogucava :  

- rotiranje kamere oko objekta koji je stacionaran (i time se dobije efekat turntable)

- rotiranje objekta oko stacionarne kamere (kojom prilikom je i svetlo stacionarno)

Kako bi se aktivirao add-on potrebno je selektovati File > User Preferences > Add-ons > Animation > Animation: Turtable

Selektovati opciju Save User Settings

Sa desne strane interfejsa nalazi se Properties (ako je settings default), potrebno je seletkovati Scene

Na dnu se nalazi Turntable sa opcijama : Animation, Rotate Camera, Rotate Mesh

Animation : korisnik ima mogucnost da definise pocetni i zavrsni frejm animacije

Rotate Camera :

- Objekti koji se nalaze na sceni (konkretno MESH) su grupisani i njihov pivot je postavljen u centar grupe

- Kursor je postavljen gde je i pivot, a zatim na toj lokaciji je kreiran empty.(Kod blender-a, geometrija se kreira tamo gde je kursor)

- Izmedju kamere i empty-a je kreiran odnosno child-parent. 

- Takodje je ukljucene opcije select mesh, a za kameru view selected kako bi ceo/li objekat/objekti stali u FOV.(Field of view)

- Kamera se zatim rotira za 360 stepeni i proces se upisuje u dva frejma, pocetni i kranji.

- Isti princip vazi i za grupu objekata i za jedan objekat.

Rotate Mesh : 

- Objekti koji se nalaze na sceni (konkretno MESH) su grupisani.

- Omoguceno je rotiranje geometrije za 360 stepeni i proces je upisan u dva frejma, pocetni i kranji.

- Takodje je ukljucene opcije select mesh, a za kameru view selected kako bi ceo/li objekat/objekti stali u FOV.(Field of view)

		
Cesto softveri daju opciju ili samo rotiranje kamere ili rotiranje mesh-a. (ponekad ni to)		
Zato su napravljene dve opcije za turntable kako bi korisnik mogao odabrati zeljeni efekat. 
		