//------------------------------------------------------------------------
/*
 * Template source file generated by piklab 
 *
 * File:   main.c
 * Author: Jose Luis Cáceres Escudero & Jeison ...
 *
 * Created on December 2, 2015, 9:46 PM
 */
//
#define NO_BIT_DEFINES

#include <stdlib.h>
#include <pic18fregs.h>
#include "ints.h"

//configuración del pic 18F4550 a 48MHz con un cristal externo de 20MHz
#pragma config PLLDIV = 5
#pragma config FOSC = HSPLL_HS
#pragma config CPUDIV = OSC1_PLL2
#pragma config USBDIV = 2
#pragma config WDT = OFF
#pragma config LVP = OFF
#pragma config PBADEN = OFF
#pragma config FCMEN = OFF
#pragma config PWRT = ON
#pragma config BOR = ON
#pragma config VREGEN = ON
#pragma config MCLRE = OFF
#pragma config CCP2MX = ON
#pragma config STVREN = ON
#pragma config XINST = OFF

#define setTmr0(x) {TMR0H=((x-1)>>8); TMR0L=((x-1)&0x00FF);}
#define startTmr0 T0CONbits.TMR0ON=1;

//constante de 1us en ciclos
#define US 12
#define PRESCALER 4

// número de servos
#define NServo 5
// asignación de pines a cada linea de control de los servos
#define servo0 LATBbits.LATB0
#define servo1 LATBbits.LATB1
#define servo2 LATBbits.LATB2
#define servo3 LATBbits.LATB3
#define servo4 LATBbits.LATB4
#define prueba LATBbits.LATB7
#define PinD0  LATDbits.LATD0
#define PinD1  LATDbits.LATD1
#define PinD2  LATDbits.LATD2
#define PinD3  LATDbits.LATD3
//tamaño del bufer de tipo char
#define bufSize 128
//incremento y reinicialización del bufer de tipo char
#define inc(x){	x++; x&=(bufSize-1);}

// identifica al servo activo en la presente interrupción
unsigned int servoActive = 0;
// variable tipo array que contiene el ancho de pulso de cada linea de control
int servoPosition[NServo] = {0, 0, 0, 0, 0};
// inicialización del timer0;
unsigned int tmr0Ini = 1;
//tiempo para completar 20 milisegundos
unsigned int elapsedTm = 0;
int led0counter = 0;

//configuración del bufer de TX
unsigned int txBuf[bufSize];
unsigned int txNext = 0; 
unsigned int txSend = 0;

//configuración del bufer de RX
unsigned int rxBuf[bufSize];
unsigned int rxNext = 0; 
unsigned int rxRead = 0;

// declaración de las funciones llamadas por la interrupciones
// función manejadora de interrupciones causadas por el desbordamiento del timer 0
void tmr0Isr (void);
// función manejadora de interrupciones causadas por la recepción de datos en el pin Rx
void rxIsr (void);
// función manejadora de interrupciones causadas por la solicitud de envío de datos por el pin Tx
void txIsr (void);

// funcion que solicita el envió de un dato tipo char por el pin Tx
void _putc (unsigned char);
// funcion que envia cadenas de caracteres llamando a la función _putc
void puts (const unsigned char[]);
// funcion que devuelve el ultimo dato tipo char del buffer Rx
unsigned char getCh (void);
// funcion que inicializa los pines de comunicación Rx/Tx y configura el bit rate de comunicación
void setupUART ();
// funcion que 
void mover (void);
// función que establece la posición de un servo a partir de 16 posiciones claves establecidas (duty cylce)
void setServoPosition (int);
// función que pone las lineas de control de los servos en espera hasta completar los 20 ms despues del duty cycle
void setElapsedTm (void);



/*Cada vez que se genere una interrupción se ejecuta esta función*/
void highIsr (void) __interrupt 1
{
	if (RX_flag)
	{
		rxIsr ();
	}
	
	if (TX_flag)
	{
		txIsr ();
	}
	
	if (TMR0_flag)
	{
		tmr0Isr ();
	}	
}


// función que calcula los ciclos necesarios para ubicar el servo en una posición especifica dentro de 16 posibles.
void setServoPosition (int position)
{
    unsigned int cl = 1500;
    
    switch (position)
    {	
	case -4: cl = 1450; break;
	
	case -3: cl = 2087; break;
	
	case -2: cl = 2725; break;
	
	case -1: cl = 3362; break;
	
	case 0: cl = 4000; break;
	
	case 1: cl = 4900; break;
	
	case 2: cl = 5700; break;
	
	case 3: cl = 6500; break;
	
	case 4: cl = 7300; break;
    }
    
    elapsedTm = elapsedTm+cl;
    
    tmr0Ini = 65535-cl;
}


void setElapsedTm (void)
{
    tmr0Ini = elapsedTm+5535;
}


void tmr0Isr (void)
{
    led0counter++;
    if (led0counter >= 240)
    {	
	PinD0 = 1 - PinD0;
	led0counter = 0;
    }
        
    switch (servoActive)
    {
	case 0:
		servo0 = 1;
		servo1 = 0;
		servo2 = 0;
		servo3 = 0;
		servo4 = 0;
		elapsedTm = 0;
		setServoPosition(servoPosition[0]);
		servoActive++;
		break;
			
	case 1:
		servo0 = 0;
		servo1 = 1;
		servo2 = 0;
		servo3 = 0;
		servo4 = 0;
		setServoPosition(servoPosition[1]);
		servoActive++;
		break;
		
	case 2:
		servo0 = 0;
		servo1 = 0;
		servo2 = 1;
		servo3 = 0;
		servo4 = 0;
		setServoPosition(servoPosition[2]);
		servoActive++;
		break;
		
	case 3:
		servo0 = 0;
		servo1 = 0;
		servo2 = 0;
		servo3 = 1;
		servo4 = 0;
		setServoPosition(servoPosition[3]);
		servoActive++;
		break;
		
	case 4:
		servo0 = 0;
		servo1 = 0;
		servo2 = 0;
		servo3 = 0;
		servo4 = 1;
		setServoPosition(servoPosition[4]);
		servoActive++;
		break;
		
	case 5:
		servo0 = 0;
		servo1 = 0;
		servo2 = 0;
		servo3 = 0;
		servo4 = 0;
		setElapsedTm ();
		servoActive=0;
    }
    
    setTmr0(tmr0Ini);
    
    TMR0_flag = 0;
}


void rxIsr (void) 
{
    rxBuf[rxNext] = (unsigned char) RCREG;
    inc(rxNext);
    
    mover ();
    RX_flag = 0;
}



void txIsr (void)
{
  if (txSend==txNext)
  {
      disable_TX_int;
  }
  else
  {
      TXREG = txBuf[txSend];
      inc(txSend);
  }	
  TX_flag = 0;
}



void _putc (unsigned char ch)
{
	txBuf[txNext]=ch;
	inc(txNext);
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



unsigned char getCh (void)
{
	unsigned char ch = rxBuf[rxRead];
	inc(rxRead);
	return ch;
}



void setupUART ()
{
	TRISCbits.TRISC6 = 1; 	//TX
	TXSTAbits.TXEN = 1;	//transmisión habilitada
	TXSTAbits.SYNC = 0; 	//modo asíncrono
	TXSTAbits.BRGH = 0;	//velocidad de boud rate 0 baja velocidad 1 alta velocidad
	
	TRISCbits.TRISC7 = 1; 	//RX
	RCSTAbits.SPEN = 1;	//habilitar el puerto serial
	RCSTAbits.CREN = 1;	//habilitar RX para recibir
	
	//control del baud rate
	BAUDCONbits.BRG16 = 0; 	//16 bit baud rate desactivado
	
	SPBRG = 77;
}

char ch;

void mover (void)
{
	ch = getCh();
	
	if (ch == 'a')
	{	
		if (servoPosition[0] > -4)
		{
			servoPosition[0]--;
		}
	}
	
	if (ch == 'b')
	{
		if (servoPosition[0] < 4)
		{
			servoPosition[0]++;
		}
	}
		
	if (ch == 'c')
	{
		if (servoPosition[1] > -4)
		{
			servoPosition[1]--;
		}
	}
	
	if (ch == 'd')
	{
		if (servoPosition[1] < 4)
		{
			servoPosition[1]++;
		}
	}
		
	if (ch == 'e')
	{
		if (servoPosition[2] > -4)
		{
			servoPosition[2]--;
		}
	}
	
	if (ch == 'f')
	{
		if (servoPosition[2] < 4)
		{
			servoPosition[2]++;
		}
	}
		
	if (ch == 'g')
	{
		if (servoPosition[3] > -4)
		{
			servoPosition[3]--;
		}
	}
	
	if (ch == 'h')
	{
		if (servoPosition[3] < 4)
		{
			servoPosition[3]++;
		}
	}
		
	if (ch == 'i')
	{
		if (servoPosition[4] > -4)
		{
			servoPosition[4]--;
		}
	}
			
	if (ch == 'j')
	{
		if (servoPosition[4] < 4)
		{
			servoPosition[4]++;
		}
	}

}



void main(void)
{
	//habilitar las interrupciones globales
	enable_global_ints;
	
	
	//habilitadas las interrupciones de desborde de timer 0
	enable_TMR0_int;
	//inicializacion del timer 0
	tmr0Ini = 5535;
	setTmr0(tmr0Ini);
	//inicialización del timer 0 a 16bits prescaler de 256 (262114 ciclos)
	T0CONbits.TMR0ON = 1;
	T0CONbits.T08BIT = 0;
	T0CONbits.T0CS = 0;
	T0CONbits.T0SE = 0;
	T0CONbits.PSA = 0;
	T0CONbits.T0PS2 = 0;
	T0CONbits.T0PS1 = 0;
	T0CONbits.T0PS0 = 1;
	
	
	// Configuracion de pines a digital y todos a salida
	TRISA = 0;
	PORTA = 0;	
	TRISB = 0;
	PORTB = 0;
	TRISC = 0;
	PORTC = 0;
	TRISD = 0;
	PORTD = 0;
	
	
	//habilitar las interrupciones asociadas a Rx
	enable_RX_int;
	//configuración de EUART
	setupUART ();

	
	while (1)
	{
        
	}
}