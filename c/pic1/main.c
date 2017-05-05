/*
 * File:   main.c
 * Author: joseluis
 *
 * Created on December 2, 2015, 9:46 PM
 */


#include <pic18fregs.h>
#include <delay.h>
#include "ints.h"

#pragma config FOSC = HSPLL_HS
#pragma config WDT = OFF
#pragma config LVP = OFF
#pragma config PBADEN = OFF
#pragma config PLLDIV = 5
#pragma config USBDIV = 1
#pragma config CPUDIV = OSC1_PLL2
#pragma config FCMEN = OFF
#pragma config PWRT = ON
#pragma config BOR = ON
#pragma config VREGEN = ON
#pragma config MCLRE = OFF
#pragma config CCP2MX = ON
#pragma config STVREN = ON
#pragma config XINST = OFF

// asignación del Timer 0
#define set_TMR0(x) {TMR0H=(x>>8); TMR0L=(x&0x00FF);}
#define start_TMR0 T0CONbits.TMR0ON=1

// número de servos
#define N_SERVO 5
#define SERVO_0 LATBbits.LATB0
#define SERVO_1 LATBbits.LATB1
#define SERVO_2 LATBbits.LATB2
#define SERVO_3 LATBbits.LATB3
#define SERVO_4 LATBbits.LATB4

#define slot (20000/N_SERVO)
#define c_slot (65536-slot+30)

//tamaño del bufer de chars
#define BUF_SIZE 128
#define inc(x){	x++; x&=(BUF_SIZE-1);}

// variable que identifica al servo activo en la presente interrupción
// variable tipo array que contiene el ancho de pulso de cada linea de control
// inicialización del timer;
unsigned int servo_active = 0;
unsigned int pulse[N_SERVO] = {1000, 1250, 1500, 1750, 2000};
unsigned int TMR0_ini;

unsigned int milisec = 0;

//configuración del bufer de TX
unsigned int tx_buf[BUF_SIZE];
unsigned int tx_next = 0; 
unsigned int tx_send = 0;

//configuración del bufer de RX
unsigned int rx_buf[BUF_SIZE];
unsigned int rx_next = 0; 
unsigned int rx_read = 0;

// interrupciones
void TMR0_isr (void);
void RX_isr (void);
void TX_isr (void);

// funciones personalizadas
void _putc (unsigned char);
void puts (const unsigned char[]);
unsigned char getch (void);
void setup_UART (unsigned int , unsigned int);
void Mover (void);



//interrupción del timer 0 
/*Cada vez que el timer 0 genere una interrupción por desbordamiento 
 * se ejecuta esta función que establece la duracción de los pulsos
 * de las 5 lineas que controlan los 5 servos
 */
void high_ISR (void) __interrupt 1
{
	/*if (RX_flag)
	{
		RX_isr ();
		Mover ();
	}
	
	if (TX_flag)
	{
		TX_isr ();
	}*/
    
	if (TMR0_flag)
	{
		TMR0_isr ();
	}
}



void TMR0_isr (void)
{
	TMR0_ini = 53536;
	if (milisec == 1000){SERVO_0 = 1 - SERVO_0; milisec = 0;}
	milisec++;
	
	//if (SERVO_0) TMR0_ini = pulse [0];
	//else {TMR0_ini = c_slot + pulse [0];}
	/*switch (servo_active)
	{
		case 0:
			SERVO_0 = 1 - SERVO_0;
			if (SERVO_0) TMR0_ini = pulse [0] - 25;
			else {TMR0_ini = c_slot + pulse [0]; servo_active++;}
			break;
			
		case 1:
			SERVO_1 = 1 - SERVO_1;
			if (SERVO_1) TMR0_ini = pulse [1] - 25;
			else {TMR0_ini = c_slot + pulse [1]; servo_active++;}
			break;
				
		case 2:
			SERVO_2 = 1 - SERVO_2;
			if (SERVO_2) TMR0_ini = pulse [2] - 25;
			else {TMR0_ini = c_slot + pulse [2]; servo_active++;}
			break;
				
		case 3:
			SERVO_3 = 1 - SERVO_3;
			if (SERVO_3) TMR0_ini = pulse [3] - 25;
			else {TMR0_ini = c_slot + pulse [3]; servo_active++;}
			break;
				
		case 4:
			SERVO_4 = 1 - SERVO_4;
			if (SERVO_4) TMR0_ini = pulse [4] - 25;
			else {TMR0_ini = c_slot + pulse [4]; servo_active = 0;}
			break;	
	}
	*/
	
	set_TMR0 (TMR0_ini);
	TMR0_flag = 0;
}



void RX_isr (void) 
{
	rx_buf[rx_next] = RCREG;
	inc(rx_next);

	RX_flag = 0;
}



void TX_isr (void)
{
	if (tx_send==tx_next)
	{
		disable_TX_int;
	}
	else
	{
		TXREG = tx_buf[tx_send];
		inc(tx_send);
	}
	TX_flag = 0;
}




void _putc (unsigned char ch)
{
	tx_buf[tx_next]=ch;
	inc(tx_next);
	enable_TX_int;
}



void puts (const unsigned char ch[])
{
	int i = 0;
	do 
	{
		_putc (ch[i]);
		i++;
	}
	while (ch[i] != '\0');
}



unsigned char getch (void)
{
	char ch = rx_buf[rx_read];
	inc(rx_read);
	return ch;
}




void setup_UART (unsigned int brgh, unsigned int spbrg)
{
	TRISCbits.TRISC6 = 0; 	//TX
	TRISCbits.TRISC7 = 1; 	//RX
	
	
	
	TXSTA = 0x00;		//reiniciar el estado de TX
	TXSTAbits.SYNC = 0; //trabajar asíncronamente
	TXSTAbits.TXEN = 1;	//habilitar TX para enviar
	TXSTAbits.TRMT = 1;	//limpiado del registro de envio
	
	
	
	RCSTA = 0x00;		//reiniciar el estado de RX
	RCSTAbits.SPEN = 1;	//habilitar el puerto serial
	RCSTAbits.CREN = 1;	//habilitar RX para recibir
	
	
	TXSTAbits.BRGH = brgh;
	SPBRG = spbrg;
}



void Mover (void)
{
	char ch = getch ();
	if (ch == 'a' || ch == 'c' || ch == 'e' || ch == 'g' || ch == 'i')
	{
		
		if (ch == 'a')
		{
			//if (pulse[0] > 1000)
			//{
				pulse[0]-=20;
			//}
		}
		
		if (ch == 'c')
		{
			//if (pulse[1] > 1000)
			//{
				pulse[1]-=20;
			//}
		}
		
		if (ch == 'e')
		{
			//if (pulse[2] > 1000)
			//{
				pulse[2]-=20;
			//}
		}
		
		if (ch == 'g')
		{
			//if (pulse[3] > 1000)
			//{
				pulse[3]-=20;
			//}
		}
		
		if (ch == 'i')
		{
			//if (pulse[4] > 1000)
			//{
				pulse[4]-=20;
			//}
		}
	}
		
	if (ch == 'b' || ch == 'd' || ch == 'f' || ch == 'h' || ch == 'j')
	{
		if (ch == 'b')
		{
			//if (pulse[0] < 2000)
			//{
				pulse[0]+=20;
			//}
		}
		
		if (ch == 'd')
		{
			//if (pulse[1] < 2000)
			//{
				pulse[1]+=20;
			//}
		}
		
		if (ch == 'f')
		{
			//if (pulse[2] < 2000)
			//{
				pulse[2]+=20;
			//}
		}
		
		if (ch == 'h')
		{
			//if (pulse[3] < 2000)
			//{
				pulse[3]+=20;
			//}
		}
		
		if (ch == 'j')
		{
			//if (pulse[4] < 2000)
			//{
				pulse[4]+=20;
			//}
		}
	}
}



void main(void)
{
	T0CON = 0b00001000;
	enable_global_ints;
	
	enable_TMR0_int;
	start_TMR0;
	
	//ADCON1 = 0x0F;
	
	TRISA = 0;
	PORTA = 0;	
	TRISB = 0;
	PORTB = 0;
	TRISC = 0;
	PORTC = 0;
	TRISD = 0;
	PORTD = 0;
	
	/*enable_RX_int;
	//setup_UART (1, 129);
	setup_UART (0, 77);
	
	//puts ("AT+RESET\r\n");
	//puts ("AT+ROLE=0\r\n");
	//puts ("AT+ORGL\r\n");

	puts ("AT+UART=9600,1,2\r\n");
	puts ("AT+NAME=BrazoRobotico\r\n");
	puts ("AT+PSWD=1010\r\n");*/

	while (1)
	{
        
	}
}