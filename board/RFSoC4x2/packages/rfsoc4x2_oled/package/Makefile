OBJSC = oled.o 

all:	
	gcc -fPIC -c -g oled.c
	gcc -shared -fPIC -rdynamic $(OBJSC) -o libNHD0216AWSB3.so
	rm *.o
